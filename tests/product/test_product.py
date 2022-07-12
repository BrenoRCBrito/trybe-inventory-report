from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, "Bolo", "Padaria", "01-01-2020", "01-12-2020", "11111", "Geladeira"
    )
    assert product.id == 1
    assert product.nome_do_produto == "Bolo"
    assert product.nome_da_empresa == "Padaria"
    assert product.data_de_fabricacao == "01-01-2020"
    assert product.data_de_validade == "01-12-2020"
    assert product.numero_de_serie == "11111"
    assert product.instrucoes_de_armazenamento == "Geladeira"


def test_relatorio_produto():
    product = Product(
        1, "Bolo", "Padaria", "01-01-2020", "01-12-2020", "11111", "Geladeira"
    )
    assert (
        str(product.__repr__()) == f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
