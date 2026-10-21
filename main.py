import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(
    page_title="Subway Surfers: 3D Endless Runner",
    page_icon="🛹",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #1a1a2e; border: 1px dashed #f59e0b; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# Native Adsterra Banners
def render_banner_ad(position="top"):
    st.markdown(f"""
    <div class="ad-banner">
        <p style="color: #9ca3af; font-size: 10px; margin: 0; text-transform: uppercase;">SPONSORED AD ({position})</p>
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🛹 SUBWAY RUNNER 3D</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Dodge Trains, Collect Coins & Escape the Inspector!</p>", unsafe_allow_html=True)

# HTML5/JS 3D Perspective Subway Surfers Engine
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #050b14; color: white; font-family: sans-serif; text-align: center; user-select: none; }
    #gameCanvas { background: linear-gradient(to bottom, #1e293b 0%, #020617 100%); border: 3px solid #f59e0b; border-radius: 12px; box-shadow: 0 0 30px rgba(245,158,11,0.4); }
    .hud { display: flex; justify-content: space-around; padding: 10px; width: 640px; margin: 0 auto; font-size: 16px; font-weight: bold; background: #111827; border-radius: 8px; margin-bottom: 8px; }
    .controls-hint { font-size: 13px; color: #9ca3af; margin-top: 8px; background: #111827; padding: 8px; border-radius: 6px; max-width: 640px; margin-left: auto; margin-right: auto; }
</style>
</head>
<body>

<div class="hud">
    <div>🪙 Coins: <span id="coinCount" style="color: #facc15;">0</span></div>
    <div>🏆 Score: <span id="scoreCount" style="color: #38bdf8;">0</span></div>
    <div>⚡ Speed: <span id="speedCount" style="color: #f43f5e;">1.0x</span></div>
</div>

<canvas id="gameCanvas" width="640" height="380"></canvas>

<div class="controls-hint">
    <b>CONTROLS:</b> [A / D] or [LEFT / RIGHT ARROWS] Switch Lanes | [W / UP] Jump Over Barriers
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let score = 0;
let coins = 0;
let gameSpeed = 5;
let isGameOver = false;

// 3 Lanes: -1 (Left), 0 (Middle), 1 (Right)
let playerLane = 0;
let playerY = 0;
let isJumping = false;
let jumpVelocity = 0;

let obstacles = [];
let collectibles = [];

// Input Handling
window.addEventListener('keydown', (e) => {
    if (isGameOver) {
        if (e.key === 'r' || e.key === 'R') resetGame();
        return;
    }
    if ((e.key === 'a' || e.key === 'ArrowLeft') && playerLane > -1) {
        playerLane--;
    }
    if ((e.key === 'd' || e.key === 'ArrowRight') && playerLane < 1) {
        playerLane++;
    }
    if ((e.key === 'w' || e.key === 'ArrowUp') && !isJumping) {
        isJumping = true;
        jumpVelocity = -12;
    }
});

function spawnObstacle() {
    let lane = Math.floor(Math.random() * 3) - 1;
    let type = Math.random() > 0.4 ? 'train' : 'barrier';
    obstacles.push({ lane: lane, z: 400, type: type });
}

function spawnCollectible() {
    let lane = Math.floor(Math.random() * 3) - 1;
    collectibles.push({ lane: lane, z: 400 });
}

let spawnTimer = 0;

function update() {
    if (isGameOver) return;

    score += 1;
    gameSpeed = 5 + Math.floor(score / 300);

    // Jump Physics
    if (isJumping) {
        playerY += jumpVelocity;
        jumpVelocity += 0.8;
        if (playerY >= 0) {
            playerY = 0;
            isJumping = false;
        }
    }

    spawnTimer++;
    if (spawnTimer % 60 === 0) spawnObstacle();
    if (spawnTimer % 40 === 0) spawnCollectible();

    // Update Obstacles
    for (let i = obstacles.length - 1; i >= 0; i--) {
        let obs = obstacles[i];
        obs.z -= gameSpeed;

        // Collision Check
        if (obs.z < 30 && obs.z > 0 && obs.lane === playerLane) {
            if (obs.type === 'barrier' && playerY > -25) {
                isGameOver = true;
            } else if (obs.type === 'train') {
                isGameOver = true;
            }
        }

        if (obs.z < -20) obstacles.splice(i, 1);
    }

    // Update Coins
    for (let i = collectibles.length - 1; i >= 0; i--) {
        let c = collectibles[i];
        c.z -= gameSpeed;

        if (c.z < 30 && c.z > 0 && c.lane === playerLane && playerY > -30) {
            coins += 10;
            collectibles.splice(i, 1);
        }

        if (c.z < -20) collectibles.splice(i, 1);
    }

    document.getElementById('coinCount').innerText = coins;
    document.getElementById('scoreCount').innerText = score;
    document.getElementById('speedCount').innerText = (gameSpeed / 5).toFixed(1) + 'x';
}

function draw3D() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Perspective Sky & Ground
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, 190);
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 190, canvas.width, 190);

    // 3 Subway Tracks (Perspective Lines)
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 4;
    
    // Center vanishing point
    let cx = canvas.width / 2;
    let cy = 190;

    // Track 1 (Left)
    ctx.beginPath(); ctx.moveTo(cx - 80, 380); ctx.lineTo(cx - 30, cy); ctx.stroke();
    // Track 2 (Right)
    ctx.beginPath(); ctx.moveTo(cx + 80, 380); ctx.lineTo(cx + 30, cy); ctx.stroke();

    // Draw Collectibles (Coins)
    collectibles.forEach(c => {
        let scale = 50 / (c.z + 50);
        let x = cx + c.lane * 70 * scale * 2 - (scale * 10);
        let y = cy + (c.z * 0.45) - 15;
        
        ctx.fillStyle = '#facc15';
        ctx.beginPath();
        ctx.arc(x, y, 10 * scale * 3, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ca8a04';
        ctx.stroke();
    });

    // Draw Obstacles (Trains & Barriers)
    obstacles.forEach(obs => {
        let scale = 50 / (obs.z + 50);
        let x = cx + obs.lane * 70 * scale * 2 - (scale * 25);
        let y = cy + (obs.z * 0.45) - (scale * 40);
        let width = 60 * scale * 3;
        let height = 50 * scale * 3;

        if (obs.type === 'train') {
            ctx.fillStyle = '#ef4444';
            ctx.fillRect(x - width/2, y - height, width, height);
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(x - width/4, y - height + 10, width/2, 15); // Train Window
        } else {
            ctx.fillStyle = '#f97316';
            ctx.fillRect(x - width/2, y - height/2, width, 15); // Barrier Bar
        }
    });

    // Draw Player (Surfer)
    let pX = cx + playerLane * 90 + (playerY * 0.2);
    let pY = 320 + playerY;

    // Surfer Body Animation
    ctx.fillStyle = '#38bdf8';
    ctx.fillRect(pX - 12, pY - 45, 24, 35); // Torso
    ctx.fillStyle = '#facc15';
    ctx.beginPath(); ctx.arc(pX, pY - 55, 10, 0, Math.PI * 2); ctx.fill(); // Head
    ctx.fillStyle = '#22c55e';
    ctx.fillRect(pX - 16, pY, 32, 8); // Hoverboard

    if (isGameOver) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.85)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 28px sans-serif';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '16px sans-serif';
        ctx.fillStyle = '#facc15';
        ctx.fillText('Press "R" to Restart', canvas.width / 2, canvas.height / 2 + 20);
    }
}

function resetGame() {
    score = 0;
    coins = 0;
    gameSpeed = 5;
    isGameOver = false;
    obstacles = [];
    collectibles = [];
    playerLane = 0;
    playerY = 0;
}

function loop() {
    update();
    draw3D();
    requestAnimationFrame(loop);
}

loop();
</script>
</body>
</html>
"""

components.html(game_html, height=620)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
