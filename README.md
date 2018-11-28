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
