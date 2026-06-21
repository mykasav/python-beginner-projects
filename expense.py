#yooo expense tracker type shit
# funcionalidades: meter as expenses, calcular quantas expenses temos no total, no que gastamos
#poder aceder as expenses duma forma kawai >_<
#menu, registar gasto, ver os gastos

class exepensetracker:
    def __init__(self):
        # É melhor criar a lista aqui dentro como variável do objeto
        self.listex = []
        
    def registerex(self, expense):
        # Append não precisa de return, ele só adiciona à lista
        self.listex.append(expense)
        
    def checkex(self):
        return self.listex
    
    def removeex(self, removed):
        # Em vez de um for-loop problemático, usamos o operador "in" na própria lista
        if removed in self.listex:
            self.listex.remove(removed)
        else:
            print("Nao tens isso ai")

def main():
    
    ex = exepensetracker()
    
    while True:
        print("\n1.Register Expense\n2.Check Expenses \n3.Remove Expense\n4.Exit")
        
        
        try:
            answer = int(input("What u want: 1, 2, 3 ou 4? "))
        except ValueError:
            print("Please enter a valid number!")
            continue # Volta para o início do menu se não for número
            
        
        if answer == 1:
            while True:
                try:
                    expense = int(input("SO whats ur expense: "))
                    ex.registerex(expense)
                    
                    # Correção do `.lower` -> precisa de parênteses e fica no final do input!
                    validation = input("Queres adicionar outra coisa?:(S/N) ").lower()
                    
                    # Correção da lógica: se for "n", é que damos break!
                    if validation == "n":
                        break
                    else:
                        continue
                except ValueError:
                    print("Gimme sum valid")
        
        elif answer == 2:
           
            print(ex.checkex())
        
        elif answer == 3:
            while True:
                print(ex.checkex())
                try:
                    removeex = int(input("What expense you wanna remove: "))
                    ex.removeex(removeex)
                except ValueError:
                    print("Gimme sum valid")
                    continue
                
                validation = input("Wanna remove sum else: (S/N) ").lower()
                if validation == "n":
                    break
                else:
                    continue
                    
        elif answer == 4:
            print("Bye bye! >_<")
            break # Quebra o loop principal e encerra o programa

if __name__ == "__main__":
    main()