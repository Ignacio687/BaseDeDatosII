from abc import ABCMeta, abstractmethod
from typing import Any
import json
from pymongo import MongoClient

class GeneratorABC(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def generateJsonObj(self, key:str, element: Any) -> dict[str, Any]:
        pass

    def generateJsonFile(self, registros: dict[str, Any], name:str) -> None:
        registros_json = json.dumps(registros, indent=4)
        with open(f'data/{name.lower()}.json', 'w') as archivo_json:
            archivo_json.write(registros_json)

    @abstractmethod
    def generateData(self, name:str, data_base) -> list[dict[str, Any]]:
        pass