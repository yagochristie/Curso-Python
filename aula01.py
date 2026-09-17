#O super() serve para chamar a classe pai dentro de uma classe filha 
# Serve para acessar o comportamento da classe pai sem precisar escrever o nome dela diretamente. 

class MyString(str):
    def upper (self):
        print("call upper")
        call = super().upper()
        print("after upper")
        return call

string= MyString('Yago')
print(string.upper())