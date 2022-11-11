# -*- coding: utf-8 -*-
from CalcRating import RatingType

QuartileType = (str, float)

class RatingCalculate:

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating
        self.result: QuartileType = {}

    def getRatingSecondQuartile(self) -> QuartileType:
        self.result = self.rating.copy()
        self.result = {key:val for key,val in self.result.items() if 50 <= val <= 75 }
        return self.result








