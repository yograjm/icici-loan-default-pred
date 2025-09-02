
from fastapi import FastAPI       # import FastAPI class from fastapi package


# Instantiate FastAPI object
app = FastAPI()

# HTTP methods: GET, POST, DELETE, PUT

# GET method

@app.get("/hi")
def func1():
    return {"message": "Hello everyone!"}

# Query parameter     # /hello?fname=Suresh&lname=Kumar
@app.get("/hello")
def func2(fname, lname):
    return {"message": "Hello " + fname + " " + lname + " !"}

# Path parameter     # /hello/Suresh/Kumar
@app.get("/hello/{fname}/{lname}")
def func2(fname, lname):
    return {"message": "Hello " + fname + " " + lname + " !"}


# Swagger Documentation  avaiable on this endpoint ->   /docs 

# POST;   with query parameter     (We can't make a request to POST endpoint through Browser)
@app.post("/hey")
def func3(fname, lname):
    return {"message": "Hello " + fname + " " + lname + " !"}



# POST, with request body
from pydantic import BaseModel          # Pydantic is a Data Validation library

class Person(BaseModel):
    name: str
    age: int
    address: str


@app.post("/person")
def func4(person: Person):
    response = "Your name is " + person.name
    response += "Your age is " + str(person.age)
    response += "Your address is " + person.address
    return {"message": response}


# Prediction

class Feature(BaseModel):
    person_age: float
    person_income: float
    person_home_ownership: str
    person_emp_length: int
    loan_intent: str
    loan_grade: str
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int



from app import predict_loan_status

@app.post("/predict")
def func5(f: Feature):
    label = predict_loan_status(f.person_age, 
                        f.person_income, 
                        f.person_home_ownership, 
                        f.person_emp_length, 
                        f.loan_intent, 
                        f.loan_grade, 
                        f.loan_amnt, 
                        f.loan_int_rate, 
                        f.loan_percent_income, 
                        f.cb_person_default_on_file, 
                        f.cb_person_cred_hist_length
                        )
    return {"prediction": label}


# Webserver -> Uvicorn
import uvicorn

uvicorn.run(app, host="0.0.0.0", port=8080)
