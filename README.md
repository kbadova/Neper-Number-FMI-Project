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
 
 ## You can either test how effective the calculation is either by:

  * Use the interface at the upper url
  * Execute the program by:
 ```
   cd neper_numer/management/commands && python3 neper_number.py -p 100 -t 6 -q=True -o result2.txt
```
