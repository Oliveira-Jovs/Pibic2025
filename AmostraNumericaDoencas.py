import matplotlib.pyplot as plt

# Seus dados
doencas = ["No Finding", "Infiltration", "Atelectasis", "Effusion", "Consolidation",
           "Nodule", "Mass", "Cardiomegaly", "Pneumothorax", "Edema",
           "Emphysema", "Pleural_Thickening", "Fibrosis", "Pneumonia", "Hernia"]

quantidades = [59993, 11731, 11478, 8001, 3305, 2991, 2911, 2389, 2183, 1857,
               1718, 1213, 1211, 324, 156]

plt.figure(figsize=(12, 6))
bars = plt.bar(doencas, quantidades, color='skyblue')

# Adicionar os valores acima das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, str(yval), ha='center', va='bottom', fontsize=10)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Quantidade de Imagens")
plt.title("Distribuição das Imagens por Doença")

plt.tight_layout()
plt.savefig("distribuicao_doencas.png")  # Salva o gráfico
plt.show()
