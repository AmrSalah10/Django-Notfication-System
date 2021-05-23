# Django Notifcation System

* This project is about creating notification system like twitter or linkedIn
 using python Django framework

## Tools

- Back-End:
* Django framework
To achieve this project I had to install django-notifications-hq package
 by ```pip install django-notifications-hq``` command

- Front-End:

* Django templates
* CSS
* CSS libary --> Bootstrap 
* javaScript and JS library --> jQuery

## Project Structure

The project is structured by VT design pattern

- View part

It has three function based views

1- index: It is resonsible for rendering index template
2- logout_view: It is resonsible for logging user out and redirecting him to login template
3- sendMsg: It is resonsible for sending the admin message then redirecting him to index template
4- sendMsgAll: It is resonsible for sending the admin message for all users at once

Template part

* It consists of one dynamic template (index.html) for admin and each user and (login.html) template
It has a navbar which has a notification icon for displaying notifications
The admin one hasform components to send a message to each user or to all users  

* Each view is controlled by a specific URL
There are URLS of django-notifications-hq package to delete notifications and mark notifications as read


## Third Party Resouces
[medium](https://medium.com/star-gazers/how-to-add-notifications-to-django-app-74df1dac984e)








