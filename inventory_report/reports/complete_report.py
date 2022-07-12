from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def product_quantity_by_company(product_dict):
        company_name_list = CompleteReport.company_names(product_dict)
        no_repetition_name_list = list(dict.fromkeys(company_name_list))
        name_quantity_tuple_list = [
            (name, company_name_list.count(name))
            for name in no_repetition_name_list
        ]
        return "".join(
            f"- {name_tuple[0]}: {name_tuple[1]}\n"
            for name_tuple in name_quantity_tuple_list
        )

    @staticmethod
    def generate(product_dict):
        return (
            f"{SimpleReport.generate(product_dict)}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.product_quantity_by_company(product_dict)}"
        )
