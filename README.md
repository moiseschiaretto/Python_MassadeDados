## Projeto "GerarMassaDados"
- Autor Moisés Ademir Chiaretto
  
- Descrição das explicações de cada item da 'estrutura do projeto "GerarMassaDados" desenvolvido'.
  
- **Python com Selenium WeDriver**
  
- **LibreOffice CALC com Macro em BASIC, pode utilizar também o Microsoft Excel com Macro em VBA.**

| ![04_Python](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/beabdf64-9d5f-493b-a24c-1f976962f1e9) | ![08_Selenium_Webdriver_02](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/69d76fa1-2cdb-4f3d-a379-d4eb27fd63ae)|
| ![19_LibreOffice_CALC](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/3663d8fb-efe1-48f1-8b71-afd62177b30e)     | ![20_MS_EXCEL_02](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/5e35925a-d8ba-41fd-822d-2bf7bce6f386)
 |


## Estrutura do Projeto "projeto_web"

```
GerarMassaDados
    |
    |-----.gitgnore
    |-----cpf_datanasc.csv
    |-----Extrair_CPF_DataNasc_Web.py
    |-----PLAN_CALC_MASSA_DADOS.ods
    |-----README.md
    |-----requirements.txt
    |
    |-----validacoes
    | 	    |---ValidacoesParaCadastrar.py

```

## Arquivo README.md
Explicações da Estrutura do Projeto e as suas respectivas configurações.


## Arquivo 'requeriments.txt'
Constam todas as 'bibliotecas' do projeto para serem instaladas, neste caso somente o Selenium WebDriver.
```
# requeriments.txt
selenium>=4.20.0
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

## Arquivo 'cpf_datanasc.csv'
Constam os dados que são **"CPF" e "Data de Nascimento"** extraídos do site da Web, para a geração da Massa de Dados, sendo um arquivo de log que armazena os dados capturados/extraídos, podendo também esses dados serem armaenados em uma tabela de um banco de dados.

https://geradorbrasileiro.com/pessoa

- URL que é acessada para capturar CPF e Data de Nascimento.

- Estes CPFs são válidos, porém não são quentes, ou seja, não constar no site da RF - Receita Federal.

-  Sendo assim podem serem utilizados em um Ambiente de Stage ou Produção.

https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp

![Dados_Gerados_Arquivo_Log](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/033176c9-82f0-4c60-8a78-2d20ffc52299)


## Arquivo 'Extrair_CPF_DataNasc_Web.py'

Arquivo do Python contém a programção utilizando a biblioteca "Selenium WebDriver" para acessar o Browser Mozilla Firefox e a URL abaixo para a geração de massa de dados, como CPF e Data de Nascimento, por exemplo.

https://geradorbrasileiro.com/pessoa

- Ao gerar no site da Web o "CPF" e a "Data de Nascimento" esse dados são armazenados em um **"arquivo de log"** para depois em uma **"segunda etapa"** serem inseridos em um sistema a quantidade de massa de dados desejada.

![Massa_de_Dados](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/31e9c224-e82a-4047-9209-539861e7fb31)

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

**Planilha do LibreOffice CALC com o botão "Gerar Letras na Coluna "D",** são geradas letras para os **sobrenomes** dos nomes sitéticos a serem cadastrados, por exemplo:
  - Teste A, Teste B, Teste C, ..., Teste Z,
  - Teste AA, Teste AB, Teste AC, ..., Teste AZ,
  - Teste BA, Teste BB, Teste BC, ..., Teste BZ,
  - E assim sucessivamente...

![Planilha_Massa_Dados_Gerada](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/951e32ec-8030-4f8f-b95f-81033857b566)

Código desenvolvido **na Macro BASIC utilizado no botão da planilha do LibreOffice CALC, para a geração dos **sobrenomes** dos nomes sintéticos.**

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
## Planilha do LibreOffice CALC com a Massa de Dados pronta para o Cadastro em um Sistema

- Este planilha, podendo ser também uma tabela no banco de dados, contém os dados, ou seja, a massa de dados, como "Nome Completo", "CPF" e "Data de Nascimento", pronta para o Cadastro em um Sistema.

![Planilha_Massa_Dados_Gerada](https://github.com/moiseschiaretto/Python_Massa_de_Dados/assets/84775466/c080b0f0-4818-4cc8-bcdc-90ffca4a77c8)


## Pasta validacoes

Contém o arquivo **"ValidacoesParaCadastrar.py"** com 3 (três) validações, são elas:

**- validarCPF**
  
  - Antes de realizar o cadastro em um sistema da massa de dados, é validado o **CPF com 10 (dez) dígitos,** os CPFs antigos são com menos de 10 (dez) dígitos, neste caso é completado com zeros à esquerda.

**- converterDataNasc**
  
  - É validada também a **Data de Nascimento** com a seguinte máscara ou formato dd/mm/yyyy.
 
**- validarCEP**

  - É validado também o **CEP com 8 (oito) dígitos,** os CEPs antigos são com menos de 8 (oito) dígitos, neste caso é completado com zeros à esquerda.

