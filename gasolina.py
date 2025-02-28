import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.columns[0], y=df.columns[1], marker='o')
plt.xlabel("Data")
plt.ylabel("Preço da Gasolina")
plt.title("Variação do Preço da Gasolina")
plt.xticks(rotation=45)
plt.grid(True)

# Salvar o gráfico
plt.savefig("gasolina.png", dpi=300, bbox_inches='tight')
plt.show()
