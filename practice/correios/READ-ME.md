Como rodar o bot:

    1) Descompactar todos os arquivo em uma pasta raiz.
    2) Alterar a constante DRIVER_PATH com o caminho no qual se encontra o driver do Chrome a ser usado pelo Selenium.
    3) Rodar o script 'run.py'

A partir daí, o bot estará monitorando a pasta de entrada (default: 'data', porém pode ser alterada na constante "DATA_PATH").

Quando o processamento do arquivo acabar, o mesmo será movido para a respectiva pasta de acordo com o status da demanda (aceita / recusada).  O caminho dessas pastas podem ser alterados nas constantes 'COMPLETED' e 'DENIED'.

Também, algumas infos sobre a demanda (executada/negada) serão gravadas num arquivo de log (é criado caso não exista).

Os métodos estão todos comentados e uma documentação criada automaticamente (com pdoc3) para a classe Correios está disponível em html/correios.

Obs.: O arquivo gerar_exemplos.py é um script para gerar arquivo(s) Excel para fins de teste. Tem a opção de limpar todos os arquivos das pastas de entrada e saída.

Oportunidade de melhorias (aposto que sejam muitas, mas entre elas):
    - Trocar os sleep() que estão espalhados pelo código
    - Usar convenção para nome de variáveis / métodos