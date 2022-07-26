from inventory_report.importer.importer import Importer

import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split(".")[1] != "xml":
            raise ValueError("Arquivo inválido")
        with open(file_name, encoding="utf-8") as file:
            xml_dict = xmltodict.parse(file.read())
            return xml_dict["dataset"]["record"]
