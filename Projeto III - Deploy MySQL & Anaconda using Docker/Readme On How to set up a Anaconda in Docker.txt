Tutorial - https://hub.docker.com/r/continuumio/anaconda3

https://www.youtube.com/watch?v=mGVfR94gtzg

anaconda is a python distribution, famous one.

Commands:
- Open a CMD after docker container is already running

- docker run -i -t -p 8888:8888 -v "%CD%":/home --name anaconda3_cpsc322 continuumio/anaconda3:2024.02-1
		-it -> launcehs an iteractive terminal for the container once it is created and running
		-p  -> forward and opens port 8888 for jupter use later
		-v  -> mounts the current working directory or you termina as the home directory of the container
		--name provides you own name for the container
	Pull the container image and create the image/conainer

- Propt a prompt and if type "pwd" it'll be in the root directory of the container

- Caso você já tenha criado o container e ele tenha parado, poderá inicializá-lo novamente com o comando:
	docker start [nome container]
	docker exec -it [nome do container] bash
	
	Abre o bash dentro do container tbm
	
- python --version -> aleady instaled

- Lunch jupter notebook or lab

	Port 8888 published
	
	In the container CLI (opened bash inside the container)
	
	jupyter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root --notebook-dir=/home
	
	Copy and past the URL in a browser
	
	when you are done... close any running notebooks -> (File ->Close and shut down notebook ) then shut down jupter lab ( File -> Shutdown )
	
- Can use with remote-container	
	- Install pyhon extensions in VS Code
	- select python interpreter CRLT + P -> Python Interpreter
	Select the python interpreter and run things.... 
	

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