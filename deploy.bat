@echo off 
echo Deploying with Docker... 
docker build -t flask-calculator . 
docker run -d -p 5000:5000 flask-calculator 
