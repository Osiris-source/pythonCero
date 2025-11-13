
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import smtplib 
from email.mime.text import MIMEText    
from email.mime.multipart import MIMEMultipart
import os
import datetime


st.set_page_config(page_title="Mi Portafolio Personal",
                   layout="wide", page_icon="O",
                   initial_sidebar_state="expanded")



st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.8rem;
        color: #ff6b6b;
        border-bottom: 2px solid #ff6b6b;
        padding-bottom: 0.5rem;
        
    }

</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Menu")
    st.markdown("---")
    seccion = st.radio(
        "Ir a:",
        ["📁 Inicio","👨‍🎓 Sobre Mí","💼 Habilidades", "📂 Proyectos", "📞 Contacto"]
    )

def mostrar_inicio():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        
        st.image( 
                 "sets/osiris.jpg", 
                 caption = "Soy egresado y quiero ser un profesional en python", 
                 use_container_width=True)

    with col2:
        st.markdown(
            "<h1 style='color:#1f77b4; text-align:center; font-weight:bold;'>Bienvenido a Mi Portafolio Personal</h1>",
            unsafe_allow_html=True
        )
        
        st.markdown("# Hola, soy Osiris")
        st.write("""
        Soy un entusiasta del desarrollo de software estoy practicando con python y streamlit, 
        análisis de datos y desarrollo web. Me apasiona crear soluciones innovadoras 
        que resuelvan problemas del mundo real.
        
        📍Soy de Sisa-Peru.
        🎓 Estudié en la UNI-Ingeniería de Sistemas gg.
        💡 Me gusta el lenguaje de python, usando tecnologías streamlit para el desarrollo web, machine learnig.
        """)
        
        col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
        with col_metrics1:
            st.metric("Años de Experiencia", "1+")
        with col_metrics2:
            st.metric("Proyectos Completados", "1+")
        with col_metrics3:
            st.metric("Clientes Satisfechos", "100+")

