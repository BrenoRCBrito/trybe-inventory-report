import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

TYPES = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        _, file_path, report_type = sys.argv
        inventory = InventoryRefactor(TYPES[file_path.split(".")[1]])
        data = inventory.import_data(file_path, report_type)
        print(data, end="")
