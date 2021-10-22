"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Lucia de Santi Serafim
  NUSP : 12552346
  Turma: 4(civil)
  Prof.: Kelly Rosa Braghetto


"""

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
