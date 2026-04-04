from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/hello-world")
def hello_world():
    return {"message": "Hello from The Best Engineer!"}


