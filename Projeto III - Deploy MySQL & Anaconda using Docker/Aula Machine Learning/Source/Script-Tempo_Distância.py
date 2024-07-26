# %%
# Importação do que vai ser utilizado
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
from statstests.process import stepwise

# Importação do banco de dados
alunos = pd.read_excel("/home/Resources/tempo_distancia.xlsx")


# Estatísticas descritivas

## Variáveis métricas
print(alunos[['tempo', 'distancia', 'semaforos']].describe())

## Variáveis categóricas - A descritiva de uma variável categórica é uma tabela de frequências
print(alunos[['periodo']].value_counts())
print(alunos[['perfil']].value_counts())


# Regressão Linear Simples (OLS)
## Modelo propost tempo = f(distancia)

# %%
sns.regplot(data=alunos, x='distancia', y='tempo',
            ci=False, line_kws={'color':'red', 'lw':1})
plt.xlabel('Distância Percorrida', fontsize=10)
plt.ylabel('Tempo para Chegar à Escola', fontsize=10)
plt.show()

#%% Análise do coeficiente de correlação de Pearson

# Variação de -1 a 1, sempre entre pares de variáveis
# -1 -> Relação são distintas
# 1  -> Correlação entre as variáveis
# 0  -> Não relação entre os cados

pg.rcorr(alunos[['tempo', 'distancia']],
         method = 'pearson', upper = 'pval', 
         decimals = 4, 
         pval_stars = {0.01: '***', 0.05: '**', 0.10: '*'})



#%% Regressão Linear Simples

# Estimação do modelo
# formula = tempo "em função de" distancia
reg_simples = sm.OLS.from_formula(formula = 'tempo ~ distancia',
                                  data=alunos).fit()

# Obtenção dos outputs
print(reg_simples.summary())

# ANOVA da regressão
sm.stats.anova_lm(reg_simples)

## Alpha = 5,8784
## Beta  = 1,4189
## Y = 5,87 + 1,4189 * X -> Modelo de regressão linear simples


# %%
