from http import HTTPStatus

from fastapi import FastAPI, HTTPException

# Importar classes ausentes
from schemas.app_schemas import StudentDB, Studentlist, StudentPublic, StudentSchema

app = FastAPI()

database = []


@app.post(
    '/student', response_model=StudentPublic, status_code=HTTPStatus.CREATED.value
)
def create_student(student: StudentSchema):
    student_with_id = StudentDB(id=len(database) + 1, **student.model_dump())
    database.append(student_with_id)
    return student_with_id


@app.get('/students/', response_model=Studentlist)
async def read_students():
    return {'students': database}


@app.put('/students/{student_id}', response_model=StudentPublic)
def update_student(student_id: int, student: StudentSchema):
    if student_id > len(database) or student_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail='Student not found',
        )
    student_with_id = StudentDB(**student.model_dump(), id=student_id)
    database[student_id - 1] = student_with_id
    return student_with_id
