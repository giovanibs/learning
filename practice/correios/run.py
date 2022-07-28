'''
Monitora a pasta definida na constante DATA_PATH (por default, é a pasta 'data').
Usa 'os.walk()' para obter a lista de arquivos presentes nela.
Verifica se a extensão do arquivo é '.xlsx'. Se sim, inicia validação e obtenção de dados.
Move o arquivo para uma pasta de acordo com o status do job:
    \denied\ caso a demanda tenha sido negada.
    \completed\ caso a demanda tenha sido completada
Faz o log das tarefas executadas/recusadas num arquivo de
'''
from correios.correios import Correios, const
from time import time, sleep
import shutil
import os
import csv

data_dir = os.path.join(os.getcwd(), const.DATA_PATH)

def log_file(file_src, file_dest, start_time, end_time, job_status):
    '''Método para excrever no log de jobs executados'''
    # LOG DOS JOBS EXECUTADOS
    log_exists = os.path.isfile('log_file.csv')
                
    with open('log_file.csv', mode='a', newline='') as log_file:
        log_writer = csv.writer(log_file, delimiter=',')
        if not log_exists:
            log_writer.writerow(['file_src','file_dest','job_status','start_time','end_time'])
                    
        log_str = [
                        file_src,
                        file_dest,
                        job_status,
                        start_time,
                        end_time
                    ]
        log_writer.writerow(log_str)

while True:
    print('\nMonitorando...')

    # !!! trocar para: for file in os.listdir(data_dir)
    for dirpath, dirnames, filenames in os.walk(data_dir):
        for file in filenames:
            file_src = os.path.join(dirpath, file)
            is_excel = os.path.splitext(file)[1] == '.xlsx'
            file_dest = ''
            job_status = ''

            if is_excel:
                print(f'Excel encontrado: {file_src}')
                start_time = time()
                with Correios(teardown=True) as bot:
                    file_dest, job_status = bot.get_results(file_src)
                end_time = time()
                
                log_file(file_src, file_dest, start_time, end_time, job_status)   
                shutil.move(file_src, file_dest)
        break #break pra ler apenas os arquivos da pasta data_dir
    sleep(3)
