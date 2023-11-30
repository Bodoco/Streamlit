''' Este é um pequeno programa para introdução ao streamlit
Nele havera um um titulo, um subtitulo e um grafico de linhas com dados aleatórios gerados por numpy
'''
import streamlit as st
import numpy as np
import pandas as pd

st.title('Meu primeiro programa em streamlit')
st.subheader('Bem vindo ao meu programa')

#agora vamos gerar os dados aleatórios

dados = np.random.randn(100,2)

#agora vamos criar um dataframe com os dados
df=pd.DataFrame(dados,columns=['coluna1','coluna2'])

#agora vamos criar um grafico de linhas com os dados
st.line_chart(df)

