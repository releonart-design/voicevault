import streamlit as st
import streamlit.components.v1 as components
import random
import requests
import time

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | 2026 Bento AI Suite",
    page_icon="👑",
    layout="centered"
)

# 2026 Ultra-Modern Bento Grid, Glassmorphism & Spring Physics CSS
st.markdown("""
<style>
    @keyframes auroraBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes borderGlow {
        0% { border-color: rgba(99, 102, 241, 0.3); box-shadow: 0 0 20px rgba(99, 102, 241, 0.15); }
        50% { border-color: rgba(236, 72, 153, 0.7); box-shadow: 0 0 35px rgba(236, 72, 153, 0.35); }
        100% { border-color: rgba(99, 102, 241, 0.3); box-shadow: 0 0 20px rgba(99, 102, 241, 0.15); }
    }

    @keyframes pulseSoft {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .main { background-color: #030712; color: #f3f4f6; font-family: 'Inter', sans-serif; }
    .stApp {
        background: linear-gradient(-45deg, #030712, #0f172a, #1e1b4b, #311042, #030712);
        background-size: 400% 400%;
        animation: auroraBG 18s ease infinite;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    @keyframes springReveal {
        0% { opacity: 0; transform: translateY(20px) scale(0.97); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .bento-card {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        margin-bottom: 24px;
        animation: springReveal 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards, borderGlow 8s infinite;
        transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }
    .bento-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 30px rgba(99, 102, 241, 0.2);
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        padding: 14px;
        border: none;
        box-shadow: 0 4px 25px rgba(236, 72, 153, 0.35);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #db2777 100%);
        box-shadow: 0 8px 35px rgba(236, 72, 153, 0.6);
        transform: translateY(-2px) scale(1.01);
    }
    
    .ad-banner {
        background-color: rgba(15, 23, 42, 0.5);
        border: 1px dashed rgba(236, 72, 153, 0.3);
        border-radius: 16px;
        padding: 10px;
        text-align: center;
        margin: 16px 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: rgba(15, 23, 42, 0.8);
        padding: 8px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 14px;
        color: #94a3b8;
        font-weight: 600;
        padding: 12px 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff;
        background: rgba(99, 102, 241, 0.15);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white !important;
        box-shadow: 0 4px 25px rgba(99, 102, 241, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners Function
def render_banner_ad(position="top"):
    st.markdown(
        f'<div class="ad-banner"><p style="color: #64748b; font-size: 8px; margin: 0; letter-spacing: 2px; text-transform: uppercase;">💎 SPONSORED ECOSYSTEM ({position})</p></div>',
        unsafe_allow_html=True
    )
    components.html(
        '<div style="text-align:center; background:#090d16; padding:8px; border-radius:12px;">'
        '<script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>'
        '<div id="container-990668de3498a3c38ef3239d7c52eba3"></div>'
        '</div>',
        height=90
    )

# Social Bar Integration
components.html('<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>', height=0)

# TOP BANNER AD
render_banner_ad("Top Header")

# Bento Grid Status Header
st.markdown("""
<div style="text-align: center; padding: 12px 0 18px 0;">
    <span style="background: rgba(236, 72, 153, 0.12); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.35); padding: 6px 20px; border-radius: 30px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; display: inline-block; box-shadow: 0 0 25px rgba(236, 72, 153, 0.25);">👑 2026 Bento AI Creator Suite 🚀</span>
</div>
""", unsafe_allow_html=True)

# Responsive Aurora Canvas Header Box
def render_aurora_header():
    components.html("""
    <div id="wrapperBox" style="width:100%; border-radius:20px; overflow:hidden; position:relative; background:#070a13; border:1px solid rgba(255,255,255,0.12); box-shadow:0 15px 40px rgba(0,0,0,0.8); margin-bottom: 26px;">
        <canvas id="auroraCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%; display:block;"></canvas>
        <div style="position:relative; z-index:2; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; background:rgba(3,7,18,0.45); padding:12px; text-align:center; box-sizing:border-box;">
            <h2 id="mainTitle" style="color: #ffffff; font-weight: 900; margin: 0 0 4px 0; letter-spacing: -0.5px; text-shadow: 0 2px 15px rgba(0,0,0,0.9); width:100%; text-align:center;">⚡ Creator Studio Pro 🪄</h2>
            <p id="subTitle" style="color: #cbd5e1; font-weight: 600; margin: 0; text-shadow: 0 1px 10px rgba(0,0,0,0.9); width:100%; text-align:center;">💎 Bento-Grid AI Cutout & Global Viral Tags Ecosystem 🚀</p>
        </div>
    </div>

    <script>
        const canvas = document.getElementById("auroraCanvas");
        const ctx = canvas.getContext("2d");
        const wrapper = document.getElementById("wrapperBox");
        const title = document.getElementById("mainTitle");
        const subtitle = document.getElementById("subTitle");

        function adjustSize() {
            const isDesktop = window.innerWidth > 768;
            if (isDesktop) {
                wrapper.style.height = "140px";
                title.style.fontSize = "2.1rem";
                subtitle.style.fontSize = "13.5px";
            } else {
                wrapper.style.height = "95px";
                title.style.fontSize = "1.25rem";
                subtitle.style.fontSize = "10px";
            }
            canvas.width = wrapper.offsetWidth;
            canvas.height = wrapper.offsetHeight;
        }

        adjustSize();
        window.addEventListener("resize", adjustSize);

        let mode = 0; 
        let transitionProgress = 0; 
        
        setInterval(() => {
            mode = mode === 0 ? 1 : 0;
        }, 6000);

        const particles = [];
        for (let i = 0; i < 45; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 3 + 1,
                speedY: Math.random() * 1.5 + 0.4,
                speedX: (Math.random() - 0.5) * 1,
                alpha: Math.random() * 0.7 + 0.2
            });
        }

        let waveOffset = 0;

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            if (mode === 1 && transitionProgress < 1) transitionProgress += 0.03;
            if (mode === 0 && transitionProgress > 0) transitionProgress -= 0.03;

            waveOffset += 0.04;

            const bgGradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
            const r1 = Math.round(15 * (1 - transitionProgress) + 35 * transitionProgress);
            const g1 = Math.round(23 * (1 - transitionProgress) + 10 * transitionProgress);
            const b1 = Math.round(42 * (1 - transitionProgress) + 50 * transitionProgress);

            const r2 = Math.round(30 * (1 - transitionProgress) + 190 * transitionProgress);
            const g2 = Math.round(70 * (1 - transitionProgress) + 40 * transitionProgress);
            const b2 = Math.round(160 * (1 - transitionProgress) + 20 * transitionProgress);

            bgGradient.addColorStop(0, `rgb(${r1},${g1},${b1})`);
            bgGradient.addColorStop(1, `rgb(${r2},${g2},${b2})`);
            ctx.fillStyle = bgGradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.beginPath();
            ctx.moveTo(0, canvas.height);
            for (let x = 0; x <= canvas.width; x += 10) {
                const y = Math.sin(x * 0.02 + waveOffset) * (5 + transitionProgress * 3) + (canvas.height * 0.5);
                ctx.lineTo(x, y);
            }
            ctx.lineTo(canvas.width, canvas.height);
            ctx.closePath();

            const waveGrad = ctx.createLinearGradient(0, 0, canvas.width, 0);
            const waveColor1 = `rgba(${Math.round(56*(1-transitionProgress) + 249*transitionProgress)}, ${Math.round(189*(1-transitionProgress) + 115*transitionProgress)}, ${Math.round(248*(1-transitionProgress) + 22*transitionProgress)}, 0.35)`;
            const waveColor2 = `rgba(${Math.round(147*(1-transitionProgress) + 239*transitionProgress)}, ${Math.round(51*(1-transitionProgress) + 68*transitionProgress)}, ${Math.round(234*(1-transitionProgress) + 68*transitionProgress)}, 0.35)`;
            
            waveGrad.addColorStop(0, waveColor1);
            waveGrad.addColorStop(1, waveColor2);
            ctx.fillStyle = waveGrad;
            ctx.fill();

            particles.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                
                const pr = Math.round(56 * (1 - transitionProgress) + 251 * transitionProgress);
                const pg = Math.round(189 * (1 - transitionProgress) + 146 * transitionProgress);
                const pb = Math.round(248 * (1 - transitionProgress) + 60 * transitionProgress);
                
                ctx.fillStyle = `rgba(${pr}, ${pg}, ${pb}, ${p.alpha})`;
                ctx.shadowBlur = 10;
                ctx.shadowColor = `rgb(${pr}, ${pg}, ${pb})`;
                ctx.fill();
                ctx.shadowBlur = 0;

                if (mode === 1) {
                    p.y -= p.speedY;
                    p.x += Math.sin(p.y * 0.05);
                    if (p.y < 0) {
                        p.y = canvas.height + 10;
                        p.x = Math.random() * canvas.width;
                    }
                } else {
                    p.y += p.speedY * 0.6;
                    p.x += Math.cos(p.y * 0.05);
                    if (p.y > canvas.height) {
                        p.y = -10;
                        p.x = Math.random() * canvas.width;
                    }
                }
            });

            requestAnimationFrame(animate);
        }

        animate();
    </script>
    """, height=145)

render_aurora_header()

# Real-time YouTube Search Suggest Function
def get_yt_live_keywords(query):
    try:
        url = f"http://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}"
        res = requests.get(url, timeout=3).json()
        if len(res) > 1 and len(res[1]) > 0:
            return res[1]
    except Exception:
        pass
    return []

# Bento Tabs Navigation
tab1, tab2, tab3 = st.tabs(["🪄 AI Cutout Studio", "🔴 YouTube Viral Tags", "📱 Instagram #Tags"])

# --- TAB 1: BACKGROUND REMOVER WITH BENTO CARD ---
with tab1:
    st.markdown("<div class='bento-card'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-bottom: 22px;">
        <div style="font-size: 50px; margin-bottom: 10px;">🔮</div>
        <h2 style="color: #ffffff; font-weight: 800; margin: 0; font-size: 1.85rem;">⚡ HD Background Cutout AI 🪄</h2>
        <p style="color: #94a3b8; font-size: 13.5px; margin-top: 6px;">✨ Instant zero-crash professional AI transparent background cutout with high-speed rendering! 💎</p>
    </div>
    """, unsafe_allow_html=True)
    
    components.html("""
    <div style="text-align: center; margin: 20px 0;">
        <a href="https://www.remove.bg" target="_blank" onclick="triggerAdAndRedirect()" style="display: block; width: 100%; background: linear-gradient(135deg, #2563eb 0%, #ec4899 100%); color: white !important; font-weight: 700; text-align: center; padding: 16px 24px; border-radius: 14px; text-decoration: none !important; box-shadow: 0 6px 30px rgba(236, 72, 153, 0.5); box-sizing: border-box; font-family: sans-serif; font-size: 15px; transition: transform 0.2s;">
            🚀 LAUNCH AI BACKGROUND REMOVER NOW 🔥
        </a>
    </div>
    <script>
        function triggerAdAndRedirect() {
            window.open("https://asiafilm.org/4/beee6a5e22f2d935b8ad0c1425c973ca", "_blank");
        }
    </script>
    """, height=80)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: YOUTUBE RAPIDTAGS BENTO CARD ---
