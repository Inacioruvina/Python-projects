products = []

while True :
    print ("[1]Cadastrar")
    print ("[2]Atualizar")
    print ("[3]Deletar")
    print ("[4]Mostrar Todos")
    print ("[5]Consultar (Código)")
    print ("[6]Consultar (Nome)")
    print ("[7]Sair")
    variant = int (input ("selecione uma opção:" ))
    
    match variant:
        
        case 1:
            print ("Insira as seguintes informações referentes ao produto")
            code = input ("Código do produto:")
            name = input ("Nome do produto:")
            balance = input ("Quantidade do produto:")
            value = input ("Valor do produto:")
            
            info = {
                "code": code,
                "name": name,
                "balance": balance,
                "value": value
            }
            
            products.append(info)
            
            
        case 2:
            
            for numero, info in enumerate (products, start =1):
                print (numero, "-", info["name"])
            
            i = int (input("Digite o número referente ao produto que deseja atualizar")) - 1
            
            
            
            if 0 <= i < len(products):
                    
                    yn = input ("Deseja alterar o codigo?[y][n]")
                        
                    if yn == "y":
                        cods = input ("Digite o novo codigo: ")
                        products[i]["code"] = cods
                            
                    yn = input ("Deseja alterar o nome?[y][n]")
                    if yn == "y":
                        nams = input ("Digite o novo nome: ")
                        products[i]["name"] = nams
                        
                    yn = input ("Deseja alterar a quantidade?[y][n]")
                    if yn == "y":
                        balancs = input ("Digite o novo nome: ")
                        products[i]["balance"] = balancs
                        
                    yn = input ("Deseja alterar o valor?[y][n]")
                    if yn == "y":
                        valus = input ("Digite o novo nome: ")
                        products[i]["value"] = valus
            else:
                print ("Valor invalido")
                
        case 3:
            
            for numero, info in enumerate (products, start =1):
                print (numero, "-", info["name"])
                
            i = int (input ("Digite o numero referente ao produto que será deletado")) - 1
            if 0 <= i < len(products):
                products.pop(i)
                
            else:
                print ("Produto invalido")
            
        case 4:  
            
            for numero, info in enumerate (products, start =1):
                print (numero, "-")
                print (info["code"])  
                print (info["name"])
                print (info["balance"])
                print (info["value"])  
            
        case 5:
            
            
            for numero, info in enumerate (products, start =1):
                print (numero, "-", info["code"])
                 
            print ("Qual o codigo do produto que deseja acessar?")
            
            codp = input("Digite o código do produto a ser alterado")
            
            found = False
            for info in products :
                if info ["code"] == codp :
                
                    print ("Produto encontrado")
                    print (info["code"])  
                    print (info["name"])
                    print (info["balance"])
                    print (info["value"])
                    
                    found = True
                    break
                
            if not found:
                print("Produto invalido")
            
        case 6:
            for numero, info in enumerate (products, start =1):
                print (numero, "-", info["code"])
            
            print ("Qual o nome do produto que deseja acessar?")
            
            namp = input("Digite o código do produto a ser alterado")
            
            founds = False
            for info in products :
                if info ["name"] == namp :
                
                    print ("Produto encontrado")
                    print (info["code"])  
                    print (info["name"])
                    print (info["balance"])
                    print (info["value"])
                    
                    founds = True
                    break
                    
            if not founds:
                print("Produto invalido")
                    
            
        case 7:
            
            print ("Saindo do sistema")
            break
        