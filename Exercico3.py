"3)	Um funcionário irá receber"
"um aumento de acordo com o seu " \
"plano de trabalho" \
"de acordo com a tabela abaixo:"
"A-- 10% de aumento"
"b--15% de aumento"
"c--20% de aumemnto"
"Faça um programa que leia o plano de trabalho" \
" e o salário atual de um funcionário " \
"e calcula e imprime o seu novo salário"

sal=float(input("Digite seu salario atual R$"))
print("A--- 10% de amuento")
print("B--- 15% de amuneto")
print("C---20% de aumento")

OP=input("escolha a opção desejada:")

match OP:
    case "A":
       opa= (sal*0.10) + sal
       print(f"O salario iria para R${opa}")
    case "B":
        opb= (sal*0.15) + sal
        print(f"o salario iria para R${opb}")
    case "C":
        opc= (sal*0.20) + sal
        print(f"o salario iria para R${opc}")
    case _:
        print("opção não disponivel")




