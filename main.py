import streamlit as st
import streamlit.components.v1 as components
import json

# Page Setup
st.set_page_config(
    page_title="Shadow Stick Fighter - Arcade 2D",
    page_icon="⚔️",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #f0f6fc; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #238636 0%, #2ea043 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #161b22; border: 1px dashed #30363d; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #8b949e; font-size: 10px; margin: 0; text-transform: uppercase;">SPONSORED ARENA BANNER ({position})</p>
    </div>
    """, unsafe_allow_html=True)
    components.html("""
    <div style="text-align:center; background:#161b22; padding:5px; border-radius:6px;">
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚔️ SHADOW STICK FIGHTER 2D</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Tekken-Style Shadow Arena | Win Fights to Level Up Rank & Unlock Warriors</p>", unsafe_allow_html=True)

# HTML5/JS 2D Shadow Fighting Engine
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #050505; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; }
    #gameCanvas { background: radial-gradient(circle, #222 0%, #000 100%); border: 2px solid #444; border-radius: 8px; box-shadow: 0 0 20px rgba(0,0,0,0.8); }
    .hud { display: flex; justify-content: space-between; padding: 10px; width: 640px; margin: 0 auto; font-weight: bold; }
    .hp-bar { width: 220px; height: 18px; background: #333; border: 2px solid #555; border-radius: 4px; overflow: hidden; }
    .hp-fill { height: 100%; width: 100%; background: #22c55e; transition: width 0.1s; }
    .controls-panel { margin-top: 10px; font-size: 13px; color: #aaa; }
    .btn-act { background: #ff4757; color: white; border: none; padding: 10px 15px; font-weight: bold; border-radius: 5px; cursor: pointer; margin: 5px; }
    .char-select { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin: 10px auto; max-width: 640px; }
    .char-card { background: #1e1e1e; border: 2px solid #444; padding: 8px; border-radius: 6px; width: 110px; cursor: pointer; font-size: 11px; }
    .char-card.active { border-color: #22c55e; background: #2a3b2c; }
    .char-card.locked { opacity: 0.5; cursor: not-allowed; border-color: #ff4757; }
</style>
</head>
<body>

<div class="hud">
    <div>
        <span id="p1-name">Shadow Brawler</span> (P1)
        <div class="hp-bar"><div id="p1-hp" class="hp-fill"></div></div>
    </div>
    <div>
        <h3 style="margin:0; color:#e11d48;" id="rank-display">RANK 1</h3>
        <span id="score-display">Wins: 0</span>
    </div>
    <div>
        <span id="p2-name">Shadow Bot</span> (CPU)
        <div class="hp-bar"><div id="p2-hp" class="hp-fill" style="background:#ef4444;"></div></div>
    </div>
</div>

<canvas id="gameCanvas" width="640" height="320"></canvas>

<div class="controls-panel">
    <strong>CONTROLS:</strong> [A / D] Move Left/Right | [W] Jump | [J] Punch Attack | [K] Kick Attack | [L] Special Skill
</div>

<h4 style="margin: 10px 0 5px 0;">CHOOSE YOUR SHADOW WARRIOR:</h4>
<div class="char-select" id="charContainer"></div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let playerRank = 1;
let totalWins = 0;

const characters = [
    { id: 1, name: "Brawler", weapon: "Fists", reqRank: 1, color: "#ffffff", range: 35, speed: 5, power: 10 },
    { id: 2, name: "Blade Shinobi", weapon: "Katana", reqRank: 1, color: "#38bdf8", range: 50, speed: 6, power: 12 },
    { id: 3, name: "Spear Master", weapon: "Spear", reqRank: 5, color: "#facc15", range: 70, speed: 4, power: 15 },
    { id: 4, name: "Cyber Cyborg", weapon: "Laser", reqRank: 5, color: "#4ade80", range: 60, speed: 5, power: 16 },
    { id: 5, name: "Shadow Ninja", weapon: "Teleport", reqRank: 5, color: "#c084fc", range: 45, speed: 8, power: 14 },
    { id: 6, name: "Dagger Assassin", weapon: "Daggers", reqRank: 10, color: "#f43f5e", range: 30, speed: 9, power: 18 },
    { id: 7, name: "Titan General", weapon: "Greatsword", reqRank: 10, color: "#fb923c", range: 65, speed: 3, power: 25 },
    { id: 8, name: "Shadow Reaper", weapon: "Scythe", reqRank: 10, color: "#e879f9", range: 75, speed: 5, power: 22 },
    { id: 9, name: "Demon King", weapon: "Chaos Blade", reqRank: 10, color: "#dc2626", range: 55, speed: 7, power: 24 },
    { id: 10, name: "God of Shadows", weapon: "Ultimate Aura", reqRank: 10, color: "#6366f1", range: 80, speed: 8, power: 30 }
];

let selectedChar = characters[0];

let p1 = { x: 100, y: 220, vx: 0, vy: 0, hp: 100, isGrounded: true, attacking: false, attackType: '', facing: 1 };
let p2 = { x: 500, y: 220, vx: 0, vy: 0, hp: 100, isGrounded: true, attacking: false, facing: -1 };

let keys = {};

function renderCharacterList() {
    const container = document.getElementById('charContainer');
    container.innerHTML = '';
    characters.forEach(c => {
        const isUnlocked = playerRank >= c.reqRank;
        const card = document.createElement('div');
        card.className = `char-card ${c.id === selectedChar.id ? 'active' : ''} ${!isUnlocked ? 'locked' : ''}`;
        card.innerHTML = `<strong>${c.name}</strong><br><span style="color:#aaa;">${c.weapon}</span><br><b>${isUnlocked ? 'UNLOCKED' : 'Req: Rank ' + c.reqRank}</b>`;
        if(isUnlocked) {
            card.onclick = () => { selectedChar = c; renderCharacterList(); document.getElementById('p1-name').innerText = c.name; resetBattle(); };
        }
        container.appendChild(card);
    });
}

window.addEventListener('keydown', e => keys[e.key.toLowerCase()] = true);
window.addEventListener('keyup', e => keys[e.key.toLowerCase()] = false);

function resetBattle() {
    p1.hp = 100; p2.hp = 100;
    p1.x = 100; p2.x = 500;
    p1.vy = 0; p2.vy = 0;
    document.getElementById('p1-hp').style.width = '100%';
    document.getElementById('p2-hp').style.width = '100%';
}

function update() {
    // Player Controls
    if (keys['a']) { p1.vx = -selectedChar.speed; p1.facing = -1; }
    else if (keys['d']) { p1.vx = selectedChar.speed; p1.facing = 1; }
    else { p1.vx = 0; }

    if (keys['w'] && p1.isGrounded) { p1.vy = -12; p1.isGrounded = false; }

    if ((keys['j'] || keys['k'] || keys['l']) && !p1.attacking) {
        p1.attacking = true;
        p1.attackType = keys['j'] ? 'Punch' : (keys['k'] ? 'Kick' : 'Special');
        setTimeout(() => p1.attacking = false, 250);
        
        // Hit Detection
        let dist = Math.abs((p1.x + p1.facing * selectedChar.range) - p2.x);
        if (dist < 50 && Math.abs(p1.y - p2.y) < 40) {
            let dmg = selectedChar.power + (p1.attackType === 'Special' ? 8 : 0);
            p2.hp = Math.max(0, p2.hp - dmg);
            document.getElementById('p2-hp').style.width = p2.hp + '%';
        }
    }

    // Physics
    p1.x += p1.vx;
    p1.y += p1.vy;
    if (p1.y < 220) { p1.vy += 0.8; } else { p1.y = 220; p1.vy = 0; p1.isGrounded = true; }
    p1.x = Math.max(30, Math.min(610, p1.x));

    // Simple AI Enemy Engine
    if (p2.hp > 0) {
        if (p2.x > p1.x + 40) p2.x -= 2;
        else if (p2.x < p1.x - 40) p2.x += 2;
        
        if (Math.abs(p2.x - p1.x) < 50 && Math.random() < 0.03) {
            p2.attacking = true;
            p1.hp = Math.max(0, p1.hp - (6 + playerRank));
            document.getElementById('p1-hp').style.width = p1.hp + '%';
            setTimeout(() => p2.attacking = false, 200);
        }
    }

    // Win/Lose Conditions
    if (p2.hp <= 0) {
        totalWins++;
        if (totalWins % 2 === 0) playerRank++;
        document.getElementById('rank-display').innerText = 'RANK ' + playerRank;
        document.getElementById('score-display').innerText = 'Wins: ' + totalWins;
        renderCharacterList();
        alert('VICTORY! Rank Up Progress Saved.');
        resetBattle();
    } else if (p1.hp <= 0) {
        alert('DEFEATED! Try Again Shadow Warrior.');
        resetBattle();
    }
}

function drawStickman(x, y, color, facing, isAttacking, weaponName) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 4;

    // Head
    ctx.beginPath();
    ctx.arc(x, y - 40, 10, 0, Math.PI * 2);
    ctx.stroke();

    // Body
    ctx.beginPath();
    ctx.moveTo(x, y - 30);
    ctx.lineTo(x, y - 10);
    ctx.stroke();

    // Legs
    ctx.beginPath();
    ctx.moveTo(x, y - 10);
    ctx.lineTo(x - 10, y);
    ctx.moveTo(x, y - 10);
    ctx.lineTo(x + 10, y);
    ctx.stroke();

    // Arms & Weapon Attack Animation
    ctx.beginPath();
    ctx.moveTo(x, y - 25);
    if (isAttacking) {
        ctx.lineTo(x + facing * 30, y - 25);
        // Weapon Draw
        ctx.strokeStyle = "#ffffff";
        ctx.moveTo(x + facing * 25, y - 25);
        ctx.lineTo(x + facing * 50, y - 25);
    } else {
        ctx.lineTo(x - 10, y - 15);
        ctx.moveTo(x, y - 25);
        ctx.lineTo(x + 10, y - 15);
    }
    ctx.stroke();
}

function loop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Arena Floor
    ctx.fillStyle = '#333';
    ctx.fillRect(0, 240, 640, 80);
    ctx.fillStyle = '#22c55e';
    ctx.fillRect(0, 238, 640, 2);

    // Draw Fighters
    drawStickman(p1.x, p1.y, selectedChar.color, p1.facing, p1.attacking, selectedChar.weapon);
    drawStickman(p2.x, p2.y, "#ef4444", p2.facing, p2.attacking, "Hand");

    update();
    requestAnimationFrame(loop);
}

renderCharacterList();
loop();
</script>
</body>
</html>
"""

components.html(game_html, height=580)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
