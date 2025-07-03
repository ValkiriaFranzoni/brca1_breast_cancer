import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulação dos dados
dados = {
    'Status': ['Vivo', 'Óbito', 'Vivo', 'Óbito', 'Vivo', 'Óbito', 'Vivo', 'Óbito'],
    'Expressão': [2.5, 5.1, 2.7, 4.9, 2.9, 5.2, 2.6, 5.0]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 6))
sns.boxplot(x='Status', y='Expressão', data=df, palette='coolwarm', width=0.5)
sns.swarmplot(x='Status', y='Expressão', data=df, color='black', alpha=0.8)

plt.title('Expressão da Protein1 por Status Vital')
plt.xlabel('Status Vital')
plt.ylabel('Nível de Expressão')
plt.tight_layout()
plt.savefig('images/04_box_swarm_status_vital.png')
plt.show()

