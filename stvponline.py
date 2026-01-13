import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Oficial",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. ESTILOS DE ALTA VISIBILIDAD (FONDO CELESTE) ---
st.markdown("""
    <style>
    .stApp { background-color: #E3F2FD; }
    .section-title {
        font-size: 2.5rem; font-weight: 800; color: #0D47A1;
        text-align: center; margin: 2rem 0; text-transform: uppercase;
    }
    .white-container {
        background-color: #ffffff; padding: 30px; border-radius: 20px;
        border: 3px solid #0D47A1; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .benefit-card {
        padding: 20px; border-radius: 15px; background-color: #ffffff;
        border-left: 8px solid #1E88E5; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px; min-height: 180px;
    }
    .whatsapp-float {
        position: fixed; width: 60px; height: 60px; bottom: 30px; right: 30px;
        background-color: #25d366; color: white; border-radius: 50px;
        text-align: center; z-index: 9999; display: flex; 
        align-items: center; justify-content: center; text-decoration: none;
    }
    </style>
    
    <a href="https://wa.me/5491152628936" class="whatsapp-float" target="_blank">
        <svg width="30" height="30" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. CONEXIÓN A GOOGLE SHEETS ---
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit#gid=6508803"
conn = st.connection("gsheets", type=GSheetsConnection)

def guardar_nuevo_afiliado(datos_dict):
    try:
        # Intentar leer la hoja existente
        df_old = conn.read(spreadsheet=URL_SHEET, worksheet="Afiliaciones", ttl=0)
        # Crear DataFrame con el nuevo registro
        df_new_row = pd.DataFrame([datos_dict])
        # Unir y actualizar
        df_final = pd.concat([df_old, df_new_row], ignore_index=True)
        conn.update(spreadsheet=URL_SHEET, worksheet="Afiliaciones", data=df_final)
        return True
    except Exception as e:
        st.error(f"Error de conexión: {e}")
        return False

# --- 4. CONTENIDO: INICIO ---
c1, c2 = st.columns([1, 3])
with c1: st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=150)
with c2:
    st.markdown("<h1 style='color: #0D47A1;'>STVP - Portal de Autogestión</h1>", unsafe_allow_html=True)
    st.write("Gestiona tu afiliación y accede a beneficios exclusivos para vigiladores.")

# --- 5. SECCIÓN BENEFICIOS (CARDS + TURISMO) ---
st.markdown('<div class="section-title">Beneficios y Convenios</div>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1: st.markdown('<div class="benefit-card"><h3>🏨 Turismo</h3><p>Convenios con Luz y Fuerza. Hoteles en la Costa, Córdoba y Bariloche.</p></div>', unsafe_allow_html=True)
with b2: st.markdown('<div class="benefit-card"><h3>🏍️ Ciudad Moto</h3><p>Descuentos especiales en la compra de tu unidad y repuestos.</p></div>', unsafe_allow_html=True)
with b3: st.markdown('<div class="benefit-card"><h3>⚖️ Gremiales</h3><p>Asesoría legal gratuita y apoyo en el lugar de trabajo.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
st.subheader("🏖️ Detalle Temporada 25/26")
t1, t2, t3 = st.tabs(["San Bernardo", "Villa Giardino", "Bariloche"])
with t1:
    st.write("**Hotel 'Por la Liberación Nacional'**")
    st.table({"Categoría": ["Doble", "Triple", "Cuádruple"], "Tarifa": ["$100.000", "$95.000", "$90.000"]})
with t2:
    st.write("**Villa Giardino, Córdoba**")
    st.write("Estadías semanales de 7 días. Tarifa base desde $74.700.")
with t3:
    st.write("**Bariloche - Hotel Alún Nehuén**")
    st.write("Media pensión incluida. Vistas al Nahuel Huapi.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FORMULARIO DE AFILIACIÓN CORREGIDO ---
st.markdown('<div class="section-title">Afiliación Online</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="white-container">', unsafe_allow_html=True)
    with st.form("form_afi_final", clear_on_submit=True):
        f1, f2 = st.columns(2)
        nombre = f1.text_input("Nombre y Apellido*")
        dni = f2.text_input("DNI (solo números)*")
        empresa = f1.text_input("Empresa de Seguridad*")
        celular = f2.text_input("WhatsApp de contacto*")
        
        intereses = st.multiselect("¿Qué beneficios te interesan más?", 
                                   ["Turismo", "Kit Escolar", "Asesoría Legal", "Salud"])
        
        st.caption("Los datos se tratan conforme a la Ley 25.326 de Protección de Datos.")
        acepto = st.checkbox("Acepto los términos y autorizo el tratamiento de mis datos.")
        
        enviar = st.form_submit_button("ENVIAR SOLICITUD")
        
        if enviar:
            if not (nombre and dni and celular and acepto):
                st.warning("⚠️ Completa los campos obligatorios y acepta los términos.")
            elif not dni.isdigit():
                st.error("❌ El DNI debe ser solo números.")
            else:
                # Preparamos los datos
                nuevo_registro = {
                    "Nombre": nombre,
                    "DNI": str(dni),
                    "Empresa": empresa,
                    "Celular": str(celular),
                    "Intereses": ", ".join(intereses),
                    "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "Estado": "Pendiente"
                }
                
                if guardar_nuevo_afiliado(nuevo_registro):
                    st.success(f"✅ ¡Excelente {nombre}! Tu solicitud se guardó correctamente.")
                    st.balloons()
                else:
                    st.error("❌ Error al guardar. Verifica la conexión con Google Sheets.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PIE DE PÁGINA ---
st.markdown("<p style='text-align:center; color:#0D47A1; font-weight: bold;'>Piedras 1065, CABA | STVP Sindicato</p>", unsafe_allow_html=True)
