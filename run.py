import cv2
import urllib
import numpy as np

USER="admin"
PASS="admin"
SERVER_IP="192.168.1.10"
from client import Client
c = Client(USER,PASS,SERVER_IP)
c.login()


stream=urllib.urlopen(c.stream_url)
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_GRAYSCALE)
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)