nota1 = float(input("insira a primeira nota"))
nota2 = float(input("insira a segunda nota"))
nota3 = float(input("insira a terceira nota"))
nota4 = float(input("insira a quarta nota"))
media=(nota1 + nota2 + nota3 + nota4)/4
print("media final ",media)
if media >= 7: 
    print("aluno aparovado")
else:
    print("aluno reprovado")