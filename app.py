import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Título do Dashboard
st.header('Dashboard de Análise de Dados de Veículos')

hist_button_1 = st.button('Criar histograma')
hist_button_2 = st.button('Criar gráfico de dispersão')


if hist_button_1:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig_1 = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_1, use_container_width=True)

if hist_button_2:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig_2 = px.scatter(car_data, x="odometer", y='price')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_2, use_container_width=True)
