'''Este é um dashboard em streamlit no qual faremos uma carteira de ações para o Benas

'''
# Importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf

# Importando os dados
#amazon= yf.download('AMZO34.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Benas
#amazon.head()
#petrobras= yf.download('PETR4.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Benas
#embraer= yf.download('EMBR3.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Benas
#magalu= yf.download('MGLU3.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Bena
#apple= yf.download('AAPL34.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Benas
#tesla= yf.download('TSLA34.SA',start='2022-01-01',end='2023-11-20') # Ações da carteira do Benas




# Lista de ações para escolher
acoes = ['AMZO34.SA', 'PETR4.SA', 'EMBR3.SA', 'MGLU3.SA', 'AAPL34.SA', 'TSLA34.SA']

# Criação do menu dropdown
acao_selecionada = st.selectbox('Escolha uma ação para analisar:', acoes)

# Baixando os dados da ação selecionada
dados_acao = yf.download(acao_selecionada, start='2022-01-01', end='2023-11-20')

# Mostrando os dados
st.write(dados_acao)

import matplotlib.pyplot as plt

# Calculando os retornos
dados_acao['Retorno'] = dados_acao['Adj Close'].pct_change()

# Criando o gráfico
plt.figure(figsize=(14,7))
plt.title('Retorno da ação ' + acao_selecionada)
plt.plot(dados_acao['Retorno'])
plt.xlabel('Data')
plt.ylabel('Retorno')
st.pyplot(plt)

#Agora vamos criarr o dashboard da carteira do Benas
import matplotlib.pyplot as plt

# Supondo que a carteira do Benas seja um dicionário com o nome do investimento e o valor investido
carteira_benas = {'PETR4.SA': 10000, 'AMAZO34.SA': 10000, 'MGLU3.SA': 20000, 'AAPL34.SA': 20000, 'TSLA34.SA': 15000, 'EMBR3.SA': 15000}

# Criando o gráfico de setores
plt.figure(figsize=(10, 5))
plt.pie(carteira_benas.values(), labels=carteira_benas.keys(), autopct='%1.1f%%')
plt.title('Composição da Carteira do Benas')
st.pyplot(plt)

# Criando o gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(carteira_benas.keys(), carteira_benas.values())
plt.title('Composição da Carteira do Benas')
plt.xlabel('Investimento')
plt.ylabel('Valor Investido')
st.pyplot(plt)

