#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
print('bom dia, loja de tintas. Como podemos te ajudar?')
area=float(input('qual e o total da area a ser pintada?'))
tinta=area/6
lata=math.ceil(tinta/18)
galao=math.ceil(tinta/3.6)
preco_lata=lata*80
preco_galao=galao*25
preco_mistura= preco_galao + preco_lata
escolha=int(input('voce quer comprar: 1)somente galoes(3,6L) 2)somente latas(18L) 3)mistura entre elas?'))
if escolha == 1 :
    quantidadef=galao
    precof=preco_galao
    print(f'a quantidade foi de:{quantidadef}'+ f'e o preco foi de:{precof}' )
elif escolha==2 :
    quantidadef=lata
    precof=preco_lata
    print(f'a quantidade foi de:{quantidadef}'+ f' e o preco foi de: {precof} reais')
elif escolha==3 :
    lata=int(tinta/18)
    galao=math.ceil((tinta%18)/3.6)
    precof=lata*80 + galao*25
    if galao > 3:
        galao=0
        lata=int(tinta/18) + 1
        precof=lata*80

    print(f'a quantidade na mistura de galões:{galao} ' + f'e quantidade de latas e:{lata}'+'\n assim, o preco foi de:{:1f} reais'.format(precof))


