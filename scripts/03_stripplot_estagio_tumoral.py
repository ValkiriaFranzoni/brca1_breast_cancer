import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulação dos dados
dados = {
    'Estágio': ['I', 'II', 'III', 'I', 'II', 'III', 'I', 'II', 'III'],
    'Expressão': [2.3, 3.5, 5.0, 2.1, 3.2, 4.9, 2.0, 3.0, 5.1]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 6))
sns.stripplot(x='Estágio', y='Expressão', data=df, jitter=True, palette='Set2')

plt.title('Expressão da Protein1 por Estágio Tumoral')
plt.xlabel('Estágio Tumoral')
plt.ylabel('Nível de Expressão')
plt.tight_layout()
plt.savefig('images/03_stripplot_estagio_tumoral.png')
plt.show()
