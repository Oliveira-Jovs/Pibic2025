import os

caminho = "/media/docente/408CFDC68CFDB68E/archive"

arquivos = os.listdir(caminho)

for arquivo in arquivos:
    print(arquivo)
