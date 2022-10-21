from banksystem import nubanco

if __name__ =="__main__":
    
    bank = nubanco()

    while True:
        print("\n\nDigite 1 para fazer um saque")
        print("Digite 2 para fazer um deposito")
        print("Digite 3 para ver o saldo")
        print("Digite 4 para ver o historico de transações")
        print("Digite 5 para sair\n\n")
        escolha = str(input("Sua escolha? 1 2 3 4 ou 5? ")).strip()
        print("\n\n")

        if (escolha[0]!="1" and escolha[0]!="2" and escolha[0]!="3" and escolha[0]!="4" and escolha[0]!="5"):
            print("RESPONDE DIREITO!!! \n\n")

        elif escolha[0] == "1":
            bank.sacarDinheiro()
            
        elif escolha[0] == "2":
            bank.depositarDinheiro()

        elif escolha[0] == "3":
            bank.mostrar_saldo()
            
        elif escolha[0] == "4":
            bank.mostrar_historico()

        elif escolha[0] == "5":
            break

print("\n===================== seção finalizada =========================\n")