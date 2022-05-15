# berry
To build docker image running rest api app run -

"sudo docker-compose up --build"

Dependencies before running the API-

docker, composer. 

Expected output should be a message that  app is "Running on http://0.0.0.0:8080/ "

App itself consists of 2 python modules- berry.py and dataHandler.py.
berry.py runs the actual queries and communicates with sqlite database and responds to requests. dataHandler.py is responsible for handling the data- running the stastical tests etc. 

To check if app is running correctly connect to http://127.0.0.1:8080 and the correct response should be- "It works!".
If you get anything else- app is not functioning correctly. 

If you want to return all the data in JSON format just run http://127.0.0.1:8080/getAll
Expected outcome should be all the data in JSON format, if there is no data, emoty brackets [] will be returned.

