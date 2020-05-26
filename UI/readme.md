# Instructions

To run the code locally on your machine the following lines should be all that's needed.

pip install -r Cluster-and-Cloud-Project/UI/requirements.txt

python Cluster-and-Cloud-Project/UI/dash_files/app.py

the app will be accessible on http://172.26.134.13:3000/app/


A quick rundown of the files and their roles:

app - creates and deploys the server+app (main file)

layout - contains the overall structure and design of the app

tabs - contains the structure and elements of each tab

callbacks - functions that allow for interactive updating of elements in the app (optional)

database - database class for handling couchdb
