products = []


def load_products():

    arquivo = open("products.txt", "r")

    linhas = arquivo.readlines()

    arquivo.close()

    i = 0

    while i < len(linhas):

        code = linhas[i].strip()
        category = linhas[i + 1].strip()
        name = linhas[i + 2].strip()
        balance = linhas[i + 3].strip()
        value = linhas[i + 4].strip()

        info = {
            "code": code,
            "category": category,
            "name": name,
            "balance": balance,
            "value": value
        }

        products.append(info)

        i = i + 5


def save_products():

    arquivo = open("products.txt", "w")

    for info in products:

        arquivo.write(info["code"] + "\n")
        arquivo.write(info["category"] + "\n")
        arquivo.write(info["name"] + "\n")
        arquivo.write(info["balance"] + "\n")
        arquivo.write(info["value"] + "\n")

    arquivo.close()


def show_all():

    if len(products) == 0:

        print("Nenhum produto cadastrado.")

    else:

        for numero, info in enumerate(products, start=1):

            print()
            print("Produto", numero)
            print("Código:", info["code"])
            print("Categoria:", info["category"])
            print("Nome:", info["name"])
            print("Quantidade:", info["balance"])
            print("Valor:", info["value"])


load_products()


while True:

    print()
    print("[1] Cadastrar")
    print("[2] Atualizar")
    print("[3] Deletar")
    print("[4] Mostrar Todos")
    print("[5] Consultar (Código)")
    print("[6] Consultar (Nome)")
    print("[7] Salvar e sair")

    variant = int(input("Selecione uma opção: "))

    match variant:

        case 1:
            print("Insira as seguintes informações referentes ao produto")
            code = input("Código do produto: ")
            category = input("Digite a categoria em que o produto se encaixa: ")
            name = input("Nome do produto: ")
            balance = input("Quantidade do produto: ")
            value = input("Valor do produto: ")
            info = {
                "code": code,
                "category": category,
                "name": name,
                "balance": balance,
                "value": value
            }

            products.append(info)
            save_products()

            print("Produto cadastrado com sucesso!")

        case 2:

            for numero, info in enumerate(products, start=1):
                print(numero, "-", info["name"]) 

            i = int(
                input(
                    "Digite o número referente ao produto que deseja atualizar: "
                )
            ) - 1

            if 0 <= i < len(products):

                yn = input("Deseja alterar o código? [y][n] ")

                if yn == "y":
                    cods = input("Digite o novo código: ")
                    products[i]["code"] = cods

                yn = input("Deseja alterar a categoria? [y][n] ")

                if yn == "y":
                    categors = input("Digite a nova categoria: ")
                    products[i]["category"] = categors

                yn = input("Deseja alterar o nome? [y][n] ")

                if yn == "y":
                    nams = input("Digite o novo nome: ")
                    products[i]["name"] = nams

                yn = input("Deseja alterar a quantidade? [y][n] ")

                if yn == "y":
                    balancs = input("Digite a nova quantidade: ")
                    products[i]["balance"] = balancs

                yn = input("Deseja alterar o valor? [y][n] ")

                if yn == "y":
                    valus = input("Digite o novo valor: ")
                    products[i]["value"] = valus

                save_products()

                print("Produto atualizado com sucesso!")

            else:

                print("Valor inválido")

        case 3:

            for numero, info in enumerate(products, start=1):
                print(numero, "-", info["name"]) 

            i = int(
                input(
                    "Digite o número referente ao produto que será deletado: "
                )
            ) - 1

            if 0 <= i < len(products):

                products.pop(i)
                save_products()

                print("Produto deletado com sucesso!")

            else:

                print("Produto inválido")

        case 4:

            show_all()

        case 5:

            for numero, info in enumerate(products, start=1):
                print(numero, "-", info["code"]) 

            print("Qual o codigo do produto que deseja acessar?")
            codp = input("Digite o código do produto: ")

            found = False

            for info in products:

                if info["code"] == codp:

                    print()
                    print("Produto encontrado")
                    print("Código:", info["code"])
                    print("Categoria:", info["category"])
                    print("Nome:", info["name"])
                    print("Quantidade:", info["balance"])
                    print("Valor:", info["value"])

                    found = True

                    break

            if not found:

                print("Produto inválido")

        case 6:
        case 6:

            for numero, info in enumerate(products, start=1):
                print(numero, "-", info["code"]) 

            print("Qual o nome do produto que deseja acessar?")
            namp = input("Digite parte do nome do produto a ser pesquisado: ")

            founds = False

            for info in products:

                if namp.lower() in info["name"].lower():

                    print()
                    print("Produto encontrado")
                    print("Código:", info["code"])
                    print("Categoria:", info["category"])
                    print("Nome:", info["name"])
                    print("Quantidade:", info["balance"])
                    print("Valor:", info["value"])

                    founds = True

            if not founds:
                print("Produto inválido")

        case 7:

            save_products()

            print("Salvando dados...")
            print("Saindo do sistema...")
            print("Salvando dados...")
            print("Saindo do sistema...")

            break

        case _:

            print("Opção inválida.")

