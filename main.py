# entrada de dados
nome = input('Informe o seu nome: ') ; idade = int(input('Informe a sua idade: ')) ; idade_min_1 = 10 ; idade_min_2 = 11 ; idade_min_3 = 12 ; idade_min_4 = 13 ; idade_min_5 = 14

while True:
    # exibe a lista de filmes e suas salas
    print ('LISTA DE FILMES\n')
    print (f'Sala 1 - A Volta dos Que não Foram. Classificação indicativa: {idade_min_1} anos ')
    print (f'Sala 2 - A Roda Quadrada. Classificação indicativa: {idade_min_2} anos ')
    print (f'Sala 3 - Poeira em Alto Mar. Classificação indicativa: {idade_min_3} anos ')
    print (f'Sala 4 - As Tranças do Rei Careca. Classificação indicativa: {idade_min_4} anos ')
    print (f'Sala 5 - A Vingança do Peixe Frito. Classificação indicativa: {idade_min_5} anos ')

    # recebe a sala escolhida
    sala = int(input('Informe a sala desejada: '))

    if idade >= idade_min_1 and sala == 1:
        print(f'ingresso para {nome} da Sala 1.')
        break
    elif idade >= idade_min_2 and sala == 2:
        print(f'ingresso para {nome} da Sala 2.')
        break
    elif idade >= idade_min_3 and sala == 3:
        print(f'ingresso para {nome} da Sala 3.')
        break
    elif idade >= idade_min_4 and sala == 4:
        print(f'ingresso para {nome} da Sala 4.')
        break
    elif idade >= idade_min_5 and sala == 5:
        print(f'ingresso para {nome} da Sala 5.')
        break
    else:
        print(f'Prezado {nome}, escolhe um filme indicado para a sua idade.')
        continue

    



