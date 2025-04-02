import os

pastas_imagens = [f"/media/docente/408CFDC68CFDB68E/archive/images_{str(i).zfill(3)}/images" for i in range(1, 13)]

for pasta in pastas_imagens:
    if os.path.exists(pasta):
        print(f"{pasta}: {len(os.listdir(pasta))} imagens")
    else:
        print(f"{pasta}: Pasta não encontrada")
