# Motivation
FOllowing the Safari Books Online course "Professional RESTful API Design using Python Flask".
First thing is to see if the contens are upgradeable from year 2017 to 2018.
Security fixes following then.

# Warning
As of now to foreseeable future, there are security holes in libraries used in this rehearsal. Be warned.


# Running

## Build
before anything you need build the docker image.
Build the file based on docker.yml
```bash
docker-compose build

```

## DB Server
Start the database server as daemon, separately from the flask server.
```bash
docker-compose up -d db
```

Check that the db server is running as expected by issuing
```bash
docker ps
```

which should state something like "mongo" in the IMAGE column.

## Flask API
```bash
docker-compose run --service-ports web
```
## Browsing
Due to a networking configuration done in the examples, the app listens on localhost, that is, http://127.0.0.1.

# Relevant information
## HTTP Status Codes
 HTTP Status Codes: http://www.restapitutorial.com/httpstatuscodes.html
### 2xx Client Succes (OK)
 - 200 OK
 - 201 OK as return to post (insert)
 - 204 OK as return to delete
### 4xx Client Error (NOK)
 - 400 NOK as return to malformed (bad) request
 - 401 NOK as return to access failed request (invalid access (credentials))
 - 403 NOK as return to unauthorized request (invalid authorization)
 - 404 NOK as return to not found
 - 409 NOK as return in conflict case (duplicate records)
### 5xx Server error (NOK)
 - 500 NOK


 ## Modifying Python dependecies
 If in need to modify python dependencies, i.e. the the requirements.txt, then
 - modify the file
 - rebuild the docker image and relaunch the flask services
 ```bash
  docker-compose build
  docker-compose run --service-ports web
 ```

## Connect to mongodb from application Server

Pay attentention to the NAMES. Pick the one that starts with `petsapi_web_run_`
```bash
 docker ps
```
In my case this was `petsapi_web_run_12`, so issuing the command
```bash
docker exec -it petsapi_web_run_12 mongo --host mongodb
```
opens a shell in our mongodb instance.

## Running tests
```bash
 docker ps
 docker exec -it petsapi_web_run_13 python tests.py
```
