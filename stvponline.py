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
        font-size: 2.2rem; font-weight: 800; color: #0D47A1;
        text-align: center; margin: 1.5rem 0; text-transform: uppercase;
    }

    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%;
        background-color: #ffffff; z-index: 1000; padding: 10px;
        text-align: center; border-bottom: 3px solid #0D47A1;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .nav-bar a { 
        margin: 0 12px; text-decoration: none; color: #0D47A1; 
        font-weight: bold; font-size: 0.9rem;
    }

    .white-container {
        background-color: #ffffff; padding: 25px; border-radius: 15px;
        border: 1px solid #BBDEFB; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }

    .btn-whatsapp-rolsol {
        background-color: #0080ff; color: white !important;
        padding: 10px 15px; text-decoration: none; border-radius: 6px;
        font-weight: bold; display: inline-block; font-size: 0.8rem;
    }
    
    .download-btn {
        display: inline-block; padding: 12px 20px; background-color: #D32F2F;
        color: white !important; text-decoration: none; border-radius: 8px;
        font-weight: bold; text-align: center; font-size: 0.9rem;
    }

    .whatsapp-float {
        position: fixed; width: 60px; height: 60px; bottom: 30px; right: 30px;
        background-color: #25d366; color: white; border-radius: 50px;
        text-align: center; box-shadow: 2px 5px 15px rgba(0,0,0,0.3);
        z-index: 9999; display: flex; align-items: center; justify-content: center;
    }
    </style>
    
    <a href="https://wa.me/5491152628936" class="whatsapp-float" target="_blank">
        <svg width="30" height="30" fill="white" viewBox="0 0 16 16">
            <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
        </svg>
    </a>
    """, unsafe_allow_html=True)

# --- 3. NAVEGACIÓN ---
st.markdown("""
    <div class="nav-bar">
        <a href="#inicio">INICIO</a>
        <a href="#turismo">TURISMO</a>
        <a href="#camping">CAMPING</a>
        <a href="#hoteles">HOTELES LyF</a>
        <a href="#afiliacion">AFILIACIÓN</a>
        <a href="#contacto">SEDE</a>
    </div>
    <div style="margin-top: 80px;"></div>
""", unsafe_allow_html=True)

# --- 4. CONEXIÓN G-SHEETS ---
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

# --- 5. CABECERA ---
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
c_logo, c_title = st.columns([1, 4])
with c_logo: st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=140)
with c_title:
    st.markdown("<h1 style='color: #0D47A1; margin-bottom:0;'>STVP - Sindicato Vigilancia</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #1565C0;'>Gestión, Turismo y Beneficios</h4>", unsafe_allow_html=True)

# --- 6. TURISMO ROLSOL (IMÁGENES PEQUEÑAS) ---
st.markdown('<div id="turismo" class="section-title">🚌 Turismo RolSol</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
ct1, ct2 = st.columns([3, 1])
with ct1: st.subheader("Temporada Verano 2026")
with ct2:
    canal_whatsapp = "https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B"
    st.markdown(f'<a href="{canal_whatsapp}" target="_blank" class="btn-whatsapp-rolsol">📢 Canal de WhatsApp</a>', unsafe_allow_html=True)

# Usamos 4 columnas para que las fotos se vean más pequeñas y compactas
r1c1, r1c2, r1c3, r1c4 = st.columns(4)
with r1c1: st.image("https://i.postimg.cc/g0cwqwtH/rolsol1.jpg", caption="Bariloche", width=220)
with r1c2: st.image("https://i.postimg.cc/8CkFBFXH/rolsol2.jpg", caption="Villa de Merlo", width=220)
with r1c3: st.image("https://i.postimg.cc/5t9HqHKp/rolsol.jpg", caption="Mar del Plata", width=220)
with r1c4: st.image("https://i.postimg.cc/7LPCMCtM/rolsol3.jpg", caption="Noroeste", width=220)

r2c1, r2c2, r2c3, r2c4 = st.columns(4)
with r2c1: st.image("https://i.postimg.cc/6Q67L7bV/rolsol4.jpg", caption="Patagonia", width=220)
with r2c2: st.image("https://i.postimg.cc/bvYGHGV1/rolsol5.jpg", caption="Cataratas", width=220)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. CAMPING FATICA ---
st.markdown('<div id="camping" class="section-title">🌳 Camping Néstor Kirchner</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_camp1, col_camp2 = st.columns([1, 1.5])
with col_camp1:
    st.image("https://i.postimg.cc/HLWJ4JvB/centro-nestor-kirchner.jpg", caption="Tarifario 25/26", width=400)
with col_camp2:
    st.markdown("### Tarifas Afiliados STVP")
    st.markdown("- **Entrada General:** $3.000")
    st.markdown("- **Alojamiento diario:** $10.000")
    st.markdown("- **Parcela carpa:** $8.000")
    st.info("📍 Ruta 8 km. 76, Exaltación de la Cruz")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. HOTELES LUZ Y FUERZA ---
st.markdown('<div id="hoteles" class="section-title">🏖️ Hotelería Luz y Fuerza</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
col_lyf1, col_lyf2 = st.columns([3, 1])
with col_lyf1:
    st.markdown("##### Convenio de Turismo Social - Temporada de Verano")
    st.write("Contamos con plazas en San Bernardo, Mar del Plata y Villa Giardino.")
with col_lyf2:
    folleto_drive = "https://drive.google.com/file/d/1jhcYwAVWGr9ZSHIiAgaPyU_j4eJho_yx/view?usp=drive_link"
    st.markdown(f'<a href="{folleto_drive}" target="_blank" class="download-btn">📥 PDF COMPLETO</a>', unsafe_allow_html=True)

tabs_lyf = st.tabs(["San Bernardo", "Mar del Plata", "Villa Giardino"])
with tabs_lyf[0]:
    st.write("**Hotel Por la Liberación Nacional** - Calle Chiozza 2455")
    st.markdown("- Media Pensión / Baño Privado / TV")
    st.table({"Habitación": ["Doble", "Triple", "Cuádruple"], "Tarifa Afiliado": ["$100.000", "$95.000", "$90.000"]})
with tabs_lyf[1]:
    st.write("**Hotel Oscar Lescano** - Frente al Mar")
    st.write("Servicio de buffet completo y recreación para niños.")
with tabs_lyf[2]:
    st.write("**Villa Giardino (Córdoba)**")
    st.write("Entorno natural serrano con pileta y pensión completa.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Solicitud de Afiliación</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container">', unsafe_allow_html=True)
with st.form("afi_form", clear_on_submit=True):
    f1, f2 = st.columns(2)
    nombre = f1.text_input("Nombre y Apellido*")
    dni = f2.text_input("DNI*")
    empresa = f1.text_input("Empresa de Seguridad*")
    celular = f2.text_input("WhatsApp de Contacto*")
    interes = st.multiselect("Me interesa info de:", ["Turismo RolSol", "Hoteles LyF", "Camping", "Gremiales"])
    if st.form_submit_button("ENVIAR DATOS"):
        if nombre and dni and celular:
            if guardar_registro(nombre, dni, empresa, celular, interes):
                st.success("✅ Datos recibidos. Nos contactaremos a la brevedad.")
                st.balloons()
        else: st.warning("Por favor complete los campos obligatorios.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 10. SEDE Y MAPA ---
st.markdown('<div id="contacto" class="section-title">📍 Sede Central</div>', unsafe_allow_html=True)
st.markdown('<div class="white-container" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("#### Piedras 1065, Constitución, CABA")
map_data = pd.DataFrame({'lat': [-34.6215322], 'lon': [-58.3814838]})
st.map(map_data, zoom=14)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#666;'>© 2026 STVP - Sindicato de Trabajadores de Vigilancia Privada</p>", unsafe_allow_html=True)
