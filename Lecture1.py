from fastapi import FastAPI, Path

app = FastAPI()

# At terminal
'''
How to start server: uvicorn Lecture1:app --reload
swagger api -> IP += "/docs"
'''

#JSON
students = {
    1: {
        "name" : "Seunghyeon Kim",
        "age" : 17,
        "class" : "year 21"
    },
    2: {
        "name" : "Seunghyeon Kim",
        "age" : 17,
        "class" : "year 21"
    }
}

# PATH: /
'''
get - info get
post - create new
put - update info
delete - delete info
'''
@app.get("/")
def index():
    return {"name" : "Seunghyeon Kim"}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description = "학생의 고유번호로 학생을 검색하는 API입니다", gt = 1)):
    return students[student_id]

#Query
@app.get("/get-by-name")
def get_student(student_id, name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not Found"}