import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(
    page_title="Shadow Combat: Mortal Arena",
    page_icon="⚔️",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #050508; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #dc2626 0%, #7f1d1d 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #111118; border: 1px dashed #dc2626; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
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
    <div style="text-align:center; background:#111118; padding:5px; border-radius:6px;">
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚔️ SHADOW COMBAT: MORTAL ARENA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Mature Hardcore Fighting Game | Master Combos, Blocks & Brutal Finishers</p>", unsafe_allow_html=True)

# HTML5/JS Hardcore Fighting Game Engine
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #050508; color: white; font-family: 'Segoe UI', Tahoma, sans-serif; text-align: center; user-select: none; }
    #gameCanvas { background: radial-gradient(circle, #1a1a2e 0%, #050508 100%); border: 3px solid #dc2626; border-radius: 10px; box-shadow: 0 0 30px rgba(220,38,38,0.4); touch-action: none; }
    .hud { display: flex; justify-content: space-between; padding: 10px; width: 100%; max-width: 420px; margin: 0 auto; font-weight: bold; background: #111118; border-radius: 8px; margin-bottom: 6px; }
    .hp-box { width: 160px; }
    .hp-bar { width: 100%; height: 16px; background: #222; border: 1px solid #444; border-radius: 4px; overflow: hidden; }
    .hp-fill { height: 100%; width: 100%; background: #22c55e; transition: width 0.1s; }
    .fighters-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; margin: 8px auto; max-width: 420px; }
    .fighter-card { background: #111118; border: 1px solid #333; padding: 6px 2px; border-radius: 6px; font-size: 10px; cursor: pointer; text-align: center; }
    .fighter-card.active { border-color: #dc2626; background: #2a1215; }
    .fighter-card.locked { opacity: 0.3; cursor: not-allowed; }
    .touch-pad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; max-width: 420px; margin: 8px auto; }
    .action-btn { background: #1e1e2d; border: 2px solid #dc2626; color: white; padding: 14px 0; font-size: 14px; font-weight: bold; border-radius: 8px; cursor: pointer; }
    .action-btn:active { background: #dc2626; }
</style>
</head>
<body>

<div class="hud">
    <div class="hp-box">
        <span id="p1-name" style="color: #38bdf8; font-size: 12px;">SHADOW BRAWLER</span>
        <div class="hp-bar"><div id="p1-hp" class="hp-fill"></div></div>
    </div>
    <div>
        <span id="rank-txt" style="color: #facc15; font-size: 14px;">RANK 1</span><br>
        <span id="wins-txt" style="font-size: 10px; color: #9ca3af;">Wins: 0</span>
    </div>
    <div class="hp-box">
        <span id="p2-name" style="color: #ef4444; font-size: 12px;">NETHER BOT</span>
        <div class="hp-bar"><div id="p2-hp" class="hp-fill" style="background:#ef4444;"></div></div>
    </div>
</div>

<canvas id="gameCanvas" width="420" height="260"></canvas>

<div class="fighters-grid" id="rosterUI"></div>

<div class="touch-pad">
    <button class="action-btn" onclick="playerMove(-1)">◄ MOVE</button>
    <button class="action-btn" onclick="playerJump()">▲ JUMP</button>
    <button class="action-btn" onclick="playerMove(1)">MOVE ►</button>
    <button class="action-btn" onclick="playerAttack('punch')" style="border-color:#38bdf8;">PUNCH</button>
    <button class="action-btn" onclick="playerAttack('kick')" style="border-color:#facc15;">KICK</button>
    <button class="action-btn" onclick="playerSpecial()" style="border-color:#a855f7;">SPECIAL</button>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let playerRank = 1;
let totalWins = 0;

const roster = [
    { id: 1, name: "Shadow Brawler", reqRank: 1, color: "#ffffff", power: 12 },
    { id: 2, name: "Blade Assassin", reqRank: 1, color: "#38bdf8", power: 15 },
    { id: 3, name: "Iron Monolith", reqRank: 3, color: "#facc15", power: 18 },
    { id: 4, name: "Viper Striker", reqRank: 3, color: "#4ade80", power: 16 },
    { id: 5, name: "Cyber Ninja", reqRank: 5, color: "#a855f7", power: 22 },
    { id: 6, name: "Hellfire Demon", reqRank: 5, color: "#f43f5e", power: 24 },
    { id: 7, name: "Titan Berserker", reqRank: 7, color: "#fb923c", power: 28 },
    { id: 8, name: "Dark Reaper", reqRank: 8, color: "#e879f9", power: 30 },
    { id: 9, name: "Chaos Sovereign", reqRank: 9, color: "#dc2626", power: 34 },
    { id: 10, name: "God of Darkness", reqRank: 10, color: "#6366f1", power: 40 }
];

let selectedFighter = roster[0];

let p1 = { x: 100, y: 180, vx: 0, vy: 0, hp: 100, action: 'idle', isGrounded: true };
let p2 = { x: 320, y: 180, vx: 0, vy: 0, hp: 100, action: 'idle' };

let particles = [];

function buildRoster() {
    const container = document.getElementById('rosterUI');
    container.innerHTML = '';
    roster.forEach(f => {
        let unlocked = playerRank >= f.reqRank;
        let card = document.createElement('div');
        card.className = `fighter-card ${f.id === selectedFighter.id ? 'active' : ''} ${!unlocked ? 'locked' : ''}`;
        card.innerHTML = `<b>${f.name.split(' ')[0]}</b><br><b style="color:${unlocked?'#22c55e':'#dc2626'}">${unlocked ? 'OPEN' : 'R' + f.reqRank}</b>`;
        if (unlocked) {
            card.onclick = () => {
                selectedFighter = f;
                document.getElementById('p1-name').innerText = f.name;
                buildRoster();
                resetMatch();
            };
        }
        container.appendChild(card);
    });
}

function playerMove(dir) {
    p1.x = Math.max(30, Math.min(390, p1.x + (dir * 25)));
}

function playerJump() {
    if (p1.isGrounded) {
        p1.vy = -12;
        p1.isGrounded = false;
    }
}

function playerAttack(type) {
    p1.action = type;
    setTimeout(() => p1.action = 'idle', 200);

    let dist = Math.abs(p1.x - p2.x);
    if (dist < 55) {
        let dmg = selectedFighter.power * (type === 'kick' ? 1.3 : 1);
        p2.hp = Math.max(0, p2.hp - dmg);
        document.getElementById('p2-hp').style.width = p2.hp + '%';
        spawnSparks(p2.x, p2.y - 30);
    }
}

function playerSpecial() {
    p1.action = 'special';
    setTimeout(() => p1.action = 'idle', 300);

    let dist = Math.abs(p1.x - p2.x);
    if (dist < 80) {
        let dmg = selectedFighter.power * 2;
        p2.hp = Math.max(0, p2.hp - dmg);
        document.getElementById('p2-hp').style.width = p2.hp + '%';
        spawnSparks(p2.x, p2.y - 30);
        spawnSparks(p2.x + 10, p2.y - 20);
    }
}

function spawnSparks(x, y) {
    for (let i = 0; i < 8; i++) {
        particles.push({
            x: x, y: y,
            vx: (Math.random() - 0.5) * 8,
            vy: (Math.random() - 0.5) * 8,
            life: 15,
            color: '#facc15'
        });
    }
}

function updateAI() {
    if (p2.hp > 0) {
        if (p2.x > p1.x + 40) p2.x -= 1.5 + (playerRank * 0.2);
        else if (p2.x < p1.x - 40) p2.x += 1.5 + (playerRank * 0.2);
        else if (Math.random() < 0.03) {
            p1.hp = Math.max(0, p1.hp - (6 + playerRank * 1.2));
            document.getElementById('p1-hp').style.width = p1.hp + '%';
            spawnSparks(p1.x, p1.y - 30);
        }
    }

    // Check Win/Loss
    if (p2.hp <= 0) {
        totalWins++;
        if (totalWins % 2 === 0) playerRank++;
        document.getElementById('rank-txt').innerText = 'RANK ' + playerRank;
        document.getElementById('wins-txt').innerText = 'Wins: ' + totalWins;
        buildRoster();
        alert('BRUTAL VICTORY! Rank Up Unlocked.');
        resetMatch();
    } else if (p1.hp <= 0) {
        alert('FATALITY! You Were Defeated.');
        resetMatch();
    }
}

function resetMatch() {
    p1.hp = 100; p2.hp = 100;
    p1.x = 100; p2.x = 320;
    document.getElementById('p1-hp').style.width = '100%';
    document.getElementById('p2-hp').style.width = '100%';
}

function drawFighter(f, color, isP1) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;

    // Head
    ctx.beginPath();
    ctx.arc(f.x, f.y - 35, 8, 0, Math.PI * 2);
    ctx.stroke();

    // Torso
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 27);
    ctx.lineTo(f.x, f.y - 10);
    ctx.stroke();

    // Arms & Attack action
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 22);
    if (f.action === 'punch') {
        ctx.lineTo(f.x + (isP1 ? 25 : -25), f.y - 22);
    } else if (f.action === 'special') {
        ctx.lineTo(f.x + (isP1 ? 35 : -35), f.y - 25);
        ctx.strokeStyle = '#a855f7';
    } else {
        ctx.lineTo(f.x - 10, f.y - 12);
        ctx.moveTo(f.x, f.y - 22);
        ctx.lineTo(f.x + 10, f.y - 12);
    }
    ctx.stroke();

    // Legs
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.moveTo(f.x, f.y - 10);
    ctx.lineTo(f.x - 8, f.y);
    ctx.moveTo(f.x, f.y - 10);
    ctx.lineTo(f.x + 8, f.y);
    ctx.stroke();
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Arena Floor
    ctx.fillStyle = '#111118';
    ctx.fillRect(0, 200, 420, 60);
    ctx.fillStyle = '#dc2626';
    ctx.fillRect(0, 198, 420, 2);

    // Gravity for P1 Jump
    p1.y += p1.vy;
    if (p1.y < 180) { p1.vy += 0.8; } else { p1.y = 180; p1.vy = 0; p1.isGrounded = true; }

    drawFighter(p1, selectedFighter.color, true);
    drawFighter(p2, '#ef4444', false);

    // Draw Hit Sparks Particles
    for (let i = particles.length - 1; i >= 0; i--) {
        let pt = particles[i];
        pt.x += pt.vx;
        pt.y += pt.vy;
        pt.life--;
        ctx.fillStyle = pt.color;
        ctx.fillRect(pt.x, pt.y, 3, 3);
        if (pt.life <= 0) particles.splice(i, 1);
    }

    updateAI();
    requestAnimationFrame(gameLoop);
}

buildRoster();
gameLoop();
</script>
</body>
</html>
"""

components.html(game_html, height=610)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
