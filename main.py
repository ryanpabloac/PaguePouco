import pymysql
from os import system
from datetime import  datetime, date

def menu():
    print("===== PAGUE POUCO ===== \n Selecione a opção que deseja:")
    print("[0] -> Pesquisar medicamento")
    print("[1] -> Cadastrar novo produto")
    print("[2] -> Cadastrar novo farmacêutico")
    print("[3] -> Cadastrar novo cliente")
    print("[4] -> Atualizar estoque")
    print("[5] -> Realizar Venda")
    print("[6] -> Relatório")
    return int(input("Digite aqui: "))
def procurarMedicamento():
    pesquisa = input("Digite o composto ou nome do medicamento: \n")

    if pesquisa == '#':
        conexao.close()
        print("\n Programa Finalizado! ")
        exit()
    elif pesquisa == '/':
        return 'continuar'

    cursor.execute(f"SELECT * FROM produto WHERE nomeProduto LIKE '%{pesquisa}%' OR composto LIKE '%{pesquisa}%';")
    resposta = cursor.fetchall()
    if len(resposta) == 0:
        return print("Produto não encontrado!")
    else:
        for i in range(len(resposta)):
            print(resposta[i])
def cadastrarProduto():
    try:
        nome = input("Digite o nome do produto com sua determinada porção:  ").capitalize()
        composto = input("Digite o composto do medicamento:  ")
        qtde = int(input("Quantidade em estoque:  "))
        dt_validade = input("Digite a data de validade [AAAA-MM-DD]:  ")
        v_compra = float(input("Valor de compra:  R$"))
        v_venda = float(input("Valor de venda: R$"))

        cursor.execute(f"INSERT INTO produto(nomeProduto, composto, qtdeEstoque, valorCusto, valorVenda, dtValidade) VALUES ('{nome}', '{composto}', {qtde}, {v_compra}, {v_venda}, '{dt_validade}')")
        conexao.commit()

        print("\n Produto adicionado com sucesso!")
    except ValueError:
        print("Entrada Inválida. Tente novamente!")
def cadastrarFarmaceutico():
        try:
            nome = input("Digite o nome do farmacêutico:  ").capitalize()
            crf = input("Digite o CRF com 5 dígitos:  ")
            local_registro = input("Digite a sigla do Estado de registro:  ")
            telefone = input("Digite o telefone com DDD sem formatação:  ")

            cursor.execute(f"INSERT INTO farmaceutico(nomeFarmaceutico, crf, localRegistro, telefone) VALUES ('{nome}', '{crf}', '{local_registro}', '{telefone}')")
            conexao.commit()

            print("\n Farmaceutico adicionado com sucesso!")
        except ValueError:
            print("Entrada Inválida. Tente novamente!")
def cadastrarCliente():
    try:
        nome = input("*Digite o nome do cliente:  ").capitalize()
        cpf = input("Digite o CPF sem formatação(opcional):  ")
        dt_nasc = input("Digite a data de nascimento (opcional) AAAA-MM-DD:  ")
        telefone = input("*Digite o telefone com DDD sem formatação:  ")
        endereco = input("Digite o endereço(opcional):  ")

        cursor.execute(f"INSERT INTO cliente(nomeCliente, cpf, dtNasc, telefone, endereco) VALUES ('{nome}', '{cpf}', '{dt_nasc}', '{telefone}', '{endereco}')")
        conexao.commit()

        print("\n Cliente adicionado com sucesso!")
    except ValueError:
        print("Entrada Inválida. Tente novamente!")
def controleEstoque():
    print("O que deseja fazer?")
    print("[0] -> Aumentar estoque \n[1] -> Diminuir estoque")
    op  = int(input("| -> "))
    
    if op == 0:
        
        id_produto = int(input("Digite o ID do produto que deseja aumentar o estoque: "))
        estoque = int(input("Quanto deseja adicionar: "))
        cursor.execute(f"SELECT nomeProduto, qtdeEstoque FROM produto WHERE idProduto = {id_produto}")
        resp = cursor.fetchall()
        total = resp[0][1] + estoque
        print(f"Estoque de {resp[0][0]} atualizado: ", total)

        cursor.execute(f"UPDATE produto SET qtdeEstoque = {total} WHERE idProduto = {id_produto}")
        conexao.commit()
    elif op == 1:
        print("Conhece o id do produto a alterar? [s/n]")
        x = input("| -> ").lower()

        if x == "n":
            print(" ")
            procurarMedicamento()
            print(" ")
        id_produto = int(input("Digite o ID do produto que deseja diminuir o estoque: "))
        estoque = int(input("Quanto deseja retirar: "))
        cursor.execute(f"SELECT nomeProduto, qtdeEstoque FROM produto WHERE idProduto = {id_produto}")
        resp = cursor.fetchall()
        if estoque > int(resp[0][1]):
            print(f"A quantidade retirada é maior que o estoque disponível. \nEstoque disponível = {resp[0][0]}")
        else:
            total = int(resp[0][1]) - estoque 
            print(f"Estoque de {resp[0][0]} atualizado: ", total)

        cursor.execute(f"UPDATE produto SET qtdeEstoque = {total} WHERE idProduto = {id_produto}")
        conexao.commit()
