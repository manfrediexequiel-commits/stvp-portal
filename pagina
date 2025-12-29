import streamlit as st
import time
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #2563eb;
        color: white;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        border: none;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.75rem;
        background-color: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA ---
if 'mock_afiliaciones' not in st.session_state:
    st.session_state.mock_afiliaciones = []

mock_deudas = [
    {"dni": "12345678", "nombre": "Juan Pérez", "deuda": 1500, "mes": "Diciembre 2024"},
    {"dni": "23456789", "nombre": "Ana García", "deuda": 0, "mes": "Al día"},
    {"dni": "34567890", "nombre": "Carlos López", "deuda": 2500, "mes": "Noviembre/Diciembre 2024"}
]

# --- FUNCIONES DE NAVEGACIÓN ---
def home():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Bienvenido al Portal STVP")
        st.subheader("Sindicato de Trabajadores de Vigilancia Privada")
        st.write("""
        Unidos por tus derechos y bienestar laboral desde 1982. 
        Accede a tus beneficios, gestiona tu credencial y mantente al día con tu sindicato.
        """)
        if st.button("Quiero Afiliarme"):
            st.session_state.page = "Afiliación"
            st.rerun()
    with col2:
        st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png")

def beneficios():
    st.title("🎁 Beneficios para Afiliados")
    cols = st.columns(3)
    beneficios_list = [
        {"icon": "🏥", "title": "Salud", "desc": "Cobertura médica extendida para ti y tu familia."},
        {"icon": "🎓", "title": "Educación", "desc": "Cursos de capacitación y kits escolares."},
        {"icon": "🏨", "title": "Turismo", "desc": "Hoteles propios y convenios en todo el país."}
    ]
    for i, b in enumerate(beneficios_list):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
                <h3>{b['icon']} {b['title']}</h3>
                <p>{b['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

def credenciales():
    st.title("🪪 Credencial Digital")
    st.info("Serás redirigido al sistema de credenciales en breve...")
    
    url = "https://stvp-credencial.streamlit.app/#stvp-digital"
    st.markdown(f'''
        <a href="{url}" target="_blank">
            <button style="width:100%; background-color:#2563eb; color:white; padding:10px; border:none; border-radius:8px; cursor:pointer;">
                Abrir Mi Credencial Ahora
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    with st.spinner("Redirigiendo..."):
        time.sleep(2)
        st.success("Si no se abrió la pestaña, utiliza el botón de arriba.")

def afiliacion():
    st.title("📝 Formulario de Afiliación")
    with st.form("form_afiliacion"):
        col1, col2 = st.columns(2)
        nombre = col1.text_input("Nombre")
        apellido = col2.text_input("Apellido")
        dni = col1.text_input("DNI")
        celular = col2.text_input("Celular")
        empresa = st.text_input("Empresa donde trabajas")
        
        submitted = st.form_submit_button("Enviar Solicitud")
        if submitted:
            if nombre and apellido and dni:
                nueva_solicitud = {"nombre": nombre, "dni": dni, "fecha": str(datetime.now())}
                st.session_state.mock_afiliaciones.append(nueva_solicitud)
                st.balloons()
                st.success("¡Solicitud enviada con éxito! Nos contactaremos pronto.")
            else:
                st.error("Por favor completa los campos obligatorios.")

def consulta_pago():
    st.title("🔍 Consulta de Estado de Cuenta")
    dni_busqueda = st.text_input("Ingresa tu DNI (sin puntos)")
    
    if st.button("Consultar"):
        resultado = next((item for item in mock_deudas if item["dni"] == dni_busqueda), None)
        
        if resultado:
            st.markdown("---")
            if resultado["deuda"] > 0:
                st.warning(f"### Deuda Pendiente: ${resultado['deuda']}")
                st.write(f"**Afiliado:** {resultado['nombre']}")
                st.write(f"**Período:** {resultado['mes']}")
                st.write("Contacto para pago: stvp.sindicatodeseguridad@gmail.com")
            else:
                st.success(f"### ✅ ¡Estás al día, {resultado['nombre']}!")
        else:
            st.error("No se encontró información para ese DNI.")

def contacto():
    st.title("📞 Contacto")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Información General
        - **📧 Email:** stvp.sindicatodeseguridad@gmail.com
        - **🏛️ Inscripción Gremial:** Nº 2822
        - **⏰ Horario:** Lunes a Viernes 9:00 - 17:00 hs
        """)
    with col2:
        st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=200)

# --- LÓGICA DE NAVEGACIÓN ---
if 'page' not in st.session_state:
    st.session_state.page = "Inicio"

with st.sidebar:
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=100)
    st.title("Menú STVP")
    page = st.radio("Ir a:", ["Inicio", "Beneficios", "Credenciales", "Afiliación", "Consulta de Pago", "Contacto"])
    st.session_state.page = page

# Renderizar la página seleccionada
if st.session_state.page == "Inicio":
    home()
elif st.session_state.page == "Beneficios":
    beneficios()
elif st.session_state.page == "Credenciales":
    credenciales()
elif st.session_state.page == "Afiliación":
    afiliacion()
elif st.session_state.page == "Consulta de Pago":
    consulta_pago()
elif st.session_state.page == "Contacto":
    contacto()

# --- FOOTER ---
st.markdown("---")
st.caption("© 2024 Sindicato de Trabajadores de Vigilancia Privada (STVP). Todos los derechos reservados.")
