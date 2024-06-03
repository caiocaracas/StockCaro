def mostrar_usuario(usuario:dict):
    print(" ########## INFORMAÇÕES DO USUARIO ##########")
    print("")
    print(f"ID_Usuario = {usuario['id_usuario']}")
    print(f"Residencia = {usuario['residencia_id']}")
    print(f"Nome = {usuario['nome']}")
    print(f"Email = {usuario['email']}")
    print(f"Senha = {usuario['senha']}")
    print("")
    
def mostrar_residencia(residencia:list, moradores:list):
    print("########## INFORMAÇÕES DA RESIDENCIA ##########")
    print("")
    print(f"ID_residencia = {residencia['id_residencia']}")
    print(f"Administrador da residencia = {residencia['usuario_adm_id']}")
    print(f"{moradores}")
    print("")
    
def mostrar_produtos_da_residencia(produtos:list):
    print("########## PRODUTOS REGISTRADOS NA RESIDENCIA ##########")
    print("")
    for produto in produtos:
        print(f"ID_produto_residencia = {produto['id_produto_residencia']}")
        print(f"ID residencia = {produto['residencia_id']}")
        print(f"Nome = {produto['nome']}")
        print(f"Quantidade em uma unidade = {produto['quantidade_unid']}")
        print(f"Unidade de medida = {produto['unidade_de_medida']}")
        print(f"Categoria = {produto['categoria']}")
        print(f"Preco medio = {produto['preco_medio']}")
        print("")
    
def mostrar_lista_pessoal(lista:list):
    print("########## PRODUTOS NA LISTA PESSOAL ##########")
    print("")
    for produto in lista:
        print(f"ID_produto_listado = {produto['id_produto_listado']}")
        print(f"ID_produto_residencia = {produto['produto_residencia_id']}")
        print(f"ID residencia = {produto['residencia_id']}")
        print(f"ID lista = {produto['lista_id']}")
        print(f"Quantidade = {produto['quantidade_listada']}")
        print(f"Nome = {produto['nome']}")
        print(f"Quantidade em uma unidade = {produto['quantidade_unid']}")
        print(f"Unidade de medida = {produto['unidade_de_medida']}")
        print(f"Categoria = {produto['categoria']}")
        print(f"Preco medio = {produto['preco_medio']}")
        print("")
        
def mostrar_compras(compras:list):
    print("########## COMPRAS ##########")
    print("")
    for compra in compras:
        print(f"ID_Compra = {compra['id_compra']}")
        print(f"ID residencia = {compra['residencia_id']}")
        print(f"ID de quem fez a compra = {compra['usuario_id']}")
        print(f"Data da compra = {compra['data_compra']}")
        print(f"Supermercado = {compra['supermercado']}")
        print("")
        
def mostrar_produtos_compra(produtos:list):
    print("########## PRODUTOS COMPRADOS ##########")
    print("")
    for produto in produtos:
        print(f"ID_produto_residencia = {produto['residencia_id']}")
        print(f"ID_produto_comprado = {produto['id_produto_comprado']}")
        print(f"ID compra = {produto['compra_id']}")
        print(f"Quantidade comprada = {produto['quantidade_comprada']}")
        print(f"Nome = {produto['nome']}")
        print(f"Quantidade em uma unidade = {produto['quantidade_unid']}")
        print(f"Unidade de medida = {produto['unidade_de_medida']}")
        print(f"Categoria = {produto['categoria']}")
        print(f"Preco medio = {produto['preco_medio']}")
        print("")
    
def mostrar_dispensa(dispensa:list):
    print("########## PRODUTOS NA DISPENSA ##########")
    print("")
    for produto in dispensa:
        print(f"ID_produto_comprado = {produto[1]}")
        print(f"ID_produto_residencia = {produto[0]}")
        print(f"ID compra = {produto[2]}")
        print(f"Nome = {produto['nome']}")
        print(f"Preco = {produto['preco']}")
        print(f"Quantidade em uma unidade = {produto['quantidade_unid']}")
        print(f"Unidade de medida = {produto['unidade_de_medida']}")
        print(f"Categoria = {produto['categoria']}")
        print(f"Preco medio = {produto['preco_medio']}")
        print(f"Quantidade comprada = {produto['quantidade_comprada']}")
        print(f"Quantidade existente = {produto['quantidade_existente']}")
        print("")
        
def mostrar_dividas(dividas:list):
    print("########## DIVIDAS ##########")
    print("")
    for divida in dividas:
        print(f"ID divida = {divida['id_divida']}")
        print(f"Valor = {divida['valor']}")
        print(f"ID compra = {divida['compra_id']}")
        print(f"ID Beneficiario = {divida['beneficiario']}")
        print(f"ID Pagador= {divida['pagador']}")
        print(f"Data da divida = {divida['data_divida']}")
        print(f"Data do debito = {divida['data_debito']}")
        print("")