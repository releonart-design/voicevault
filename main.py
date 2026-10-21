import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(
    page_title="Shadow Tekken Arena: PvP Fighters",
    page_icon="🥋",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #080c14; color: #f1f5f9; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #f43f5e 0%, #be123c 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #111827; border: 1px dashed #f43f5e; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 10px; margin: 0; text-transform: uppercase;">SPONSORED ARENA BANNER ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#111827; padding:5px; border-radius:6px;">
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🥋 SHADOW TEKKEN: ARCADE BATTLES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Master Combos, Clear Ranks & Unlock All 10 Shadow Fighters</p>", unsafe_allow_html=True)

# HTML5/JS Tekken-Style Fighting Engine Code
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #030712; color: white; font-family: 'Segoe UI', Tahoma, sans-serif; text-align: center; user-select: none; }
    #gameCanvas { background: radial-gradient(circle, #1e293b 0%, #020617 100%); border: 2px solid #f43f5e; border-radius: 10px; box-shadow: 0 0 25px rgba(244,63,94,0.3); }
    .hud { display: flex; justify-content: space-between; padding: 12px; width: 680px; margin: 0 auto; font-weight: bold; }
    .hp-container { width: 240px; }
    .hp-bar { width: 100%; height: 20px; background: #1e293b; border: 2px solid #475569; border-radius: 4px; overflow: hidden; }
    .hp-fill { height: 100%; width: 100%; background: #22c55e; transition: width 0.1s; }
    .fighters-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; margin: 12px auto; max-width: 680px; }
    .fighter-card { background: #111827; border: 2px solid #374151; padding: 8px 4px; border-radius: 6px; font-size: 11px; cursor: pointer; text-align: center; }
    .fighter-card.active { border-color: #f43f5e; background: #1f1118; box-shadow: 0 0 10px rgba(244,63,94,0.5); }
    .fighter-card.locked { opacity: 0.4; cursor: not-allowed; border-color: #1f2937; }
    .controls-hint { font-size: 12px; color: #94a3b8; margin-top: 6px; background: #111827; padding: 8px; border-radius: 6px; max-width: 680px; margin-left: auto; margin-right: auto; }
</style>
</head>
<body>

<div class="hud">
    <div class="hp-container">
        <span id="p1-title" style="color: #38bdf8;">SHADOW RYU</span>
        <div class="hp-bar"><div id="p1-hp" class="hp-fill"></div></div>
    </div>
    <div>
        <span id="rank-badge" style="color: #fbbf24; font-size: 16px;">RANK 1</span><br>
        <span id="score-wins" style="font-size: 11px; color: #9ca3af;">Wins: 0</span>
    </div>
    <div class="hp-container">
        <span id="p2-title" style="color: #f43f5e;">BOT ASSASSIN</span>
        <div class="hp-bar"><div id="p2-hp" class="hp-fill" style="background:#ef4444;"></div></div>
    </div>
</div>

<canvas id="gameCanvas" width="680" height="340"></canvas>

<div class="controls-hint">
    <b>CONTROLS:</b> [A/D] Move | [W] Jump | [S] Crouch/Block | [J] Punch | [K] Kick | [L] Special Combo
</div>

<h4 style="margin: 10px 0 5px 0; color: #f3f4f6;">SELECT YOUR SHADOW FIGHTER (10 ROSTER):</h4>
<div class="fighters-grid" id="rosterContainer"></div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let playerRank = 1;
let totalWins = 0;

const roster = [
    { id: 1, name: "Shadow Ryu", style: "Balanced", reqRank: 1, color: "#ffffff", power: 12, speed: 6 },
    { id: 2, name: "Blade Jin", style: "Katana", reqRank: 1, color: "#38bdf8", power: 15, speed: 5 },
    { id: 3, name: "Iron Fist", style: "Brawler", reqRank: 3, color: "#facc15", power: 18, speed: 4 },
    { id: 4, name: "Viper Kicks", style: "Striker", reqRank: 3, color: "#4ade80", power: 14, speed: 7 },
    { id: 5, name: "Cyborg X", style: "Mech", reqRank: 5, color: "#a855f7", power: 20, speed: 5 },
    { id: 6, name: "Ninja Shin", style: "Assassination", reqRank: 5, color: "#f43f5e", power: 16, speed: 8 },
    { id: 7, name: "Titan Brute", style: "Heavy", reqRank: 7, color: "#fb923c", power: 25, speed: 3 },
    { id: 8, name: "Demon Claw", style: "Fierce", reqRank: 8, color: "#dc2626", power: 22, speed: 6 },
    { id: 9, name: "Shadow Reaper", style: "Scythe", reqRank: 9, color: "#e879f9", power: 26, speed: 5 },
    { id: 10, name: "God of War", style: "Supreme", reqRank: 10, color: "#6366f1", power: 32, speed: 8 }
];

let selectedFighter = roster[0];

let p1 = { x: 140, y: 240, vx: 0, vy: 0, hp: 100, isGrounded: true, action: 'idle', facing: 1 };
let p2 = { x: 540, y: 240, vx: 0, vy: 0, hp: 100, isGrounded: true, action: 'idle', facing: -1 };

let keys = {};

function buildRosterUI() {
    const container = document.getElementById('rosterContainer');
    container.innerHTML = '';
    roster.forEach(f => {
        let unlocked = playerRank >= f.reqRank;
        let card = document.createElement('div');
        card.className = `fighter-card ${f.id === selectedFighter.id ? 'active' : ''} ${!unlocked ? 'locked' : ''}`;
        card.innerHTML = `<b>${f.name}</b><br><span style="color:#9ca3af;">${f.style}</span><br><b style="color:${unlocked?'#22c55e':'#f43f5e'}">${unlocked ? 'READY' : 'Rank ' + f.reqRank}</b>`;
        if (unlocked) {
            card.onclick = () => {
                selectedFighter = f;
                document.getElementById('p1-title').innerText = f.name;
                buildRosterUI();
                resetRound();
            };
        }
        container.appendChild(card);
    });
}

window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

function resetRound() {
    p1.hp = 100; p2.hp = 100;
    p1.x = 140; p2.x = 540;
    document.getElementById('p1-hp').style.width = '100%';
    document.getElementById('p2-hp').style.width = '100%';
}

function updateGame() {
    // Player Movement
    if (keys['a']) { p1.vx = -selectedFighter.speed; p1.facing = -1; p1.action = 'walk'; }
    else if (keys['d']) { p1.vx = selectedFighter.speed; p1.facing = 1; p1.action = 'walk'; }
    else { p1.vx = 0; p1.action = 'idle'; }

    if (keys['w'] && p1.isGrounded) { p1.vy = -13; p1.isGrounded = false; }
    if (keys['s']) { p1.action = 'block'; }

    // Attacks
    if ((keys['j'] || keys['k'] || keys['l']) && p1.action !== 'attack') {
        p1.action = 'attack';
        let dmgMultiplier = keys['j'] ? 1 : (keys['k'] ? 1.3 : 1.8);
        setTimeout(() => p1.action = 'idle', 250);

        let dist = Math.abs(p1.x - p2.x);
        if (dist < 65) {
            let hitDmg = selectedFighter.power * dmgMultiplier;
            if (p2.action === 'block') hitDmg *= 0.3; // Block reduces damage
            p2.hp = Math.max(0, p2.hp - hitDmg);
            document.getElementById('p2-hp').style.width = p2.hp + '%';
        }
    }

    // Physics
    p1.x += p1.vx;
    p1.y += p1.vy;
    if (p1.y < 240) { p1.vy += 0.8; } else { p1.y = 240; p1.vy = 0; p1.isGrounded = true; }
    p1.x = Math.max(30, Math.min(650, p1.x));

    // Enemy AI Logic
    if (p2.hp > 0) {
        if (p2.x > p1.x + 50) { p2.x -= 2 + (playerRank * 0.2); p2.facing = -1; }
        else if (p2.x < p1.x - 50) { p2.x += 2 + (playerRank * 0.2); p2.facing = 1; }
        else if (Math.random() < 0.04) {
            // AI Attack
            p1.hp = Math.max(0, p1.hp - (8 + playerRank * 1.5));
            document.getElementById('p1-hp').style.width = p1.hp + '%';
        }
    }

    // Check Win/Loss
    if (p2.hp <= 0) {
        totalWins++;
        if (totalWins % 2 === 0) playerRank++;
        document.getElementById('rank-badge').innerText = 'RANK ' + playerRank;
        document.getElementById('score-wins').innerText = 'Wins: ' + totalWins;
        buildRosterUI();
        alert('FLAWLESS VICTORY! Rank Up Unlocked.');
        resetRound();
    } else if (p1.hp <= 0) {
        alert('KO! Defeated by AI Opponent.');
        resetRound();
    }
}

function drawFighter(f, color, isCustom) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 4;

    // Head
    ctx.beginPath();
    ctx.arc(f.x, f.y - 45, 10, 0, Math.PI * 2);
    ctx.stroke();

    // Torso / Chest
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 35);
    ctx.lineTo(f.x, f.y - 12);
    ctx.stroke();

    // Arms & Action Stance
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 30);
    if (f.action === 'attack') {
        ctx.lineTo(f.x + (f.facing * 35), f.y - 30);
    } else if (f.action === 'block') {
        ctx.lineTo(f.x + (f.facing * 12), f.y - 35);
    } else {
        ctx.lineTo(f.x - 12, f.y - 18);
        ctx.moveTo(f.x, f.y - 30);
        ctx.lineTo(f.x + 12, f.y - 18);
    }
    ctx.stroke();

    // Legs
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 12);
    ctx.lineTo(f.x - 10, f.y);
    ctx.moveTo(f.x, f.y - 12);
    ctx.lineTo(f.x + 10, f.y);
    ctx.stroke();
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Arena Floor
    ctx.fillStyle = '#111827';
    ctx.fillRect(0, 260, 680, 80);
    ctx.fillStyle = '#f43f5e';
    ctx.fillRect(0, 258, 680, 2);

    // Draw Fighters
    drawFighter(p1, selectedFighter.color, true);
    drawFighter(p2, '#ef4444', false);

    updateGame();
    requestAnimationFrame(gameLoop);
}

buildRosterUI();
gameLoop();
</script>
</body>
</html>
"""

components.html(game_html, height=620)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