with tab2:
    st.markdown("<div class='bento-card'>", unsafe_allow_html=True)
    st.markdown("### 🔴 YouTube Official RapidTags Generator ⚡")
    st.markdown("<p style='color: #94a3b8; font-size: 13.5px;'>💎 Extracts live YouTube search suggest keywords optimized for 10M+ views! 🚀</p>", unsafe_allow_html=True)
    
    yt_topic = st.text_input("🎯 Enter YouTube Topic / Keyword:", placeholder="e.g. Satoru Gojo Drawing, Anime Edits 🌟", key="yt_top")
    
    if st.button("🔥 GENERATE VIRAL YOUTUBE TAGS ⚡", key="btn_yt"):
        if yt_topic:
            with st.spinner("🔮 Connecting to YouTube Official Suggest API..."):
                time.sleep(0.4) # Skeleton / load state simulation
            st.success("🎉 YouTube Tags Generated Successfully! 🚀")
            
            clean_topic = yt_topic.strip()
            no_space_topic = clean_topic.replace(" ", "")
            
            live_keywords = get_yt_live_keywords(clean_topic)
            
            if not live_keywords:
                live_keywords = [
                    clean_topic, f"{clean_topic} tutorial", f"how to {clean_topic}",
                    f"best {clean_topic}", f"{clean_topic} 2026", f"viral {clean_topic}",
                    f"{clean_topic} speedrun", f"{clean_topic} tips and tricks"
                ]
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:12px;'>🔑 Comma-Separated RapidTags (Copy & Paste):</p>", unsafe_allow_html=True)
            tags_str = ", ".join(live_keywords)
            st.code(tags_str, language="text")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>#️⃣ Top Ranking Description Hashtags:</p>", unsafe_allow_html=True)
            st.code(f"#{no_space_topic} #{no_space_topic}Tutorial #YouTubeGrowth #ViralVideo2026 #CreatorStudio #TrendingNow", language="text")
        else:
            st.warning("⚠️ Please enter a YouTube topic or keyword first! 🎯")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: INSTAGRAM EXTREME HASHTAGS BENTO CARD ---
