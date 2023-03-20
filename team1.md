# Peer Review Instructions

## Setup

After downloading the image file team1.tar, please open your terminal and navigate to the directory containing the file. In the terminal, execute
```
docker load < team1.tar
```
Then execute
```
docker run -p 9999:9999 team1 
```
Now you should be able to access the application by navigating to http://localhost:9999/ in your web browser.

<br>

## Features

- Please check out our statistics page! There are some interesting moments when we did the annotations.

- In both Search by Title page and Search by Author page, you can search the readings based on different course topics.
  - For Type of Readings, you can choose whether they are Book, Academic Paper, or All to include both of them.
  - For Readings to Include, you can choose whether they are Require, Optional in MIT open courses, or All to include both of them.
  - Please click the Search button after making the selections.
  - If no readings appear, that means no readings match the selections. Please make other selections and try again!
