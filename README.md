# Building a Notes Application with React and Django

## Tools Used
Frontend: ReactJS 

Backend: Django, Django REST Framework

## Code Usage
- Clone the repository
- Create your environment 
 ```shell
       python3 -m venv env
 ```
 - Activate your environment 
 ```shell
       source env/bin/activate
 ```
  - Navigate to the project1 base folder that contains the requirements.txt file.
```shell
       cd project1
 ```
 - Install all requirements
 ```shell
       pip install -r requirements.txt
 ```
 - Make migrations
```shell
       python3 manage.py makemigrations
 ```
 You might get the warning below because the build folder has not been created yet. Ignore it and proceed to the next step.
``` WARNINGS:
?: (staticfiles.W004) The directory '/Users/faruq/Desktop/test/React-Django/project1/frontend/build/static' in the STATICFILES_DIRS setting does not exist.
```

 - Migrate changes
```shell
       python3 manage.py migrate
 ```
 - Navigate to the front end folder 
```shell
       cd frontend
 ```
 - Install npm
 ```shell
       npm install
 ```
 - then build the files
 ```shell
       npm run build
 ```
 - Then navigate back to the root directory
```shell
       cd ..
 ```
 - Run the following command to run the code in development mode
```shell
       python3 manage.py runserver
 ```
 - Enjoy!!!!





