from sqlalchemy import select

from backend.models.app_models import Student


def test_student_model(session):
    new_student = Student(username='alice', password='secret', email='teste@test')
    session.add(new_student)
    session.commit()

    student = session.scalar(select(Student).where(Student.username == 'alice'))

    assert student.username == 'alice'
