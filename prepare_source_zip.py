
"""
Script para criar um ZIP com o código fonte para download
"""
import os
import zipfile
import shutil

print("Preparando código fonte para download...")

# Criar pasta para download se não existir
if not os.path.exists('download'):
    os.makedirs('download')

# Arquivos e pastas a serem incluídos
to_include = [
    'main-py.py',
    'config',
    'services',
    'ui',
    'utils',
    'assets',
    'README.md',
    'pyproject.toml'
]

# Criar arquivo README de instruções
with open('download/README_SOURCE.txt', 'w', encoding='utf-8') as f:
    f.write("Clipboard Translator AI - Código Fonte\n")
    f.write("===================================\n\n")
    f.write("Desenvolvido por Paulo A. Giavoni\n\n")
    f.write("Instruções para executar o código fonte:\n\n")
    f.write("1. Extraia o conteúdo do arquivo ZIP\n")
    f.write("2. Instale as dependências usando:\n")
    f.write("   pip install -r requirements.txt\n\n")
    f.write("3. Execute o programa usando:\n")
    f.write("   python main-py.py\n\n")
    f.write("Obrigado por usar o Clipboard Translator AI!")

# Criar requirements.txt
with open('download/requirements.txt', 'w', encoding='utf-8') as f:
    f.write("pyperclip>=1.9.0\n")
    f.write("requests>=2.32.3\n")
    f.write("tkinter\n")

# Criar arquivo ZIP com código fonte
with zipfile.ZipFile('download/ClipboardTranslatorAI_Source.zip', 'w') as zipf:
    # Adicionar arquivos do projeto
    for item in to_include:
        if os.path.isfile(item):
            zipf.write(item, item)
        elif os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = file_path  # Preservar a estrutura de diretórios
                    zipf.write(file_path, arcname)
    
    # Adicionar requirements.txt
    zipf.write('download/requirements.txt', 'requirements.txt')
    
    # Adicionar README
    zipf.write('download/README_SOURCE.txt', 'README.txt')

print("Código fonte preparado para download!")
print("Você pode baixar o arquivo ZIP 'ClipboardTranslatorAI_Source.zip' da pasta 'download'.")
