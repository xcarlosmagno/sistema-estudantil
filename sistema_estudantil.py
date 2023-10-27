# -*- coding: utf-8 -*-
"""Sistema Estudantil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KkGPUB-XQLmWg0grzkiGKBzJdGGDtSCk

Sistema Estudantil - Registro das disciplinas de Professores e Alunos
"""

id_professor = 1
id_aluno = 1

professores = []
alunos = []

# Definição das funções de ação do menu PROFESSORES

# Função de cadastro de um professor
def cadastrar_professor():

  professor = {"id": None, "nome": None, "disciplinas": None}

  professor["id"] = id_professor
  professor["nome"] = input("\nDigite o nome do professor a ser cadastrado\n>>>")

  qtd_disciplinas = int(input("\nDigite a quantidade de disciplinas ministradas por esse professor\n>>>"))
  disciplina = None
  disciplinas = []

  for i in range(qtd_disciplinas):

    disciplina = input(f"\nDigite a {i + 1}ª disciplina\n>>>")
    disciplinas.append(disciplina)

  professor["disciplinas"] = disciplinas

  professores.append(professor)
  print("\nProfessor cadastrado com sucesso!\n")

# Função de remoção de um professor por meio do ID
def remover_professor():

  id = int(input("\nDigite o id do professor a ser removido\n>>>"))

  professor_encontrado = False

  for professor_em_consulta in professores:
    if professor_em_consulta["id"] == id:

      professor_encontrado = True
      professores.remove(professor_em_consulta)
      print("\nProfessor removido com sucesso!\n")

  if not professor_encontrado:
    print(f"\nNão há professor associado ao ID {id}. Por favor, consultar a lista de professores cadastrados.\n")

# Função para buscar os dados de um professor por meio do ID
def buscar_professor():

  id = int(input("\nDigite o id do professor a ser procurado\n>>>"))

  professor_encontrado = False

  for professor_em_consulta in professores:
    if professor_em_consulta["id"] == id:

      professor_encontrado = True

      print(f"\nID: {professor_em_consulta['id']}")
      print(f"Nome: {professor_em_consulta['nome']}")
      print("Disciplinas Ministradas:")

      disciplinas_ministradas = ""
      for disciplina_em_consulta in professor_em_consulta["disciplinas"]:
        disciplinas_ministradas += f"> {disciplina_em_consulta} "

      print(disciplinas_ministradas)

  if not professor_encontrado:
    print(f"\nNão há professor associado ao ID {id}. Por favor, consultar a lista de professores cadastrados.\n")

# Função para listar todos os professores cadastrados
def listar_professores():

  for professor_em_consulta in professores:

      print(f"\nID: {professor_em_consulta['id']}")
      print(f"Nome: {professor_em_consulta['nome']}")
      print("Disciplinas Ministradas:")

      disciplinas_ministradas = ""
      for disciplina_em_consulta in professor_em_consulta["disciplinas"]:
        disciplinas_ministradas += f"> {disciplina_em_consulta} "

      print(disciplinas_ministradas)

# Definição das funções de ação do menu ALUNOS

# Função de cadastro de um aluno
def cadastrar_aluno():

  aluno = {"id": None, "nome": None, "disciplinas": None}

  aluno["id"] = id_aluno
  aluno["nome"] = input("\nDigite o nome do aluno a ser cadastrado\n>>>")

  qtd_disciplinas = int(input("\nDigite a quantidade de disciplinas matriculadas para esse aluno\n>>>"))
  disciplina = None
  disciplinas = []

  for i in range(qtd_disciplinas):

    disciplina = input(f"\nDigite a {i + 1}ª disciplina\n>>>")
    disciplinas.append(disciplina)

  aluno["disciplinas"] = disciplinas

  alunos.append(aluno)
  print("\nAluno cadastrado com sucesso!\n")

