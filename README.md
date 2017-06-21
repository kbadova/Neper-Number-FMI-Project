# Neper-Number-FMI-Project
Implementing spreading the calculation of neper number into threads.

## Steps to setup the project:
 ```
 cd neper_number
 pip install -r requiremetes/base.txt
 pip install -r requiremetes/test.txt
 sudo -u postgres createdb -O your_postgres_username neper_number
 ```
## Steps to run the project:
 ```
 python3 manage.py migrate
 python3 manage.py runserver
 go to localhost:8000/rsa to see the result
 ```
