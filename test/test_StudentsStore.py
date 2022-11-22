import pytest
from src.CalcRating import RatingType
from src.StudentsStore import StudentsStore

QuartileTypes = {str, float}

class TestStudentsStore:

    def test_without_students(self):
        data: RatingType = {}
        students_store = StudentsStore(data)
        result = students_store.getSecondQuartileStudents()
        assert result == data

    def test_with_result(self):
        students = self.get_students()
        students_store = StudentsStore(students)
        result = students_store.getSecondQuartileStudents()
        assert "Антонов Антон Антонович", 2 in result
        assert "Владимир Владимирович Пупкин", 3 in result

    @staticmethod
    def get_students() -> RatingType:
        data: RatingType = {
            'Иванов Иван Иванович': 1,
            'Антонов Антон Антонович': 2,
            'Владимир Владимирович Пупкин': 3,
            'Альбертов Иннокентий Иванович': 4,
            'Куликова Дарья Николаевна': 5
        }
        return data
