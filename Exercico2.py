"2)	Faça um programa que receba dois números e"
"execute"
"as operações listadas a"
"seguir de acordo com a escolha do usuário: "

print("Opção 1- média entre os numeros digitados")
print("opção 2_ maior valor dos numeros digitados")
print("opção 3 - menor valor dos nunmeros digitados")
print("opcao 4 - divisão inteira dos numeros digitados")

num1= int(input("Digite o valor:"))
num2 = int(input("Digite o valor 2:"))
cod= int(input("Digite o comando desejado:"))

match cod:
    case 1:
        med=(num2+num1)/2
        print(f"o valor da média é de {med}")
    case 2:
        if num1>num2:
            print(f"o valor de {num1} é maior")
        else:
            print(f"o valor de {num2} é menor")

    case 3:
        if num1<num2:
            print(f"o valor de {num1} é maior")
        else:
            print(f"o valor de {num2} é maior")

    case 4:
        div= (num1//num2)
        print(f"A divisão intera é de {div}")
