import faker
import random

# Inicializa o Faker para geração de dados aleatórios
fake = faker.Faker('pt_BR')

# Função para gerar um CPF aleatório
def gerar_cpf():
    base = [random.randint(0, 9) for _ in range(9)]

    # Gera os dois dígitos verificadores
    val1 = sum([base[i] * (10 - i) for i in range(9)]) % 11
    base.append(11 - val1 if val1 >= 2 else 0)
    val2 = sum([base[i] * (11 - i) for i in range(10)]) % 11
    base.append(11 - val2 if val2 >= 2 else 0)

    return ''.join(map(str, base))

# Lista para armazenar os dados gerados
nomes = []
cpfs = []
datas_nascimento = []

with open("dados_faker.csv", 'a+', newline="") as arquivo:
    # Gerar 10 nomes, CPFs e datas de nascimento
    for _ in range(10):
        # Gerar nome aleatório
        nome = fake.name()
        nomes.append(nome)

        # Gerar CPF aleatório
        cpf = gerar_cpf()
        cpfs.append(cpf)

        # Gerar data de nascimento entre 18 e 65 anos atrás
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        datas_nascimento.append(data_nascimento.strftime('%d/%m/%Y'))

        cpf = cpf.replace('.', '').replace('-', '')
        arquivo.write(nome + ';' + cpf + ';' + data_nascimento.strftime('%d/%m/%Y') + ';\n')
        arquivo.flush()

# Exibir os dados gerados
print("Nomes:")
for nome in nomes:
    print(nome)

print("\nCPFs:")
for cpf in cpfs:
    print(cpf)

print("\nDatas de Nascimento:")
for data in datas_nascimento:
    print(data)
