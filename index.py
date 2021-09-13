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



print("\n---------------------------------------------------------------------------")

print("\n {} {}, Bem-Vindo á Mystic Dungeon, desbrave essa grande aventura em busca pelo fragmento da pedra mágica.\n".format(classe,nome))

print("\n---------------------------------------------------------------------------")

print("\n Olha {} cuidado,Mystic Dungeon tem varias armadilhas cuidado para nao cair \n".format(nome))

print(" A cada sala que você entra uma pedra desliza da caverna se passar por + de 7 salas a caverna caíra e voce morrerá\n".format(nome))

salaAtual = 1
interacoes = 0

while(salaAtual != 9  and interacoes < 7):
    if(salaAtual == 6):
        print("\n---------------------------------------------------------------------------")
        print("\n ALERTA: PEDRAS CAIDAS: {}".format(interacoes))
        print("\n{} {}, Você está na sala: {}\n".format(classe,nome,salaAtual))
        escolha = int(input("Escolha seu caminho:\n[2] - Caminho preto\n"))
        salaAtual = salaAtual+2
        interacoes = interacoes+1
    elif(salaAtual == 10):
        print("\n---------------------------------------------------------------------------")
        print("\n ALERTA: PEDRAS CAIDAS: {}".format(interacoes))
        print("\n{} {}, VOCÊ CAIU NO PORTAL!!\n".format(classe,nome))
        salaAtual = random.randint(1,5)
        print("\n---------------------------------------------------------------------------")
        print("\n{} {}, Você está na sala: {}\n".format(classe,nome,salaAtual))
        escolha = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
        salaAtual = salaAtual+escolha
        interacoes = interacoes+1
    else:
        print("\n---------------------------------------------------------------------------")
        print("\n ALERTA: PEDRAS CAIDAS: {}".format(interacoes))
        print("\n{} {}, Você está na sala: {}\n".format(classe,nome,salaAtual))
        escolha = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
        salaAtual = salaAtual+escolha
        interacoes = interacoes+1 