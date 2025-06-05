Projeto Streamlit – Análise Financeira da Microsoft
Este projeto é um app feito em Python com Streamlit para visualizar dados financeiros da Microsoft a partir de um arquivo CSV.

O que você precisa
Python 3.8 ou mais recente

pip (gerenciador de pacotes do Python)

Instalando as bibliotecas
Abra o terminal e execute:

bash
Copiar
Editar
pip install streamlit pandas matplotlib

Arquivos necessários
Coloque na mesma pasta os dois arquivos:

app.py → código do app

MS_Financial Sample.csv → arquivo com os dados

Como rodar
Abra o terminal (Prompt de Comando ou PowerShell)

Vá até a pasta onde estão os arquivos:

bash
Copiar
Editar
cd C:\Users\SeuUsuario\Desktop\PROVA
Rode o comando:

bash
Copiar
Editar
streamlit run app.py
O navegador abrirá automaticamente em http://localhost:8501. Se não abrir, acesse esse link manualmente.

Observação
O CSV precisa ter as colunas Date e Sales. O código já trata separadores e formatações comuns (como R$, , e .).
