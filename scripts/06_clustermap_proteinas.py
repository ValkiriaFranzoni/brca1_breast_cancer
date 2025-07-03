import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Simulação de dados de expressão de proteínas
dados = {
    'Protein1': [2.1, 3.4, 1.8, 3.3],
    'Protein2': [1.9, 3.1, 2.0, 3.2],
    'Protein3': [2.0, 3.2, 1.7, 3.0],
    'Protein4': [2.2, 3.3, 1.9, 3.4]
}

df = pd.DataFrame(dados, index=['Amostra1', 'Amostra2', 'Amostra3', 'Amostra4'])

# Criar o clustermap
sns.clustermap(df, cmap="viridis", standard_scale=1)
plt.savefig('images/06_clustermap_proteinas.png')
plt.show()