def realizarVenda():
    dt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    print("FARMACEUTICO \n------------")
    func = int(input("ID do farmacêutico em atendimento: "))
    system('cls')

    print("CLIENTE \n-------")
    print("[0] -> Cliente existente \n[1] -> Novo Cliente")
    op = int(input("|-> "))
    if op == 1:
        cadastrarCliente()
        print("\n")
    elif op == 0:
        print("\n Consulta de Cliente \n")
        cliente = input("Digite nome e/ou sobrenome do cliente: \n|-> ")
        cursor.execute(f"SELECT idCliente, nomeCliente FROM cliente WHERE nomeCliente LIKE '%{cliente}%';")
        resp = cursor.fetchall()
        for indice in range(len(resp)):
            print(resp[indice])
        cliente = int(input("Selecione o ID do cliente desejado: "))

    cursor.execute(f"INSERT INTO venda(idFarmaceutico, idCliente, DataVenda) VALUES ({func}, {cliente}, '{dt}');")
    conexao.commit()

    cursor.execute(f"SELECT idVenda FROM venda WHERE DataVenda = '{dt}' AND idCliente = {cliente}")
    venda = cursor.fetchall()
    venda = int(venda[0][0])
    system('cls')
    print(f"O ID da sua venda será: {venda} \n")

    print("PRODUTO\n-------")
    valor_total = 0
    while True:
        datetime.today()
        op = input("Deseja pesquisar produto? [s/n]: ")
        
        while True:
            if op == 's':
                print("Digite '#' para sair")
                ans = procurarMedicamento()
                print("\n")

                if ans == "Produto não Encontrado!":
                    pass
                
                break
            else:
                break
                
        prod = int(input("ID do produto desejado: "))
        qtd = int(input("Quantidade comprada: "))
        
        cursor.execute(f"SELECT nomeProduto,valorVenda FROM produto WHERE idProduto = {prod}")
        r = cursor.fetchall()
        nome, valor_uni, valor_c = r[0][0], r[0][1], float(r[0][1] * qtd)
        valor_total  += float(valor_c)

        print(f"\nCONFIRME AS INFORMAÇÕES \n Nome do Produto = {nome} \n Valor Unitário  =R${valor_uni} \n Qtde Comprada = {qtd} \n Valor Total = R${valor_c} ")
        i = input("Tudo certo? [s/n]: ").lower()
        if i == 'n':
            print("Reinicie o programa para resetar!")
            break
        cursor.execute(f"INSERT INTO vendaproduto(qtdeVendida, idProduto, idVenda) VALUES ({qtd}, {prod}, {venda});")
        conexao.commit()
        op = input("\n Algo mais? [s/n]: ")
        if op == 'n':
            break
    system('cls')

    cursor.execute(f"SELECT produto.idProduto, produto.nomeProduto, vendaproduto.qtdeVendida, produto.valorVenda FROM vendaproduto JOIN produto ON produto.idProduto = vendaproduto.idProduto WHERE idVenda = {venda};")
    resp = cursor.fetchall()

    print("RESUMO DO PEDIDO \n")
    print("ID|Nome do Produto|QTDE|Valor Unitário|")
    print("----------------------------------------------------------------------")
    for resultado in resp:
        print(resultado)
    print(f"\n Valor Total: R${valor_total}")
    resp = input("\n Tudo Certo? [s/n]: ").lower()
    if resp == 'n':
        cursor.execute(f"DELETE FROM venda WHERE idVenda = {venda}")
        conexao.commit()
        print("\n Programa Finalizado!")
        conexao.close()
        exit()

    cursor.execute(f"INSERT INTO venda(idFarmaceutico, idCliente, DataVenda) VALUES ({func}, {cliente}, '{dt}');")
    conexao.commit()
