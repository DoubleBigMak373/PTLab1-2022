# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from CalcQuartile import RatingCalculate
from YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = YamlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    averagePoints = CalcRating(students).calc()
    print("Средний балл:", averagePoints)
    studentsInSecondQuartile = RatingCalculate(averagePoints).getRatingSecondQuartile()
    print("Студенты во второй квартили распределения по рейтингам:",studentsInSecondQuartile)


if __name__ == "__main__":
    main()
