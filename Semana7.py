import streamlit as st

def verificar_contrasena():
    st.title("Verificación de contraseña")

    # Variable para almacenar la contraseña
    contrasena_correcta = "asdasd"
    contrasena_ingresada = ""
    attempt_count = 0  # Contador de intentos para clave única

    # Repetir hasta que la contraseña sea correcta
    while contrasena_ingresada != contrasena_correcta:
        # Incrementar el contador en cada intento
        attempt_count += 1
        contrasena_ingresada = st.text_input(f"Introduce la contraseña (intento {attempt_count}):", type="password", key=f"password_input_{attempt_count}")
        
        if contrasena_ingresada == contrasena_correcta:
            st.success("Bienvenido")
            break
        elif contrasena_ingresada:
            st.error("Contraseña incorrecta, intenta de nuevo")

if __name__ == "__main__":
    verificar_contrasena()
