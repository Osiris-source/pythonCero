import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import requests  # ✅ CAMBIADO: Agregar requests
import datetime
# ❌ ELIMINADO: smtplib y email
import os

st.set_page_config(
    page_title="Mi Portafolio Personal",
    layout="wide", 
    page_icon="👨‍💻",
    initial_sidebar_state="expanded"
)

# ✅ CSS SEGURO - Solo estilos básicos sin manipulación del DOM
st.markdown("""
<style>
    /* Solo colores y fuentes - nada que manipule la estructura */
    .main-header {
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
    }
    .section-header {
        color: #ff6b6b;
        border-bottom: 2px solid #ff6b6b;
        padding-bottom: 10px;
    }
    .card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🎯 Menú")
    st.markdown("---")
    seccion = st.radio(
        "Navegar a:",
        ["🏠 Inicio", "👤 Sobre Mí", "💼 Habilidades", "🚀 Proyectos", "📞 Contacto"]
    )

def mostrar_inicio():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("sets/osiris.jpg", 
                caption="🚀 Futuro Desarrollador Python", 
                use_container_width=True)

    with col2:
        # ✅ Usando markdown seguro con las clases CSS
        st.markdown('<p class="main-header">Bienvenido a Mi Portafolio Personal</p>', unsafe_allow_html=True)
        
        st.markdown("## Hola, soy **Osiris** 👋")
        
        # ✅ Usando containers de Streamlit en lugar de HTML personalizado
        with st.container():
            st.write("""
            🌟 **Soy un apasionado del desarrollo de software** con experiencia en Python y Streamlit. 
            Me encanta crear soluciones innovadoras que resuelvan problemas reales.
            
            📍 **Ubicación:** Sisa, Perú  
            🎓 **Educación:** Ingeniería de Sistemas - UNI  
            💡 **Especialidad:** Python, Streamlit, Análisis de Datos, Machine Learning
            """)
        
        # Métricas con mejor diseño
        st.markdown("---")
        col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
        with col_metrics1:
            st.metric("🎯 Experiencia", "1+ Años")
        with col_metrics2:
            st.metric("📂 Proyectos", "5+ Completados")
        with col_metrics3:
            st.metric("😊 Clientes", "100+ Satisfechos")

def mostrar_sobre_mi():
    st.markdown('<p class="section-header">👨‍🎓 Sobre Mí</p>', unsafe_allow_html=True)
    
    col_foto, col_texto = st.columns([1, 2])

    with col_foto:
        st.image("sets/io.jpg", width=280, caption="Flavio Becerra - Desarrollador")
        # Botones de redes sociales SEGUROS
        st.markdown("### 📱 Sígueme")
        st.write("[**Facebook**](https://www.facebook.com/flavio.becerrahernandez)")
        st.write("[**Instagram**](https://instagram.com/flavio_becerra)")
        st.write("[**WhatsApp**](https://wa.me/51982695101)")

    with col_texto:
        # ✅ Usando st.info, st.success para diseño sin CSS peligroso
        st.info("""
        ### 🎯 Mi Historia
        
        Soy un profesional dedicado y curioso, siempre en busca de nuevos desafíos. 
        Mi pasión por la programación comenzó cuando descubrí el poder de Python 
        para resolver problemas complejos.
        
        **Ahora estoy cumpliendo mi sueño** de convertirme en un desarrollador 
        de software competente y confiable, aprendiendo constantemente nuevas 
        tecnologías para ofrecer soluciones de alta calidad.
        """)
    
    # Galería de fotos MEJORADA
    st.markdown("---")
    st.subheader("📸 Galería de Mis Momentos")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("sets/osiris1.jpg", caption="👤 Personal", use_container_width=True)
    with col2:
        st.image("sets/cr7.jpg", caption="⚽ Ídolo", use_container_width=True)
    with col3:
        st.image("sets/girl.jpg", caption="💕 Novia", use_container_width=True)
    with col4:
        st.image("sets/Bachiller.jpg", caption="🎓 Bachiller", use_container_width=True)

def mostrar_habilidades():
    st.markdown('<p class="section-header">💼 Habilidades Técnicas</p>', unsafe_allow_html=True)
    
    # Diseño de habilidades MÁS VISUAL
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🐍 Python")
        st.progress(85)
        st.caption("Streamlit, Pandas, NumPy, FastAPI")
        
        st.subheader("📊 Análisis de Datos")
        st.progress(75)
        st.caption("Pandas, Power BI, Excel, SQL")
    
    with col2:
        st.subheader("🌐 Desarrollo Web")
        st.progress(90)
        st.caption("HTML, CSS, JavaScript, Angular")
        
        st.subheader("🤖 Machine Learning")
        st.progress(80)
        st.caption("Scikit-learn, TensorFlow")
    
    with col3:
        st.subheader("🗄️ Bases de Datos")
        st.progress(70)
        st.caption("MySQL, PostgreSQL, SQLite")
        
        st.subheader("🛠️ Herramientas")
        st.progress(80)
        st.caption("Git, GitHub, VS Code, Docker")

def mostrar_proyectos():
    st.markdown('<p class="section-header">🚀 Proyectos Destacados</p>', unsafe_allow_html=True)
    
    # Proyecto 1 con mejor diseño
    with st.container():
        st.subheader("👁️ Sistema de Reconocimiento Facial")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("""
            **Desarrollo completo de un sistema de reconocimiento facial utilizando:**
            - ✅ Python y OpenCV para procesamiento de imágenes
            - ✅ Algoritmos de Machine Learning para alta precisión
            - ✅ Base de datos para gestión de usuarios
            - ✅ Interfaz amigable con Streamlit
            
            **Tecnologías:** Python, OpenCV, Streamlit, SQLite
            """)
        
        with col2:
            st.image("sets/facial.jpg", caption="Sistema de Reconocimiento", use_container_width=True)
    
    st.markdown("---")
    
    # Proyecto 2 con mejor diseño
    with st.container():
        st.subheader("📈 Dashboard de Préstamos Bancarios")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("""
            **Análisis exhaustivo y visualización de datos financieros:**
            - 📊 Dashboard interactivo con Power BI
            - 🔍 Identificación de tendencias y patrones
            - 📋 Reportes automatizados para gerencia
            - 💡 Optimización de estrategias de ventas
            
            **Tecnologías:** Power BI, Pandas, SQL, Streamlit
            """)
        
        with col2:
            st.image("sets/pbi.jpg", caption="Dashboard Interactivo", use_container_width=True)

def mostrar_contacto():
    st.markdown('<p class="section-header">📞 Contáctame</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📬 Información de Contacto")
        
        # ✅ Usando st.metric para información de contacto visual
        st.write("**📧 Email:** osirishernandez171@gmail.com")
        st.write("**📞 Teléfono:** +51 982695101")
        st.write("**📍 Ubicación:** Sisa, Perú")
        
        st.markdown("---")
        st.subheader("🌐 Redes Sociales")
        st.write("💼 **[LinkedIn](https://www.linkedin.com/in/flavio-osiris-becerra-hernandez-7a6b46297/)**")
        st.write("💻 **[GitHub](https://github.com/Osiris-source)**")
        st.write("📱 **[Facebook](https://www.facebook.com/flavio.becerrahernandez)**")
    
    with col2:
        # ✅ Usando st.success para el cuadro de disponibilidad
        st.success("""
        ### 🎯 Disponibilidad
        
        **¡Estoy disponible para nuevas oportunidades!**
        
        - 💼 Ofertas laborales
        - 🤝 Colaboraciones en proyectos
        - 📚 Mentorías y asesorías
        - 🚀 Proyectos freelance
        
        **¡No dudes en contactarme!**
        """)
    
    st.markdown("---")
    st.subheader("💬 Envíame un Mensaje Directo")
    
    # Formulario MEJORADO visualmente CON FORMSPREE
    with st.form(key='contact_form'):
        col_nombre, col_email = st.columns(2)
        
        with col_nombre:
            nombre = st.text_input("👤 Nombre Completo", placeholder="Ej: Flavio Becerra")
        with col_email:
            email = st.text_input("📧 Email", placeholder="Ej: flavio@example.com")
        
        mensaje = st.text_area("💭 Mensaje", 
                             placeholder="¡Hola! Me gustaría contactarte porque...", 
                             height=120)
        
        enviar = st.form_submit_button("🚀 Enviar Mensaje")
        
        if enviar:
            if not all([nombre, email, mensaje]):
                st.error("❌ Por favor, completa todos los campos.")
            else:
                try:
                    # ✅ FORMSPREE - CON TU URL
                    FORMSPREE_URL = "https://formspree.io/f/xkgkgaqa"  # ← TU URL DE FORMSPREE
                    
                    # Datos para enviar a Formspree
                    data = {
                        "name": nombre,
                        "email": email,
                        "message": mensaje,
                        "_subject": f"📧 Nuevo mensaje de {nombre} - Portafolio",
                        "_replyto": email
                    }
                    
                    # Enviar el formulario
                    with st.spinner("📤 Enviando mensaje..."):
                        response = requests.post(
                            FORMSPREE_URL,
                            data=data,
                            headers={
                                "Accept": "application/json"
                            }
                        )
                    
                    if response.status_code == 200:
                        st.success("✅ ¡Mensaje enviado con éxito! Te contactaré pronto.")
                        st.balloons()
                        
                        # Mostrar resumen
                        with st.expander("📋 Ver resumen del mensaje enviado"):
                            st.write(f"**👤 Nombre:** {nombre}")
                            st.write(f"**📧 Email:** {email}")
                            st.write(f"**💭 Mensaje:** {mensaje}")
                            st.write(f"**📅 Fecha:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    else:
                        st.error("❌ Error al enviar el mensaje. Por favor, intenta nuevamente.")
                        
                except Exception as e:
                    st.error(f"❌ Ha ocurrido un error al enviar el mensaje: {e}")
                    st.info("🔍 Asegúrate de que tu conexión a Internet esté activa y vuelve a intentarlo.")

# Navegación
if seccion == "🏠 Inicio":
    mostrar_inicio()
elif seccion == "👤 Sobre Mí":
    mostrar_sobre_mi()
elif seccion == "💼 Habilidades":
    mostrar_habilidades()
elif seccion == "🚀 Proyectos":
    mostrar_proyectos()
elif seccion == "📞 Contacto":
    mostrar_contacto()

# Footer profesional
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Hecho con ❤️ usando Streamlit y Python | © 2024 Flavio Osiris Becerra Hernández"
    "</div>",
    unsafe_allow_html=True
)