# Função de remoção de um aluno por meio do ID
def remover_aluno():

  id = int(input("\nDigite o id do aluno a ser removido\n>>>"))

  aluno_encontrado = False

  for aluno_em_consulta in alunos:
    if aluno_em_consulta["id"] == id:

      aluno_encontrado = True
      alunos.remove(aluno_em_consulta)
      print("\nAluno removido com sucesso!\n")

  if not aluno_encontrado:
    print(f"\nNão há aluno associado ao ID {id}. Por favor, consultar a lista de alunos cadastrados.\n")

# Função para buscar os dados de um aluno por meio do ID
def buscar_aluno():

  id = int(input("\nDigite o id do aluno a ser procurado\n>>>"))

  aluno_encontrado = False

  for aluno_em_consulta in alunos:
    if aluno_em_consulta["id"] == id:

      aluno_encontrado = True

      print(f"\nID: {aluno_em_consulta['id']}")
      print(f"Nome: {aluno_em_consulta['nome']}")
      print("Disciplinas Matriculadas:")

      disciplinas_matriculadas = ""
      for disciplina_em_consulta in aluno_em_consulta["disciplinas"]:
        disciplinas_matriculadas += f"> {disciplina_em_consulta} "

      print(disciplinas_matriculadas)

  if not aluno_encontrado:
    print(f"\nNão há aluno associado ao ID {id}. Por favor, consultar a lista de alunos cadastrados.\n")

# Função para listar todos os alunos cadastrados
def listar_alunos():

  for aluno_em_consulta in alunos:

      print(f"\nID: {aluno_em_consulta['id']}")
      print(f"Nome: {aluno_em_consulta['nome']}")
      print("Disciplinas Matriculadas:")

      disciplinas_matriculadas = ""
      for disciplina_em_consulta in aluno_em_consulta["disciplinas"]:
        disciplinas_matriculadas += f"> {disciplina_em_consulta} "

      print(disciplinas_matriculadas)

# Verificar quantidade de professores e alunos de uma disciplina específica
def professores_alunos_por_disciplina():

  disciplina = input("\nDigite a disciplina a ser procurada\n>>>")

  qtd_professores = 0
  qtd_alunos = 0

  for professor_em_consulta in professores:
    for disciplina_em_consulta in professor_em_consulta['disciplinas']:
      if disciplina == disciplina_em_consulta:

        qtd_professores += 1

  for aluno_em_consulta in alunos:
    for disciplina_em_consulta in aluno_em_consulta['disciplinas']:
      if disciplina == disciplina_em_consulta:

        qtd_alunos += 1

  print(f"\nDisciplina: {disciplina}")
  print(f"Professores: {qtd_professores}, Alunos: {qtd_alunos}")

print(">>>>>>>>>> Bem vindo ao sistema <<<<<<<<<<")

while True:

  action = None

  print("\n*** Menu ***\n")
  print("* PROFESSORES *")
  print("p1 - Cadastrar professor")

  # Opções p2, p3 e p4 só serão exibidas se houver pelo menos um professor cadastrado
  if len(professores):
    print("p2 - Remover um professor")
    print("p3 - Buscar um professor")
    print("p4 - Listar todos os professores cadastrados")

  print("\n* ALUNOS *")
  print("a1 - Cadastrar aluno")

  # Opções a2, a3 e a4 só serão exibidas se houver pelo menos um aluno cadastrado
  if len(alunos):
    print("a2 - Remover um aluno")
    print("a3 - Buscar um aluno")
    print("a4 - Listar todos os alunos cadastrados")

  print("\n* OUTROS *")
  print("o1 - verificar a quantidade de professores e alunos de uma disciplina específica")
  print("o2 - Sair")

  action = input("\nDigite a operação que deseja executar\n>>>")

  if action == "p1":
    cadastrar_professor()
    id_professor += 1

  elif action == "p2":
    remover_professor()

  elif action == "p3":
    buscar_professor()

  elif action == "p4":
    listar_professores()

  elif action == "a1":
    cadastrar_aluno()
    id_aluno += 1

  elif action == "a2":
    remover_aluno()

  elif action == "a3":
    buscar_aluno()

  elif action == "a4":
    listar_alunos()

  elif action == "o1":
    professores_alunos_por_disciplina()

  elif action == "o2":
    break

  else:
    print("\nOperação inválida!")