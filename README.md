# Django-Secure-Authentication-API
A secure RESTful API for enabling sign up, login & logout of users using JSON Web Tokens (JWT)

### Functionalities

- You Can Register New Users

![](https://github.com/steve-njuguna-k/Django-Secure-Authentication-API/blob/master/screenshots/1.PNG)

- You Can Login Current Users

![](https://github.com/steve-njuguna-k/Django-Secure-Authentication-API/blob/master/screenshots/2.PNG)

- You Can View Logged In Users via JWT inserted in cookies

![](https://github.com/steve-njuguna-k/Django-Secure-Authentication-API/blob/master/screenshots/3.PNG)

- You Can Retrieve Both Refresh & Access Tokens For Different Users

![](https://github.com/steve-njuguna-k/Django-Secure-Authentication-API/blob/master/screenshots/4.PNG)

- You Can Logout Users

![](https://github.com/steve-njuguna-k/Django-Secure-Authentication-API/blob/master/screenshots/5.PNG)

# Project Setup Instructions
1) Git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Secure-Authentication-API.git
```
2. Go To Project Directory
```
cd Django-Secure-Authentication-API
```
3. Create Virtual Environment
```
virtualenv env
```
4. Active Virtual Environment
```
env\scripts\activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate Database
```
py manage.py migrate
```
8. Run Project
```
py manage.py runserver
```
9. Open Postman

10. Head over to the URL & perform a POST request
```
http://127.0.0.1:8000/api/register
```

© 2021 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
