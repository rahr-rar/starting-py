nome = input('Diga o seu nome: ')
altura = float (input ('Diga sua altura: '))
peso = float (input('Diga o seu peso: '))
imc = peso / (altura * altura)

resultado = f'{nome} o calculo do seu peso dividido por sua altura ao quadrado, resultou em um IMC de: {imc:.2f}'
print(resultado)