'''Constantes utilizadas no projeto
'''
DRIVER_PATH = r'C:\SeleniumDrivers'
'''Diretório de onde carregar o driver do Chrome. Deve ser alterado se necessário'''

BASE_URL = 'https://buscacepinter.correios.com.br/app/endereco/index.php'

# movido para a constante 'CRITERIA'
#CEP_URL = 'https://buscacepinter.correios.com.br/app/cep/index.php'

REGEX_CEP_COMPLETE = r'^\d{5}-?\d{3}$'
'''CEP completo tem o formato: '00000-000' '''

REGEX_CEP_INCOMPLETE = r'^\d{4,5}-?$|^\d{4,6}$' 
'''O site permite buscas a partir de 5 números.
Estou considerando 4 números também, para os
casos em que o CEP se inicia com 0. '''

REGEX_NAME = r'\w{2,}'
'''O site dos correios permite realizar a busca a partir de 2 \w'''

DATA_PATH = r'data'
'''pasta onde serão colocadas as demandas e arquivos resultantes'''

COMPLETED = 'demandas aceitas'
'''Nome da pasta de destino para salvar as buscas terminadas

Observação: a pasta deve ser criada manualmente (a implementar auto)'''

DENIED = 'demandas recusadas'
'''Nome da pasta de destino para salvar as demandas recusadas

Observação: a pasta deve ser criada manualmente (a implementar auto)'''

NO_RESULTS = 'Não há dados a serem exibidos'

CRITERIA = {
        'URL': {
                'Nome': 'https://buscacepinter.correios.com.br/app/endereco/index.php',
                'CEP': 'https://buscacepinter.correios.com.br/app/cep/index.php'
        },

        'SEARCH_BTN_ID': {
                'Nome': 'endereco',
                'CEP': 'cep'
        },
        
        'SEARCH_LOG': {
                'Nome': 'Resultado da Busca por Endereço ou CEP',
                'CEP': 'Resultado da Busca por CEP'
        },

        'COL': {
                'Nome': 0,
                'CEP': 1
        }
}
'''Dicionário que reúne alguns atributos de Nome e CEP, a fim de deixar o código
mais flexível'''

MSG_STATUS = {
        'Success_CEP':                          'A busca é feita com sucesso, pois a coluna "B" está preenchida e o CEP é válido',
        'Success_CEP_incomplete':               'A busca é feita com sucesso, pois a coluna "B" está preenchida e o CEP é valido, mesmo sendo incompleto',
        'Denied_no_CEP':                        'A busca é recusada pelo robô, erro de preenchimento (foi enforçado a busca por CEP, mas o CEP NÃO foi informado',
        'Denied_invalid_CEP':                   'A busca é recusada pelo robô, erro de preenchimento (foi enforçado a busca por CEP, mas o CEP é inválido',
        'Success_name':                         'A busca é feita com sucesso, pois a coluna "A" está preenchida e o nome (aparenta) ser válido',
        'Denied_no_name':                       'A busca é recusada pelo robô, erro de preenchimento (foi enforçado a busca por NOME, mas a coluna "A" está vazia',
        'Denied_invalid_name':                  'A busca é recusada pelo robô, erro de preenchimento (foi enforçado a busca por NOME, mas o nome é inválido',
        'Success_no_criteria_CEP':              'A busca é feita com sucesso, pois mesmo sem a coluna "C", temos ainda um CEP válido.',
        'Success_no_criteria_CEP_incomplete':   'A busca é feita com sucesso, pois mesmo sem a coluna "C", temos ainda um CEP válido.',
        'Success_no_criteria_name':             'A busca é feita com sucesso, pois mesmo sem a coluna "C" e sem um CEP válido, o nome da rua consta e (aparenta) ser válido.',
        'Denied_poor_parameters':               'A busca é recusada pelo robô, erro de preenchimento: a coluna "C" não está preenchida e ambos o nome o CEP não são válidos)',
        'No_results':                           'Não há dados a serem exibidos'
    }

RESULTS_HEADER = [
        'Linha Excel Entrada',                  # 0
        'Critério de Busca Utilizado',          # 1
        'Parâmetro de busca utilizado',         # 2
        'Logradouro/Nome',                      # 3
        'Bairro/Distrito',                      # 4
        'Localidade/UF',                        # 5
        'CEP',                                  # 6
        'Mensagem de status'                    # 7
        ]

SUMMARY_HEADER = [
        'Linha Excel Entrada',
        'Nome rua ou logradouro',
        'CEP',
        'Critério de busca',
        'Status da busca'
]

