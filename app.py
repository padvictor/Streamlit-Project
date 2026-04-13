import streamlit as st

st.header('Jogando uma moeda')

# Cria o controle deslizante (mínimo 1, máximo 1000, padrão 10)
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)

# Cria o botão
start_button = st.button('Executar')

# Se o botão for clicado, executa o código abaixo
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')

st.write('Ainda não é um aplicativo funcional. Em construção.')