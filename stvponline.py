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

# --- 2. ESTILOS DE ALTA VISIBILIDAD (FONDO CELESTE Y DISEÑO MODERNO) ---
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

    .benefit-card {
        padding: 25px; border-radius: 15px; background-color: #ffffff;
        border-left: 10px solid #1E88E5; box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 20px; min-height: 250px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    
    .white-container {
        background-color: #ffffff; padding: 30px; border-radius: 20px;
        border: 3px solid #0D47A1; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin-bottom: 30px;
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
st.markdown("""<div class="nav-bar"><a href="#inicio">INICIO</a><a href="#beneficios">BENEFICIOS</a><a href="#afiliacion">AFILIACIÓN</a><a href="#contacto">CONTACTO</a></div><div style="margin-top: 100px;"></div>""", unsafe_allow_html=True)

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
with c_logo: st.image("https://customer-assets.emergentagent.com/job_stvp-portal-1/artifacts/xlt7u219_logo_stvp.png", width=160)
with c_title:
    st.markdown("<h1 style='color: #0D47A1; margin-bottom:0;'>Sindicato STVP</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1565C0;'>Vigilancia Privada - Piedras 1065, CABA</h3>", unsafe_allow_html=True)

# --- 6. SECCIÓN BENEFICIOS EXCLUSIVOS ---
st.markdown('<div id="beneficios" class="section-title">🎁 Beneficios y Convenios</div>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown('<div class="benefit-card" style="border-left-color: #FF9800;"><h3>🚌 Turismo RolSol</h3><p>Viajes grupales con planes de pago. <a href="https://whatsapp.com/channel/0029VbAua9BJENy8oScpAH2B">Ver Canal</a></p></div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div class="benefit-card" style="border-left-color: #E91E63;"><h3>🏍️ Ciudad Moto</h3><p>Descuentos directos en unidades y repuestos para afiliados con credencial.</p></div>', unsafe_allow_html=True)
with b3:
    st.markdown('<div class="benefit-card" style="border-left-color: #4CAF50;"><h3>⚖️ Asesoría Legal</h3><p>Defensa gremial y legal gratuita. Lunes a Viernes de 10 a 16hs.</p></div>', unsafe_allow_html=True)

# --- 7. DETALLE TEMPORADA LUZ Y FUERZA ---
st.markdown('<div class="white-container">', unsafe_allow_html=True)
st.subheader("🏖️ Temporada Verano 25/26 - Convenio Luz y Fuerza")
st.warning("⚠️ Tarifas válidas hasta Dic 2025. Desde Enero se ajustan por IPC.")

t1, t2, t3, t4 = st.tabs(["🌊 San Bernardo", "🏖️ Mar del Plata", "🌲 Villa Giardino", "🏔️ Bariloche"])

with t1:
    st.markdown("**Hotel 'Por la Liberación Nacional'** - Chiozza 2455 [cite: 80]")
    st.write("✅ Todo Incluido, Piscina Climatizada, Cochera[cite: 81, 83].")
    st.table({
        "Habitación": ["Individual", "Doble p/p", "Triple p/p", "Cuádruple p/p", "Menores (3-12)"],
        "Afiliado": ["$200.000", "$100.000", "$95.000", "$90.000", "$45.000 a $50.000"] # 
    })

with t2:
    st.markdown("**Hotel 'Oscar Lescano'** - Av. De Los Trabajadores 3971 [cite: 118]")
    st.write("✅ Todo Incluido, Vista al mar, Piscina Climatizada[cite: 120].")
    st.table({
        "Habitación": ["Individual", "Doble p/p", "Triple p/p", "Menores (3-12)"],
        "Afiliado": ["$200.000", "$100.000", "$95.000", "$47.500 a $50.000"] # [cite: 111]
    })

with t3:
    st.markdown("**Hotel 'Por los Derechos del Trabajador'** - Villa Giardino [cite: 34]")
    st.write("✅ Contingentes de 7 días. Entorno serrano[cite: 34].")
    st.table({
        "Habitación": ["Doble p/p", "Triple p/p", "Cuádruple p/p", "Menores (3-12)"],
        "Afiliado": ["$83.000", "$78.850", "$74.700", "$37.300 a $41.500"] # [cite: 37]
    })

with t4:
    st.markdown("**Hotel 'Alún Nehuén'** - Av. Bustillo km 32, Bariloche [cite: 31]")
    st.write("✅ Media Pensión (Desayuno y Cena), Spa y Gimnasio[cite: 32].")
    st.table({
        "Habitación": ["Doble p/p", "Triple p/p", "Menores (3-12)"],
        "Afiliado": ["$88.000", "$83.600", "$41.800 a $44.000"] # [cite: 29]
    })
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FORMULARIO DE AFILIACIÓN ---
st.markdown('<div id="afiliacion" class="section-title">📝 Afiliación Online</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="white-container">', unsafe_allow_html=True)
    with st.form("form_afi", clear_on_submit=True):
        f_col1, f_col2 = st.columns(2)
        nom = f_col1.text_input("Nombre y Apellido*")
        dni = f_col2.text_input("DNI (solo números)*")
        emp = f_col1.text_input("Empresa de Seguridad*")
        cel = f_col2.text_input("WhatsApp*")
        
        inte = st.multiselect("Intereses:", ["Turismo", "Kit Escolar", "Asesoría Legal", "Salud"])
        acepto = st.checkbox("Acepto los términos y el tratamiento de mis datos (Ley 25.326).")
        
        if st.form_submit_button("ENVIAR SOLICITUD"):
            if acepto and nom and dni.isdigit() and cel:
                if guardar_registro(nom, dni, emp, cel, inte):
                    st.success(f"✅ ¡Gracias {nom}! Solicitud guardada exitosamente.")
                    st.balloons()
                else: st.error("❌ Error de conexión con la base de datos.")
            else: st.warning("⚠️ Completa los campos obligatorios.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 9. MAPA Y UBICACIÓN ---
st.markdown('<div id="contacto" class="section-title">📍 Ubicación</div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="white-container" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("### Sede Central STVP")
    st.write("Piedras 1065, Constitución, CABA.")
    # Mapa centrado en la dirección del sindicato
    map_data = pd.DataFrame({'lat': [-34.6215], 'lon': [-58.3815]})
    st.map(map_data)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-weight:bold; color:#0D47A1; padding:20px;'>© 2026 STVP Sindicato de Trabajadores de Vigilancia Privada</p>", unsafe_allow_html=True)
