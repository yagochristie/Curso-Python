#O super() serve para chamar a classe pai dentro de uma classe filha 

class MyString(str):
    def upper (self):
        print("call upper")
        call = super().upper()
        print("after upper")
        return call

string= MyString('Yago')
print(string.upper())

print('teste')
print('teste2')