import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Basic CSS - minimal to avoid JavaScript errors
st.markdown("""
<style>
    body {
        background-color: #0a1931;
        color: white;
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #0a1931;
    }
    h1 {
        color: #d4af37;
        text-align: center;
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    h2 {
        color: #d4af37;
        text-align: center;
    }
    p {
        text-align: center;
    }
    .container {
        margin: 1rem auto;
        max-width: 1000px;
    }
    .gold-text {
        color: #d4af37;
    }
    .gold-border {
        border: 2px solid #d4af37;
        border-radius: 10px;
        padding: 1rem;
        background-color: rgba(10, 25, 49, 0.6);
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        opacity: 0.7;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Eid Mubarak</h1>", unsafe_allow_html=True)
st.markdown("<p>Het gezegende feest vieren met vreugde en dankbaarheid</p>", unsafe_allow_html=True)

# Simple mosque - plain image with fixed dimensions
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <svg width="300" height="150" xmlns="http://www.w3.org/2000/svg">
        <rect x="60" y="60" width="180" height="90" fill="#ffc94b" />
        <ellipse cx="150" cy="60" rx="45" ry="20" fill="#ffc94b" />
        <rect x="40" y="60" width="10" height="90" fill="#ffc94b" />
        <rect x="250" y="60" width="10" height="90" fill="#ffc94b" />
        <rect x="140" y="110" width="20" height="40" fill="#0a1931" />
    </svg>
</div>
""", unsafe_allow_html=True)

# Countdown Section
st.markdown("<h2>Resterende Tijd Tot Eid</h2>", unsafe_allow_html=True)
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

# Display countdown - no JavaScript, just Python calculations
days, hours, minutes, seconds = get_countdown()

with col1:
    st.markdown(f"""
    <div class="gold-border" style="text-align: center;">
        <h2 style="font-size: 2.5rem; margin: 0;">{days:02d}</h2>
        <p>Dagen</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="gold-border" style="text-align: center;">
        <h2 style="font-size: 2.5rem; margin: 0;">{hours:02d}</h2>
        <p>Uren</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="gold-border" style="text-align: center;">
        <h2 style="font-size: 2.5rem; margin: 0;">{minutes:02d}</h2>
        <p>Minuten</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="gold-border" style="text-align: center;">
        <h2 style="font-size: 2.5rem; margin: 0;">{seconds:02d}</h2>
        <p>Seconden</p>
    </div>
    """, unsafe_allow_html=True)

# Add space
st.markdown("<br>", unsafe_allow_html=True)

# Eid message - simple div with no complex styling
st.markdown("""
<div class="gold-border" style="margin: 1rem auto; padding: 1.5rem; text-align: center;">
    <h2>Eid Mubarak</h2>
    <p>Moge deze Eid vreugde, geluk, vrede en voorspoed brengen voor jou en je familie. De gezegende maand Ramadan leert ons de waarde van mededogen, geduld en dankbaarheid. Terwijl we wachten op Eid al-Fitr, laten we deze lessen onthouden en meenemen in ons leven.</p>
</div>
""", unsafe_allow_html=True)

# Islamic decoration - minimized
st.markdown("""
<div style="text-align: center; font-size: 2rem; color: #d4af37; margin: 1.5rem 0;">
    ﷽
</div>
""", unsafe_allow_html=True)

# Footer - very simple
st.markdown("""
<div class="footer">
    <p>Gemaakt door Zakaria Akanni</p>
</div>
""", unsafe_allow_html=True)

# Refresh button for updating the countdown
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ververs Aftellen"):
        st.experimental_rerun()
