lista = []
contador = 0

print("Por favor me informe três números para preencher a lista...")

#Fazendo a solicitação de três números para o usuário e adicionado na lista
for contador in range(3):
  numeros = float(input("Digite o número: "))
  lista.append(numeros)
  contador += 1 

#Função para fazer a soma de todos os valores da lista
def somar(lista):
  soma = 0
  for valor in lista:
    soma += valor
  
  print("\n")
  print(f"O valor total da soma da lista é {soma}\n")

#Função para tirar a média da lista -> Calculo - somar todos os valores da lista e dividir pela quantidade dela
def media(lista):
  soma = 0
  for valor in lista:
    soma += valor

  media = soma / len(lista)
  print(f"A média dos valores informados na lista é igual a {media}\n")

#Função para descobrir o maior e menor número de duas maneiras
def maior_menor(lista):
  # print(F"O maior número da lista é {max(lista)}\n") forma simplificada de pegar o maior valor
  # print(f"O menor número da lista é {min(lista)}") forma simplificada de pegar o maior valor
  max = float('-inf')
  min = float('inf')

#Maior valor
  for valor in lista:
    valor = int(valor)
    if valor > max:
      max = valor

#Menor valor
  for valor in lista:
    valor = int(valor)
    if valor < min:
      min = valor
  
  print(f"O maior valor da lista é: {max}\n")
  print(f"O menor valor da lista é: {min}")
  
#Chamando todas as funções para funcionar
somar(lista)
media(lista)
maior_menor(lista)
