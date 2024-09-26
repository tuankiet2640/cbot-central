from fastapi import FastAPI

app = FastAPI()

students = {
    1:{
        "firstName": "kiet",
        "lastname": "bui",
        "age":"23",
        "email":"tuankiet2640@gmail.com"
    }
}
@app.get("/")
def index ():
    return {"name":"first data"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students[student_id]
