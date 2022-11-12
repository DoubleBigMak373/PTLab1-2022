import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str,DataType]:
        text = "- Иванов Иван Иванович:\n" +\
                "    - математика: 45\n"+\
                "    - программирование: 40\n"+\
                "    - литература: 55\n"+\
                "- Петров Петр Петрович:\n"+\
                "    - литература: 78\n"+\
                "    - программирование: 89\n"+\
                "    - математика: 45"

        data = {
            "Иванов Иван Иванович": [
            ("математика", 45), ("программирование",40), ("литература",55)
            ],
            "Петров Петр Петрович": [
            ("литература", 78) , ("программирование", 89), ("математика",45)
            ]
            }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content:tuple[str,DataType], tmpdir) -> tuple[str,DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str,DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_emptyPath(self) -> None:
        with pytest.raises(FileNotFoundError):
            str = ""
            expected_result = DataType()
            file_content = YamlDataReader().read(str)