import shutil

# Copiando o arquivo para simular o backup
shutil.copy("dados.txt", "backup_dados.txt")

print("\nBackup realizado com sucesso!")