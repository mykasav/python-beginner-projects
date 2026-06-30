import os
       
def user_exists(name):
    # Correção 3: Prevenir crash se o ficheiro não existir
    if not os.path.exists("users.txt"):
        return False
        
    with open ("users.txt","r",encoding="utf-8") as file:
        for line in file:
            clean_line=line.strip()
            if "," in clean_line:
                # Correção 1: Usar split em vez de strip
                data = clean_line.split(",")
                name_saved = data[0] 
                
                if name_saved==name:
                    return True
    return False

def auth_user(name_auth,password_auth):
    # Correção 3: Prevenir crash se o ficheiro não existir
    if not os.path.exists("users.txt"):
        return False
        
    with open ("users.txt","r",encoding="utf-8") as file:
        for line in file:
            clean_line=line.strip()
            if "," in clean_line:
                data=clean_line.split(",")
                user_saved=data[0]
                pass_saved=data[1]
                if user_saved==name_auth and pass_saved == password_auth:
                    return True
    return False

def register_new_user(name,password):
    if user_exists(name):
        return False
    
    with open ("users.txt","a",encoding="utf-8") as file:
        # Correção 2: Adicionar \n no final
        file.write(f"{name},{password}\n")
    
    with open(f"{name}_passwords.txt","w",encoding="utf-8") as file:
        pass
        
    return True
    
        
def menu_logado(nome_utilizador):
    ficheiro_pessoal = f"{nome_utilizador}_passwords.txt"
    
    while True:
        print(f"\n--- Cofre de {nome_utilizador} ---")
        print("1. Ver as minhas passwords")
        print("2. Guardar nova password")
        print("3. Apagar uma password")
        print("4. Terminar sessão (Sair)")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- As Suas Passwords ---")
            if not os.path.exists(ficheiro_pessoal) or os.stat(ficheiro_pessoal).st_size == 0:
                print("O seu cofre está vazio.")
            else:
                with open(ficheiro_pessoal, "r", encoding="utf-8") as file:
                    for linha in file:
                        linha_limpa = linha.strip()
                        if "," in linha_limpa:
                            servico, senha = linha_limpa.split(",")
                            print(f"Serviço: {servico} | Password: {senha}")
                            
        elif opcao == "2":
            servico = input("Para que serviço/site é esta password? ")
            nova_senha = input("Digite a password: ")
            with open(ficheiro_pessoal, "a", encoding="utf-8") as file:
                file.write(f"{servico},{nova_senha}\n")
            print("Password guardada com sucesso!")
            
        elif opcao == "3":
            servico_apagar = input("Qual o nome do serviço que quer apagar? ")
            
            # Para apagar, lemos tudo, filtramos o que não queremos, e reescrevemos
            linhas_mantidas = []
            apagou_algo = False
            
            with open(ficheiro_pessoal, "r", encoding="utf-8") as file:
                for linha in file:
                    if not linha.startswith(servico_apagar + ","):
                        linhas_mantidas.append(linha)
                    else:
                        apagou_algo = True
                        
            
            with open(ficheiro_pessoal, "w", encoding="utf-8") as file:
                for linha in linhas_mantidas:
                    file.write(linha)
                    
            if apagou_algo:
                print("Password apagada!")
            else:
                print("Serviço não encontrado.")
                
        elif opcao == "4":
            print("A terminar sessão...")
            break
        else:
            print("Opção inválida!")



def main():
    while True:
        print("\n=== GESTOR DE PASSWORDS ===")
        print("1. Fazer Login")
        print("2. Criar Novo Utilizador")
        print("3. Fechar Programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
    # Adicionamos .strip() para limpar espaços acidentais ao digitar
            nome = input("Nome de utilizador: ").strip() 
            senha = input("Password-Mestre: ").strip()
    
            if auth_user(nome, senha):
                print(f"\nBem-vindo de volta, {nome}!")
                menu_logado(nome) 
            else:
                print("\nERRO: Utilizador ou password incorretos!")
                
        elif opcao == "2":
            nome = input("Escolha um nome de utilizador: ")
            
            if user_exists(nome):
                print("\nERRO: Esse nome já está em uso. Escolha outro.")
            else:
                senha = input("Crie uma Password-Mestre: ")
                if register_new_user(nome, senha):
                    print(f"\nSucesso! Utilizador {nome} criado. Já pode fazer login.")
                
        elif opcao == "3":
            print("A encerrar programa...")
            break
            
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()