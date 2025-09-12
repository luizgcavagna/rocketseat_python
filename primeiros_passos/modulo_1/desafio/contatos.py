def adicionar_contato(contatos, nome, telefone, email):
    
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)

    print(f"{nome} adicionado com sucesso!")

    return

def ver_contatos(contatos):

    print("\nLista de contatos")
    
    for indice, contato in enumerate(contatos, start=1):
        favorito = "𖤐" if contato["favorito"] else " "
        nome_contato= contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. {favorito} {nome_contato} \n     Telefone: {telefone}\n     E-mail: {email}")

    return

def ver_contatos_favoritos(contatos):

    print("\nLista de contatos favoritos")
    
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favorito = "𖤐" if contato["favorito"] else " "
            nome_contato= contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. {favorito} {nome_contato} \n     Telefone: {telefone}\n     E-mail: {email}")

    return

def editar_contato(contatos, indice_contato, nome, telefone, email):
    indice = int(indice_contato) - 1
    
    if indice >= 0 and indice < len(contatos):
        contato = contatos[indice]
        if nome != "":
            contato["nome"] = nome
        if email != "":
            contato["email"] = email
        if telefone != "":
            contato["telefone"] = telefone

        print(f"Contato {indice} atualizado para {contato["nome"]} \n   Telefone: {contato["telefone"]}\n   E-mail: {contato["email"]}")
    else:
        print("Indice de Contato invalido")

    return

def favoritar_contato(contatos, indice_contato):
    indice = int(indice_contato) - 1

    contatos[indice]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito")
    
    return

def deletar_contato(contatos, indice_contato):
    indice = int(indice_contato) - 1

    if indice >= 0 and indice < len(contatos):
        contatos.remove(contatos[indice])
    
    print("Contato deletado com sucesso!")

    return

contatos = []

while True:
    print("\nMenu do gerenciador de Lista de contatos:")
    print("1. Adicionar Contato")
    print("2. Ver contatos")
    print("3. Atualizar Contato")
    print("4. Favoritar contato")
    print("5. Contatos Favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do contato que deseja adicionar: ")
        telefone = input("Digite o telefone do contato que deseja adicionar: ")
        email = input("Digite o e-mail do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ")
        nome = input("Digite o novo nome do contato ou deixe em branco para nao atualizar: ")
        telefone = input("Digite o novo telefone do contato ou deixe em branco para nao atualizar: ")
        email = input("Digite o novo e-mail do contato ou deixe em branco para nao atualizar: ")
        editar_contato(contatos, indice_contato, nome, telefone, email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja marcar como favorito: ")
        favoritar_contato(contatos, indice_contato)
    
    elif escolha == "5":
        ver_contatos_favoritos(contatos)

    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ")
        deletar_contato(contatos, indice_contato)
        ver_contatos(contatos)

    elif escolha == "7":
        break

print("Programa finalizado")