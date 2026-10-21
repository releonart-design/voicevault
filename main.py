import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(
    page_title="Shadow Archers: PvP Duels",
    page_icon="🏹",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #e11d48 0%, #be123c 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #1a1a2e; border: 1px dashed #e11d48; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
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
    <div style="text-align:center; background:#1a1a2e; padding:5px; border-radius:6px;">
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🏹 SHADOW ARCHERS: FAST DUELS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Drag & Release to Aim Bow | Clear Ranks to Unlock Legendary Bows & Gear</p>", unsafe_allow_html=True)

# HTML5/JS Archery Engine Code
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #070a12; color: white; font-family: sans-serif; text-align: center; user-select: none; }
    #gameCanvas { background: linear-gradient(to bottom, #0f172a 0%, #020617 100%); border: 2px solid #e11d48; border-radius: 8px; cursor: crosshair; }
    .hud { display: flex; justify-content: space-between; padding: 10px; width: 640px; margin: 0 auto; font-weight: bold; }
    .hp-bar { width: 180px; height: 16px; background: #1e293b; border: 1px solid #475569; border-radius: 4px; overflow: hidden; }
    .hp-fill { height: 100%; width: 100%; background: #22c55e; transition: width 0.2s; }
    .gear-panel { display: flex; justify-content: center; gap: 8px; margin: 10px auto; max-width: 640px; }
    .gear-card { background: #1e293b; border: 2px solid #334155; padding: 6px; border-radius: 6px; width: 110px; font-size: 11px; cursor: pointer; }
    .gear-card.active { border-color: #e11d48; background: #31121f; }
    .gear-card.locked { opacity: 0.4; cursor: not-allowed; }
</style>
</head>
<body>

<div class="hud">
    <div>
        <span>P1 ARCHER</span>
        <div class="hp-bar"><div id="p1-hp" class="hp-fill"></div></div>
    </div>
    <div>
        <span id="rank-txt" style="color: #fbbf24;">RANK 1</span><br>
        <span id="wins-txt" style="font-size: 12px; color: #94a3b8;">Wins: 0</span>
    </div>
    <div>
        <span>ENEMY ARCHER</span>
        <div class="hp-bar"><div id="p2-hp" class="hp-fill" style="background:#ef4444;"></div></div>
    </div>
</div>

<canvas id="gameCanvas" width="640" height="340"></canvas>

<h4 style="margin: 8px 0 4px 0;">SELECT BOW & GEAR:</h4>
<div class="gear-panel" id="gearContainer"></div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let rank = 1;
let wins = 0;

const bows = [
    { id: 1, name: "Wooden Bow", reqRank: 1, dmg: 35, color: "#a16207" },
    { id: 2, name: "Shadow Recurve", reqRank: 1, dmg: 45, color: "#38bdf8" },
    { id: 3, name: "Viper Compound", reqRank: 5, dmg: 60, color: "#22c55e" },
    { id: 4, name: "Inferno Greatbow", reqRank: 5, dmg: 75, color: "#f97316" },
    { id: 5, name: "God-Killer Bow", reqRank: 10, dmg: 100, color: "#a855f7" }
];

let selectedBow = bows[0];

let p1 = { x: 90, y: 220, hp: 100, headY: 190 };
let p2 = { x: 550, y: 220, hp: 100, headY: 190 };

let isAiming = false;
let aimStart = { x: 0, y: 0 };
let aimCurrent = { x: 0, y: 0 };

let arrows = [];

function renderGear() {
    const container = document.getElementById('gearContainer');
    container.innerHTML = '';
    bows.forEach(b => {
        const isUnlocked = rank >= b.reqRank;
        const card = document.createElement('div');
        card.className = `gear-card ${b.id === selectedBow.id ? 'active' : ''} ${!isUnlocked ? 'locked' : ''}`;
        card.innerHTML = `<strong>${b.name}</strong><br><span style="color:#e2e8f0;">Dmg: ${b.dmg}</span><br><b>${isUnlocked ? 'EQUIPPED' : 'Req: Rank ' + b.reqRank}</b>`;
        if (isUnlocked) {
            card.onclick = () => { selectedBow = b; renderGear(); };
        }
        container.appendChild(card);
    });
}

canvas.addEventListener('mousedown', (e) => {
    const rect = canvas.getBoundingClientRect();
    aimStart = { x: e.clientX - rect.left, y: e.clientY - rect.top };
    isAiming = true;
});

canvas.addEventListener('mousemove', (e) => {
    if (!isAiming) return;
    const rect = canvas.getBoundingClientRect();
    aimCurrent = { x: e.clientX - rect.left, y: e.clientY - rect.top };
});

canvas.addEventListener('mouseup', () => {
    if (!isAiming) return;
    isAiming = false;
    
    let dx = aimStart.x - aimCurrent.x;
    let dy = aimStart.y - aimCurrent.y;
    
    // Shoot Arrow
    arrows.push({
        x: p1.x + 15,
        y: p1.y - 15,
        vx: dx * 0.15,
        vy: dy * 0.15,
        owner: 'p1',
        dmg: selectedBow.dmg,
        color: selectedBow.color
    });

    // Enemy Retaliation Attack (AI)
    setTimeout(enemyShoot, 1000);
});

function enemyShoot() {
    if (p2.hp <= 0) return;
    let targetDx = p1.x - p2.x;
    let targetDy = (p1.y - 20) - (p2.y - 20);
    
    // AI Accuracy improves with Rank
    let noise = (Math.random() - 0.5) * (40 / rank);
    
    arrows.push({
        x: p2.x - 15,
        y: p2.y - 15,
        vx: (targetDx * 0.12) + noise,
        vy: (targetDy * 0.12) - 8 + (noise * 0.2),
        owner: 'p2',
        dmg: 30 + (rank * 3),
        color: "#ef4444"
    });
}

function updatePhysics() {
    for (let i = arrows.length - 1; i >= 0; i--) {
        let a = arrows[i];
        a.x += a.vx;
        a.y += a.vy;
        a.vy += 0.25; // Gravity effect

        // Hit P2 (Enemy)
        if (a.owner === 'p1') {
            let distHead = Math.hypot(a.x - p2.x, a.y - p2.headY);
            let distBody = Math.hypot(a.x - p2.x, a.y - p2.y);

            if (distHead < 15) { // Headshot
                p2.hp = Math.max(0, p2.hp - (a.dmg * 1.8));
                document.getElementById('p2-hp').style.width = p2.hp + '%';
                arrows.splice(i, 1);
                checkMatchStatus();
                continue;
            } else if (distBody < 25) { // Body Hit
                p2.hp = Math.max(0, p2.hp - a.dmg);
                document.getElementById('p2-hp').style.width = p2.hp + '%';
                arrows.splice(i, 1);
                checkMatchStatus();
                continue;
            }
        }

        // Hit P1 (Player)
        if (a.owner === 'p2') {
            let distHead = Math.hypot(a.x - p1.x, a.y - p1.headY);
            let distBody = Math.hypot(a.x - p1.x, a.y - p1.y);

            if (distHead < 15 || distBody < 25) {
                let hitDmg = distHead < 15 ? a.dmg * 1.5 : a.dmg;
                p1.hp = Math.max(0, p1.hp - hitDmg);
                document.getElementById('p1-hp').style.width = p1.hp + '%';
                arrows.splice(i, 1);
                checkMatchStatus();
                continue;
            }
        }

        // Remove ground hit arrows
        if (a.y > 280) arrows.splice(i, 1);
    }
}

function checkMatchStatus() {
    if (p2.hp <= 0) {
        wins++;
        if (wins % 2 === 0) rank++;
        document.getElementById('rank-txt').innerText = 'RANK ' + rank;
        document.getElementById('wins-txt').innerText = 'Wins: ' + wins;
        renderGear();
        alert('HEADSHOT / VICTORY! Rank Up Progress Saved.');
        resetMatch();
    } else if (p1.hp <= 0) {
        alert('DEFEATED! Try Again Archer.');
        resetMatch();
    }
}

function resetMatch() {
    p1.hp = 100; p2.hp = 100;
    document.getElementById('p1-hp').style.width = '100%';
    document.getElementById('p2-hp').style.width = '100%';
    arrows = [];
}

function drawStickmanArcher(x, y, isEnemy, bowColor) {
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 3;

    // Head
    ctx.beginPath();
    ctx.arc(x, y - 30, 9, 0, Math.PI * 2);
    ctx.stroke();

    // Body
    ctx.beginPath();
    ctx.moveTo(x, y - 21);
    ctx.lineTo(x, y);
    ctx.stroke();

    // Legs
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x - 8, y + 15);
    ctx.moveTo(x, y);
    ctx.lineTo(x + 8, y + 15);
    ctx.stroke();

    // Bow
    ctx.strokeStyle = bowColor;
    ctx.beginPath();
    let dir = isEnemy ? -1 : 1;
    ctx.arc(x + (dir * 12), y - 15, 16, -Math.PI / 2, Math.PI / 2);
    ctx.stroke();
}

function drawLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Ground Platform
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 250, 640, 90);
    ctx.fillStyle = '#e11d48';
    ctx.fillRect(0, 248, 640, 2);

    // Draw Stickmen
    drawStickmanArcher(p1.x, p1.y, false, selectedBow.color);
    drawStickmanArcher(p2.x, p2.y, true, "#ef4444");

    // Trajectory Aiming Line
    if (isAiming) {
        ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(p1.x + 15, p1.y - 15);
        ctx.lineTo(p1.x + 15 + (aimStart.x - aimCurrent.x), p1.y - 15 + (aimStart.y - aimCurrent.y));
        ctx.stroke();
        ctx.setLineDash([]);
    }

    // Draw Arrows
    arrows.forEach(a => {
        ctx.strokeStyle = a.color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(a.x - (a.vx * 2), a.y - (a.vy * 2));
        ctx.stroke();
    });

    updatePhysics();
    requestAnimationFrame(drawLoop);
}

renderGear();
drawLoop();
</script>
</body>
</html>
"""

components.html(game_html, height=600)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
