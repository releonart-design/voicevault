import streamlit as st
import streamlit.components.v1 as components
import random
import requests

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | 2026 Ultra AI",
    page_icon="⚡",
    layout="centered"
)

# Dark Mode & Theme State Management
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

bg_gradient = "linear-gradient(-45deg, #030712, #1e1b4b, #311042, #0f172a, #030712)" if st.session_state.dark_mode else "linear-gradient(-45deg, #f8fafc, #e2e8f0, #cbd5e1, #f1f5f9, #f8fafc)"
card_bg = "rgba(17, 24, 39, 0.75)" if st.session_state.dark_mode else "rgba(255, 255, 255, 0.85)"
text_color = "#f3f4f6" if st.session_state.dark_mode else "#0f172a"
sub_text = "#9ca3af" if st.session_state.dark_mode else "#475569"
border_color = "rgba(255, 255, 255, 0.1)" if st.session_state.dark_mode else "rgba(0, 0, 0, 0.1)"

# Clean & Professional CSS with Dark/Light Mode Support & Animated Face SVG
st.markdown(f"""
<style>
    @keyframes auroraBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    @keyframes blink {{
        0%, 40%, 100% {{ transform: scaleY(1); }}
        45% {{ transform: scaleY(0.1); }}
        50% {{ transform: scaleY(1); }}
    }}

    @keyframes mouthMorph {{
        0%, 30% {{ d: path("M 7.5 18.5 Q 12 15 16.5 18.5"); }}
        50%, 80% {{ d: path("M 7.5 16 Q 12 21 16.5 16"); }}
        100% {{ d: path("M 7.5 18.5 Q 12 15 16.5 18.5"); }}
    }}

    @keyframes ringGlow {{
        0% {{ filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.4)); }}
        50% {{ filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.8)); }}
        100% {{ filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.4)); }}
    }}

    .animated-face-svg {{
        display: inline-block;
        width: 32px;
        height: 32px;
        vertical-align: middle;
        flex-shrink: 0;
        animation: ringGlow 2.5s infinite ease-in-out;
    }}

    .eye {{
        animation: blink 3s infinite;
        transform-origin: center;
    }}

    .mouth {{
        animation: mouthMorph 4s infinite ease-in-out;
    }}
    
    .main {{ background-color: {'#030712' if st.session_state.dark_mode else '#f8fafc'}; color: {text_color}; font-family: 'Inter', sans-serif; }}
    .stApp {{
        background: {bg_gradient};
        background-size: 400% 400%;
        animation: auroraBG 18s ease infinite;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    .glass-card {{
        background: {card_bg};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid {border_color};
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, {'0.5' if st.session_state.dark_mode else '0.1'});
        margin-bottom: 20px;
    }}
    
    .stButton>button {{
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 14px;
        border: none;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        box-shadow: 0 6px 25px rgba(168, 85, 247, 0.6);
        transform: translateY(-2px);
    }}
    
    .ad-banner {{
        background-color: {card_bg};
        border: 1px dashed rgba(225, 29, 72, 0.4);
        border-radius: 12px;
        padding: 8px;
        text-align: center;
        margin: 12px 0;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 10px;
        background-color: {card_bg};
        padding: 6px;
        border-radius: 14px;
        border: 1px solid {border_color};
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        color: {sub_text};
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }}
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }}
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners Function
def render_banner_ad(position="top"):
    st.markdown(
        f'<div class="ad-banner"><p style="color: {sub_text}; font-size: 9px; margin: 0; letter-spacing: 1.5px; text-transform: uppercase;">SPONSORED AD ({position})</p></div>',
        unsafe_allow_html=True
    )
    components.html(
        '<div style="text-align:center; background:#0b0f19; padding:6px; border-radius:10px;">'
        '<script async="async" data-cfasync="false" src="https://bauval.org/21/990668de3498a3c38ef3239d7c52eba3"></script>'
        '<div id="container-990668de3498a3c38ef3239d7c52eba3"></div>'
        '</div>',
        height=100
    )

# Social Bar Integration
components.html('<script data-cfasync="false" src="https://bauval.org/14/f54a8efc196977f6b40a8746bbbc035a"></script>', height=0)

# TOP BANNER AD
render_banner_ad("Top Header")

# Top Header with Dark Mode Toggle Button
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.markdown("""
    <div style="padding: 8px 0 12px 0;">
        <span style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">⚡ 2026 Next-Gen AI Suite</span>
    </div>
    """, unsafe_allow_html=True)
with col2:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

# Anime Header Box
def render_anime_elemental_box():
    components.html("""
    <div id="wrapperBox" style="width:100%; border-radius:16px; overflow:hidden; position:relative; background:#070a13; border:1px solid rgba(255,255,255,0.12); box-shadow:0 8px 30px rgba(0,0,0,0.6); margin-bottom: 20px;">
        <canvas id="animeCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%; display:block;"></canvas>
        <div style="position:relative; z-index:2; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; background:rgba(3,7,18,0.35); padding:10px; text-align:center; box-sizing:border-box;">
            <h2 id="mainTitle" style="color: #ffffff; font-weight: 900; margin: 0 0 4px 0; letter-spacing: -0.5px; text-shadow: 0 2px 10px rgba(0,0,0,0.8); width:100%; text-align:center;">Creator Studio Pro</h2>
            <p id="subTitle" style="color: #cbd5e1; font-weight: 600; margin: 0; text-shadow: 0 1px 6px rgba(0,0,0,0.8); width:100%; text-align:center;">Professional AI Background Cutout & Tags Generator</p>
        </div>
    </div>

    <script>
        const canvas = document.getElementById("animeCanvas");
        const ctx = canvas.getContext("2d");
        const wrapper = document.getElementById("wrapperBox");
        const title = document.getElementById("mainTitle");
        const subtitle = document.getElementById("subTitle");

        function adjustSize() {
            const isDesktop = window.innerWidth > 768;
            if (isDesktop) {
                wrapper.style.height = "130px";
                title.style.fontSize = "2rem";
                subtitle.style.fontSize = "13px";
            } else {
                wrapper.style.height = "85px";
                title.style.fontSize = "1.2rem";
                subtitle.style.fontSize = "9px";
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
        for (let i = 0; i < 35; i++) {
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
            const r1 = Math.round(15 * (1 - transitionProgress) + 40 * transitionProgress);
            const g1 = Math.round(23 * (1 - transitionProgress) + 10 * transitionProgress);
            const b1 = Math.round(42 * (1 - transitionProgress) + 15 * transitionProgress);

            const r2 = Math.round(30 * (1 - transitionProgress) + 180 * transitionProgress);
            const g2 = Math.round(70 * (1 - transitionProgress) + 40 * transitionProgress);
            const b2 = Math.round(160 * (1 - transitionProgress) + 10 * transitionProgress);

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
            const waveColor1 = `rgba(${Math.round(56*(1-transitionProgress) + 249*transitionProgress)}, ${Math.round(189*(1-transitionProgress) + 115*transitionProgress)}, ${Math.round(248*(1-transitionProgress) + 22*transitionProgress)}, 0.3)`;
            const waveColor2 = `rgba(${Math.round(147*(1-transitionProgress) + 239*transitionProgress)}, ${Math.round(51*(1-transitionProgress) + 68*transitionProgress)}, ${Math.round(234*(1-transitionProgress) + 68*transitionProgress)}, 0.3)`;
            
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
                ctx.shadowBlur = 6;
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
    """, height=135)

render_anime_elemental_box()

# YouTube Keywords function
def get_yt_live_keywords(query):
    try:
        url = f"http://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}"
        res = requests.get(url, timeout=3).json()
        if len(res) > 1 and len(res[1]) > 0:
            return res[1]
    except Exception:
        pass
    return []

# SVG Animated Face
animated_face_html = """
<svg class="animated-face-svg" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <circle cx="12" cy="12" r="11" fill="none" stroke="#ffffff" stroke-width="0.9"/>
  <circle cx="12" cy="12" r="9.8" fill="none" stroke="#ffffff" stroke-width="0.7"/>
  <ellipse class="eye" cx="8.5" cy="9" rx="1.1" ry="1.7" fill="#ffffff"/>
  <ellipse class="eye" cx="15.5" cy="9" rx="1.1" ry="1.7" fill="#ffffff"/>
  <path class="mouth" d="M 7.5 18.5 Q 12 15 16.5 18.5" fill="none" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round"/>
</svg>
"""

# Tabs
tab1, tab2, tab3 = st.tabs(["✨ AI Background Remover", "🔴 YouTube Tags", "📸 Instagram Tags"])

# --- TAB 1: BACKGROUND REMOVER ---
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="font-size: 45px; margin-bottom: 10px;">🪄</div>
        <h2 style="color: {text_color}; font-weight: 800; margin: 0; font-size: 1.8rem;">HD Background Remover</h2>
        <p style="color: {sub_text}; font-size: 13px; margin-top: 6px;">Instant zero-crash professional AI transparent background cutout.</p>
    </div>
    """, unsafe_allow_html=True)
    
    components.html("""
    <div style="text-align: center; margin: 20px 0;">
        <a href="https://www.remove.bg" target="_blank" onclick="triggerAdAndRedirect()" style="display: block; width: 100%; background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%); color: white !important; font-weight: 700; text-align: center; padding: 16px 24px; border-radius: 12px; text-decoration: none !important; box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4); box-sizing: border-box; font-family: sans-serif; font-size: 15px;">
            🚀 LAUNCH AI BACKGROUND REMOVER ➔
        </a>
    </div>
    <script>
        function triggerAdAndRedirect() {
            window.open("https://asiafilm.org/4/beee6a5e22f2d935b8ad0c1425c973ca", "_blank");
        }
    </script>
    """, height=80)
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: YOUTUBE TAGS ---
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: {text_color};'>🔴 YouTube Official Tags Generator</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {sub_text}; font-size: 13px;'>Extracts real-time YouTube search suggest tags in comma-separated format.</p>", unsafe_allow_html=True)
    
    yt_topic = st.text_input("Enter YouTube Topic / Keyword:", placeholder="e.g. Satoru Gojo Drawing, Anime Edits", key="yt_top")
    
    if st.button("⚡ GENERATE YOUTUBE TAGS", key="btn_yt"):
        if yt_topic:
            components.html("""
            <script>
                window.open("https://asiafilm.org/4/beee6a5e22f2d935b8ad0c1425c973ca", "_blank");
            </script>
            """, height=0)
            
            st.success("YouTube Tags Generated Successfully (Ad Triggered)!")
            clean_topic = yt_topic.strip()
            no_space_topic = clean_topic.replace(" ", "")
            
            live_keywords = get_yt_live_keywords(clean_topic)
            
            if not live_keywords:
                live_keywords = [
                    clean_topic, f"{clean_topic} tutorial", f"how to {clean_topic}",
                    f"best {clean_topic}", f"{clean_topic} 2026", f"viral {clean_topic}",
                    f"{clean_topic} speedrun", f"{clean_topic} tips and tricks"
                ]
            
            st.markdown(f"<p style='color:{text_color}; font-weight:600; margin-top:10px;'>🔑 Comma-Separated YouTube Tags (RapidTags Style):</p>", unsafe_allow_html=True)
            tags_str = ", ".join(live_keywords)
            st.code(tags_str, language="text")
            
            st.markdown(f"<p style='color:{text_color}; font-weight:600;'>#️⃣ Description Hashtags:</p>", unsafe_allow_html=True)
            st.code(f"#{no_space_topic} #{no_space_topic}Tutorial #YouTubeGrowth #ViralVideo2026 #CreatorStudio", language="text")
        else:
            st.warning("Please enter a YouTube topic first!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: INSTAGRAM TAGS (WITH FLEXBOX ALIGNMENT) ---
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 4px;">
        {animated_face_html}
        <h3 style="color: {text_color}; margin: 0; font-size: 1.5rem; line-height: 1.2;">Instagram Extreme Trending Tags</h3>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"<p style='color: {sub_text}; font-size: 13px; margin-top: 4px;'>Generates high-reach extreme trending Instagram Reels hashtags.</p>", unsafe_allow_html=True)
    
    reel_topic = st.text_input("Enter Reel Topic / Concept:", placeholder="e.g. Speed Art, Anime Edit, Gym Motivation", key="reel_top")
    
    if st.button("🔥 GENERATE INSTAGRAM TAGS", key="btn_reel"):
        if reel_topic:
            components.html("""
            <script>
                window.open("https://asiafilm.org/4/beee6a5e22f2d935b8ad0c1425c973ca", "_blank");
            </script>
            """, height=0)
            
            st.success("Instagram Viral Tags Generated (Ad Triggered)!")
            clean_reel = reel_topic.strip()
            no_space_reel = clean_reel.replace(" ", "")
            
            st.markdown(f"<p style='color:{text_color}; font-weight:600; margin-top:10px;'>🔥 Extreme Viral Reels #Hashtags (Copy-Paste Ready):</p>", unsafe_allow_html=True)
            
            extreme_hashtags = f"#{no_space_reel} #{no_space_reel}Art #{no_space_reel}Edits #reels #reelsinstagram #reelsviral #reelsindia #explore #explorepage #trendingreels #viralreels #instareels #creators #creatorgrams #reelslovers #reelsaddict #fyp #viral #foryou #2026trends"
            st.code(extreme_hashtags, language="text")
        else:
            st.warning("Please enter a reel topic first!")
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
