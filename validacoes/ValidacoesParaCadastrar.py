from datetime import datetime
from datetime import date
import pandas as pd
import re

def validarCPF(cpf):
    # Muitos CPFs na planilha de massa de dados não estão com os zeros à esquerda
    # Valida se o CPF contém 11, 10, 9 ou 8 digitos, senão completar com 0 (zeros) à esquerda do CPF
    cpf = str(row['CPF'])
    cpf = re.sub("\.0", "", cpf)
    print('CPF da planilha de Massa de Dados: ', cpf)
    cpf_digitos = len(str(cpf))
    print('Qtde de dígitos no CPF: ', cpf_digitos)
    if (cpf_digitos == 10):
        cpf_10 = ('0' + str(cpf))
        cpf = cpf_10
    elif (cpf_digitos == 9):
        cpf_09 = ('00' + str(cpf))
        cpf = cpf_09
    elif (cpf_digitos == 8):
        cpf_08 = ('000' + str(cpf))
        cpf = cpf_08
    print('CPF preechido com zeros à esquerda: ', cpf, '\n')
    return cpf

def converterDataNasc(data):
    # Inserir a Data de Nascimento no formato = dd/mm/yyyy, "SEM A BARRA", somente os dígitos, exemplo: 23082022
    # Converter de DateTime para Date, formato = dd/mm/aaaa (não usar o "str" na data, exemplo, data = (row['Data Nascimento'])
    # /%Y = retorna o ano com 4 dígitos (letra "Y" maiúscula)
    # /%y = retorna o ano com 2 dígitos (letra "Y" minúscula)
    # data_nasc = data.strftime('%d/%m/%Y')
    data = re.sub("\.0", "", data)
    print('Data sem formatação da planilha de Massa de Dados: ', data)
    data_digitos = len(str(data))
    print('Qtde de dígitos na Data de Nascimento: ', data_digitos)
    if (data_digitos == 7):
        data_digitos = ('0' + str(data))
        data = data_digitos
    # data_nasc = data.strftime('%d%m%Y')
    data_nasc = data
    print('Data com a formatação e SEM AS BARRAS, para uso no cadastro: ', data_nasc, '\n')
    return data_nasc

def validarCEP(cep):
    # Valida se o CEP contém 8 digitos senão adiciona o um 0 (zero) à esquerda do CEP (senão o CEP será inválido)
    # Muitos CEPs da planilha de massa de dados não estão com um zero à esquerda
    cep = str(row['CEP'])
    cep = re.sub("\.0", "", cep)
    print('CEP da planilha de Massa de Dados: ', cep)
    print('Qtde de dígitos no CEP: ', len(str(cep)))
    if len(str(cep)) < 8:
        cep_8 = ('0' + str(cep))
        cep = cep_8
    print('CEP preechido com zeros à esquerda: ', cep, '\n')
    return cep
