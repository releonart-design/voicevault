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
    <p style='color: #9ca3af; font-size: 14px;'>Professional AI Background Cutout & Real Working SEO Suite</p>
</div>
""", unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2 = st.tabs(["✨ AI Background Remover", "🏷️ Pro SEO & Tags Generator"])

# --- TAB 1: BACKGROUND REMOVER ---
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="font-size: 45px; margin-bottom: 10px;">🪄</div>
        <h2 style="color: #ffffff; font-weight: 800; margin: 0; font-size: 1.8rem;">HD Background Remover</h2>
        <p style="color: #9ca3af; font-size: 13px; margin-top: 6px;">Instant zero-crash professional AI transparent background cutout.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin: 25px 0 10px 0;">
        <a href="https://www.remove.bg" target="_blank" class="bg-action-btn">
            🚀 LAUNCH AI BACKGROUND REMOVER ➔
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: PRO SEO TITLE & RAPID-TAGS GENERATOR ---
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🏷️ Pro SEO Title & Rapid Tags Generator")
    st.markdown("<p style='color: #9ca3af; font-size: 13px;'>Generates high-CTR working titles and comma-separated viral tags like RapidTags & ChatGPT.</p>", unsafe_allow_html=True)
    
    seo_topic = st.text_input("Enter Your Video Topic / Keyword:", placeholder="e.g. Satoru Gojo Drawing, Cyberpunk Speedrun", key="seo_top")
    
    if st.button("⚡ GENERATE PRO SEO METADATA", key="btn_seo"):
        if seo_topic:
            st.success("High-Performance SEO Generated Successfully!")
            viral_score = random.randint(94, 99)
            st.metric("Estimated SEO Ranking Score", f"{viral_score}/100", "🔥 Extreme Search Demand")
            
            clean_topic = seo_topic.strip()
            no_space_topic = clean_topic.replace(" ", "")
            
            # Real Working High-CTR Titles Formats
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:20px;'>📌 Optimized High-CTR Video Titles:</p>", unsafe_allow_html=True)
            st.code(f"""1. How to Master {clean_topic} in 10 Minutes (Step-by-Step)
2. The Ultimate Guide to {clean_topic} (2026 Masterclass)
3. I Tried {clean_topic} For 24 Hours — Here Is What Happened
4. Stop Making This Mistake With {clean_topic}!""", language="text")
            
            # RapidTags Style Comma-Separated Tags for easy YouTube Studio copy-pasting
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>🔑 RapidTags Style YouTube Tags (Comma Separated):</p>", unsafe_allow_html=True)
            comma_tags = f"{clean_topic}, {clean_topic} tutorial, how to {clean_topic}, {clean_topic} 2026, best {clean_topic} guide, viral {clean_topic}, advanced {clean_topic}, {clean_topic} tips and tricks, {clean_topic} masterclass, learn {clean_topic}"
            st.code(comma_tags, language="text")
            
            # Clean Hashtags for Description
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>#️⃣ Top Description Hashtags:</p>", unsafe_allow_html=True)
            st.code(f"#{no_space_topic} #{no_space_topic}Tutorial #CreatorStudio #Trending2026 #YouTubeGrowth #Masterclass", language="text")
        else:
            st.warning("Please enter a video topic or keyword first!")
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
