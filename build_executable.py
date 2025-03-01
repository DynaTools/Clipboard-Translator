
"""
Script para criar executável do Clipboard Translator AI
"""
import os
import subprocess
import sys
import traceback

print("Iniciando script build_executable.py")
print(f"Diretório atual: {os.getcwd()}")
print(f"Python versão: {sys.version}")

# Verificar se PyInstaller está instalado
try:
    import PyInstaller
    print(f"PyInstaller versão: {PyInstaller.__version__}")
except ImportError:
    print("PyInstaller não está instalado. Instalando...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    print("PyInstaller instalado com sucesso!")

# Criando diretório para o executável se não existir
if not os.path.exists('dist'):
    os.makedirs('dist')
    print("Diretório 'dist' criado.")

# Verificar se o arquivo principal existe
if not os.path.exists('main-py.py'):
    print("ERRO: O arquivo main-py.py não foi encontrado!")
    sys.exit(1)

# Verificar se a pasta assets existe
if not os.path.exists('assets'):
    print("AVISO: A pasta 'assets' não foi encontrada. Criando pasta vazia...")
    os.makedirs('assets')

# Executar PyInstaller via comando de shell para melhor compatibilidade com Replit
command = [
    'pyinstaller',
    'main-py.py',                  # Script principal
    '--name=ClipboardTranslatorAI',# Nome do executável
    '--onefile',                   # Arquivo único
    '--add-data=assets:assets',    # Incluir a pasta assets
    '--clean'                      # Limpar cache antes de construir
]

# No Replit, o modo console é mais confiável
if os.environ.get('REPLIT_ENVIRONMENT') == 'true':
    print("Detectado ambiente Replit: usando modo console")
else:
    command.append('--windowed')
    # Adicionar ícone apenas se existir
    if os.path.exists('assets/logo.png'):
        command.extend(['--icon=assets/logo.png'])

print(f"Comando a ser executado: {' '.join(command)}")
print("Iniciando a criação do executável...")
print("Isso pode levar alguns minutos...")

try:
    # Execute com mais informações de saída
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    
    # Exibir saída padrão e de erro para debug
    print("\nSaída do comando:")
    print(result.stdout)
    
    if result.returncode != 0:
        print("\nERRO na execução do comando:")
        print(result.stderr)
        print(f"Código de saída: {result.returncode}")
    else:
        print("Executável criado com sucesso! Disponível na pasta 'dist'.")
        
        # Verificar se o executável realmente foi criado
        exe_path = os.path.join('dist', 'ClipboardTranslatorAI.exe')
        unix_path = os.path.join('dist', 'ClipboardTranslatorAI')
        
        if os.path.exists(exe_path):
            print(f"Executável confirmado em: {exe_path}")
        elif os.path.exists(unix_path):
            print(f"Executável confirmado em: {unix_path}")
        else:
            print("AVISO: Executável não encontrado na pasta 'dist'!")
            print("Conteúdo da pasta 'dist':")
            for item in os.listdir('dist'):
                print(f"- {item}")
                
except Exception as e:
    print(f"Erro ao criar o executável: {e}")
    print("Detalhes do erro:")
    traceback.print_exc()
