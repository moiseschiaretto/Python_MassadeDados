## Projeto "GerarMassaDados"
- Autor Moisés Ademir Chiaretto
  
- Descrição das explicações de cada item da 'estrutura do projeto "GerarMassaDados" desenvolvido'.

**- Exemplos em Python de como gerar Massa de Dados.**

    - Exemplo 1: Python gera os dados aleatórios / faker (nome ; cpf ; data de nascimento).

    - Exemplo 2: Extrair os dados da Web e gerar os nomes personalizados e sintéticos.

- **Python com Selenium WeDriver**
  
- **LibreOffice CALC com Macro em BASIC, pode utilizar também o Microsoft Excel com Macro em VBA.**

| ![04_Python](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/85379dcd-9c54-435b-806c-3a32f9c3379a) | ![08_Selenium_Webdriver_02](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/40d3a46a-f2c2-43fe-9b16-c44531b01952)|

| ![19_LibreOffice_CALC](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/444cf3aa-5ff3-4712-a0bd-f893bbe43478)
 | ![20_MS_EXCEL_02](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/44fdd4b7-2484-41ba-bd00-0e3feba6227c)
 |

## Estrutura do Projeto "projeto_web"

![Dados_Extrair_Web_Gerar_Faker](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/a7a8e035-6e41-4984-b92a-e84720c00a69)


```

GerarMassaDados
    |
    |-----Extrair_Dados_Web
    | 	    |---cpf_datanasc.csv
    | 	    |---Extrair_CPF_DataNasc_Web.py
    | 	    |---PLAN_CALC_MASSA_DADOS.ods
    |
    |-----Gerar_Dados_Faker
    | 	    |---Gerar_Aleatorios.py
    | 	    |---dados_faker.csv
    |
    |-----resources
    | 	    |---geckodriver.exe
    |
    |-----validacoes
    | 	    |---ValidacoesParaCadastrar.py
    |
    |-----.gitgnore
    |-----README.md
    |-----requirements.txt

```

## Arquivo README.md
Explicações da Estrutura do Projeto e as suas respectivas configurações.


## Arquivo 'requeriments.txt'
Constam todas as 'bibliotecas' do projeto para serem instaladas.

  - Biblioteca do **Selenium WebDriver** para acessar o browser.

  - Biblioteca do **Faker** para gerar os dados aleatórios / faker (nome ; cpf ; data de nascimento).

```
# requeriments.txt
selenium>=4.20.0
faker>=25.1.0
```


## Arquivo '.gitignore'
Constam todos os diretórios e os arquivos que devem serem ignorados ao subir o código para o git (controle de versão).

```
/.venv/
/.idea/
/resources/
```

## Arquivo "geckodriver.exe"

- Este arquivo está dentro da **pasta "resources,** não exibida aqui no repositório por estar no arquivo ".gitignore", porém ese arquivo "geckodriver.exe" é do browser Mozilla Firefox, utilizado pelo Selenium WebDriver para acessar o browser.


## Exemplo 1: Python gera os dados aleatórios / faker (nome ; cpf ; data de nascimento).
  - Gerar Dados Faker com o Python......

  ```

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
    
    
  ```


  - CPFs gerados pelo Python utilizando a biblioteca **"Faker".**

  ![CPF_FAKER_GERADOS_PYTHON](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/fb1baa9f-1cd7-4097-aaaf-766cc3041441)


  - Validando os CPFs gerados pelo Pyhton com a biblioteca "Faker" se os mesmos são válidos.

  - https://www.4devs.com.br/validador_cpf

  ![VALIDACAO_CPF_FAKER](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/b4fa05ad-c0f3-41dd-91e2-ce6174b263bf)


## Exemplo 2: Extrair os dados da Web e gerar os nomes personalizados e sintéticos.
## Arquivo 'cpf_datanasc.csv'

Constam os dados que são **"CPF" e "Data de Nascimento"** extraídos do site da Web, para a geração da Massa de Dados, sendo um arquivo de log que armazena os dados capturados / extraídos, podendo também esses dados serem armaenados em uma tabela de um banco de dados.

https://geradorbrasileiro.com/pessoa

- URL que é acessada para capturar CPF e Data de Nascimento.

- Estes CPFs são válidos, porém não são quentes, ou seja, não constar no site da RF - Receita Federal.

-  Sendo assim podem serem utilizados em um Ambiente de Stage ou Produção.

https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp

![Dados_Gerados_Arquivo_Log](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/46ff1bb2-2fea-422d-834e-6dc9566e1304)


## Arquivo 'Extrair_CPF_DataNasc_Web.py'

