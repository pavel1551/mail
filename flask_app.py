# A very simple Flask Hello World app for you to get started with...
 
from flask import Flask, request, json
import vk
import numpy as np
import random
token = 'ec26f81e721b444281bad7a27e1094bf3167d7c2544fde6547d164e0a66c77e30e6926bf80b0461c0f5a4'
confirmation_token = '987229df'
 
def auth_vk():
    session = vk.Session(access_token=token)
    api = vk.API(session, v='5.103')
    return api
 
app = Flask(__name__)
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
api = auth_vk()
def send_message(user_id, token, message, attachment=""):
    r = np.int64(random.randint(1, 10000000000000000))
    message = message
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment,random_id=r)
def get_answer(body):
   message = body
   return message
 
def create_answer(data, token):
   user_id = data['from_id']
   message = get_answer(data['text'].lower())
   send_message(user_id, token, message)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = json.loads(request.data)
        if 'type' not in data.keys():
            return 'not vk'
        if data['type'] == 'confirmation':
            return confirmation_token
        elif data['type'] == 'message_new':
            create_answer(data['object']['message'], token)
            return 'ok'
        else:
            return 'ok'
    else:
        return 'Wrong request'