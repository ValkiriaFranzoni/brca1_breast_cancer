import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulação de dados dos tamanhos das isoformas
dados = {
    'Isoforma': ['Isoforma1', 'Isoforma2', 'Isoforma3', 'Isoforma4', 'Isoforma5'],
    'Tamanho': [1800, 1850, 1900, 1700, 1750]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 6))
sns.histplot(df['Tamanho'], kde=True, bins=5, color='skyblue')

plt.title('Distribuição dos Tamanhos das Isoformas da Proteína BRCA1')
plt.xlabel('Tamanho (aa)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('images/02_histograma_isoformas_brca1.png')
plt.show()
