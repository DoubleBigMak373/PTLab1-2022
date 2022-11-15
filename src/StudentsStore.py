# -*- coding: utf-8 -*-
from CalcRating import RatingType
import numpy as np

QuartileType = []

class StudentsStore:

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating
        self.result: QuartileType = {}

    def getSecondQuartileStudents(self) -> QuartileType:
        self.result = self.rating.copy()
        sorted_data = sorted(self.result.values())
        q1 = np.quantile(sorted_data, .25)
        q2 = np.quantile(sorted_data, .50)
        lis = []
        for student in self.result.items():
            if q1 <= student[1] <= q2:
               lis.append(student[0])
        return lis







