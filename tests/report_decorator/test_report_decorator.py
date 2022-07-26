from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)
    reset = "\033[0m"
    green = "\033[32m"
    blue = "\033[36m"
    red = "\033[31m"
    product_list = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        }
    ]
    generated_report = colored_report.generate(product_list)
    splitted_lines = generated_report.split("\n")
    splitted_first_line = splitted_lines[0].split(":")
    splitted_second_line = splitted_lines[1].split(":")
    splitted_third_line = splitted_lines[2].split(":")
    assert (
        splitted_first_line[0][0:5] == green
        and splitted_first_line[1][0:4] == reset
    )
    assert (
        splitted_first_line[1][5:10] == blue
        and splitted_first_line[1][-4:] == reset
    )
    assert (
        splitted_second_line[0][0:5] == green
        and splitted_second_line[1][0:4] == reset
    )
    assert (
        splitted_second_line[1][5:10] == blue
        and splitted_second_line[1][-4:] == reset
    )
    assert (
        splitted_third_line[0][0:5] == green
        and splitted_third_line[1][0:4] == reset
    )
    assert (
        splitted_third_line[1][5:10] == red
        and splitted_third_line[1][-4:] == reset
    )
