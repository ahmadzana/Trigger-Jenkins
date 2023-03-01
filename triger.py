from dotenv import load_dotenv
import os
import jenkins
import time
load_dotenv()

JENKINS_URL = os.getenv('JENKINS_URL')
JENKINS_USERNAME = os.getenv('JENKINS_USERNAME')
JENKINS_PASSWORD =  os.getenv('JENKINS_PASSWORD')
NAME_OF_JOB = os.getenv('NAME_OF_JOB')
PARAMETERS = None

class Jenkins:
    def __init__(self):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
    def build_job(self, name, parameters=None, token=None):
        BuildNumber = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        self.jenkins_server.build_job(name, parameters=parameters, token=token)
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, BuildNumber)
        return build_info
