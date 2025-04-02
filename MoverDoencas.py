import os
import shutil
import pandas as pd
from tqdm import tqdm

caminho_csv = "/media/docente/408CFDC68CFDB68E/archive/Data_Entry_2017.csv"
pastas_imagens = [f"/media/docente/408CFDC68CFDB68E/archive/images_{str(i).zfill(3)}/images" for i in range(1, 13)]
pasta_saida = "/media/docente/408CFDC68CFDB68E/archive/imagens_separadas"

os.makedirs(pasta_saida, exist_ok=True)

df = pd.read_csv(caminho_csv)

total_imagens = len(df)

with tqdm(total=total_imagens, desc="Movendo imagens", unit="img") as pbar:
    for _, linha in df.iterrows():
        nome_imagem = linha["Image Index"]
        doencas = linha["Finding Labels"].split("|")

        for doenca in doencas:
            caminho_doenca = os.path.join(pasta_saida, doenca)
            os.makedirs(caminho_doenca, exist_ok=True)

            origem = next((os.path.join(pasta, nome_imagem) for pasta in pastas_imagens if os.path.exists(os.path.join(pasta, nome_imagem))), None)

            if origem:
                destino = os.path.join(caminho_doenca, nome_imagem)
                shutil.move(origem, destino)

        pbar.update(1)

print("Separação concluída!")
