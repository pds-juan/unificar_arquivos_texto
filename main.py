import os
from datetime import datetime
import shutil

## também funciona para arquivos TXT
## apenas trocar as menções da extensão .ret/.RET para .txt

# caminho da pasta onde estão os arquivos de entrada
pasta_entrada = './input'

# caminho das pastas para os arquivos de saída
pasta_output = f'./output/{datetime.now().strftime('%d_%m_%Y')}'
pasta_backup = f'./backup/{datetime.now().strftime('%d_%m_%Y')}'

# criando as pastas de saída caso elas não existam
for pasta in [pasta_output, pasta_backup]:
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# nome do arquivo de saída
arquivo_saida = f'{pasta_output}/arquivo_unificado.RET'

contador = 0
erros = 0

# abre ou cria, caso não exista, o arquivo de saída para escrita
with open(arquivo_saida, 'w', encoding='utf-8') as saida:
    # para cada arquivo na pasta, percorrendo em ordem alfabética
    for nome_arquivo in sorted(os.listdir(pasta_entrada)):
        # se o arquivo contiver a extensão .ret
        if nome_arquivo.lower().endswith('.ret'):
            # salva o caminho do arquivo de entrada
            caminho_arquivo = os.path.join(pasta_entrada, nome_arquivo)

            try:
                # abre o arquivo de entrada
                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                    # salva o conteúdo do arquivo lido
                    conteudo = arquivo.read()
                    # escreve o conteúdo no arquivo de saída
                    saida.write(conteudo)

                # quebra de linha entre o conteúdo de cada arquivo de entrada
                saida.write('\n\n')

                contador += 1
                print(f'✔ Arquivo lido com sucesso: {nome_arquivo}')

                # movendo arquivo lido para a pasta backup
                shutil.copy2(caminho_arquivo, pasta_backup)
                os.remove(caminho_arquivo)

            except Exception as e:
                # aumenta o contador de erros
                erros += 1
                print(f'✖ Erro ao ler o arquivo {nome_arquivo}: {e}')

print('\nArquivos .RET unificados com sucesso!')

# informa o número de arquivos não lidos por erro
if erros == 1:
    print(f'\nPorém {erros} arquivo não lido por erro continua na pasta input.')
elif erros != 0:
    print(f'\nPorém {erros} arquivos não lidos por erro continuam na pasta input.')

print(f'\nTotal de arquivos lidos: {contador}.')