# CSE5914Leftovers

## How to start the Flask app with Elastic Search (updated 3/25/24)
Prerequisites:
  A docker container running elastic search
  
1. Download, pull, or clone the repository
2. Start your docker container running elastic search
3. run "docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt ." in the CSE5914LEFTOVERS directory, which copies the http certification to the directory.
     **note, my container is called "es01". Change yours accordingly.
5. Open config.py
6. Copy the password from your docker container (listed under "Password for the elastic user" in the container logs).
7. change the elastic_password variable in config.py to be this password.
8. run app.py
9. your app should be up and running.


## Quickstart with Docker

Once you clone or download this repository, you will use a virtual environment (venv) and Docker to build the app, which should be viewable from your localhost and will just display a line of text for now.

### How to initialize the virtual environment (done every time you download a new version of the repo. I don't know if these files should be added to version control, so I would say don't.)

#### Mac OS

python3 -m venv env

#### Windows

python -m venv env

### Activate the virtual environment:

#### Mac OS

source env/bin/activate

#### Windows

env\Scripts\activate.bat
\*\*\* On windows you may get a permissions error (which is what I got). I get this error from the vscode terminal, but not from opening a command prompt and doing it from there. Good luck.

### How to build your Docker Image and Container

From the venv terminal, run:

docker build --tag python-docker . 
### This creates an image called python-docker based on the included Dockerfile in the specified directory ( . in this case, if you are in the CSE5914Leftovers direcotry)

docker run -dp 5000:5000 python-docker 
### This starts a container built from the docker image we just made. -d makes it run in the browser. -p 5000:5000 maps Docker port 5000 to our local port 5000.

You should get a hash-looking string after running the command. Then in your browser, go to localhost:5000.
If all went well, you will see a header.
