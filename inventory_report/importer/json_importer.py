from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split(".")[1] != "json":
            raise ValueError("Arquivo inválido")
        with open(file_name, encoding="utf-8") as file:
            reader = json.load(file)
            return [row for row in reader]
