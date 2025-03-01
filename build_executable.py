
"""
Script para criar executável do Clipboard Translator AI
"""
import os
import shutil
import PyInstaller.__main__

# Criando diretório para o executável se não existir
if not os.path.exists('dist'):
    os.makedirs('dist')

# Configuração para o PyInstaller
PyInstaller.__main__.run([
    'main-py.py',                          # Script principal
    '--name=ClipboardTranslatorAI',        # Nome do executável
    '--onefile',                           # Arquivo único
    '--windowed',                          # Modo de janela (sem console)
    '--add-data=assets:assets',            # Incluir a pasta assets
    '--icon=assets/logo.png',              # Ícone (se existir)
    '--clean',                             # Limpar cache antes de construir
])

print("Executável criado com sucesso! Disponível na pasta 'dist'.")
