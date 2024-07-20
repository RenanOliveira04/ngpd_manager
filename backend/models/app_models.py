from datetime import datetime
from sqlalchemy import func, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()

@table_registry.mapped_as_dataclass
class BaseEntity:
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_date: Mapped[datetime] = mapped_column(default=func.now())
    last_modified_date: Mapped[datetime] = mapped_column(onupdate=func.now())

@table_registry.mapped_as_dataclass
class Class(BaseEntity):
    __tablename__ = 'Class'
    name: Mapped[str] = mapped_column(unique=True)
    students: Mapped[list["Student"]] = relationship("Student", back_populates="class_")
    squads: Mapped[list["Squad"]] = relationship("Squad", back_populates="class_")
    availabilities: Mapped[list["ClassAvailability"]] = relationship("ClassAvailability", back_populates="class_")

@table_registry.mapped_as_dataclass
class Student(BaseEntity):
    __tablename__ = 'Student'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    class_id: Mapped[int] = mapped_column(ForeignKey('Class.id'))
    
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

    class_: Mapped["Class"] = relationship("Class", back_populates="students")
    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="student")

Class.students = relationship("Student", order_by=Student.id, back_populates="class_")

@table_registry.mapped_as_dataclass
class Course:
    __tablename__ = 'Course'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    
    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="course")

@table_registry.mapped_as_dataclass
class Enrollment:
    __tablename__ = 'Enrollment'
    
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('Student.id'))
    course_id: Mapped[int] = mapped_column(ForeignKey('Course.id'))
    
    student: Mapped["Student"] = relationship("Student", back_populates="enrollments")
    course: Mapped["Course"] = relationship("Course", back_populates="enrollments")

Student.enrollments = relationship("Enrollment", order_by=Enrollment.id, back_populates="student")
Course.enrollments = relationship("Enrollment", order_by=Enrollment.id, back_populates="course")

@table_registry.mapped_as_dataclass
class Squad(BaseEntity):
    __tablename__ = 'Squad'
    class_id: Mapped[int] = mapped_column(ForeignKey('Class.id'))
    mentor_id: Mapped[int] = mapped_column(ForeignKey('Mentor.id'))
    company_id: Mapped[int] = mapped_column(ForeignKey('Company.id'))
    class_: Mapped["Class"] = relationship("Class", back_populates="squads")
    mentor: Mapped["Mentor"] = relationship("Mentor", back_populates="squads")
    company: Mapped["Company"] = relationship("Company")
    squad_availabilities: Mapped[list["SquadAvailability"]] = relationship("SquadAvailability", back_populates="squad")

@table_registry.mapped_as_dataclass
class Mentor(BaseEntity):
    __tablename__ = 'Mentor'
    name: Mapped[str]
    squads: Mapped[list["Squad"]] = relationship("Squad", back_populates="mentor")
    mentor_availabilities: Mapped[list["MentorAvailability"]] = relationship("MentorAvailability", back_populates="mentor")

@table_registry.mapped_as_dataclass
class Faculty(BaseEntity):
    __tablename__ = 'Faculty'
    name: Mapped[str]
    classes: Mapped[list["Class"]] = relationship("Class")

@table_registry.mapped_as_dataclass
class Company(BaseEntity):
    __tablename__ = 'Company'
    name: Mapped[str]
    company_availabilities: Mapped[list["CompanyAvailability"]] = relationship("CompanyAvailability", back_populates="company")

@table_registry.mapped_as_dataclass
class SquadAvailability(BaseEntity):
    __tablename__ = 'SquadAvailability'
    squad_id: Mapped[int] = mapped_column(ForeignKey('Squad.id'))
    day_of_week: Mapped[int]
    start_time: Mapped[Time]
    end_time: Mapped[Time]
    squad: Mapped["Squad"] = relationship("Squad", back_populates="squad_availabilities")

@table_registry.mapped_as_dataclass
class MentorAvailability(BaseEntity):
    __tablename__ = 'MentorAvailability'
    mentor_id: Mapped[int] = mapped_column(ForeignKey('Mentor.id'))
    day_of_week: Mapped[int]
    start_time: Mapped[Time]
    end_time: Mapped[Time]
    mentor: Mapped["Mentor"] = relationship("Mentor", back_populates="mentor_availabilities")

@table_registry.mapped_as_dataclass
class CompanyAvailability(BaseEntity):
    __tablename__ = 'CompanyAvailability'
    company_id: Mapped[int] = mapped_column(ForeignKey('Company.id'))
    day_of_week: Mapped[int]
    start_time: Mapped[Time]
    end_time: Mapped[Time]
    company: Mapped["Company"] = relationship("Company", back_populates="company_availabilities")

@table_registry.mapped_as_dataclass
class ClassAvailability(BaseEntity):
    __tablename__ = 'ClassAvailability'
    class_id: Mapped[int] = mapped_column(ForeignKey('Class.id'))
    day_of_week: Mapped[int]
    start_time: Mapped[Time]
    end_time: Mapped[Time]
    class_: Mapped["Class"] = relationship("Class", back_populates="availabilities")