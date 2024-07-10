Tutorial - https://dev.mysql.com/doc/refman/8.4/en/docker-mysql-getting-started.html

https://www.youtube.com/watch?v=YpoWbngIBoM

docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.37

Commands:
- Open a CMD after docker container is already running

- Docker Login 
- Docker pull MySQL
- docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.37
- Docker PS

- stop the container deleting the image

		Stop the Container:

		bash
		Copy code
		docker stop my_container
		Remove the Container:

		bash
		Copy code
		docker rm my_container
		Remove the Image:

		bash
		Copy code
		docker rmi my_image:latest