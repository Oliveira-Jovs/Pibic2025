import os
import matplotlib.pyplot as plt
from collections import Counter

pasta_saida = "/media/docente/408CFDC68CFDB68E/archive/imagens_separadas"

contagem = Counter()

for doenca in os.listdir(pasta_saida):
    caminho_doenca = os.path.join(pasta_saida, doenca)
    if os.path.isdir(caminho_doenca):
        contagem[doenca] = len(os.listdir(caminho_doenca))

contagem_ordenada = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

print("Quantidade de imagens por doença:")
for doenca, qtd in contagem_ordenada:
    print(f"{doenca}: {qtd}")

plt.figure(figsize=(12, 6))
plt.barh([x[0] for x in contagem_ordenada], [x[1] for x in contagem_ordenada], color='skyblue')
plt.xlabel("Quantidade de Imagens")
plt.ylabel("Doença")
plt.title("Distribuição das Imagens por Doença")
plt.gca().invert_yaxis()
plt.savefig("distribuicao_doencas.png")
plt.show()
