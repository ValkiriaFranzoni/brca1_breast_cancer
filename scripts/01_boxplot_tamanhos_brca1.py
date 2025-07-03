import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulação dos dados de comprimento do BRCA1
dados = {
    'Tipo': ['DNA', 'RNA', 'Proteína'],
    'Comprimento': [125000, 10000, 1900]
}

df = pd.DataFrame(dados)

# Criar o gráfico
plt.figure(figsize=(8, 6))
sns.barplot(x='Tipo', y='Comprimento', data=df, palette='Set2')

plt.title('Comprimentos das Sequências do Gene BRCA1')
plt.ylabel('Comprimento (pb ou aa)')
plt.xlabel('Tipo de Sequência')
plt.tight_layout()

# Salvar o gráfico como imagem PNG na pasta /images
plt.savefig('images/01_boxplot_tamanhos_brca1.png')

# Mostrar o gráfico na tela
plt.show()
