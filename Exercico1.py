"Escreva um algoritmo que leia o código do item adquirido pelo"
"consumidor e a"
"quantidade, calculando e mostrando o valor a pagar." \
" Não será necessário exibir o produto e o valor, somente o valor final"
"100-- cachorro quente--1.70"
"101-- bauru simples -- 2.30"
"102-- hamburguerm -- 2.40"
"103-- chesburgue --- 2.50"
"104 -- rfri-- 1.00"
"105 -- bauru com ovo"

cod= int(input("Digite o codigo do produto:"))
qt= int(input("Digite a quantidade desejada:"))

match cod:
    case 100:
        A=1.70 * qt
        print(f"o valor total de cahorros quentes deu {A}")
    case 101:
        b=2.30 * qt
        print(f"O valor total de bauru simples é de {b}")
    case 102:
        c= 2.60 * qt
        print(f"O valor total dos Baurus com ovo é de {c}")
    case 103:
        d= 2.40 * qt
        print(f"O valor total dos hambuerguers é de {d}")
    case 104:
        e= 2.50 * qt
        print(f"O valor total de Cheeseburguers é de {e}")
    case 105:
        f=1.00 * qt
        print(f"O valor total dos refrigerantes é de {f}")
    case _:
        print("o codigo digitado não existe")



