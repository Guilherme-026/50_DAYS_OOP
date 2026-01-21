lista = []
contador = 0

print("Por favor me informe três números para preencher a lista...")

#Fazendo a solicitação de três números para o usuário e adicionado na lista
for contador in range(3):
  numeros = float(input("Digite o número: "))
  lista.append(numeros)
  contador += 1 

#Função para fazer a soma de todos os valores da lista
def operacoes(lista):

#-----------------------------------------------------#
#                AMBIENTE DE VARIÁVEIS                #
  max = float('-inf')
  min = float('inf')
  soma = 0
#-----------------------------------------------------#

  for valor in lista: #LOPPING PRINCIPAL DA FUNÇÃO
    soma += valor #Soma de itens da lista.
    valor = int(valor)

    media = soma / len(lista) #Média da lista.

    if valor > max: #Condição para verificar maior item da lista.
     max = valor

    if valor < min: #Condição para verificar o menor item da lista.
      min = valor
  
#-----------------------------------------------------#
#          AMBIENTE DA SAÍDA DE RESULTADOS            #
  print("\n")
  print(f"O valor total da soma da lista é {soma}\n")
  print(f"A média dos valores informados na lista é igual a {media}\n")
  print(f"O maior valor da lista é: {max}\n")
  print(f"O menor valor da lista é: {min}")
#-----------------------------------------------------#

operacoes(lista)
