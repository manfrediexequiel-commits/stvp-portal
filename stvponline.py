import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Portal STVP - Sindicato de Vigilancia",
    page_icon="🛡️",
    layout="wide"
)

# --- 2. ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #E3F2FD; }
    
    .section-title {
        font-size: 2.8rem; font-weight: 800; color: #0D47A1;
        text-align: center; margin: 2rem 0; text-transform: uppercase;
    }

    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%;
        background-color: #ffffff; z-index: 1000; padding: 12px;
        text-align: center; border-bottom: 4px solid #0D47A1;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .nav-bar a { 
        margin: 0 15px; text-decoration: none; color: #0D47A1; 
        font-weight: bold; font-size: 1rem;
    }

    .white-container {
        background-color: #ffffff; padding: 30px; border-radius: 20px;
        border: 2px solid #0D47A1; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }

    .btn-whatsapp-rolsol {
        background-color: #0080ff; color: white !important;
        padding: 12px 20px; text-decoration: none; border-radius: 8px;
        font-weight: bold; display: inline-block; margin-top: 15px;
    }
    
    .download-btn {
        display: inline-block; padding: 15px 25px; background-color: #D32F2F;
        color: white !important; text-decoration: none; border-radius: 10px;
        font-weight: bold; margin-top: 10px; border: 2px solid #B71C1C;
        text-align: center;
    }

    .whatsapp-float {
        position: fixed; width: 65px; height: 65px; bottom: 30px; right: 30px;
        background-color: #25d366; color: white; border-radius: 50px;
        text-align: center; box-shadow: 2px 5px 20px rgba(0,0,0,0.4);
        z-index: 9999; display: flex; align-items: center; justify-content: center;
        text-decoration: none;
    }
    </style>
    
    <a href="https://wa.me/5491152628936" class="whatsapp-float" target="_blank">
        <svg width="35" height="35" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
st.markdown("""<div class="nav-bar"><a href="#inicio">INICIO</a><a href="#beneficios">TURISMO</a><a href="#camping">CAMPING</a><a href="#afiliacion">AFILIACIÓN</a><a href="#contacto">SEDE</a></div><div style="margin-top: 100px;"></div>""", unsafe_allow_html=True)

# --- 4. CONEXIÓN A GOOGLE SHEETS ---
URL_SHEET = "https://docs.google.com/spreadsheets/d/1mmMbsH6BNfrcmtq3T7xDizBVxjd--sWUIUdBZtSPuFM/edit#gid=6508803"
conn = st.connection("gsheets", type=GSheetsConnection)

def guardar_registro(nombre, dni, empresa, celular, intereses):
    try:
        df_old = conn.read(spreadsheet=URL_SHEET, worksheet="Afiliaciones", ttl=0)
        nuevo = pd.DataFrame([{
            "Nombre": nombre, "DNI": str(dni), "Empresa": empresa,
            "Celular": str(celular), "Intereses": ", ".join(intereses),
            "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"), "Estado": "Pendiente"
        }])
        df_final = pd.concat([df_old, nuevo], ignore_index=True)
        conn.update(spreadsheet=URL_SHEET, worksheet="Afiliaciones", data=df_final)
        return True
    except Exception: return False

# --- 5. SECCIÓN INICIO ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
c_logo, c_title = st.columns([1, 3])
with c_logo: 
    st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=160)
with c_title:
    st.markdown("<h1 style='color: #0D47A1; margin-bottom:0;'>STVP - Sindicato Vigilancia</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1565C0;'>Gestión y Beneficios para el Trabajador</h3>", unsafe_allow_html=True)

# --- 6. SECCIÓN TURISMO ROLSOL ---
st.markdown('<div id="beneficios" class="section-title">🚌 Turismo RolSol</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_t1, col_t2 = st.columns([2, 1])
with col_t1:
    st.subheader("Ofertas de Verano - Salidas Enero 2026")
with col_t2:
    canal_whatsapp = "https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B"
    st.markdown(f'<a href="{canal_whatsapp}" target="_blank" class="btn-whatsapp-rolsol">📢 Canal de WhatsApp</a>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.image("https://i.postimg.cc/g0cwqwtH/rolsol1.jpg", caption="Bariloche", use_container_width=True)
with c2: st.image("https://i.postimg.cc/8CkFBFXH/rolsol2.jpg", caption="Villa de Merlo", use_container_width=True)
with c3: st.image("https://i.postimg.cc/5t9HqHKp/rolsol.jpg", caption="Mar del Plata", use_container_width=True)

c4, c5, c6 = st.columns(3)
with c4: st.image("https://i.postimg.cc/7LPCMCtM/rolsol3.jpg", caption="Noroeste Argentino", use_container_width=True)
with c5: st.image("https://i.postimg.cc/6Q67L7bV/rolsol4.jpg", caption="Patagonia Soñada", use_container_width=True)
with c6: st.image("https://i.postimg.cc/bvYGHGV1/rolsol5.jpg", caption="Cataratas (Aéreo)", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. CAMPING NÉSTOR KIRCHNER (FATICA) ---
st.markdown('<div id="camping" class="section-title">🌳 Centro Social Néstor Kirchner</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
st.image("https://i.postimg.cc/HLWJ4JvB/centro-nestor-kirchner.jpg", caption="Tarifario Temporada 2025/2026", use_container_width=True)
st.info("📍 Ruta 8 km. 76, Exaltación de la Cruz | 📞 Reservas: (011) 6155-0927")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FORMULARIO DE AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Afiliación Online</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
with st.form("form_afi", clear_on_submit=True):
    f_c1, f_c2 = st.columns(2)
    nom = f_c1.text_input("Nombre y Apellido*")
    dni = f_c2.text_input("DNI (sin puntos)*")
    emp = f_c1.text_input("Empresa de Seguridad*")
    cel = f_c2.text_input("WhatsApp*")
    inte = st.multiselect("Me interesa:", ["Turismo", "Camping", "Legal"])
    acepto = st.checkbox("Acepto tratamiento de datos.")
    if st.form_submit_button("ENVIAR SOLICITUD"):
        if acepto and nom and dni and cel:
            if guardar_registro(nom, dni, emp, cel, inte):
                st.success(f"✅ ¡Gracias {nom}! Solicitud registrada.")
                st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. SEDE CENTRAL Y MAPA (CORREGIDO) ---
st.markdown('<div id="contacto" class="section-title">📍 Sede Central</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("### Dirección: Piedras 1065, Constitución, CABA")

# Coordenadas exactas para Piedras 1065, CABA
map_data = pd.DataFrame({
    'lat': [-34.6215322],
    'lon': [-58.3814838]
})

# Renderizado del mapa
st.map(map_data, zoom=14)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-weight:bold; color:#0D47A1; padding:20px;'>© 2026 STVP - Sindicato de Trabajadores de Vigilancia Privada</p>", unsafe_allow_html=True)
