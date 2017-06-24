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
 
 ## You can test how effective the calculation is either by:

  ### Use the interface at the upper url
  ### Execute the program by:
```
   cd neper_numer/management/commands && python3 neper_number.py -p 1000 -t 14 -q=True -o 14_threads_per_1000_members_results.txt
```
#### Expected result is:
```
     Members - 1000, Threads - 14, Output_name - 14_threads_per_1000_members_results.txt, Quiet mode - False
     Executing start time is 16:20:47.025409
     Thread 1 started
     Thread 2 started
     Thread 3 started
     Thread 4 started
     Thread 5 started
     Thread 6 started
     Thread 7 started
     Thread 8 started
     Thread 9 started
     Thread 10 started
     Thread 11 started
     Thread 12 started
     Thread 13 started
     Thread 14 started
     Calculated neper number is 2.71828182846
     Executing end time is 16:20:47.782239
     Total executing time is 0.75683
```
