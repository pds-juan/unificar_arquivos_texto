import os

## também funciona para arquivos TXT
## apenas trocar as menções da extensão .ret/.RET para .txt

# caminho da pasta onde estão os arquivos de entrada
arquivos_entrada = './input'

# nome do arquivo de saída
arquivo_saida = 'arquivo_unificado.RET'

contador = 0

# abre ou cria, caso não exista, o arquivo de saída para escrita
with open(arquivo_saida, 'w', encoding='utf-8') as saida:
    # para cada arquivo na pasta, percorrendo em ordem alfabética
    for nome_arquivo in sorted(os.listdir(arquivos_entrada)):
        # se o arquivo contiver a extensão .ret
        if nome_arquivo.lower().endswith('.ret'):
            # salva o caminho do arquivo de entrada
            caminho_arquivo = os.path.join(arquivos_entrada, nome_arquivo)

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

            except Exception as e:
                print(f'✖ Erro ao ler o arquivo {nome_arquivo}: {e}')

print(f'\nArquivos .RET unificados com sucesso!')

print(f'\nTotal de arquivos lidos: {contador}.')