from pydantic import BaseModel, EmailStr
from datetime import time
from typing import List


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
    students: List[StudentPublic]


class AvailabilityBase(BaseModel):
    day_of_week: int
    start_time: time
    end_time: time


class SquadAvailabilitySchema(AvailabilityBase):
    squad_id: int


class MentorAvailabilitySchema(AvailabilityBase):
    mentor_id: int


class CompanyAvailabilitySchema(AvailabilityBase):
    company_id: int


class ClassAvailabilitySchema(AvailabilityBase):
    class_id: int


class ClassSchema(BaseModel):
    id: int
    name: str
    students: List[StudentPublic]
    squads: List["SquadSchema"]
    availabilities: List[ClassAvailabilitySchema]

    class Config:
        orm_mode = True


class SquadSchema(BaseModel):
    id: int
    class_id: int
    mentor_id: int
    company_id: int
    class_: ClassSchema
    mentor: "MentorSchema"
    company: "CompanySchema"
    squad_availabilities: List[SquadAvailabilitySchema]

    class Config:
        orm_mode = True


class MentorSchema(BaseModel):
    id: int
    name: str
    squads: List[SquadSchema]
    mentor_availabilities: List[MentorAvailabilitySchema]

    class Config:
        orm_mode = True


class CompanySchema(BaseModel):
    id: int
    name: str
    company_availabilities: List[CompanyAvailabilitySchema]

    class Config:
        orm_mode = True