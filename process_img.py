import os
import io
from datetime import datetime
from datetime import timedelta
from flask import Flask, request, redirect, session, render_template
import twilio.twiml
from twilio.rest import Client
from google.cloud import datastore
from google.cloud import storage
from google.cloud import vision
from google.cloud.vision import types
from data_dict import *
import json
import urllib

app = Flask(__name__)
app.config.from_object(__name__)
ans=[]
file_name="C:/Users/HP/Desktop/Fridge/fanta.jpeg"
@app.route('/')
def detect_labels_cloud_storage():
    
    theLabel = []
    vision_client = vision.ImageAnnotatorClient()
    with io.open(file_name, 'rb') as image_file:
    	content = image_file.read()
    image = types.Image(content=content)
    # image = vision_client.image('storage.googleapis.com/twilio-160408/apple.jpg')
    labels_x = vision_client.label_detection(image,max_results=50)
    object_x = vision_client.object_localization(image,max_results=50)
    labels=labels_x.label_annotations
    ans.clear()
    
    for label in labels:
    	if(label.description=="Tomato" or label.description=="Apple" or label.description =="Orange drink" or label.description =="Pineapple" or label.description =="Banana" or label.description =="Cabbage" or label.description =="Bringel"):
    		ans.append(label.description)
    		count[label.description]+=1
    labels=object_x.localized_object_annotations
    for label in labels:
    	if(label.name=="Tomato" or label.name=="Apple" or label.name =="Orange drink" or label.name =="Pineapple" or label.name =="Banana" or label.name =="Cabbage" or label.name =="Bringel"):
    		ans.append(label.name)
    		count[label.name]+=1
    send_msg()
    data = {}
    if len(ans)!=0:
        data["Success"] = True
    else:
        data["Success"] = False
    data["Item_List"]=ans;
    json_data=json.dumps(data)
    return str(json_data)

    
def send_msg():
    account_sid = "ACeaea28036b8ffb449b5d283755533e9a"
# Your Auth Token from twilio.com/console
    auth_token  = "db04b88715ba93cbc0ca2ecfa902f9cf"
    client = Client(account_sid, auth_token)
    message = client.messages.create( body="You have following items present in your fridge"+str(ans),
    	from_='whatsapp:+14155238886',to='whatsapp:+917685957508'
   	)


if __name__ == '__main__':
    # __main__ function used for testing
    # detect_labels_cloud_storage("C:/Users/HP/Desktop/Fridge/fanta.jpeg")
    app.run(host='127.0.0.1', port=8080, debug=True)
    # Your Account SID from twilio.com/console
    account_sid = "ACeaea28036b8ffb449b5d283755533e9a"
# Your Auth Token from twilio.com/console
    auth_token  = "db04b88715ba93cbc0ca2ecfa902f9cf"
    client = Client(account_sid, auth_token)
    message = client.messages.create( body="ab nhi ayenge",
    	from_='whatsapp:+14155238886',to='whatsapp:+919161961471'
   	)