TABELA_BPA = {
        'Name': 'Exemplos BPA',
        'data': [ 
                #['NOME RUA OU LOGRADOURO', 'CEP', 'CRITÉRIO DE PESQUISA'],
                ['Escolastica Rosa de Almeida',     '18060',        'CEP'],     # Success_CEP_incomplete
                ['Escolastica Rosa de Almeida',     '',             'CEP'],     # Denied_no_CEP
                ['Escolastica',                     '18060-110',    'Nome'],    # Success_name
                ['Cleóbulo Amazonas Duarte',        '11020-220',    'CEP'],     # Success_CEP
                ['Escolastica Rosa de Almeida',     'aaaa',         'CEP'],     # Denied_invalid_CEP
                ['Escolastica Rosa de Almeida',     '18060-110',    ''],        # Success_no_criteria_name
                ['',                                '11020',        ''],        # Success_no_criteria_CEP
                ['',                                '18060-110',    'Nome']     # Denied_no_name
]}

TEST_CASE = {
        'Name': 'Teste',
        'data': [
                ['Escolastica Rosa de Almeida',     '050250',            'CEP'],         # Success_CEP_incomplete
                ['Escolastica',                     '18060-110',        'Nome'],        # 9 Success_name
                ['Escolastica Rosa de Almeida',     'aaaa',             'CEP'],         # 8 Denied_invalid_CEP
                ['Escolastica Rosa de Almeida',     '76920-000',        'CEP']          # Success_CEP
]}

TABELA_TESTA_TUDO = {
        'Name': 'Teste tudo',
        'data': [
                #['NOME RUA OU LOGRADOURO', 'CEP', 'CRITÉRIO DE PESQUISA'],
                ['Cleóbulo Amazonas Duarte',        '11020-220',        'CEP'],         # 1 Success_CEP
                ['Escolastica Rosa de Almeida',     '5025',             'CEP'],         # 2 Success_CEP_incomplete
                ['Escolastica Rosa de Almeida',     '05025',            'CEP'],         # 3 Success_CEP_incomplete
                ['Escolastica Rosa de Almeida',     '05025-',           'CEP'],         # 4 Success_CEP_incomplete
                ['Escolastica Rosa de Almeida',     '050250',           'CEP'],         # 5 Success_CEP_incomplete
                ['Escolastica Rosa de Almeida',     '0502501',          'CEP'],         # 6 Denied_invalid_CEP
                ['Escolastica Rosa de Almeida',     '',                 'CEP'],         # 7 Denied_no_CEP
                ['Escolastica Rosa de Almeida',     'aaaa',             'CEP'],         # 8 Denied_invalid_CEP
                ['Escolastica',                     '18060-110',        'Nome'],        # 9 Success_name
                ['',                                '18060-110',        'Nome'],        # 10 Denied_no_name
                ['A',                                '18060-110',       'Nome'],        # 11 Denied_invalid_name
                ['',                                '11020',            ''],            # 12 Success_no_criteria_CEP_incomplete
                ['Escolastica',                     '11020-220',        ''],            # 13 Success_no_criteria_CEP_complete
                ['Escolastica Rosa de Almeida',     '',                 ''],            # 14 Success_no_criteria_name
                ['Escolastica Rosa de Almeida',     '123',              ''],            # 15 Success_no_criteria_name
                ['A',                                '180',             '']             # 16 Denied_poor_parameters
]}

TABELA_TUDO_INVALIDO = {
                        'Name': 'Sem nenhum resultado',
                        'data': [
                                #['NOME RUA OU LOGRADOURO', 'CEP', 'CRITÉRIO DE PESQUISA'],
                                ['A',   '11',   'CEP'],
                                ['',    '',     'CEP'],
                                ['C',   'A',    'A'],
                                ['',    'aaaa', 'Nome'],
                                ['',    'aaaa', ''],
                                ['A',    '',    ''],
                                ['E',   '18060', 'Nome']  
]}

TABELA_2_COL = {
        'Name': 'Exemplo 2 colunas',
        'data': [ 
                #['NOME RUA OU LOGRADOURO', 'CEP', 'C. PESQUISA'],
                ['Escolastica Rosa de Almeida',     '18060'],
                ['Escolastica Rosa de Almeida',     ''],
                ['Escolastica',                     '18060-110'],
                ['Cleóbulo Amazonas Duarte',        '11020-220'],
                ['Escolastica Rosa de Almeida',     'aaaa'],
                ['Escolastica Rosa de Almeida',     '18060-110'],
                ['',                                '11020'],
                ['',                                '18060-110']
]}

TABELA_1_COL = {
        'Name': 'Exemplo 1 coluna',
        'data': [ 
        #['NOME RUA OU LOGRADOURO', 'CEP', 'C. PESQUISA'],
        ['Escolastica Rosa de Almeida'],
        ['Escolastica Rosa de Almeida'],
        ['Escolastica'],
        ['Cleóbulo Amazonas Duarte'],
        ['Escolastica Rosa de Almeida'],
        ['Escolastica Rosa de Almeida'],
        [''],
        ['']
]}
