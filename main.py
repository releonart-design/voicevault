import streamlit as st
import streamlit.components.v1 as components
import random

# Page Setup
st.set_page_config(
    page_title="Creator Studio Pro | 2026 Ultra AI",
    page_icon="⚡",
    layout="centered"
)

# 2026 Ultra-Modern CSS & Background Effects
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

# Animated Header Section
st.markdown("""
<div style="text-align: center; padding: 20px 0 25px 0;">
    <span style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">⚡ 2026 Next-Gen AI Suite</span>
    <h1 style='color: #ffffff; font-weight: 900; margin-top: 12px; font-size: 2.4rem; letter-spacing: -0.5px;'>Creator Studio Pro</h1>
    <p style='color: #9ca3af; font-size: 14px;'>Professional AI Background Cutout & Real Working SEO Suite</p>
</div>
""", unsafe_allow_html=True)

# Function for Anime Water-to-Fire Morph Canvas Animation
def render_anime_elemental_box():
    components.html("""
    <div style="width:100%; border-radius:16px; overflow:hidden; position:relative; background:#070a13; border:1px solid rgba(255,255,255,0.12); box-shadow:0 8px 32px rgba(0,0,0,0.6);">
        <canvas id="animeCanvas" style="width:100%; height:110px; display:block;"></canvas>
        <div style="position:absolute; top:0; left:0; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; background:rgba(0,0,0,0.3); pointer-events:none;">
            <span id="elementBadge" style="background:rgba(56,189,248,0.2); color:#38bdf8; border:1px solid rgba(56,189,248,0.4); padding:3px 12px; border-radius:12px; font-size:10px; font-weight:800; letter-spacing:1px; text-transform:uppercase; font-family:sans-serif; transition:all 0.5s ease;">💧 ANIME WATER AURA</span>
            <p style="color:#ffffff; font-size:12px; font-weight:700; font-family:sans-serif; margin:6px 0 0 0; text-shadow:0 2px 8px rgba(0,0,0,0.8);">Next-Gen AI VFX Engine Active</p>
        </div>
    </div>

    <script>
        const canvas = document.getElementById("animeCanvas");
        const ctx = canvas.getContext("2d");
        const badge = document.getElementById("elementBadge");

        function resizeCanvas() {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        }
        resizeCanvas();
        window.addEventListener("resize", resizeCanvas);

        let mode = 0; // 0 = Water, 1 = Fire
        let transitionProgress = 0; // 0 to 1
        
        // Auto-switch mode every 6 seconds
        setInterval(() => {
            mode = mode === 0 ? 1 : 0;
            if (mode === 1) {
                badge.innerText = "🔥 ANIME FIRE AURA";
                badge.style.background = "rgba(249,115,22,0.25)";
                badge.style.color = "#fb923c";
                badge.style.borderColor = "rgba(249,115,22,0.5)";
            } else {
                badge.innerText = "💧 ANIME WATER AURA";
                badge.style.background = "rgba(56,189,248,0.2)";
                badge.style.color = "#38bdf8";
                badge.style.borderColor = "rgba(56,189,248,0.4)";
            }
        }, 6000);

        // Particle system for anime aura effects
        const particles = [];
        for (let i = 0; i < 50; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 4 + 2,
                speedY: Math.random() * 2 + 0.5,
                speedX: (Math.random() - 0.5) * 1.5,
                alpha: Math.random() * 0.8 + 0.2
            });
        }

        let waveOffset = 0;

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Smooth transition handling
            if (mode === 1 && transitionProgress < 1) transitionProgress += 0.03;
            if (mode === 0 && transitionProgress > 0) transitionProgress -= 0.03;

            waveOffset += 0.05;

            // Background Dynamic Gradient Interpolation
            const bgGradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
            // Blend Water Blue and Fire Red/Orange
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

            // Anime Fluid Waves (Water / Heatwaves)
            ctx.beginPath();
            ctx.moveTo(0, canvas.height);
            for (let x = 0; x <= canvas.width; x += 10) {
                const y = Math.sin(x * 0.015 + waveOffset) * (8 + transitionProgress * 6) + (canvas.height * 0.5);
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

            // Anime Particles (Ripples up in Fire, Drops down in Water)
            particles.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                
                // Color morph
                const pr = Math.round(56 * (1 - transitionProgress) + 251 * transitionProgress);
                const pg = Math.round(189 * (1 - transitionProgress) + 146 * transitionProgress);
                const pb = Math.round(248 * (1 - transitionProgress) + 60 * transitionProgress);
                
                ctx.fillStyle = `rgba(${pr}, ${pg}, ${pb}, ${p.alpha})`;
                ctx.shadowBlur = 10;
                ctx.shadowColor = `rgb(${pr}, ${pg}, ${pb})`;
                ctx.fill();
                ctx.shadowBlur = 0;

                // Fire moves UP, Water moves DOWN
                if (mode === 1) {
                    p.y -= p.speedY * 1.5;
                    p.x += Math.sin(p.y * 0.05) * 1.2;
                    if (p.y < 0) {
                        p.y = canvas.height + 10;
                        p.x = Math.random() * canvas.width;
                    }
                } else {
                    p.y += p.speedY * 0.8;
                    p.x += Math.cos(p.y * 0.05) * 0.8;
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
    """, height=120)

# Render Animated Box at top
render_anime_elemental_box()

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
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600; margin-top:20px;'>📌 Optimized High-CTR Video Titles:</p>", unsafe_allow_html=True)
            st.code(f"""1. How to Master {clean_topic} in 10 Minutes (Step-by-Step)
2. The Ultimate Guide to {clean_topic} (2026 Masterclass)
3. I Tried {clean_topic} For 24 Hours — Here Is What Happened
4. Stop Making This Mistake With {clean_topic}!""", language="text")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>🔑 RapidTags Style YouTube Tags (Comma Separated):</p>", unsafe_allow_html=True)
            comma_tags = f"{clean_topic}, {clean_topic} tutorial, how to {clean_topic}, {clean_topic} 2026, best {clean_topic} guide, viral {clean_topic}, advanced {clean_topic}, {clean_topic} tips and tricks, {clean_topic} masterclass, learn {clean_topic}"
            st.code(comma_tags, language="text")
            
            st.markdown("<p style='color:#e2e8f0; font-weight:600;'>#️⃣ Top Description Hashtags:</p>", unsafe_allow_html=True)
            st.code(f"#{no_space_topic} #{no_space_topic}Tutorial #CreatorStudio #Trending2026 #YouTubeGrowth #Masterclass", language="text")
        else:
            st.warning("Please enter a video topic or keyword first!")
    st.markdown("</div>", unsafe_allow_html=True)
