# Awwards-django

>[nyakiochristine](https://github.com/nyakiochristine)  
  
## Description

This project allows users to post their projects for other users to rate according to design, usability and content among other parameters

## Home page

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed.
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  
## Setup and Installation 

<img src:/home/moringa/awards-clone/static/images/Screenshot from 2022-06-22 00-47-23.png)


### Cloning the repository

 ```bash
https://github.com/nyakiochristine/awwards-django
```

### Navigate into the folder and install requirements  

 ```bash
 - pipenv shell
```

### Install and activate Virtual  

 ```bash
- pipenv install requests
```  

#### Install Dependencies  

 ```bash
  pipenv install 
```  

##### Setup Database  

  SetUp your database User,Password, Host then make migrate  

 ```bash
python manage.py makemigrations database name
 ```

 Now Migrate  

 ```bash
 python manage.py migrate 
```

##### Run the application  

 ```bash
 python manage.py runserver 


##### Testing the application  

 ```bash
 python manage.py test 
```

Open the application on your browser `127.0.0.1:8000`.  
  
## API Endpoints

The following endpoints are available on the server:

 /api/project/

 /api/profile/

## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
## Known Bugs  

* There are no known bugs currently but pull requests are allowed incase you spot a bug
  
## Contact Information

-Email- [Nyakio Christine](mailto:christine.mwangi@student.moringaschool.com)
-Linkedin - [Christine Mwangi](https://www.linkedin.com/in/christinemwangi/)

## License

* *MIT License:*
* Copyright (c) 2022 **Nyakio Christine**

[Go Back to the top](#awwards)
