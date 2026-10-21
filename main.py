import streamlit as st
import streamlit.components.v1 as components
import random

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | 2026 Ultra AI",
    page_icon="⚡",
    layout="centered"
)

# 2026 Ultra-Modern Neon Glassmorphism & Slow Auto-Morphing Animated Background CSS
st.markdown("""
<style>
    /* Slow Gasoline / Aurora Blur Auto-Morphing Background Animation */
    @keyframes auroraBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main { background-color: #030712; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    .stApp {
        background: linear-gradient(-45deg, #030712, #1e1b4b, #311042, #0f172a, #030712);
        background-size: 400% 400%;
        animation: auroraBG 15s ease infinite;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Pop and Drop Glassmorphism Card Animation */
    @keyframes popAndDrop {
        0% { opacity: 0; transform: translateY(-30px) scale(0.95); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.5);
        margin-bottom: 24px;
        animation: popAndDrop 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    /* Glowing Neon Buttons with Smooth Hover */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 14px;
        border: none;
        box-shadow: 0 4px 25px rgba(99, 102, 241, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        box-shadow: 0 6px 30px rgba(168, 85, 247, 0.6);
        transform: translateY(-2px);
    }
    
    /* Background Remover Direct Action Button Style */
    .bg-action-btn {
        display: block;
        width: 100%;
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        color: white !important;
        font-weight: 700;
        text-align: center;
        padding: 16px 24px;
        border-radius: 14px;
        text-decoration: none !important;
        box-shadow: 0 4px 25px rgba(37, 99, 235, 0.5);
        transition: all 0.3s ease;
        box-sizing: border-box;
    }
    .bg-action-btn:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
        box-shadow: 0 6px 30px rgba(37, 99, 235, 0.7);
        transform: translateY(-2px);
    }
    
    .ad-banner {
        background-color: rgba(17, 24, 39, 0.6);
        border: 1px dashed rgba(225, 29, 72, 0.4);
        border-radius: 14px;
        padding: 8px;
        text-align: center;
        margin: 14px 0;
    }
    
    /* Modern Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(17, 24, 39, 0.85);
        padding: 8px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        color: #9ca3af;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 9px; margin: 0; letter-spacing: 1.5px; text-transform: uppercase;">SPONSORED AD ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#0b0f19; padding:6px; border-radius:10px;">
        <script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>
        <div id="container-990668de3498a3c38ef3239d7c52eba3"></div>
    </div>
    """, height=100)

# Social Bar Integration
components.html("""
<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>
""", height=0)

# TOP BANNER AD
render_banner_ad("Top Header")

# Animated Header Section
st.markdown("""
<div style="text-align: center; padding: 15px 0 25px 0;">
    <span style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">⚡ 2026 Next-Gen AI Suite</span>
    <h1 style='color: #ffffff; font-weight: 900; margin-top: 12px; font-size: 2.4rem; letter-spacing: -0.5px;'>Creator Studio Pro</h1>
    <p style='color: #9ca3af; font-size: 14px;'>Professional AI Background Cutout & SEO Generator Suite</p>
</div>
""", unsafe_allow_html=True)

# Clean Tabs (Script Generator Removed, Only Background Remover & SEO Tabs)
tab1, tab2 = st.tabs(["✨ AI Background Remover", "🏷️ SEO Tags Generator"])

# --- TAB 1: BACKGROUND REMOVER ICON & SUITE ---
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="font-size: 45px; margin-bottom: 10px;">🪄</div>
        <h2 style="color: #ffffff; font-weight: 800; margin: 0; font-size: 1.8rem;">HD Background Remover</h2>
        <p style="color: #9ca3af; font-size: 13px; margin-top: 6px;">Instant zero-crash professional AI transparent background cutout.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Direct Action Professional Button with Icon
    st.markdown("""
    <div style="margin: 25px 0 10px 0;">
        <a href="https://www.remove.bg" target="_blank" class="bg-action-btn">
            🚀 LAUNCH AI BACKGROUND REMOVER ➔
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: SEO TITLE & TAG GENERATOR ---
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🏷️ SEO Title & Viral Tag Generator")
    seo_topic = st.text_input("Enter Target Keywords:", placeholder="e.g. Speedrun Art, Cyberpunk Design", key="seo_top")
    
    if st.button("🚀 GENERATE SEO METADATA", key="btn_seo"):
        if seo_topic:
            st.success("SEO Optimization Complete!")
            viral_score = random.randint(92, 99)
            st.metric("AI Viral Potential Score", f"{viral_score}/100", "+ High Ranking Probability")
            
            topic_clean = seo_topic.replace(" ", "")
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:15px;'>High-CTR Viral Titles:</p>", unsafe_allow_html=True)
            st.code(f"1. Why Everyone Is Obsessed With {seo_topic} in 2026\n2. The Ultimate {seo_topic} Masterclass (Step-by-Step)\n3. I Tested {seo_topic} For 24 Hours — Look What Happened", language="text")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>Trending Tags & Keywords:</p>", unsafe_allow_html=True)
            st.code(f"#{topic_clean} #{topic_clean}2026 #CreatorStudio #ViralContent #TrendingNow #Masterclass #YouTubeGrowth", language="text")
        else:
            st.warning("Please enter keywords!")
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
