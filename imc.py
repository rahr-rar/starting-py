nome = input('Diga o seu nome: ')
altura = (input ('Diga sua altura: '))
peso = (input('Diga o seu peso: '))
altura_float = float(altura)
peso_float = float(peso)
imc = peso_float / (altura_float ** 2)
resultado = f'{nome} o calculo do seu peso dividido por sua altura ao quadrado, resultou em um IMC de: {imc:.2f}'
print(resultado)


print(resultado)