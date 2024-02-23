listaAlunos = []
listaAluno = []


while True: 
    n = input(str('Digite o nome do aluno(sair=0): '))
    if n == '0':
        break

    n1 = float(input('Digite nota1: '))
    n2 = float(input('Digite nota2: '))


    listaAluno = [n, n1, n2, (n1+n2)/2]
    listaAlunos.append(listaAluno)
    
    

print('  NOME         NOTA 1      NOTA2        NOTA3')
for aluno in listaAlunos:
        print("{:<15} {:<11.2f} {:<11.2f} {:<11.2f}".format(aluno[0], aluno[1], aluno[2], aluno[3]))



