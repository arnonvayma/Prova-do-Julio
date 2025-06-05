import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análise Financeira da Microsoft")
st.write("Este é um aplicativo Streamlit básico que carrega e visualiza dados financeiros da Microsoft.")

# Leitura do CSV com separador correto
df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
df.columns = df.columns.str.strip()  # limpar espaços em nomes de colunas

st.subheader("Visualização da Tabela de Dados")
st.dataframe(df)

st.subheader("Gráfico de Vendas ao longo do Tempo")

# Verifica colunas relevantes
if 'Date' in df.columns and 'Sales' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date', 'Sales'])  # remove linhas inválidas

    # Limpeza e conversão da coluna 'Sales'
    df['Sales'] = (
        df['Sales']
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
        .astype(float)
    )

    df = df.sort_values('Date')
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel("Data")
    ax.set_ylabel("Vendas")
    ax.set_title("Vendas ao longo do tempo")
    st.pyplot(fig)
else:
    st.warning("Colunas 'Date' e 'Sales' não encontradas no dataset. Gráfico não gerado.")


