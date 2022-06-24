km = int(input('Digite os Km: '))
litros = int(input('Digites os litros: '))
res = km / litros
if res < 8:
    print(f'Seu consumo foi {res:.2f} Km por litro venda seu carro.')
elif res >=8 and res <= 14:
    print(f'Seu consumo  foi {res:.2f} Km por litro seu carro é econômico.')
else:
    res > 15
    print(f"Seu consumo foi {res:.2f} Km por litros seu carro é super econômico")