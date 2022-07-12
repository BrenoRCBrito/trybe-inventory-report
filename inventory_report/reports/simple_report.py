from datetime import date


class SimpleReport:
    @staticmethod
    def older_fabrication_date(product_dict):
        return sorted(
            product_dict, key=lambda x: x["data_de_fabricacao"], reverse=False
        )[0]["data_de_fabricacao"]

    @staticmethod
    def older_validation_date(product_dict):
        return sorted(
            product_dict,
            key=lambda x: x["data_de_validade"]
            if date.fromisoformat(x["data_de_validade"])
            > date.fromisoformat(x["data_de_fabricacao"])
            else "9999-99-99",
            reverse=False,
        )[0]["data_de_validade"]

    @staticmethod
    def company_names(product_dict):
        return [product["nome_da_empresa"] for product in product_dict]

    @staticmethod
    def generate(product_dict):
        fabrication_date = SimpleReport.older_fabrication_date(product_dict)
        validation_date = SimpleReport.older_validation_date(product_dict)
        company_name_list = SimpleReport.company_names(product_dict)
        nome = max(set(company_name_list), key=company_name_list.count)
        return (
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {validation_date}\n"
            f"Empresa com mais produtos: {nome}"
        )
