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
# formula = tempo "em função de" distancia [ tempo = f(distancia) ]
reg_simples = sm.OLS.from_formula(formula = 'tempo ~ distancia',
                                  data=alunos).fit()

# Obtenção dos outputs
print(reg_simples.summary())

# ANOVA da regressão
sm.stats.anova_lm(reg_simples)

## Alpha = 5,8784
## Beta  = 1,4189
## Y = 5,87 + 1,4189 * X -> Modelo de regressão linear simples


#%% Análise do coeficiente de explicação (R²)

# R² = SQR / (SQR + SQU)
1638.851351 / (1638.851351 + 361.148649)

# Na regressão simples, o R² pode ser obtido pelo coef_correl²
(alunos[['tempo', 'distancia']].corr())**2

#%% Valores preditos pelo modelo para as observações da amostra

## É o cálculo do valor estimado de Y com base no modelo

# Vamos elaborar uma tabela em separado
tabela_fitted = pd.DataFrame({'estudante': alunos['estudante'],
                              'tempo_real': alunos['tempo'],
                              'tempo_pred_simples': reg_simples.fittedvalues})

#%% Analisando os resíduos do modelo

# resíduos = valores observados - valores preditos
reg_simples.resid

## Note que são os erros para as observações da amostra

#%% Analisando o ajuste com o intervalo de confiança

# ci = 95%
sns.regplot(data=alunos, x='distancia', y='tempo', ci=95, line_kws={'color':'red', 'lw':1})
plt.xlabel('Distância Percorrida', fontsize=10)
plt.ylabel('Tempo para Chegar à Escola', fontsize=10)
plt.title('Ajuste do Modelo - IC 95%', fontsize=10)
plt.show()

# ci = 99%
sns.regplot(data=alunos, x='distancia', y='tempo', ci=99, line_kws={'color':'red', 'lw':1})
plt.xlabel('Distância Percorrida', fontsize=10)
plt.ylabel('Tempo para Chegar à Escola', fontsize=10)
plt.title('Ajuste do Modelo - IC 99%', fontsize=10)
plt.show()

#%% Analisando opções para os intervalos de confiança dos parâmetros do modelo

# Nível de confiança de 90%
reg_simples.conf_int(alpha=0.10)

# Nível de confiança de 95% (originalmente apresentado no output)
reg_simples.conf_int(alpha=0.05)

# Nível de confiança de 99%
reg_simples.conf_int(alpha=0.01)

#%% Realizando predições para outras observações

# Utilizando a função "predict"
obs_simples = pd.DataFrame({'distancia': [30]})
print(f'valor predito: {round(reg_simples.predict(obs_simples)[0],2)}')

# Equivale ao cálculo manual
5.8784 + (1.4189*30)

#%% Regressão Linear Múltipla (OLS)

## Modelo proposto: tempo = f(distancia, semaforos)

#%% Análise do coeficiente de correlação de Pearson

pg.rcorr(alunos[['tempo', 'distancia', 'semaforos']],
         method = 'pearson', upper = 'pval', 
         decimals = 4, 
         pval_stars = {0.01: '***', 0.05: '**', 0.10: '*'})

#%% Analisando graficamente as relações entre as variáveis

sns.pairplot(alunos[['tempo', 'distancia', 'semaforos']], plot_kws={'color': 'purple'})

#%% Regressão Linear Múltipla

# Estimação do modelo
reg_multipla = sm.OLS.from_formula(formula = 'tempo ~ distancia + semaforos',
                                   data=alunos).fit()

# Obtenção dos outputs
reg_multipla.summary()

#%%
# ANOVA da regressão
sm.stats.anova_lm(reg_multipla)

#%% Valores preditos pelo modelo para as observações da amostra

tabela_fitted['tempo_pred_multipla'] = reg_multipla.fittedvalues

#%% Analisando os resíduos do modelo

# resíduos = valores observados - valores preditos
reg_multipla.resid

#%% Realizando predições para outras observações

# Utilizando a função "predict"
obs_multipla = pd.DataFrame({'distancia': [18],
                             'semaforos': [3]})
print(f'valor predito: {round(reg_multipla.predict(obs_multipla)[0],2)}')

# Cálculo manual do valor predito
8.1512 + (0.7972*18) + (8.2963*3)

#%% Variáveis explicativas categóricas: variável dummy

## Modelo proposto: tempo = f(distancia, semaforos, periodo, perfil)

#%% Criação das variáveis binárias

alunos = pd.get_dummies(data=alunos, 
                        columns=['periodo', 'perfil'], 
                        drop_first=False,
                        dtype='float')

#%% Regressão Linear Múltipla (Variável X Categórica)

# Estimação do modelo
reg_multipla_dummy = sm.OLS.from_formula(formula = 'tempo ~ distancia + semaforos + periodo_manhã + perfil_moderado + perfil_agressivo',
                                         data=alunos).fit()

# Obtenção dos outputs
reg_multipla_dummy.summary()

## Uma categoria de cada variável categórica não é inserida (n-1 dummies)
## A categoria não especificada fica no intercepto como referência

#%% Procedimento de stepwise

# Procedimento stepwise para a remoção de variáveis não significativas
modelo_step = stepwise(reg_multipla_dummy, pvalue_limit=0.05)

#%% Valores preditos pelo modelo para as observações da amostra

tabela_fitted['tempo_pred_step'] = modelo_step.fittedvalues

#%% Analisando os resíduos do modelo

# resíduos = valores observados - valores preditos
modelo_step.resid

#%% Realizando predições para outras observações

# Utilizando a função "predict"
obs_step = pd.DataFrame({'distancia': [10],
                         'semaforos': [2],
                         'perfil_agressivo': [1]})
print(f'valor predito: {round(modelo_step.predict(obs_step)[0],2)}')

# Cálculo manual do valor predito
8.2919 + (0.7105*10) + (7.8368*2) + (8.9676*1)

#%% Comparando graficamente os ajustes dos modelos

sns.scatterplot(tabela_fitted, x='tempo_real', y='tempo_pred_simples')
sns.scatterplot(tabela_fitted, x='tempo_real', y='tempo_pred_multipla')
sns.scatterplot(tabela_fitted, x='tempo_real', y='tempo_pred_step')
plt.title('Comparando as Previsões', fontsize=10)
plt.xlabel('Tempo Observado', fontsize=10)
plt.ylabel('Tempo Previsto pelo Modelo', fontsize=10)
plt.axline((0, 0), (max(alunos['tempo']), max(alunos['tempo'])), linewidth=1, color='grey')
plt.legend(labels=['Reg. Simples','Reg. Múltipla','Reg. Múltipla Categ. (Stepwise)'], fontsize=8)
plt.show()

#%% Fim!