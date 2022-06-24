print('<<< CALCULO DE MP ANUAL >>>')
nota1 = float(input('Digite uma nota1: '))
peso1 = float(input('Digite o peso1 da nota: '))
print('-=' * 30)
nota2 = float(input('Digite uma nota2: '))
peso2 = float(input('Digite o peso2 da nota: '))
print('-=' * 30)
nota3 = float(input('Digite uma nota3: '))
peso3 = float(input('Digite o peso3 da nota: '))
print('-=' * 30)
média = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
if média >= 60:
    print(f'Sua MP É {média:.2f} PARABENS VOCÊ FOI APROVADO..')
else:
    print(f'SUA MP FOI {média:.2f} VOCÊ FOI REPROVADO ESTUDE MAIS..')