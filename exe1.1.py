# %%


frase =input("Digite a frase desejada: ")
#a função split() separa todas as palavras utilizando o  " " como delimitador
# a join vem juntando as palavras e deixando o limitador no mesmo local da frase original
invertidas = ' '.join(palavra[::-1] for palavra in frase.split())
print(frase)
print("a frase invertida: {}".format(invertidas))
# %%
