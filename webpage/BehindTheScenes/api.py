from flask import Flask
from flask import render_template
from flask import requests



 
#load image from file
file = open('hello.jpg')
headers = {'content-type': 'multipart/form-data'}
 
payload = {'apikey': 'ea3dcd7fbbfab524', 'lang': 'eng'}
files = {'file': file}
r = requests.post("http://www.bitocr.com/api", data=payload, files=files)
result = r.json()
if result['error'] == 0:
    #success
    print(result['result'])
else:
    #failed
    print("Error #" + str(result['error_code']) + " " + result['error_message'])

