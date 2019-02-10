## Requirements
* pip install -r requirement.txt

cd project_name

Migration:
* python manage.py migrate

## Running the application
* Start the backend server [python manage.py runserver]
* Visit the application on the browser - [http:localhost:8000](http:localhost:8000)


APIs:

1. URL: /check-college-links
METHOD: GET
Request: None

Response: 
Success: Save output in CSV as

College,Link
MMMUT,http://mmmut.ac.in

2. URL: /login
METHOD: POST
Request: LinkedIn credentials

Response: 
Success: Output with Name, LinkedIn profile etc.


3. URL: /logout
METHOD: POST
Request: None

Response: 
Success: Back to login page



3. URL: /string-evaluation
METHOD: POST
Request params:
Type: JSON
{
    "expression": "((2*3) +4/ (5*2))*4"
}

Response:
Success: Value of expression example: 25.6 (for above expression)



