# Instructions

To run the code locally on your machine the following lines should be all that's needed.

pip3 install -r Cluster-and-Cloud-Project/UI/requirements.txt

python3 Cluster-and-Cloud-Project/UI/dash_files/app.py

a development version of the app will be accessible on http://127.0.0.1:8050/app/


A quick rundown of the files and their roles:

app - creates and deploys the server+app (main file)

layout - contains the overall structure and design of the app

tabs - contains the structure and elements of each tab

callbacks - functions that allow for interactive updating of elements in the app (optional)

database - database class for handling couchdb
