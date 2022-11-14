# Backend Service

## How to setup the python virtual environment
- `cd .\Backend`
- `python -m venv venv`
- `.\venv\Scripts\activate`
- `pip install -r requirements.txt`

## How to run the service
- `python -m flask --app app.py run`
- The service will then be running at `http://localhost:5000`

## Endpoints
- `/api/predict`
    - POST
    - Receives: 
        ```
        { 
            "passengerClass": number, 
            "male": bool, 
            "age": number 
        }
        ```
    - Returns: 
        ```
        { 
            "survived": number 
        }
        ```
- `/api/stats`
    - GET
    - Returns:
        ```
        {
            "totalNumberOfUsers": number,
            "numberOfUsersWhoSurvived": number
        }
        ```
