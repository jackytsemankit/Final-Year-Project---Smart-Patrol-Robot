import time
from itertools import chain
import email
import imaplib
import os
import re
import requests
import json
from PIL import Image
from operator import itemgetter
import firebase_admin
from firebase_admin import credentials, firestore, storage



import chardet

try:
    os.system("start python3 C:/uno100/api/uno.py uno100")
except:
    print("An exception occurred in calling flask")


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "airport-patrol-robot",
  "private_key_id": "908cb129f58f7685ee175f233b2739344918b3d9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDUiXfYA4q06Mlh\ngw49ndQRtoYgSUxOL2HjfKYXg8vDVRroB/hFi6vydKpNS1+P3fA/Sw0IsH9xSaz/\nzqwP/88MSvUybI+R5ZxiiBxqCmMZVA1VGxmL7MyBqU5Ogq69/223v/o8Dk+Ki/8H\nEel7ZmFzGaPTq5LldvAxwJFFbArb8d77ka6WGogd0mcdUJ0wo0VShX9PRQOq0Vhz\nceSnXyYw4BwX2PNKKO4v/zorXTWwI2lwQP5mmw0UPsu/x+0rPsa7UGBip715dTre\nnMFbOFkLiELthL5XI70xgTrN5wY15TCrapXK6PWNDF2oXKsdv20gFwJprkHrT2HY\nMcAJoi+bAgMBAAECggEAGwSeBrNYkCvhjHMCaJnQ34Q8+QtoVwNrUGXESsv3J2Mr\nvaBkaBmGfRa7SYJ8k5zf5s6NycjUwpwzkPyptIpNPJ+mG51frj5/9VSejBUQSPl9\njQ/vXPF4LpQiahTvIs8UQwjKxj9UJDrXa4N+6LAjUORLBmRSvbczd0JRaqpT7RFO\n63m1nFcWq108gy4eWzAR79cJNtYGMIGZNQxu1DfMMc0tk/d2g2wRUurjboYqpbiQ\nqxQYVZ7ykM2GKZZmua+h/9+9ITq6qS1se1ZRYp3pag5q6gqtszmVKaznbZ97IK6f\nDKMqw8Bd0GbIiNLqA+szG+U4PtjBL/xo3aq22ar9sQKBgQD+2267IpUZ5IMGoCoo\nkvI/8x+8C/nuJxf/1fvnf5/hk/++JGzgGx1i/cajYD5oa+gAXJCTfwEBaJkv+LBg\n1PfDXNJJbgGm53xPU6p2zauzZi2n8BQ5wBZO6ep8aLsR2Tz+gzOvKxrrLSvR6xM8\nKEar1iO8bOY/LMVqu3O02p678QKBgQDVfXQV6UJ2t2uuYbtQ774bdrXs31vJ/pS+\nGEle2FuEdRe8xzK+A7IWRYGvcKI0bdDdU6Qvdwqkf6rStfbb/yRtoFSGWxhZM5v1\nOWvHGcCJEeKeYF7cxah7h+U1p6JOUXgxEttivLIDu/IINHeJFTJlt28rX/yR5LsX\n+TflHtMgSwKBgQDX2F667TocWNXDucia3oF/OdkJuZbuZXvE+KVFVmjBc0go8M6p\nKy3DVi1y1yNj6uftznfAA9OFLuJ2p4gyKozAkA+lkx6hDfLReImp3tzprsNCNWnb\n01zRbvlibozpO/SVlecjFz3QKkyvmAmNbIsWI+HWRuDmZnO4xpPjezju8QKBgQDS\nTd4AA6M8bR0/T/kFFtYQGdXGvJSgHBAMXsJQExO8HNjAVv4uXledRuUknPC8cv1Q\nOafANiUevMDbBvNh7inFcC4zmCMZJBTa8bCxFjYrEJpL56UrF+8LmWf6feMOAYVD\n2k6RKk62DPu0h3LFcEMQHi397XVRhp+jUxZztvTFlwKBgQCrUM3wpxXm2Bfrk0XF\nkvh1/d5IGXXeys9l3yXeGQYGlsPpNjj0EBFjwL4PEjv1LSSEvDYiNzHLRde37zOV\nUTP4BQDIEaBbEZcGy+cun1c9WQSdE/GWIBQWRgwL8QxKuXOUGVlylVhx5KxEPriN\n1zVHjWgGhHeH/OskSnAASFJGRQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-nmgyb@airport-patrol-robot.iam.gserviceaccount.com",
  "client_id": "100527550336197662650",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-nmgyb%40airport-patrol-robot.iam.gserviceaccount.com",
  
}
)
firebase_admin.initialize_app(cred,{"storageBucket" : "airport-patrol-robot.appspot.com"})

bucket = storage.bucket()

db = firestore.client()
doc_ref = db.collection(u'cases_final')

