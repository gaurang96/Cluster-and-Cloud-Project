# Cluster-Cloud-Project
CCC2020-TEAM53 is the final folder used for submission.

COMP90024 Assignment 2 - Develop a Cloud-based solution that exploits a multitude of virtual machines (VMs) across the UniMelb Research Cloud for harvesting tweets through the Twitter APIs (using both the Streaming and the Search API interfaces). Develop a social analytics dashboard utilising data from Aurin and twitter

The primary goal was to investigate the sentiment of local twitter users in particular respect to unemployment that may have arisen due to the lockdown protocols of covid-19. The twitter data was mined to focus on the tweets the mentioned a selection of key phrases or were related to those phrases.

![ss1](https://user-images.githubusercontent.com/40225761/90354353-6b644c80-e08c-11ea-90f0-cd9e880af89c.png)

In figure above, the positive and negative sentiment ratios of the 25 administrative areas with the greatest positive sentiments are shown. All areas are overwhelmingly positive with minimal negativity. The majority of these regions are within the metropolitan area of Melbourne and there seems to be some regional clustering. For example, Hughesdale, Oakliegh, Oakliegh East and Huntingdale are all suburbs that are immediately adjacent.

![Screenshot 2020-08-17 at 1 21 48 PM](https://user-images.githubusercontent.com/40225761/90354468-b8e0b980-e08c-11ea-9483-4a7b8bd709c3.png)

In figure above, the reverse of the previous is shown and the sentiment ratios of the administrative areas with the greatest negative sentiments are shown. The negativity is not as great as in the prior graph, as no value exceeds 0.5. Interestingly, two of the three areas with the greatest negativity have equal positivity. Another contrast to the prior chart is that there are a larger proportion of regional administrative areas.

![Screenshot 2020-08-17 at 1 23 47 PM](https://user-images.githubusercontent.com/40225761/90354526-eded0c00-e08c-11ea-969e-0ba49a42484e.png)

This figure above now shows the overall net difference of positive and negative tweets each day or a “happiness index”. Positive values indicate that there is stronger positive sentiment and negative values indicate stronger negative sentiment. Based on the current results, it can be seen that there has been consistent positive sentiment online. Moreover, this net difference appears to be increasing every day.

![Screenshot 2020-08-17 at 1 25 15 PM](https://user-images.githubusercontent.com/40225761/90354615-28ef3f80-e08d-11ea-993d-b237e97f4cfc.png)

The Final Figure visualizes the most recent unemployment data from various regions in Victoria. From this it can be gathered that the rates of unemployment have traditionally been higher in more regional areas of Victoria, as the city of Melbourne has by far the lowest unemployment rate of those present.

# User Guide for the Software Application
## Ansible Folder
1. Under nectar folder run the run-nectar.sh sudo ./run-nectar.sh to create instances, volume, security groups.
2. Under set-env folder run sudo ./run-container.sh to create docker image, container, mount volume, install dependencies, install CouchDB.
3. Under web-app run sudo ./run-web-app.sh to host the web app on the instance.
(Using Windows, the command dos2unix is used for the conversion of sh file before running the sudo ./run-nectar.sh.)

## Harvester Folder
The code for the harvester and web app is cloned from the git repository1. The scheduler in set-env will run the harvester.py after 30 minutes. historic_tweets.py is used to fetch the historic tweets.

## web_app Folder
To run web app locally on your machine the following lines should be all that's needed.
pip install -r Cluster-and-Cloud-Project/UI/requirements.txt
python Cluster-and-Cloud-Project/UI/dash_files/app.py
the app will be accessible on http://172.26.134.13:3000/app/
A quick rundown of the files and their roles:
app - creates and deploys the server+app (main file)
layout - contains the overall structure and design of the app
tabs - contains the structure and elements of each tab
call-backs - functions that allow for interactive updating of elements in the app (optional)
database - database class for handling couchDB

## Aurin Folder
This contains the data set used from Aurin website by downloading in JSON format.

## CouchDB Views Folder
All the views made using map reduce feature of CouchDB are mentioned under the folder. Charts, plots shown in front end are dynamically loaded by calling these views from the front-end application.