Arquivo do Python contém a programção utilizando a biblioteca "Selenium WebDriver" para acessar o Browser Mozilla Firefox e a URL abaixo para a geração de massa de dados, como CPF e Data de Nascimento, por exemplo.

https://geradorbrasileiro.com/pessoa

- Ao gerar no site da Web o "CPF" e a "Data de Nascimento" esse dados são armazenados em um **"arquivo de log"** para depois em uma **"segunda etapa"** serem inseridos em um sistema a quantidade de massa de dados desejada.

![Massa_de_Dados](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/ec1fda27-1af8-4ce9-b8f1-80f18bf71f7f)


## Importante

  - Existem outros sites gerados de dados de Pessoa Física, Pessoa Jurídica, entre outros dados, porém no caso do "CPFs" gerados a maioria são **CPFs quentes,** ou seja, constam no site da **Receita FEderal,** logo não podem serem utilizados em um **ambiente de produção,** podem já existir ou ao cadastrar um cliente "real", já existirá o "CPF de Teste" da Massa de Dados.

  - Alguns sites que geram CPFs quentes, que constam na base da Receita Federal:

  ```
    https://geradordecpf.clevert.com.br/cpf.php

    https://www.4devs.com.br/gerador_de_pessoas
```

  - Site da Receita Federal para consulta o CPF:

https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp


## Arquivo 'PLAN_CALC_MASSA_DADOS.ods'

Este arquivo é uma **planilha do LibreOffice CALC utilizando uma Macro BASIC, podendo ser também uma planilha do Microsoft Excel utilizando uma Macro do VBA,** onde são gerados os **nomes sintéticos para o cadastro, respeitando assim a LGPD.**

**Planilha do LibreOffice CALC com o botão "Gerar Letras na Coluna "D",** são geradas letras para os **sobrenomes** dos nomes personalizados e sitéticos a serem cadastrados, por exemplo:
  - Teste A, Teste B, Teste C, ..., Teste Z,
  - Teste AA, Teste AB, Teste AC, ..., Teste AZ,
  - Teste BA, Teste BB, Teste BC, ..., Teste BZ,
  - E assim sucessivamente...

![Planilha_Massa_Dados_Gerada](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/1c7e60a8-afa8-4c73-8172-be15565ab58b)


Código desenvolvido **na Macro BASIC utilizado no botão da planilha do LibreOffice CALC, para a geração dos **sobrenomes** dos nomes personalizados e sintéticos.**

```
Sub Gerar_Letras()
    Dim Numero As Integer
    Dim Letra As String
    Dim i As Integer
    Dim resto As Integer
    Dim valor As Integer
    Dim letra1 As String
    
    ' Obtém o número de letras a serem geradas da célula A2
    Numero = ThisComponent.CurrentController.ActiveSheet.getCellRangeByName("A2").Value
    
    ' Limpa a coluna D
    ThisComponent.CurrentController.ActiveSheet.getCellRangeByName("D:D").ClearContents(com.sun.star.sheet.CellFlags.VALUE)
    
    ' Gera as letras do alfabeto e insere na coluna D
    For i = 1 To Numero
        valor = i
        letra1 = ""
        Do While valor > 0
            resto = (valor - 1) Mod 26
            letra1 = Chr(65 + resto) & letra1
            valor = (valor - resto) \ 26
        Loop
        ThisComponent.CurrentController.ActiveSheet.getCellByPosition(3, i).String = letra1
    Next i
End Sub

```

![LibreOffice_Basic](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/f19db8db-be3b-4725-bdc8-fa9598d64d3d)


## Planilha do LibreOffice CALC com a Massa de Dados pronta para o Cadastro em um Sistema

- Este planilha, podendo ser também uma tabela no banco de dados, contém os dados, ou seja, a massa de dados, como "Nome Completo", "CPF" e "Data de Nascimento", pronta para o Cadastro em um Sistema.

![Planilha_Massa_Dados_Gerada](https://github.com/moiseschiaretto/Python_MassadeDados/assets/84775466/107e5754-eeac-44d1-9ee5-90ce654aac25)



## Pasta "validacoes"

Contém o arquivo **"ValidacoesParaCadastrar.py"** com 3 (três) validações, são elas:

**- validarCPF**
  
  - Antes de realizar o cadastro em um sistema da massa de dados, é validado o **CPF com 10 (dez) dígitos,** os CPFs antigos são com menos de 10 (dez) dígitos, neste caso é completado com zeros à esquerda.

**- converterDataNasc**
  
  - É validada também a **Data de Nascimento** com a seguinte máscara ou formato dd/mm/yyyy.
 
**- validarCEP**

  - É validado também o **CEP com 8 (oito) dígitos,** os CEPs antigos são com menos de 8 (oito) dígitos, neste caso é completado com zeros à esquerda.

