from DataReader import DataReader
from Types import DataType
import yaml

''''
DataType = dict[str, list[tuple[str, int]]]
'''
class YamlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as stream:
            read_data = yaml.full_load(stream)
        for string in read_data:
            for name in string:
                self.key = name
                self.students[self.key] = []
                for subject in string[name]:
                    for score in subject:
                        self.students[self.key].append(
                            (score, int(subject[score])))
        return self.students
