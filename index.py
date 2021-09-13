# Mystic Dungeon
# Bem Vindo ao RPG do Grupo 5.
import random


print("\n---------------------------------------------------------------------------")
nome = str(input("\n Olá jogador, qual o seu nome?\n"))
print("\n---------------------------------------------------------------------------")
classe = int(input("\n{}, agora escolha classe\n[1] - Grandioso Mago\n[2] - Honorável Cavaleiro\n[3] - Renomado Arqueiro\n".format(nome)))
print("\n---------------------------------------------------------------------------")

if (classe == 1):
    classe = "Grandioso Mago"
    print("\nEscolheu a classe Grandioso Mago")
elif(classe == 2):
    classe = "Honorável Cavaleiro"
    print("\nEscolheu a classe Honorável Cavaleiro")
elif(classe == 3):
    classe = "Renomado Arqueiro"
    print("\nEscolheu a classe Renomado Arqueiro")
else:
    classe = "Pobre"
    print("\nEscolheu a classe secreta POBRE")

#:ok_hand:

print("\n---------------------------------------------------------------------------")

print("\n {} {}, Bem-Vindo á Mystic Dungeon, desbrave essa grande aventura em busca pelo fragmento da pedra mágica.\n".format(classe,nome))

print("\n---------------------------------------------------------------------------")

print("\n Olha {} cuidado,Mystic Dungeon tem varias armadilhas cuidado para nao cair \n".format(nome))

print(" A cada sala que você entra uma pedra desliza da caverna se passar por + de 7 salas a caverna caíra e voce morrerá\n".format(nome))