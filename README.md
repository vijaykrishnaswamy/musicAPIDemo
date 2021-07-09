# API to modify the Payload

musicapidemo - this is the main program takes below arguments

```
usage: Call the API using URI http://192.168.0.152:9443/displaymusicapi using a web browser

```
### Arguments to start the API in Python Flask Werkzeug server
```
python3 musicapidemo
```

## Build Docker
```
docker build -t musicapidemo .
docker run -d -p 9443:9443 musicapidemo
docker ps
```

## Running it
1) Either start the API by calling API start in Flask Wekzeug server OR host the services in docker
2) Once started, we can use any web browser to send/receive the request

## Technical Details:

- Read
  ```
	This API reads the input from Energy Australia API and displays the resultant converted payload
  ```  

- Used Python Flask module to host the API service

- Do not use Python Flask Werkzeug for Production deployment. It has only been used for simulation but actual Production deployment services should be hosted in much preferred containers like Apache/NGINX etc..

  ```
  only standard python(inbuilt) libraries are used
  ```