def mostrar_sobre_mi():
    st.markdown('<div class="section-title">👨‍🎓 Sobre Mí</div>', unsafe_allow_html=True)
    
    # Columnas para foto y texto
    col_foto, col_texto = st.columns([1, 2])

    with col_foto:
        st.image("sets/io.jpg", width=260,  caption="Flavio Becerra")

    with col_texto:
        st.markdown("""
        <div style='
        background-color: #f0f8ff; 
            padding: 1.5rem; 
            border-radius: 10px; 
            border-left: 4px solid #1f77b4;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        '>
        ### Mi Historia
        
        <h3 style='color: #1f77b4; margin-top: 0;'> Mi Historia</h3>
        Soy un profesional dedicado y curioso, siempre en busca de nuevos desafíos 
        y oportunidades para aprender y crecer. Mi pasión por la programación comenzó 
        cuando descubrí el poder de Python para resolver problemas complejos. Ahora estoy cumpliendo 
        mi sueño de convertirme en un desarrollador de software competente y confiable.
        Poco a poco estoy aprendiendo nuevas tecnocnologías  y herramientas para mejorar mis habilidades
        y ofrecer soluciones de alta calidad a mis clientes.
        
        Me encanta compartir conocimiento y colaborar en proyectos que tengan 
        un impacto positivo en la sociedad.
        </div>
       
        """, unsafe_allow_html=True)
        
        # Redes sociales
        st.markdown("""
        <div style="margin-top: 15px; text-align: center;">
            <h4>📱 Sígueme en:</h4>
            <a href="https://www.facebook.com/flavio.becerrahernandez" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" width="35" style="margin: 0 10px;">
            </a>
            <a href="https://instagram.com/flavio_becerra" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="35" style="margin: 0 10px;">
            </a>
            <a href="https://wa.me/51982695101" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/124/124034.png" width="35" style="margin: 0 10px;">
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # Galería de fotos
    with st.expander("📸 **Ver mi galería de fotos**", expanded=False):
        st.markdown("### Mis Momentos")
        col1, col2, col3, col4  = st.columns(4)
        
        with col1:
            st.image("sets/osiris1.jpg", width=180, caption="Personal")
        
        with col2:
            st.image("sets/cr7.jpg", width=180, caption="Idolo")
        
            with col3:
                st.image("sets/girl.jpg", width=180, caption="Novia")

        with col4:
            st.image("sets/Bachiller.jpg", width=180, caption="Bachiller")

            
def mostrar_habilidades():
    st.markdown('<div class="section-header"> Habilidades Técnicas</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Lenguajes de Programación de Python")
        st.progress(85)
        st.write("Python, Streamlit, Pandas, NumPy, fastApi")
        
        st.subheader("Analisis de Datos ")
        st.progress(75)
        st.write("Pandas, Power BI, Excel, SQL")
    with col2:
        st.subheader("Desarrollo Web")
        st.progress(90)
        st.write("HTML, CSS, JavaScript, Angular, Streamlit")
        
        st.subheader("Machine Learning")
        st.progress(80)
        st.write("MySql, SQLite, PostgreSQL")
        
    with col3:
        st.subheader("Bases de Datos")
        st.progress(70)
        st.write("MySql, SQL, PostgreSQL")
        
        st.subheader("Herramientas")
        st.progress(80)
        st.write("Git, GitHub, VS Code")
        
def mostrar_proyectos():
    st.markdown('<div class="section-header">📂 Proyectos Destacados</div>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Sistemas de reconocimiento facial")
            st.write("""
            - Desarrollé un sistema de reconocimiento facial utilizando Python y OpenCV.
            - Implementé algoritmos de aprendizaje automático para mejorar la precisión del reconocimiento.
            - Integré el sistema con una base de datos para almacenar y gestionar los datos de los usuarios.
            """)
        with col2:
            st.image("sets/facial.jpg", caption="Reconocimiento facial", use_container_width=True)
        st.markdown("---")
    with st.container():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Dashboard de prestamos bancarios")
            st.write("""
            - Realicé un análisis exhaustivo de los datos de ventas utilizando Pandas y Matplotlib.
            -Use Power BI para crear dashboards interactivos que faciliten la toma de decisiones.
            - Identifiqué tendencias y patrones clave para optimizar las estrategias de ventas.
            - Presenté los hallazgos a la gerencia mediante visualizaciones claras y concisas.
            """)
        with col2:
            st.image("sets/pbi.jpg", caption="Análisis de ventas", use_container_width=True)
        st.markdown("---")

def mostrar_contacto():
    st.markdown('<div class="section-header">📞 Contactactame </div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Información de Contacto")
        st.write("""
        - 📧 Email: osirishernandez171@gmail.com
        - 📞 Teléfono: +51 982695101
        - 📍 Dirección: sisa, Peru
        
        **🌐 Redes Sociales:**
        https://www.linkedin.com/in/flavio-osiris-becerra-hernandez-7a6b46297/
        [GitHub](https://github.com/Osiris-source)
        """)
    with col2:
        st.markdown("""
        <div class="card">
        ### Disponibilidad 
        **Estoy abierto a nuevas oportunidades laborales y colaboraciones en proyectos interesantes.
        <div>
        """, unsafe_allow_html=True)

    st.subheader("Envíame un Mensaje")
    with st.form(key='contact_form'):
        nombre = st.text_input("Nombre", placeholder="Ej. Flavio Becerra")
        email = st.text_input("Email", placeholder="Ej. flavio@example.com")
        mensaje = st.text_area("Mensaje", placeholder="Escribe tu mensaje aquí...", height=150)
        enviar = st.form_submit_button("Enviar")
        
        if enviar:
            if not all([nombre, email, mensaje]):
                st.error("Por favor, completa todos los campos antes de enviar el formulario.")
            else:
                try:
                    Tu_correo = "flbecerrah@alumno.unsm.edu.pe"
                    password = "wymj wvka hcen rlbw"
                    
                    email_body = f"""
                    **NUEVO MENSAJE DESDE TU PORTFOLIO STREAMLIT**
                    **Nombre:** {nombre}
                    **Email:** {email}
                    **fecha:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    
                    **Mensaje:**
                    {mensaje}
                    
                    ---
                    Este mensaje fue enviado automáticamente desde tu aplicación Streamlit.
                    Responde a: {email}
                    """
                    
                    msg = MIMEText(email_body)
                    msg["Subject"]=f"portafolio nuevo mensaje de {nombre}"
                    msg["From"]=Tu_correo
                    msg["To"]=Tu_correo
                    
                    #enviar el correo
                    with st.spinner("Enviando mensaje..."):
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(Tu_correo, password)
                        server.sendmail(Tu_correo, Tu_correo, msg.as_string())
                        server.quit()
                        
                    # Mensaje de éxito
                    st.success("¡Mensaje enviado con éxito! Me pondré en contacto contigo pronto.")
                    st.balloons()
                    
                    #mostrar resumen del mensaje
                    with st.expander("Ver resumen del mensaje"):
                        st.write(f"**Nombre:** {nombre}")
                        st.write(f"**Email:** {email}")
                        st.write(f"**Mensaje:** {mensaje}")
                        st.write(f"**Fecha:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        
                except smtplib.SMTPAuthenticationError:
                    st.error("Error de autenticación. Verifica tu correo y contraseña.")
                except Exception as e:
                    st.error(f"Ha ocurrido un error al enviar el mensaje: {e}")
                    st.info("Asegúrate de que tu conexión a Internet esté activa y vuelve a intentarlo.")                        
                    
            
     



if seccion == "📁 Inicio":
    mostrar_inicio()
elif seccion == "👨‍🎓 Sobre Mí":
    mostrar_sobre_mi()
elif seccion == "💼 Habilidades":
    mostrar_habilidades()
elif seccion == "📂 Proyectos":
    mostrar_proyectos()
elif seccion == "📞 Contacto":
    mostrar_contacto()          
      