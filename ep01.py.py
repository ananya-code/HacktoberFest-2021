
import random

semente = int(input("Digite a semente do sorteio: "))
random.seed(semente)
numero_sorteado = random.randint(1,20)
print("\nEscolhi um inteiro entre 1 e 20. Adivinhe-o!")

t=1
while t<=5:
    n=int(input("Seu chute: "))
    if n==numero_sorteado:
        print("\nLegal, acertou na tentativa",t )
        t=5
    if n>numero_sorteado:
        print("\nChutou alto")
    if n<numero_sorteado:
        print("\nChutou baixo")
    if numero_sorteado%2==0 and (n-1)%2==0:
        print("Tente um par")
    if (numero_sorteado-1)%2==0 and n%2==0:
        print("Tente um impar")
    if t==5 and n%numero_sorteado>0:
        print("Tentativas esgotadas!\nO escolhido foi o",numero_sorteado)
   
    t=t+1
