import os
from tkinter.filedialog import askdirectory

# Seleção de pasta usando o módulo tkinter
id_pasta = askdirectory(title='Selecione uma pasta')

# Lista os arquivos presentes na pasta selecionada
lista_de_arquivos = os.listdir(id_pasta)

# Cria um dicionário que mapeia as extensões para as pastas correspondentes
local = {
    'imagens': ['.png', '.jpeg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
}

# Lógica principal
for arquivos in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivos)

    for pasta in local:
        if extensao in local[pasta]:
            # Constrói o caminho da pasta onde o arquivo deve ser movido
            pasta_path = os.path.join(id_pasta, pasta)

            # Verifica se a pasta de destino existe, se não, cria
            if not os.path.exists(pasta_path):
                os.mkdir(pasta_path)

            # Constrói os caminhos antigo e novo para a movimentação do arquivo
            antigo_caminho = os.path.join(id_pasta, arquivos)
            novo_caminho = os.path.join(pasta_path, arquivos)

            # Move o arquivo para a pasta de destino
            os.rename(antigo_caminho, novo_caminho)
            break # Adicionado para evitar a movimentação para múltiplos diretórios
