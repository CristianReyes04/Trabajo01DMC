import streamlit as st
import numpy as np

st.session_state

st.title("Trabajo 01 ")
st.image("Logo_python.png")
st.sidebar.image("Logo_inst.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  valor_inicial = st.number_input("Ingrese el valor inicial: ", value=0)
  valor_final = st.number_input("Ingrese el valor Final: ", value=1)
  lista_numerica = list(range(valor_inicial,valor_final))
  #similar a print es write
  st.write(lista_numerica)
elif modulo == "Ejercicio 1":
  st.write("Estas en el Ejercicio 1")
elif modulo == "Ejercicio 2":
  st.write("Estas en el Ejercicio 2")
elif modulo == "Ejercicio 3":
  st.write("Estas en el Ejercicio 3")
elif modulo == "Ejercicio 4":
  st.write("Estas en el Ejercicio 4")
else:
  st.write("Elija una Opción")

