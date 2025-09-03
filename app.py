
#impot streamlit

# aqui eu coloco o titulo 
# st.tittle('Olá, mundo')

# #criando um calendario 
# date = st.date_input("Selecione uma data")

# #Permitindo o upload 
# file = st.file_uploader("Pick a file")
#python -m streamlit run app.py
# #

import streamlit as st 
import pandas as pd 

#sidebar para mexer na barra lateral
st.sidebar.image("logo.png")
st.sidebar.title('lANA MOBI')


carros = ['Fiat Mobi', 'Renault Kwid', 'Hyundai HB20 Sedan', 'Honda Civic', 'Audi Q5', 'Mercedes-AMG GT', 'BMW X6', 'Fiat Toro']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


#-------------------------------------------------------Pricipal

st.title('Car Future - Aluguel de carros ')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo : {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km =  st.text_input(f'Quantos km você pretende rodar com o {opcao}?')

if opcao == 'Fiat Mobi':
    diaria = 130

elif opcao == 'Renaut Kwid':
    diaria = 160

elif opcao == 'Hyundai HB20 Sedan':
    diaria = 200

elif opcao == 'Honda Civic':
    diaria = 250

elif opcao == 'Audi Q5':
    diaria = 850

elif opcao == 'Mercedes-AMG GT':
    diaria = 4.500

elif opcao == 'BMW X6':
    diaria = 2.500

elif opcao == 'Fiat Toro':
    diaria = 350 


if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')

