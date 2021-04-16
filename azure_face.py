import firebase_admin
from firebase_admin import credentials, firestore, storage

from datetime import datetime

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient


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



def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = '88e42e84c2fb40d3a2eb888c6736e1aa'
    ENDPOINT = 'https://fyp-face-recognition.cognitiveservices.azure.com/'
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

def face_id(str1,str2):
    face_client = get_face_client()
    
    url1 = str(str1)
    url2 = str(str2)
    
    attributes = [] 
    include_id = True
    include_landmarks = False
    result1 = face_client.face.detect_with_url(url1, include_id, include_landmarks, attributes, raw=True)
    result2 = face_client.face.detect_with_url(url2, include_id, include_landmarks, attributes, raw=True)
    if len(result1.response.json())==0:
        return 0
    if len(result2.response.json())==0:
        return 0
    result1 = result1.response.json()[0]
    result2 = result2.response.json()[0]
    test = face_client.face.verify_face_to_face(result1['faceId'], result2['faceId'])
    #test.as_dict()
    return float(str(test.as_dict()["confidence"]))

if __name__=="__main__":

    bucket = storage.bucket()

    db = firestore.client()
    doc_ref = db.collection(u'unique_cases').where(u'processed', u'!=', u'true')


    docs = doc_ref.stream()

    docsList=[]

    for doc in docs:
        docDict=doc.to_dict()
        if docDict["img"]==None:
            continue
        if len(docDict["img"])!=3:
            continue
        docsList.append((doc.id,docDict))
        
  

    for x in range(len(docsList)):
        #print(docsList[x][0])
        docsList[x][1]["processed"]="true"
        comparedDocList=[docsList[x][1]]
        db.collection(u'unique_cases').document(docsList[x][0]).update({
            'processed': 'true'
        })
        url1=max(docsList[x][1]["img"],key=len)
        if "FACE" not in url1:
            #print(url1)
            continue

        for y in range(x+1,len(docsList)):
            #print(docsList[y][0])
            url2=max(docsList[y][1]["img"],key=len)
            if docsList[y][1]["processed"]=="true":
                continue
            
            if "FACE" not in url2:
                #print(url2)
                continue
            if face_id(url1,url2) > 0.7:
                docsList[y][1]["processed"]="true"
                db.collection(u'unique_cases').document(docsList[y][0]).update({
                    'processed': 'true'
                })
                comparedDocList.append(docsList[y][1])

        tempList=[]
        caseid=comparedDocList[0]["caseid"]
        zoneNo=comparedDocList[0]["zoneNo"]
        date=comparedDocList[0]["zoneNo"]
        timeList=[]
        wearmask=comparedDocList[0]["wearmask"]
        imgList=[]

        for doc in comparedDocList:
            tempList.extend([doc["temp"]])
            timeList.extend([doc["time"]])
            imgList.extend(doc["img"])

        print(tempList)
        print(timeList)
        print(imgList)

        
        db.collection(u'processed_cases').add({
                u'caseid':caseid,
                u'solved':"false",
                u'duplicateChecked':"true",
                u'processed':"true",
                u'zoneNo':zoneNo,
                u'date':date,
                u'time':timeList,##
                u'temp':tempList,###list of temps? or just mean
                u'wearmask':wearmask,
                u'img':imgList###
                
                
                })
        

    '''
    face_client = get_face_client()
    
    url = "https://storage.googleapis.com/airport-patrol-robot.appspot.com/MDY4NjAzOTI0MDVGNDM2MTlGMkY4NjJFQTg3M0E1Q.jpg"
    url2 = "https://storage.googleapis.com/airport-patrol-robot.appspot.com/MjNFN0EwM0U4MjRCNEE1MUE1OTg3ODU1RUE4NUY2M.jpg"
    attributes = [] #we don't need them in this case
    include_id = True
    include_landmarks = False
    result1 = face_client.face.detect_with_url(url, include_id, include_landmarks, attributes, raw=True)
    result2 = face_client.face.detect_with_url(url2, include_id, include_landmarks, attributes, raw=True)
    result1 = result1.response.json()[0]
    result2 = result2.response.json()[0]
    test = face_client.face.verify_face_to_face(result1['faceId'], result2['faceId'])
    test.as_dict()

    print(test)
    '''