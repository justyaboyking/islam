import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Eid Mubarak",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with stars animations and upgraded mosque
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New:wght@400;700&display=swap');
    
    body {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background-color: #0a0e1a;
        background-image: 
            radial-gradient(circle, rgba(255,255,255,0.03) 1px, transparent 1px),
            linear-gradient(rgba(10, 14, 26, 0.9), rgba(10, 14, 26, 0.9));
        background-size: 30px 30px, auto;
        position: relative;
        overflow: hidden;
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
    
    /* Animated Stars */
    .stars-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
    }
    
    .star {
        position: absolute;
        width: 2px;
        height: 2px;
        background-color: #ffd966;
        border-radius: 50%;
        animation: twinkle var(--duration) infinite ease-in-out;
        opacity: 0.7;
        box-shadow: 0 0 3px #ffd966;
    }
    
    @keyframes twinkle {
        0% { opacity: 0.2; transform: scale(1); box-shadow: 0 0 2px #ffd966; }
        50% { opacity: 1; transform: scale(1.5); box-shadow: 0 0 5px #ffd966, 0 0 10px rgba(255, 217, 102, 0.3); }
        100% { opacity: 0.2; transform: scale(1); box-shadow: 0 0 2px #ffd966; }
    }
    
    /* Generate 80 stars with different positions and animation durations */
    .star:nth-child(1) { top: 5%; left: 10%; --duration: 3s; width: 3px; height: 3px; }
    .star:nth-child(2) { top: 15%; left: 20%; --duration: 5s; }
    .star:nth-child(3) { top: 25%; left: 15%; --duration: 4s; width: 3px; height: 3px; }
    .star:nth-child(4) { top: 10%; left: 30%; --duration: 6s; }
    .star:nth-child(5) { top: 20%; left: 40%; --duration: 3.5s; width: 4px; height: 4px; }
    .star:nth-child(6) { top: 30%; left: 25%; --duration: 4.5s; }
    .star:nth-child(7) { top: 5%; left: 50%; --duration: 5.5s; width: 3px; height: 3px; }
    .star:nth-child(8) { top: 15%; left: 60%; --duration: 3.2s; }
    .star:nth-child(9) { top: 25%; left: 70%; --duration: 4.2s; width: 3px; height: 3px; }
    .star:nth-child(10) { top: 10%; left: 80%; --duration: 6.2s; }
    .star:nth-child(11) { top: 20%; left: 90%; --duration: 3.7s; width: 3px; height: 3px; }
    .star:nth-child(12) { top: 30%; left: 85%; --duration: 4.7s; }
    .star:nth-child(13) { top: 40%; left: 10%; --duration: 5.7s; width: 4px; height: 4px; }
    .star:nth-child(14) { top: 50%; left: 20%; --duration: 3.3s; }
    .star:nth-child(15) { top: 60%; left: 15%; --duration: 4.3s; width: 3px; height: 3px; }
    .star:nth-child(16) { top: 45%; left: 30%; --duration: 6.3s; }
    .star:nth-child(17) { top: 55%; left: 40%; --duration: 3.8s; width: 3px; height: 3px; }
    .star:nth-child(18) { top: 65%; left: 25%; --duration: 4.8s; }
    .star:nth-child(19) { top: 40%; left: 50%; --duration: 5.8s; width: 4px; height: 4px; }
    .star:nth-child(20) { top: 50%; left: 60%; --duration: 3.4s; }
    .star:nth-child(21) { top: 60%; left: 70%; --duration: 4.4s; width: 3px; height: 3px; }
    .star:nth-child(22) { top: 45%; left: 80%; --duration: 6.4s; }
    .star:nth-child(23) { top: 55%; left: 90%; --duration: 3.9s; width: 3px; height: 3px; }
    .star:nth-child(24) { top: 65%; left: 85%; --duration: 4.9s; }
    .star:nth-child(25) { top: 75%; left: 10%; --duration: 5.9s; width: 3px; height: 3px; }
    .star:nth-child(26) { top: 85%; left: 20%; --duration: 3.5s; }
    .star:nth-child(27) { top: 95%; left: 15%; --duration: 4.5s; width: 3px; height: 3px; }
    .star:nth-child(28) { top: 80%; left: 30%; --duration: 6.5s; }
    .star:nth-child(29) { top: 90%; left: 40%; --duration: 3.1s; width: 4px; height: 4px; }
    .star:nth-child(30) { top: 75%; left: 50%; --duration: 5.1s; }
    .star:nth-child(31) { top: 85%; left: 60%; --duration: 3.6s; width: 3px; height: 3px; }
    .star:nth-child(32) { top: 95%; left: 70%; --duration: 4.6s; }
    .star:nth-child(33) { top: 80%; left: 80%; --duration: 6.6s; width: 3px; height: 3px; }
    .star:nth-child(34) { top: 90%; left: 90%; --duration: 3.2s; }
    .star:nth-child(35) { top: 95%; left: 85%; --duration: 4.2s; width: 3px; height: 3px; }
    
    /* Additional stars */
    .star:nth-child(36) { top: 8%; left: 15%; --duration: 4.1s; }
    .star:nth-child(37) { top: 22%; left: 27%; --duration: 3.7s; width: 3px; height: 3px; }
    .star:nth-child(38) { top: 32%; left: 18%; --duration: 5.2s; }
    .star:nth-child(39) { top: 7%; left: 37%; --duration: 4.3s; width: 4px; height: 4px; }
    .star:nth-child(40) { top: 13%; left: 45%; --duration: 3.6s; }
    .star:nth-child(41) { top: 28%; left: 55%; --duration: 4.8s; width: 3px; height: 3px; }
    .star:nth-child(42) { top: 18%; left: 65%; --duration: 5.3s; }
    .star:nth-child(43) { top: 9%; left: 77%; --duration: 3.9s; width: 3px; height: 3px; }
    .star:nth-child(44) { top: 26%; left: 82%; --duration: 4.7s; }
    .star:nth-child(45) { top: 14%; left: 93%; --duration: 5.4s; width: 4px; height: 4px; }
    .star:nth-child(46) { top: 35%; left: 8%; --duration: 3.8s; }
    .star:nth-child(47) { top: 45%; left: 16%; --duration: 4.9s; width: 3px; height: 3px; }
    .star:nth-child(48) { top: 38%; left: 33%; --duration: 5.6s; }
    .star:nth-child(49) { top: 48%; left: 45%; --duration: 3.4s; width: 3px; height: 3px; }
    .star:nth-child(50) { top: 42%; left: 58%; --duration: 4.2s; }
    .star:nth-child(51) { top: 37%; left: 75%; --duration: 5.7s; width: 3px; height: 3px; }
    .star:nth-child(52) { top: 47%; left: 88%; --duration: 3.5s; }
    .star:nth-child(53) { top: 57%; left: 6%; --duration: 4.6s; width: 4px; height: 4px; }
    .star:nth-child(54) { top: 69%; left: 13%; --duration: 5.2s; }
    .star:nth-child(55) { top: 72%; left: 24%; --duration: 3.9s; width: 3px; height: 3px; }
    .star:nth-child(56) { top: 63%; left: 35%; --duration: 4.5s; }
    .star:nth-child(57) { top: 53%; left: 53%; --duration: 5.8s; width: 3px; height: 3px; }
    .star:nth-child(58) { top: 68%; left: 62%; --duration: 3.3s; }
    .star:nth-child(59) { top: 58%; left: 77%; --duration: 4.1s; width: 3px; height: 3px; }
    .star:nth-child(60) { top: 77%; left: 88%; --duration: 5.9s; }
    .star:nth-child(61) { top: 83%; left: 7%; --duration: 3.8s; width: 4px; height: 4px; }
    .star:nth-child(62) { top: 91%; left: 16%; --duration: 4.4s; }
    .star:nth-child(63) { top: 88%; left: 27%; --duration: 5.5s; width: 3px; height: 3px; }
    .star:nth-child(64) { top: 78%; left: 45%; --duration: 3.7s; }
    .star:nth-child(65) { top: 92%; left: 54%; --duration: 4.8s; width: 3px; height: 3px; }
    .star:nth-child(66) { top: 87%; left: 67%; --duration: 5.1s; }
    .star:nth-child(67) { top: 98%; left: 76%; --duration: 3.4s; width: 3px; height: 3px; }
    .star:nth-child(68) { top: 93%; left: 93%; --duration: 4.3s; }
    .star:nth-child(69) { top: 3%; left: 3%; --duration: 5.2s; width: 4px; height: 4px; }
    .star:nth-child(70) { top: 3%; left: 97%; --duration: 3.6s; }
    .star:nth-child(71) { top: 97%; left: 3%; --duration: 4.7s; width: 3px; height: 3px; }
    .star:nth-child(72) { top: 97%; left: 97%; --duration: 5.3s; }
    .star:nth-child(73) { top: 33%; left: 3%; --duration: 3.8s; width: 3px; height: 3px; }
    .star:nth-child(74) { top: 63%; left: 97%; --duration: 4.9s; }
    .star:nth-child(75) { top: 3%; left: 33%; --duration: 5.6s; width: 3px; height: 3px; }
    .star:nth-child(76) { top: 3%; left: 63%; --duration: 3.4s; }
    .star:nth-child(77) { top: 97%; left: 33%; --duration: 4.2s; width: 3px; height: 3px; }
    .star:nth-child(78) { top: 97%; left: 63%; --duration: 5.7s; }
    .star:nth-child(79) { top: 50%; left: 3%; --duration: 3.5s; width: 4px; height: 4px; }
    .star:nth-child(80) { top: 50%; left: 97%; --duration: 4.6s; }
    
    /* Shooting stars */
    .shooting-star {
        position: absolute;
        width: 4px;
        height: 4px;
        background: linear-gradient(to right, rgba(255,217,102,0), rgba(255,217,102,1) 50%, rgba(255,217,102,0));
        border-radius: 50%;
        animation: shoot var(--duration) infinite linear;
        opacity: 0;
        transform: rotate(var(--angle));
        box-shadow: 0 0 10px #ffd966;
    }
    
    @keyframes shoot {
        0% { 
            opacity: 0;
            transform: translateX(-100px) translateY(0) rotate(var(--angle));
        }
        5% {
            opacity: 1;
        }
        20% { 
            opacity: 0;
            transform: translateX(100vw) translateY(100px) rotate(var(--angle));
        }
        100% { 
            opacity: 0;
            transform: translateX(100vw) translateY(100px) rotate(var(--angle));
        }
    }
    
    .shooting-star:nth-child(81) { top: 15%; left: 10%; --duration: 10s; --angle: 15deg; animation-delay: 1s; }
    .shooting-star:nth-child(82) { top: 35%; left: 30%; --duration: 12s; --angle: 20deg; animation-delay: 5s; }
    .shooting-star:nth-child(83) { top: 65%; left: 5%; --duration: 15s; --angle: 25deg; animation-delay: 8s; }
    .shooting-star:nth-child(84) { top: 85%; left: 25%; --duration: 11s; --angle: 30deg; animation-delay: 2s; }
    .shooting-star:nth-child(85) { top: 45%; left: 15%; --duration: 13s; --angle: 35deg; animation-delay: 7s; }
    .shooting-star:nth-child(86) { top: 25%; left: 20%; --duration: 9s; --angle: 18deg; animation-delay: 3s; }
    .shooting-star:nth-child(87) { top: 75%; left: 40%; --duration: 14s; --angle: 22deg; animation-delay: 6s; }
    .shooting-star:nth-child(88) { top: 50%; left: 35%; --duration: 10s; --angle: 28deg; animation-delay: 9s; }
    
    /* Lantern container */
    .lantern-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        padding: 0 15%;
        position: relative;
        z-index: 1;
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
        animation: lantern-glow 3s infinite ease-in-out;
    }
    
    @keyframes lantern-glow {
        0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.5), 0 0 40px rgba(255, 215, 0, 0.3); }
        50% { box-shadow: 0 0 25px rgba(255, 215, 0, 0.6), 0 0 50px rgba(255, 215, 0, 0.4); }
        100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.5), 0 0 40px rgba(255, 215, 0, 0.3); }
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
    
    .lantern:nth-child(1) { animation-delay: 0s; }
    .lantern:nth-child(2) { animation-delay: 0.5s; }
    .lantern:nth-child(3) { animation-delay: 1s; }
    .lantern:nth-child(4) { animation-delay: 1.5s; }
    
    /* Upgraded Mosque CSS */
    .mosque-container {
        width: 100%;
        max-width: 800px;
        height: 200px;
        margin: 50px auto;
        position: relative;
        z-index: 1;
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
        animation: dome-glow 5s infinite ease-in-out;
    }
    
    @keyframes dome-glow {
        0% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
        50% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 40px rgba(230, 180, 34, 0.3); }
        100% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
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
        animation: body-glow 5s infinite ease-in-out;
    }
    
    @keyframes body-glow {
        0% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
        50% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 40px rgba(230, 180, 34, 0.3); }
        100% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
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
        animation: minaret-glow 5s infinite ease-in-out;
    }
    
    @keyframes minaret-glow {
        0% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
        50% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 40px rgba(230, 180, 34, 0.3); }
        100% { box-shadow: 0 10px 20px rgba(0,0,0,0.2), 0 0 30px rgba(230, 180, 34, 0.2); }
    }
    
    /* Position minarets */
    .minaret-left {
        left: 5%;
        animation-delay: 0.5s;
    }
    .minaret-right {
        right: 5%;
        animation-delay: 1s;
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
    
    /* Dua styling */
    .dua-container {
        background: rgba(10, 14, 26, 0.7);
        border: 1px solid #d4af37;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 800px;
        position: relative;
        z-index: 1;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
    }
    
    .dua-arabic {
        font-family: 'Scheherazade New', serif;
        font-size: 2rem;
        color: #d4af37;
        text-align: center;
        direction: rtl;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .dua-dutch {
        color: white;
        text-align: center;
        margin-top: 1rem;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .dua-title {
        color: #d4af37;
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Personal message styling */
    .personal-message {
        background: rgba(10, 14, 26, 0.7);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 2rem auto;
        max-width: 800px;
        position: relative;
        z-index: 1;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        text-align: center;
    }
    
    .personal-message p {
        color: white;
        font-size: 1.2rem;
        line-height: 1.6;
    }
    
    .personal-message .name {
        color: #d4af37;
        font-weight: bold;
        font-size: 1.3rem;
    }
    
    .message-decoration {
        display: inline-block;
        color: #d4af37;
        font-size: 1.5rem;
        margin: 0 10px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Stars container
st.markdown("""
<div class="stars-container">
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
</div>
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

# Add personalized message from Zakaria
st.markdown("""
<div class="personal-message">
    <p><span class="message-decoration">☪️</span> <span class="name">Zakaria</span> wenst iedereen een gezegend Eid al-Fitr <span class="message-decoration">☪️</span></p>
</div>
""", unsafe_allow_html=True)

# Add dua in Arabic and Dutch
st.markdown("""
<div class="dua-container">
    <h3 class="dua-title">Dua voor Eid</h3>
    <div class="dua-arabic">
        اللَّهُمَّ لَكَ صُمْنَا وَعَلَى رِزْقِكَ أَفْطَرْنَا، فَتَقَبَّلْ مِنَّا إِنَّكَ أَنْتَ السَّمِيعُ الْعَلِيم
    </div>
    <div class="dua-dutch">
        "O Allah, voor U hebben wij gevast en met Uw voorziening hebben wij ons vasten verbroken. Accepteer dit van ons, want U bent de Alhorende, de Alwetende."
    </div>
</div>
""", unsafe_allow_html=True)

# Auto-refresh using JavaScript (every 1 second for the countdown)
st.markdown("""
<script>
    function refreshPage() {
        setTimeout(function() {
            window.location.reload();
        }, 1000);
    }
    refreshPage();
</script>
""", unsafe_allow_html=True)
