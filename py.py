import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with better lanterns and upgraded mosque
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background-color: #0a0e1a;
        background-image: 
            radial-gradient(circle, rgba(255,255,255,0.03) 1px, transparent 1px),
            linear-gradient(rgba(10, 14, 26, 0.9), rgba(10, 14, 26, 0.9));
        background-size: 30px 30px, auto;
    }
    
    h1 {
        color: white;
        text-align: center;
        font-size: 4rem;
        font-family: 'Great Vibes', cursive;
        margin-top: 3rem;
        margin-bottom: 0.5rem;
    }
    
    p {
        color: white;
        text-align: center;
    }
    
    .countdown-box {
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 1.5rem 1rem;
        text-align: center;
        background-color: rgba(10, 14, 26, 0.7);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    
    .countdown-value {
        color: #d4af37;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    .countdown-label {
        color: white;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Lantern container */
    .lantern-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        padding: 0 15%;
    }
    
    /* Enhanced lanterns with glow effect */
    .lantern {
        width: 40px;
        height: 60px;
        background: linear-gradient(to bottom, #d4af37, #ffd700);
        border-radius: 10px;
        position: relative;
        box-shadow: 
            0 0 20px rgba(255, 215, 0, 0.5),
            0 0 40px rgba(255, 215, 0, 0.3);
    }
    
    .lantern:before {
        content: "";
        position: absolute;
        top: -15px;
        left: 18px;
        width: 4px;
        height: 15px;
        background-color: #d4af37;
    }
    
    .lantern:after {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 30px;
        height: 50px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        z-index: 1;
    }
    
    /* Upgraded Mosque CSS */
    .mosque-container {
        width: 100%;
        max-width: 800px;
        height: 200px;
        margin: 50px auto;
        position: relative;
    }
    
    /* Mosque dome/roof with improved curve and gradient */
    .mosque-dome {
        width: 70%;
        height: 100px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        border-radius: 100% 100% 0 0 / 180% 180% 0 0;
        margin: 0 auto;
        position: relative;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Mosque base/body with enhanced styling */
    .mosque-body {
        width: 70%;
        height: 80px;
        background: linear-gradient(to bottom, #efc22c, #d4af37);
        margin: 0 auto;
        position: relative;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Main door (center) - taller than other windows */
    .main-door {
        width: 30px;
        height: 50px;
        background-color: #0a0e1a;
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 15px 15px 0 0;
    }
    
    /* Windows styling */
    .mosque-window {
        width: 20px;
        height: 35px;
        background-color: #0a0e1a;
        position: absolute;
        bottom: 15px;
        border-radius: 10px 10px 0 0;
    }
    
    /* Position each window */
    .window-1 {
        left: 20%;
    }
    .window-2 {
        left: 35%;
    }
    .window-3 {
        right: 35%;
    }
    .window-4 {
        right: 20%;
    }
    
    /* Minaret columns with enhanced design */
    .minaret {
        width: 15px;
        height: 150px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        position: absolute;
        bottom: 0;
        box-shadow: 
            0 10px 20px rgba(0,0,0,0.2),
            0 0 30px rgba(230, 180, 34, 0.2);
    }
    
    /* Position minarets */
    .minaret-left {
        left: 5%;
    }
    .minaret-right {
        right: 5%;
    }
    
    /* Minaret tops */
    .minaret-top {
        width: 25px;
        height: 25px;
        background: linear-gradient(to bottom, #ffd966, #e6b422);
        border-radius: 50%;
        position: absolute;
        top: -12px;
        left: -5px;
        box-shadow: 0 0 20px rgba(230, 180, 34, 0.3);
    }
    
    /* Subtle decorative elements */
    .decoration {
        width: 100%;
        height: 5px;
        position: absolute;
        bottom: 0;
        left: 0;
        background: linear-gradient(to right, rgba(230, 180, 34, 0), rgba(230, 180, 34, 0.3), rgba(230, 180, 34, 0));
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button styling */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #0a0e1a !important;
        font-weight: bold !important;
        border: none !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 30px !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Eid Mubarak</h1>", unsafe_allow_html=True)
st.markdown("<p>Het gezegende feest vieren met vreugde en dankbaarheid</p>", unsafe_allow_html=True)

# Enhanced lanterns with glow effect
st.markdown("""
<div class="lantern-container">
    <div class="lantern" style="height: 55px;"></div>
    <div class="lantern" style="height: 70px;"></div>
    <div class="lantern" style="height: 60px;"></div>
    <div class="lantern" style="height: 65px;"></div>
</div>
""", unsafe_allow_html=True)

# Upgraded mosque design
st.markdown("""
<div class="mosque-container">
    <div class="mosque-dome"></div>
    <div class="mosque-body">
        <div class="main-door"></div>
        <div class="mosque-window window-1"></div>
        <div class="mosque-window window-2"></div>
        <div class="mosque-window window-3"></div>
        <div class="mosque-window window-4"></div>
        <div class="decoration"></div>
    </div>
    <div class="minaret minaret-left">
        <div class="minaret-top"></div>
    </div>
    <div class="minaret minaret-right">
        <div class="minaret-top"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Countdown Section
st.markdown("<h3 style='text-align: center; color: #d4af37; font-size: 1.8rem;'>Resterende Tijd Tot Eid</h3>", unsafe_allow_html=True)
st.markdown("<p>Zondag 30 maart 2025</p>", unsafe_allow_html=True)

# Set countdown end date
end_date = datetime(2025, 3, 30)

# Get countdown values
def get_countdown():
    now = datetime.now()
    delta = end_date - now
    
    # If countdown is finished
    if delta.total_seconds() <= 0:
        return 0, 0, 0, 0
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Create columns for countdown display
col1, col2, col3, col4 = st.columns(4)

# Display countdown
days, hours, minutes, seconds = get_countdown()

with col1:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{days:02d}</h3>
        <p class="countdown-label">Dagen</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{hours:02d}</h3>
        <p class="countdown-label">Uren</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{minutes:02d}</h3>
        <p class="countdown-label">Minuten</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="countdown-box">
        <h3 class="countdown-value">{seconds:02d}</h3>
        <p class="countdown-label">Seconden</p>
    </div>
    """, unsafe_allow_html=True)

# Refresh button for updating the countdown
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.rerun()