def relatorio():
    ANO_ATUAL, ano= int(date.today().strftime("%Y")), int(date.today().strftime("%Y"))
    anos=[ANO_ATUAL]
    
    for _ in range(4):
        anos.append(ano - 1)
        ano -= 1
    print("\n VENDAS NOS ÚLTIMOS 5 ANOS")
    for data in anos:
        cursor.execute(f"SELECT COUNT(DataVenda) FROM venda WHERE DataVenda LIKE '{data}%';")
        resultado = cursor.fetchone()
        print(f"{data} => {resultado[0]} vendas")

    print("\n LUCRO LÍQUIDO NOS ULTIMOS 5 ANOS")
    cursor.execute(f"SELECT YEAR(venda.DataVenda), SUM(qtdeVendida), SUM(produto.valorVenda), SUM(produto.valorCusto) FROM vendaproduto JOIN venda ON venda.idVenda = vendaproduto.idVenda  JOIN produto ON produto.idProduto = vendaproduto.idProduto GROUP BY YEAR(venda.DataVenda) ORDER BY YEAR(venda.DataVenda) ASC;")
    resultado = cursor.fetchall()
    for ano in range(5):
        data, qtd_total, venda_total, custo_total = resultado[ano][0], int(resultado[ano][1]), resultado[ano][2], resultado[ano][3]
        lucro_liquido = (venda_total*qtd_total) - (custo_total*qtd_total)
        print(f"{data} => R${lucro_liquido:.2f}")

    print(f"\n ANO ATUAL ({ANO_ATUAL})")
    farmaceutico = []
    qtd_vendida = []
    cursor.execute(f"""SELECT Farmaceutico.nomeFarmaceutico, COUNT(venda.idFarmaceutico) FROM vendaproduto 
                   JOIN venda ON venda.idVenda = vendaproduto.idVenda 
                   JOIN farmaceutico ON farmaceutico.idFarmaceutico = venda.idFarmaceutico 
                   WHERE venda.DataVenda LIKE '{ANO_ATUAL}%'
                   GROUP BY farmaceutico.idFarmaceutico;""")
    resultado = cursor.fetchall()
    for funcionario in range(len(resultado)):
        farmaceutico.append(resultado[funcionario][0])
        qtd_vendida.append(resultado[funcionario][1])
    i = qtd_vendida.index(max(qtd_vendida))
    print(f"Farmacêutico com mais vendas: {farmaceutico[i]}")

    produto = []
    qtd_vendida_prod = []
    cursor.execute(f"""SELECT produto.nomeProduto, COUNT(vendaproduto.idProduto), COUNT(vendaproduto.qtdeVendida) 
                   FROM vendaproduto
                   JOIN venda ON venda.idVenda = vendaproduto.idVenda 
                   JOIN produto ON produto.idProduto = vendaproduto.idProduto 
                   WHERE venda.DataVenda LIKE "{ANO_ATUAL}%" 
                   GROUP BY produto.idProduto;""")
    resultado = cursor.fetchall()
    for medicamento in range(len(resultado)):
        produto.append(resultado[medicamento][0])
        qtd_vendida_prod.append(resultado[medicamento][1] * resultado[medicamento][2])
    i = qtd_vendida_prod.index(max(qtd_vendida_prod))
    print(f"Produto mais vendido: {produto[i]}")

conexao = pymysql.Connection(
    host='localhost',
    user= 'root',
    password= '1234',
    database= 'pague_pouco'
)
cursor = conexao.cursor()

while True:
    opcao = 0
    opcao = menu()
    system('cls')
    print("===== PAGUE POUCO ===== \n ")

    match(opcao):
        case 0:
            procurarMedicamento()
        case 1:
            cadastrarProduto()
        case 2:
            cadastrarFarmaceutico()
        case 3:
            cadastrarCliente()
        case 4:
            controleEstoque()  
        case 5:
            realizarVenda()
        case 6:
            relatorio()
        case _:
            print("Opção inválida! Tente Novamente.")
    
    print(" ")
    print("Deseja realizar outro atendimento: \n[s] -> sim \n[n] -> não")
    x = input().lower()
    system('cls')

    if x != 's':
        print("PROGRAMA FINALIZADO")
        break

conexao.close()