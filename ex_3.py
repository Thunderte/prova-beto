from random import randint

def dicionarioAluno():
    matriculasJaUtilizadas = []
    dicionarioAlunos = []
    quantidadeDeAlunos = int(input("Olá quantos alunos você quer adicionar (1 a 5)? \n"))

    if quantidadeDeAlunos == 0:
        print("Error: Não é possível adicionar nenhum aluno")
    elif quantidadeDeAlunos == 1:
        nomeAluno1 = str(input("Digite o nome do primeiro aluno: \n"))
        notaFinalAluno1 = int(input("Digite a nota final do aluno de 0 a 10: \n"))
        matricula = randint(0, 100)

        for matriculas in range(len(matriculasJaUtilizadas)):
            if(matriculas[i] == matricula):
                matricula = randint(0, 1000)
        dicionarioAluno = dicionarioAlunos.append({ nomeAluno1: {"matricula": matricula, "notaFinal": notaFinalAluno1}})
    elif quantidadeDeAlunos == 2:
        nomeAluno1 = str(input("Digite o nome do primeiro aluno: \n"))
        notaFinalAluno1 = int(input("Digite a nota final do primeiro aluno de 0 a 10: \n"))
        nomeAluno2 = str(input("Digite o nome do segundo aluno: \n"))
        notaFinalAluno2 = int(input("Digite a nota final do segundo aluno de 0 a 10: \n"))
        matriculaAluno1 = randint(0, 1000)
        matriculaAluno2 = randint(0, 1000)

        for matriculas in range(len(matriculasJaUtilizadas)):
            if matriculas[i] == matriculaAluno1:
                matriculaAluno1 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno2:
                matriculaAluno2 = randint(0, 1000)
        dicionarioAlunos.append({ nomeAluno1: {"matricula": matriculaAluno1, "notaFinal": notaFinalAluno1}})
        dicionarioAlunos.append({ nomeAluno2: {"matricula": matriculaAluno2, "notaFinal": notaFinalAluno2}})
    elif quantidadeDeAlunos == 3:
        nomeAluno1 = str(input("Digite o nome do primeiro aluno: \n"))
        notaFinalAluno1 = int(input("Digite a nota final do primeiro aluno de 0 a 10: \n"))

        nomeAluno2 = str(input("Digite o nome do segundo aluno: \n"))
        notaFinalAluno2 = int(input("Digite a nota final do segundo aluno de 0 a 10: \n"))

        nomeAluno3 = str(input("Digite o nome do terceiro aluno: \n"))
        notaFinalAluno3 = int(input("Digite a nota final do terceiro aluno de 0 a 10: \n"))

        matriculaAluno1 = randint(0, 1000)

        matriculaAluno2 = randint(0, 1000)

        matriculaAluno3 = randint(0, 1000)

        for matriculas in range(len(matriculasJaUtilizadas)):
            if matriculas[i] == matriculaAluno1:
                matriculaAluno1 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno2:
                matriculaAluno2 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno3:
                matriculaAluno3 = randint(0, 1000)
        dicionarioAlunos.append({ nomeAluno1: {"matricula": matriculaAluno1, "notaFinal": notaFinalAluno1}})
        dicionarioAlunos.append({ nomeAluno2: {"matricula": matriculaAluno2, "notaFinal": notaFinalAluno2}})
        dicionarioAlunos.append({ nomeAluno3: {"matricula": matriculaAluno3, "notaFinal": notaFinalAluno3}})
    elif quantidadeDeAlunos == 4:
        nomeAluno1 = str(input("Digite o nome do primeiro aluno: \n"))
        notaFinalAluno1 = int(input("Digite a nota final do primeiro aluno de 0 a 10: \n"))

        nomeAluno2 = str(input("Digite o nome do segundo aluno: \n"))
        notaFinalAluno2 = int(input("Digite a nota final do segundo aluno de 0 a 10: \n"))

        nomeAluno3 = str(input("Digite o nome do terceiro aluno: \n"))
        notaFinalAluno3 = int(input("Digite a nota final do terceiro aluno de 0 a 10: \n"))

        nomeAluno4 = str(input("Digite o nome do quarto aluno: \n"))
        notaFinalAluno4 = int(input("Digite a nota final do quarto aluno de 0 a 10: \n"))

        matriculaAluno1 = randint(0, 1000)

        matriculaAluno2 = randint(0, 1000)

        matriculaAluno3 = randint(0, 1000)

        matriculaAluno4 = randint(0, 1000)

        for matriculas in range(len(matriculasJaUtilizadas)):
            if matriculas[i] == matriculaAluno1:
                matriculaAluno1 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno2:
                matriculaAluno2 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno3:
                matriculaAluno3 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno4:
                matriculaAluno4 = randint(0, 1000)

        dicionarioAlunos.append({ nomeAluno1: {"matricula": matriculaAluno1, "notaFinal": notaFinalAluno1}})
        dicionarioAlunos.append({ nomeAluno2: {"matricula": matriculaAluno2, "notaFinal": notaFinalAluno2}})
        dicionarioAlunos.append({ nomeAluno3: {"matricula": matriculaAluno3, "notaFinal": notaFinalAluno3}})
        dicionarioAlunos.append({ nomeAluno4: {"matricula": matriculaAluno4, "notaFinal": notaFinalAluno4}})
    elif quantidadeDeAlunos == 5:
        nomeAluno1 = str(input("Digite o nome do primeiro aluno: \n"))
        notaFinalAluno1 = int(input("Digite a nota final do primeiro aluno de 0 a 10: \n"))

        nomeAluno2 = str(input("Digite o nome do segundo aluno: \n"))
        notaFinalAluno2 = int(input("Digite a nota final do segundo aluno de 0 a 10: \n"))

        nomeAluno3 = str(input("Digite o nome do terceiro aluno: \n"))
        notaFinalAluno3 = int(input("Digite a nota final do terceiro aluno de 0 a 10: \n"))

        nomeAluno4 = str(input("Digite o nome do quarto aluno: \n"))
        notaFinalAluno4 = int(input("Digite a nota final do quarto aluno de 0 a 10: \n"))

        nomeAluno5 = str(input("Digite o nome do quinto aluno: \n"))
        notaFinalAluno5 = int(input("Digite a nota final do quinto aluno de 0 a 10: \n"))

        

        matriculaAluno1 = randint(0, 1000)

        matriculaAluno2 = randint(0, 1000)

        matriculaAluno3 = randint(0, 1000)

        matriculaAluno4 = randint(0, 1000)

        matriculaAluno5 = randint(0, 1000)

        for matriculas in range(len(matriculasJaUtilizadas)):
            if matriculas[i] == matriculaAluno1:
                matriculaAluno1 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno2:
                matriculaAluno2 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno3:
                matriculaAluno3 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno4:
                matriculaAluno4 = randint(0, 1000)
            elif matriculas[i] == matriculaAluno5:
                matriculaAluno5 = randint(0, 1000)

        dicionarioAlunos.append({ nomeAluno1: {"matricula": matriculaAluno1, "notaFinal": notaFinalAluno1}})
        dicionarioAlunos.append({ nomeAluno2: {"matricula": matriculaAluno2, "notaFinal": notaFinalAluno2}})
        dicionarioAlunos.append({ nomeAluno3: {"matricula": matriculaAluno3, "notaFinal": notaFinalAluno3}})
        dicionarioAlunos.append({ nomeAluno4: {"matricula": matriculaAluno4, "notaFinal": notaFinalAluno4}})
        dicionarioAlunos.append({ nomeAluno5: {"matricula": matriculaAluno5, "notaFinal": notaFinalAluno5}})
    else:
        print('Error: Quantidade de alunos inválida digite de 1 a 5')

    return dicionarioAlunos

def main():
    return print(f'\n Aqui está todas as matriculas de todos alunos: \n {dicionarioAluno()}')


main()
