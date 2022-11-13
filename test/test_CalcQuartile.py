import pytest
from src.CalcRating import RatingType
from src.StudentsStore import StudentsStore

QuartileTypes = {str, float}

class TestCalcQuartile:

    def test_without_students(self):
        data: RatingType = {}
        students_store = StudentsStore(data)
        result = students_store.getSecondQuartileStudents()
        assert result == {}

    def test_with_bad_students(self):
        bad_students = self.get_bad_students()
        students_store = StudentsStore(bad_students)
        result = students_store.getSecondQuartileStudents()
        assert result == {}

    def test_with_result(self):
        good_students = self.get_good_students()
        bad_students = self.get_bad_students()

        mixed_students: RatingType = good_students | bad_students

        students_store = StudentsStore(mixed_students)
        result = students_store.getSecondQuartileStudents()

        for key in good_students.keys():
            assert key in result

    @staticmethod
    def get_good_students() -> RatingType:
        data: RatingType = {
            'Иванов Иван Иванович': 73,
            'Антонов Антон Антонович': 74,
            'Владимир Владимирович Пупкин': 63,
        }
        return data

    @staticmethod
    def get_bad_students() -> RatingType:
        data: RatingType = {
            'Альбертов Иннокентий Иванович': 42,
            'Куликова Дарья Николаевна': 41,
            'АБВ': 90,
        }
        return data

