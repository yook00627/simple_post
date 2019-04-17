# Lyft Project

![lyfr logo](https://cdn.lyft.com/brochure/lyft-logo.4ac34941.svg)

This project is for Lyft apprenticeship application to create a simple web app using Python. For the project I have assumed that if string is to short or empty it would return a empty string.

## How to run

#### Setup and running

Using on your machine:

```
#must need to install python to work
#install flask
pip3 install flask

#run python script
python3 main.py
```

Using virtual environment:

```
#if flask is not installed
#setup virtualenv by 
python3 -m venv "name_of_directory"

#Activate your virtualenv by
source "name_of_directory"/bin/activate

#install dependencies using requirements.txt
pip3 install -r requirements.txt

#run python script
python3 main.py
```

#### testing

On a seperate window:

```
#to test if post request is working
curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "InputString"}' -H 'Content-Type: application/json'
```

#Example of it running

[example](https://raw.githubusercontent.com/yook00627/simple_post/master/example.png)

# Author
Kevin Yook