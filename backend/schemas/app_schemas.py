from pydantic import BaseModel, EmailStr


class StudentSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class StudentDB(StudentSchema):
    id: int


class StudentPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class Studentlist(BaseModel):
    students: list[StudentPublic]
