from flask import Flask 
from flask import request
from triger import Jenkins
import os

app = Flask('Triger-Jenkins')
NAME_OF_JOB = os.getenv('NAME_OF_JOB')
TOKEN = os.getenv('TOKEN')
PARAMETERS = os.getenv('PARAMETERS')
jenkins_obj = Jenkins()

@app.route('/build',methods=['GET'])
def triger():
    token=request.args.get('token')
    if (token == TOKEN):
        callback = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN)
        info = f"Jenkins Build URL: {callback['url']}"
        duration=f"duration: {callback['duration']}"
        return {'info':info,'duration':duration,'status':'success'}
    else :
      return {'reason':'not valid token','status':'failed'}

