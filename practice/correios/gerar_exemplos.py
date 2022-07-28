'''
Com este script, é possível:
- Gerar arquivos Excel a fim de testar a automação.
- Remover todos os arquivos antigos.
'''
from openpyxl import Workbook
import correios.constants as const
import os

wdir = os.path.join(os.getcwd(), const.DATA_PATH)

def GerarDados(fname, tabela):
        """Gera um arquivo excel como exemplo com os dados para pesquisa
            :param fname: o caminho para salvar o Workbook
            :param tabela: informações em matrix de dados
        """
        print('Gerando dados...')
        wb = Workbook()
        ws = wb.active
       
        # loop para poopular os rows
        for localidade in tabela: # EXPLICAR COMO FUNCIONA O ENUMERATE!!!
            ws.append(localidade)
        wb.save(fname)
        wb.close()

# LIMPAR TODAS AS PASTAS (entrada e saída de arquivos Excel)?
if True:
    for dirpath, dirnames, filenames in os.walk(wdir):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

if True:
    tabelas = [
        const.TABELA_1_COL,
        const.TABELA_2_COL,
        const.TABELA_BPA,
        const.TABELA_TESTA_TUDO,
        const.TEST_CASE,
        const.TABELA_TUDO_INVALIDO
    ]
    
    for tabela in tabelas:
        file_name = os.path.join(wdir,'exemplos', f'{tabela["Name"]}.xlsx')
        GerarDados(file_name, tabela['data'])