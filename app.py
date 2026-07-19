import streamlit as st
import numpy as np
import datetime
import pandas as pd

class Actividad:
  def __init__(self, nombre, tipo, presupuesto, gasto_real):
    self.nombre = nombre
    self.tipo = tipo
    self.presupuesto = presupuesto
    self.gasto_real = gasto_real
  
  def esta_en_presupuesto(self):
    return self.gasto_real <= self.presupuesto

  def mostrar_info(self):
    return (
      f"Actividad: {self.nombre} | "
      f"Tipo: {self.tipo} | "
      f"Presupuesto: S/ {self.presupuesto:.2f} | "
      f"Gasto Real: S/ {self.gasto_real:.2f}"
    )
    
st.sidebar.image("Abnaks.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Abanks - Ladonware")
  st.image("ladon.jpg")

  st.write("Módulo Home Datos Personales")
  estudiante = "Cristian Valentin Reyes Reyes"
  nom_modulo    = "Módulo 01"
  informacion = "Soy de nacionalidad Peruana, actualmente vivo en Piura."
  anio = datetime.date.today().year
  descripcion = "El Proyecto de una plaforma que puedan gestionar operaciones Bancarias"
  tecnologias = "Python, Streamlit, NumPy"
  
  st.markdown(f""" **Nombre del estudiante:** {estudiante}""")
  st.markdown(f""" **Módulo:** {nom_modulo}""")
  st.markdown(f""" **Información del estudiante:** {informacion}""")
  st.markdown(f""" **Año:** {anio}""")
  st.markdown(f""" **Descripción del proyecto:** {descripcion}""")
  st.markdown(f""" **Tecnologías utilizadas:** {tecnologias}""")
  
elif modulo == "Ejercicio 1":
  st.title("Verificado Simple")
  presupuesto = st.number_input("Ingrese Presupuesto", value=0)
  gasto = st.number_input("Ingrese Gasto", value=0)
  if st.button("Verificar"):
        if gasto <= presupuesto:
            saldo = presupuesto - gasto
            st.success(f"✅ El gasto está dentro del presupuesto.")
            st.write(f"Saldo disponible: S/ {saldo:.2f}")
        else:
            exceso = gasto - presupuesto
            st.error(f"❌ El presupuesto fue excedido.")
            st.write(f"Excedido por: S/ {exceso:.2f}")
  
elif modulo == "Ejercicio 2":
  st.title("Registro Actividades Financieras")
  if "actividades" not in st.session_state:
    st.session_state.actividades = []
    
  nombre = st.text_input("Nombre de la actividad")
  tipo = st.selectbox(
    "Tipo de actividad",
    ["Capacitación", "Consultaria", "Servicio", "Evento", "Otro"])
    
  presupuesto = st.number_input(
    "Presupuesto",
    min_value=0.0,
    value=0.0)
  
  gasto_real = st.number_input(
    "Gasto real",
    min_value=0.0,
    value=0.0
  )
  if gasto_real <= presupuesto:
    estado = "Dentro del presupuesto"
  else:
    estado = "Excedió el presupuesto"
  
  if st.button("Agregar actividad"):
    actividad = {
      "Nombre": nombre,
      "Tipo": tipo,
      "Presupuesto": presupuesto,
      "Gasto Real": gasto_real,
      "Estado": estado
    }
    st.session_state.actividades.append(actividad)
  # Mostrar la tabla
  if len(st.session_state.actividades) > 0:
    
    st.subheader("Lista de actividades")
    df = pd.DataFrame(st.session_state.actividades)
    st.dataframe(df)
  
elif modulo == "Ejercicio 3":
  st.title("Funciones y Programación Funcional")
  def calcular_retorno(presupuesto, tasa, meses):
    return presupuesto * tasa * meses
  
  tasa = st.number_input("Ingrese tasa",min_value=0.0,value=0.0)
  meses = st.number_input("Ingrese meses", min_value=0,value=0)
  
  if st.button("Calcular"):
    st.session_state.actividades = list(
      map(
        lambda actividad: {
          **actividad,
          "Retorno_Esperado": calcular_retorno(actividad["Presupuesto"],tasa,meses)
        },
        st.session_state.actividades
      )
    )
    df = pd.DataFrame(st.session_state.actividades)
    st.dataframe(df)
    
elif modulo == "Ejercicio 4":
  st.title("Programación Orientada a Objetos")
  
  if len(st.session_state.actividades) > 0:
    
    st.subheader("Actividades registradas")
    for dato in st.session_state.actividades:
      actividad = Actividad(
        dato["Nombre"],
        dato["Tipo"],
        dato["Presupuesto"],
        dato["Gasto Real"]
      )
      st.write(actividad.mostrar_info())
      if actividad.esta_en_presupuesto():
        st.success("Dentro del presupuesto")
      else:
        st.warning("Excedió el presupuesto")
else:
  st.write("Elija una Opción")