imap_ssl_host = 'imap.gmail.com'  
imap_ssl_port = 993
username = 'patrolrobotfyp@gmail.com'
password = 'fyp202020'

criteria = {
    'FROM':    'patrolrobotfyp@gmail.com',
    #'SUBJECT': 'Temperature Measurement Picture'
}
uid_max = 0

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')



def search_string(uid_max, criteria):
    c = list(map(lambda t: (t[0], '"'+str(t[1])+'"'), criteria.items())) + [('UID', '%d:*' % (uid_max+1))]
    return '(%s)' % ' '.join(chain(*c))
    # Produce search string in IMAP format:
    #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)


def get_first_text_block(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        
        for part in msg.get_payload():
            if part.get_content_type() == 'multipart/alternative':
                for subpart in part.get_payload():
                    if subpart.get_content_maintype() == 'text':
                        return subpart.get_payload()
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif type == 'text':
        return msg.get_payload()


server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
server.login(username, password)
server.select('INBOX')

result, data = server.uid('search', None, search_string(uid_max, criteria))

uids = [int(s) for s in data[0].split()]
if uids:
    uid_max = max(uids)

server.logout()

print ("listening to the inbox now")
caseid=1
while 1:

    filesizes=[]

    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
    server.login(username, password)
    server.select('INBOX')

    result, data = server.uid('search', None, search_string(uid_max, criteria))

    

    uids = [int(s) for s in data[0].split()]
    for uid in uids:
        download=False
        img=[]
        if uid > uid_max:
            result, data = server.uid('fetch', str(uid), '(RFC822)') 
            msg = email.message_from_string(data[0][1].decode('utf-8'))
            
            uid_max = uid
        
            text = get_first_text_block(msg)
            
            capdate=""
            captime=""
            temp=""
            wearmask=""
            loc=""
            zoneNo=-1

            print ('New message :::::::::::::::::::::')
            print (text)

            # extract text data and upload to Firebase
            if text:
                
                # call api to get current location of the robot
                try:
                    r = requests.get('http://192.168.8.150:5000/status')                   
                    loc=r.json()["base"]["location"]["current"]
                    #-6.31,-3.13,-0.06,2.5,5.25,8.5
                    xcor=float(loc.split(",")[0])
                    if xcor>=-6.35 and xcor<-3.13:
                        zoneNo=5
                    elif xcor>=-3.13 and xcor<-0.06:
                        zoneNo=4
                    elif xcor>=-0.06 and xcor<2.5:
                        zoneNo=3
                    elif xcor>=2.5 and xcor<5.25:
                        zoneNo=2
                    elif xcor>=5.25 and xcor<-8.5:
                        zoneNo=1
                        
                except:
                    print("An exception occurred in calling the api")
                
                
                try:
                    capturedatetime=re.search('Event Time: (.*)\r', text).group(1).split(" ")
                    capdate = capturedatetime[0]
                    captime = capturedatetime[1]
                    temp=re.search('Skin-Surface Temperature:(\d+\.*\d*)' , text).group(1)
                    wearmask=re.search('Mask:(.*),', text).group(1)
                except:
                    print("An exception occurred in regex")

            
            for part in msg.walk():

                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                #print(captime)
                fileName = part.get_filename()[10:-9]+".jpg"

                print("fileName: ", fileName)


                if bool(fileName):
                    
                    filePath = os.path.join(detach_dir, 'attachments', fileName)
                    #if not os.path.isfile(filePath) :

                    #print (fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()

                    '''
                    #upload to storage                        
                    blob = bucket.blob(fileName)
                    blob.upload_from_filename("./attachments/"+fileName)
                    blob.make_public()
                    img.append(blob.public_url)
                    '''
                im=Image.open("attachments/"+fileName)
                (width, height)=im.size
                filesizes.append((fileName,(width, height)))
                
            for imgs in filesizes:
                if imgs[1][0]==imgs[1][1]:
                    os.rename('attachments/'+imgs[0],'attachments/FACE'+imgs[0])
                    blob = bucket.blob('FACE'+imgs[0])
                    blob.upload_from_filename('attachments/FACE'+imgs[0])
                    blob.make_public()
                    img.append(blob.public_url)
                    continue
                                      
                blob = bucket.blob(imgs[0])
                blob.upload_from_filename("./attachments/"+imgs[0])
                blob.make_public()
                img.append(blob.public_url)


            doc_ref.add({
                u'caseid':caseid,
                u'solved':"false",
                u'duplicateChecked':"false",
                u'processed':"false",
                u'zoneNo':zoneNo,
                u'date':capdate,
                u'time':captime,
                u'temp':temp,
                u'wearmask':wearmask,
                u'img':img
                
                
                })
            caseid+=1
            print("upload completed")
    
    server.logout()
    time.sleep(1)
