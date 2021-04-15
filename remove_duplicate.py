import firebase_admin
from firebase_admin import credentials, firestore, storage

import chardet

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

