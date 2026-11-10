def buscar_item(catalogo, nome):

    raise NotImplementedError


def mostrar_catalogo(catalogo):

    raise NotImplementedError


def mostrar_inventario(heroi):

    print(f"{heroi['nome']} tem {heroi['ouro']} moedas.")
    if len(heroi["inventario"]) == 0:
        print("Inventário vazio.")
    for nome, quantidade in heroi["inventario"].items():
        print(f"  {quantidade} x {nome}")


def comprar(heroi, catalogo, nome, quantidade=1):

    raise NotImplementedError


def vender(heroi, catalogo, nome, quantidade=1):

    raise NotImplementedError
