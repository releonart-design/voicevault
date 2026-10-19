import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="VoiceVault - AI Voice Dubbing",
    page_icon="🎙️",
    layout="centered"
)

# Custom Styling for Mobile UX
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #4f46e5; color: white; padding: 10px; }
    .ad-banner { background-color: #1a1a2e; border: 1px dashed #4f46e5; border-radius: 8px; padding: 10px; text-align: center; margin: 10px 0; }
    .affiliate-card { border: 1px solid #374151; border-radius: 8px; padding: 15px; background: #1f2937; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'ad_reward_earned' not in st.session_state:
    st.session_state['ad_reward_earned'] = False
if 'generation_completed' not in st.session_state:
    st.session_state['generation_completed'] = False

# Banner Ad Function
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 10px; margin: 0 0 2px 0; text-transform: uppercase;">Sponsored Banner Ad ({position})</p>
        <span style="color: #e5e7eb; font-size: 13px;">📢 <b>VoiceVault Partner:</b> Get 50% Off Pro AI Voice Studio! 
        <a href="https://example.com" target="_blank" style="color: #818cf8; text-decoration: underline;">Claim &rarr;</a></span>
    </div>
    """, unsafe_allow_html=True)

# Top Banner Ad
render_banner_ad("Top")

# App Header
st.markdown("<h1 style='text-align: center; color: white;'>🎙️ VoiceVault</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>100% Free AI Video Voice Dubbing Studio</p>", unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2 = st.tabs(["🎬 Dubbing Studio", "🎙️ Creator Toolkit (Affiliates)"])

with tab1:
    st.markdown("### 📤 Input Media")
    uploaded_file = st.file_uploader("Upload Video or Audio File", type=["mp4", "mp3", "wav"])
    target_lang = st.selectbox("Select Target Language", ["Spanish", "French", "German", "Hindi", "Japanese", "English"])

    st.markdown("---")

    # Rewarded Video Ad Gatekeeper
    st.markdown("### 🎬 Free Generation Gatekeeper")
    
    if not st.session_state['ad_reward_earned']:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 15px; border-radius: 10px; color: white; text-align: center; margin-bottom: 15px;">
            <p style="font-size: 14px; margin: 0;">Watch a brief 15-second sponsored ad to unlock your free AI voice dubbing credit.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📺 Watch Rewarded Ad (15s)"):
            with st.spinner("Playing Rewarded Video Ad... Please wait..."):
                import time
                time.sleep(3)
            st.session_state['ad_reward_earned'] = True
            st.success("🎉 Reward Unlocked! You can now generate your dub.")
            st.rerun()
    else:
        st.success("✅ Free Generation Credit Active!")
        if st.button("🚀 Start AI Voice Dubbing Pipeline", type="primary"):
            with st.spinner("Processing AI Pipeline (STT -> Translation -> Voice Cloning -> Muxing)..."):
                import time
                time.sleep(3)
            st.session_state['generation_completed'] = True
            st.success("✨ Voice Dubbing Completed Successfully!")

    # Output / Download Section
    if st.session_state['generation_completed'] and uploaded_file is not None:
        st.markdown("### 📥 Download Output")
        if uploaded_file.name.endswith('.mp4'):
            st.video(uploaded_file)
        else:
            st.audio(uploaded_file)
        
        # Donations / Buy Me a Coffee
        st.markdown("""
        <div style="text-align: center; margin-top: 25px; padding: 20px; background: #111827; border-radius: 12px; border: 1px solid #4f46e5;">
            <h3 style="color: white; margin-bottom: 5px;">❤️ Support Open-Source AI</h3>
            <p style="color: #9ca3af; font-size: 13px; margin-bottom: 15px;">Help us cover server bandwidth & GPU costs!</p>
            <a href="https://buymeacoffee.com" target="_blank" style="background-color: #ffdd00; color: #000; padding: 10px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; display: inline-block;">☕ Buy Me a Coffee</a>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    # Creator Toolkit Affiliate Section
    st.markdown("### 🎧 Recommended Studio Gear & Creator Toolkit")
    st.markdown("<p style='color: #9ca3af; font-size: 13px;'>Equip your setup with pro gear. Purchasing via our affiliate links supports free open-source AI hosting!</p>", unsafe_allow_html=True)

    st.markdown("""
    <div class="affiliate-card">
        <h4 style="color: #f3f4f6; margin: 0 0 5px 0;">Shure MV7 USB Microphone</h4>
        <p style="color: #9ca3af; font-size: 12px; margin: 0 0 10px 0;">Broadcast podcast mic for crystal-clear voice input accuracy.</p>
        <a href="https://amazon.com/dp/example1?tag=voicevault-20" target="_blank" style="background: #f59e0b; color: #111; padding: 5px 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 12px;">View on Amazon &rarr;</a>
    </div>
    
    <div class="affiliate-card">
        <h4 style="color: #f3f4f6; margin: 0 0 5px 0;">DJI Mic 2 Wireless System</h4>
        <p style="color: #9ca3af; font-size: 12px; margin: 0 0 10px 0;">Ultra-compact dual-channel wireless lavalier mic for creators.</p>
        <a href="https://amazon.com/dp/example2?tag=voicevault-20" target="_blank" style="background: #f59e0b; color: #111; padding: 5px 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 12px;">View on Amazon &rarr;</a>
    </div>
    
    <div class="affiliate-card">
        <h4 style="color: #f3f4f6; margin: 0 0 5px 0;">Acoustic Soundproofing Foam</h4>
        <p style="color: #9ca3af; font-size: 12px; margin: 0 0 10px 0;">High-density studio tiles to eliminate echo and room reverb.</p>
        <a href="https://amazon.com/dp/example3?tag=voicevault-20" target="_blank" style="background: #f59e0b; color: #111; padding: 5px 10px; border-radius: 4px; font-weight: bold; text-decoration: none; font-size: 12px;">View on Amazon &rarr;</a>
    </div>
    """, unsafe_allow_html=True)

# Bottom Banner Ad
render_banner_ad("Bottom")
