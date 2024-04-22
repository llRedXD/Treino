# class teste():
#     nome:str 
#     senha:str
#     idade:int
    
#     def __init__(self, nome:str, senha:str, idade:int):
#         self.nome = nome
#         self.senha = senha
#         self.idade = idade
        
# usuario1 = teste("joao", "123", 20)
# print(usuario1.nome)

def teste(nome):
    nomeFormato = f'Bom dia {nome}'
    return nomeFormato
    
nome = teste("joao")
    
print(nome)

