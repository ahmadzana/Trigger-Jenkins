# Trigger-Jenkins

------

A very light weight web server made with flask that will trigger jenkins jobs.

The web server can be easily configured to work with any Jenkins server, allowing users to trigger jobs with a simple HTTP request. This makes it an ideal to automate their work-flow of their development process.



#### Usage

- Clone the repository.

```sh
git clone git@github.com:ahmadzana/Trigger-Jenkins.git
```

- Modify the environment variables in the docker-compose.yaml configuration file according to your specific requirements.

The **TOKEN** variable, which may be a randomly generated string, serves as a parameter in the HTTP GET request to authenticate the call.

**JENKINS_USERNAME** and JENKINS_PASSWORD is the login credential of your jenkins 

**NAME_OF_JOB** the name of the job to be triggered 

**PARAMETERS** any job build parameters 

The **JENKINS_URL** is the URL of the jenkins server running 

If your jenkins is in a separate  server where you want to host this you can add  to the docker-compose and use the private dns in the JENKINS_URL



Tip: If your jenkins is in another server from Jenkins-Trigger you can still access it by adding extra_hosts in the docker-compose.yaml pointing to the server ip address 

example: 


```yaml
   extra_hosts:
     - "anyhostname.com:162.242.195.82" #host and ip
```

then use anyhostname.com in the **JENKINS_URL** environment variable

------

#### Demo

```shell
docker-compose up -d 
```

Jenkins server is running in http://127.0.0.1:5000

accessing http://127.0.0.1:5000/builld responses

```
{"reason":"not valid token","status":"failed"}
```

add the TOKEN you added in the environment variable 

http://127.0.0.1:5000/builld?token=anystring

| info     | "Jenkins Build URL: https://jenkins.example.com/job/TESTING/44/" |
| -------- | ------------------------------------------------------------ |
| duration | 450                                                          |
| status   | "success"                                                    |





#### use case scenarios 

- If one possesses a privately hosted Jenkins server that is not publicly accessible, it is possible to make it available for external use by deploying this web server to trigger the jobs. This may be achieved by either directly exposing the Jenkins-triger server, or alternatively, by proxying it as a subpath of an application.

​       for example: 

​     i have an application running on https://www.example.com using nginx you can have a path that is not      	 used by the app and reverse proxy it to the Trigger-Jenkins server running to trigger the job that will        	 build my app 

```nginx
location /buildme {
    proxy_set_header    X-Real-IP  $remote_addr;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header    Host $http_host;
    proxy_redirect      off;
    proxy_pass          http://127.0.0.1:5000/;
}
```



a get request to url https://www.example.com/buildme?token=yourtoken will trigger the job to build the app.