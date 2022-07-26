import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def open_csv(path):
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return [row for row in reader]

    @staticmethod
    def open_json(path):
        with open(path, encoding="utf-8") as file:
            reader = json.load(file)
            return [row for row in reader]

    @staticmethod
    def open_xml(path):
        with open(path, encoding="utf-8") as file:
            xml_dict = xmltodict.parse(file.read())
            return xml_dict["dataset"]["record"]

    @staticmethod
    def import_data(path, report_type):
        file_type = path.split(".")[1]
        report = None
        products = None
        if file_type == "csv":
            products = Inventory.open_csv(path)
        elif file_type == "json":
            products = Inventory.open_json(path)
        else:
            products = Inventory.open_xml(path)
        if report_type == "completo":
            report = CompleteReport.generate(products)
        else:
            report = SimpleReport.generate(products)
        return report
