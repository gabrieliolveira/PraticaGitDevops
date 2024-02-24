# Inicialização das listas de alunos
lista_alunos = []

while True:
    # Solicitação do nome do aluno (digite '0' para sair)
    nome = input('Digite o nome do aluno (sair=0): ')
    
    # Condição de saída do loop
    if nome == '0':
        break
    
    # Solicitação das notas do aluno
    nota1 = float(input('Digite nota1: '))
    nota2 = float(input('Digite nota2: '))
    
    # Cálculo da média do aluno
    media = (nota1 + nota2) / 2
    
    # Adição do aluno à lista de alunos
    aluno = [nome, nota1, nota2, media]
    lista_alunos.append(aluno)

# Impressão do boletim
print('  NOME         NOTA 1      NOTA2        NOTA3')
for aluno in lista_alunos:
    print("{:<15} {:<11.2f} {:<11.2f} {:<11.2f}".format(aluno[0], aluno[1], aluno[2], aluno[3]))
