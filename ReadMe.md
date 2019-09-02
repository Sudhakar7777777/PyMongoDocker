Simplest Python - Mongodb - Docker app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker is configured manually without docker compose file, etc.

Running the Mongodb instance via Docker

> docker run -d -p 27017:27017 --name m1 mongo

> docker ps

docker exec -it <container name> /bin/bash
eg:
> docker exec -it m1 /bin/bash

Once you have access to bash shell, connect to the Mongo instance.Mongodb

> mongo

> show dbs

> use customers_db

> show collections

> db.customers.find()

Run Customers.py to create sample records in the Mongodb
Run QueryCustomers.py to read the saved records from the Mongodb

Trash the docker container instance after all work is completed...Mongodb

> docker ps -all
(or)
> docker container ls -a

> docker stop m1

> docker rm m1

alternatively remove a running container using this command:

> docker rm --force m1

And command to clean up all stopped containers:

> docker rm $(docker ps -a -q)
(or)
> docker container prune