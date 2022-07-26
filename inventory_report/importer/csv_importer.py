from inventory_report.importer.importer import Importer


import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split(".")[1] != "csv":
            raise ValueError("Arquivo inválido")
        with open(file_name, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in reader]
