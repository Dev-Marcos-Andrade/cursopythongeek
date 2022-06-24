nota = float(input('Digite a nota: '))
faltas = int(input('Digite as faltas: '))
if nota >= 9 and nota <= 10 and faltas <= 20:
    print('O conceito desse aluno é A')
elif nota >= 9 and nota <= 10 and faltas > 20:
    print('O conceito desse aluno é B')
elif nota >= 7.5 and nota <= 8.9 and faltas <= 20:
    print('O conceito desse aluno é B')
elif nota >= 7.5 and nota <= 8.9 and faltas > 20:
    print('O conceito desse aluno é C')
elif nota >= 5 and nota <= 7.4 and faltas <= 20:
    print('O conceito desse aluno é C')
elif nota >= 5 and nota <= 7.4 and faltas > 20:
    print('O conceito desse aluno é D')
elif nota >= 4 and nota <= 4.9 and faltas <= 20:
    print('O conceito desse aluno é D')
elif nota >= 4 and nota <= 4.9 and faltas > 20:
    print('O conceito desse aluno é E')
elif nota >= 0 and nota <= 3.9 and faltas <= 20:
    print('O conceito desse aluno é E')
elif nota >= 0 and nota <= 3.9 and faltas > 20:
    print('O conceito desse aluno é E')