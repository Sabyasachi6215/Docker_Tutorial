Assignment 1:
Demonstrate minimum 15 basic docker command with explanation and screenshot.

1) Docker Version
~~~bash
docker --version
~~~

Lists the Docker Version installed in the system :
![image](https://user-images.githubusercontent.com/54863241/195691897-6ed46701-9816-4bc2-88a4-0a16d5eb1284.png)


2) Docker images
~~~bash
docker images
~~~
Lists the Docker images available: 
![image](https://user-images.githubusercontent.com/54863241/195692267-4342fffa-09b2-45ef-b190-4bcc36ad5a8b.png)


3) Docker Container
~~~bash
docker ps
~~~
Lists the Docker Containers running: 
![image](https://user-images.githubusercontent.com/54863241/195692384-9f9b863c-e1be-498a-9053-1c30e2bad65c.png)

4) Docker build
~~~bash
docker build -t <image_name> .
~~~
Build Docker image from Dockerfile
![image](https://user-images.githubusercontent.com/54863241/195692648-6f396898-0981-4c13-95a7-c5d865179858.png)


5) Docker run
~~~bash
docker run -d -p 8000:8000 <image_name>
~~~
Run Docker image to get Docker container
![image](https://user-images.githubusercontent.com/54863241/195693002-4fd45eed-f3b4-4030-ab58-f15d7a6a5782.png)


6) Docker stop
~~~bash
docker stop <container id>
~~~
Stop container:
![image](https://user-images.githubusercontent.com/54863241/195693698-48cbd2e5-1c75-4f84-9680-a5b8e5c03dab.png)



7) Docker delete image
~~~bash
docker rmi -f <docker_image>
~~~
Delete Docker Image
![image](https://user-images.githubusercontent.com/54863241/195693560-3bdd5e40-925e-4859-93ed-2cd778d68add.png)


8) Docker build image
~~~bash
docker build -t <image name> .
~~~
Delete build image from Dockerfile
![image](https://user-images.githubusercontent.com/54863241/195696813-395e7254-4534-4240-ad62-8c75bb949ff3.png)

9) Docker run image as an application
~~~bash
docker run -d -p 8000:80 <image name>
~~~
Delete run image 
![image](https://user-images.githubusercontent.com/54863241/195697185-a58e4257-a26c-4fca-b917-dfc9b3555f9c.png)

10) Docker tag image 
~~~bash
docker tag fastapi_app:latest sam08061988/fastapi_app
~~~
Tagged image

![image](https://user-images.githubusercontent.com/54863241/195698099-c481ec61-6b73-40ea-930a-da60fa54bab5.png)

11) Docker push image to Docker/hub
~~~bash
docker push <user_id>/<image name>
~~~
Push image to DockerHub
![image](https://user-images.githubusercontent.com/54863241/195697718-73d59b53-8657-41b6-a8dc-45547241b48d.png)

12) Docker : convert Docker Image to .tar file
~~~bash
docker save 7d43ed997976  > fastapi_project.tar
~~~
Image to .tar file conversion
![image](https://user-images.githubusercontent.com/54863241/195699575-e2a25129-28d8-4ae0-866c-0197032a5a8a.png)


13) Docker Statistics : container
~~~bash
docker stats <container id>
~~~
Statistics of container
![image](https://user-images.githubusercontent.com/54863241/195700410-84456bbc-966e-41dc-ab80-cef7d8933d8a.png)


14) Docker Containers list
~~~bash
docker ps -a
~~~
List of all containers
![image](https://user-images.githubusercontent.com/54863241/195701418-8e5c2da7-1fed-45c1-96ba-c5602620c965.png)


15) Docker information about : container port ID
~~~bash
docker port <container id>
~~~
Port on which container is running
![image](https://user-images.githubusercontent.com/54863241/195703134-f54e9fcd-773f-4c8b-86d9-472640cfd795.png)
