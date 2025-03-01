
"""
Script para criar executável do Clipboard Translator AI
"""
import os
import subprocess

# Criando diretório para o executável se não existir
if not os.path.exists('dist'):
    os.makedirs('dist')

# Executar PyInstaller via comando de shell para melhor compatibilidade com Replit
command = [
    'pyinstaller',
    'main-py.py',                  # Script principal
    '--name=ClipboardTranslatorAI',# Nome do executável
    '--onefile',                   # Arquivo único
    '--windowed',                  # Modo de janela (sem console)
    '--add-data=assets:assets',    # Incluir a pasta assets
    '--icon=assets/logo.png',      # Ícone (se existir)
    '--clean'                      # Limpar cache antes de construir
]

print("Iniciando a criação do executável...")
print("Isso pode levar alguns minutos...")

try:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    print("Executável criado com sucesso! Disponível na pasta 'dist'.")
except subprocess.CalledProcessError as e:
    print(f"Erro ao criar o executável: {e}")
    print(f"Saída de erro: {e.stderr}")
