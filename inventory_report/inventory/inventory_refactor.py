from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, report_type):
        file_content = self.importer.import_data(path)
        for product in file_content:
            self.data.append(product)
        if report_type == "completo":
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)