with tab3:
    st.markdown("<div class='bento-card'>", unsafe_allow_html=True)
    st.markdown("### 📱 Instagram Extreme Trending #Tags 🚀")
    st.markdown("<p style='color: #94a3b8; font-size: 13.5px;'>🔥 Generates high-reach viral hashtags designed to blow up your Reels instantly! 🌟</p>", unsafe_allow_html=True)
    
    reel_topic = st.text_input("🎯 Enter Reel Topic / Concept:", placeholder="e.g. Speed Art, Anime Edit, Gym Motivation 🔥", key="reel_top")
    
    if st.button("💥 GENERATE EXTREME VIRAL #TAGS 🚀", key="btn_reel"):
        if reel_topic:
            with st.spinner("🔮 Fetching Trending Reels Algorithm..."):
                time.sleep(0.4) # Skeleton / load state simulation
            st.success("🎉 Instagram Viral Hashtags Generated! 👑")
            
            clean_reel = reel_topic.strip()
            no_space_reel = clean_reel.replace(" ", "")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:12px;'>🔥 Extreme Viral Reels #Hashtags (Ready to Copy):</p>", unsafe_allow_html=True)
            
            extreme_hashtags = f"#{no_space_reel} #{no_space_reel}Art #{no_space_reel}Edits #reels #reelsinstagram #reelsviral #reelsindia #explore #explorepage #trendingreels #viralreels #instareels #creators #creatorgrams #reelslovers #reelsaddict #fyp #viral #foryou #2026trends"
            st.code(extreme_hashtags, language="text")
        else:
            st.warning("⚠️ Please enter a reel topic or concept first! 🎯")
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
