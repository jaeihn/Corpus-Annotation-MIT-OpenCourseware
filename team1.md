# Peer Review Instructions

## Setup

Please download the image file [team1.tar](https://drive.google.com/drive/folders/1dFTKt4yC9jf8F6Q1rVkyimEmZC30QbP9) and launch the Docker app.

After downloading the image file team1.tar, please open your terminal and navigate to the directory containing the file. In the terminal, execute
```
docker load < team1.tar
```
Then execute
```
docker run -p 9999:9999 team1 
```
Now you should be able to access the application by navigating to http://localhost:9999/ in your web browser.<br><br>
A warning message might show up: <br><br>
WARNING: The requested image’s platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested, it is normal, please wait couple seconds to let it run.<br><br>
Please wait for couple seconds until following messages show up:<br><br>
INFO:   Started server process [1]<br>
INFO:   Waiting for application startup.<br>
INFO:   Application startup complete.<br>
INFO:   Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)<br>

<br>

## Features

- In both Search by Title page and Search by Author page, you can search the readings based on different course topics.
  - For Type of Readings, you can choose whether they are Book, Academic Paper, or All to include both of them.
  - For Readings to Include, you can choose whether they are Required, Optional in MIT open courses, or All to include both of them.
  - Please click the Search button after making the selections.
  - If no readings appear, that means no readings match the selections. Please make other selections and try again!
  
- Please check out our statistics page! There are some visualizations about our annotation progress, average number of readings by major topic, and average number of readings by major topic.
