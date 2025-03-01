
"""
Script para preparar os arquivos para download
"""
import os
import shutil
import zipfile

# Criar pasta para os arquivos
if not os.path.exists('download'):
    os.makedirs('download')

# Copiar o executável
if os.path.exists('dist/ClipboardTranslatorAI.exe'):
    shutil.copy('dist/ClipboardTranslatorAI.exe', 'download/')
elif os.path.exists('dist/ClipboardTranslatorAI'):
    shutil.copy('dist/ClipboardTranslatorAI', 'download/')

# Copiar arquivos necessários
if os.path.exists('assets'):
    if not os.path.exists('download/assets'):
        os.makedirs('download/assets')
    # Copiar arquivos da pasta assets
    for file in os.listdir('assets'):
        shutil.copy(os.path.join('assets', file), os.path.join('download/assets', file))

# Criar arquivo README
with open('download/README.txt', 'w', encoding='utf-8') as f:
    f.write("Clipboard Translator AI\n")
    f.write("======================\n\n")
    f.write("Desenvolvido por Paulo A. Giavoni\n\n")
    f.write("Instruções:\n")
    f.write("1. Execute o arquivo ClipboardTranslatorAI\n")
    f.write("2. Configure as opções de idioma e API\n")
    f.write("3. Clique em 'Iniciar Monitoramento' para começar a traduzir\n\n")
    f.write("Obrigado por usar o Clipboard Translator AI!")

# Criar arquivo ZIP para download fácil
with zipfile.ZipFile('download/ClipboardTranslatorAI.zip', 'w') as zipf:
    # Adicionar executável
    if os.path.exists('download/ClipboardTranslatorAI.exe'):
        zipf.write('download/ClipboardTranslatorAI.exe', 'ClipboardTranslatorAI.exe')
    elif os.path.exists('download/ClipboardTranslatorAI'):
        zipf.write('download/ClipboardTranslatorAI', 'ClipboardTranslatorAI')
    
    # Adicionar README
    zipf.write('download/README.txt', 'README.txt')
    
    # Adicionar pasta assets
    if os.path.exists('download/assets'):
        for root, dirs, files in os.walk('download/assets'):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.join('assets', file))

print("Arquivos preparados para download na pasta 'download'.")
print("Você pode baixar o arquivo ZIP completo para facilitar.")
