import streamlit as st

#titulo a la aplicación
st.title("Introducción a Variables y tipos de datos en Python")

#Descripción Incial
st.write("Python es un lenguaje de programación dinámico donde ...")

#Sección para variable de tipo entero
st.header("Ejemplo 1: Enteros")
st.write("En python, un entero (integer) es un número sin decimales por ejemplo:")

#Input para que el usuario ingrese un dato (de preferencia un número entero)
int_variable = st.number_input("Ingrese un número entero:", value=42, step=1)

#Mostrando el valor
st.code(f"int_variable = {int_variable} # Tipo: {type(int_variable)}")