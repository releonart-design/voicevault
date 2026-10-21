import streamlit as st
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(
    page_title="Gravity Golf: Space Delivery",
    page_icon="🪐",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #030712; color: #f3f4f6; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); color: white; padding: 12px; }
    .ad-banner { background-color: #111827; border: 1px dashed #8b5cf6; border-radius: 8px; padding: 5px; text-align: center; margin: 10px 0; }
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

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🪐 GRAVITY GOLF: SPACE DELIVERY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Tap Screen to Pulse Gravity | Swing Package Past Asteroids to Reach the Portal!</p>", unsafe_allow_html=True)

# HTML5/JS Physics Game Engine (Touch & Tap)
game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; background: #030712; color: white; font-family: sans-serif; text-align: center; user-select: none; }
    #gameCanvas { background: radial-gradient(circle, #0f172a 0%, #030712 100%); border: 3px solid #8b5cf6; border-radius: 12px; box-shadow: 0 0 25px rgba(139,92,246,0.4); touch-action: none; }
    .hud { display: flex; justify-content: space-around; padding: 10px; width: 100%; max-width: 400px; margin: 0 auto; font-size: 16px; font-weight: bold; background: #1f2937; border-radius: 8px; margin-bottom: 8px; }
    .tap-btn { width: 100%; max-width: 400px; background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); color: white; border: none; padding: 15px; font-size: 18px; font-weight: bold; border-radius: 10px; cursor: pointer; margin-top: 10px; box-shadow: 0 4px 15px rgba(139,92,246,0.4); }
</style>
</head>
<body>

<div class="hud">
    <div>📦 Level: <span id="lvlCount" style="color: #a78bfa;">1</span></div>
    <div>⭐ Score: <span id="scoreCount" style="color: #facc15;">0</span></div>
</div>

<canvas id="gameCanvas" width="380" height="420"></canvas>

<div>
    <button class="tap-btn" onclick="applyGravityPulse()">🔮 PULSE GRAVITY / BOOST</button>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let level = 1;
let score = 0;
let isGameOver = false;
let levelWon = false;

// Package (Space Cargo)
let pkg = {
    x: 50,
    y: 350,
    vx: 2,
    vy: -3,
    radius: 10
};

// Target Portal
let portal = { x: 320, y: 80, radius: 22 };

// Planets with Gravitational Pull
let planets = [
    { x: 190, y: 220, radius: 35, pull: 0.18, color: '#3b82f6' },
    { x: 100, y: 120, radius: 25, pull: 0.15, color: '#ec4899' },
    { x: 280, y: 280, radius: 30, pull: 0.16, color: '#10b981' }
];

// Floating Asteroids
let asteroids = [
    { x: 150, y: 180, radius: 12, vx: 1, vy: -0.5 },
    { x: 240, y: 150, radius: 14, vx: -0.8, vy: 1 }
];

// Touch or Click Anywhere on Canvas to Pulse Gravity
canvas.addEventListener('pointerdown', () => {
    applyGravityPulse();
});

function applyGravityPulse() {
    if (isGameOver || levelWon) {
        resetGame();
        return;
    }
    // Give package a boost towards center/upward
    pkg.vx += (Math.random() - 0.5) * 4;
    pkg.vy -= 4;
}

function updatePhysics() {
    if (isGameOver || levelWon) return;

    // Apply Planet Gravity Pull
    planets.forEach(p => {
        let dx = p.x - pkg.x;
        let dy = p.y - pkg.y;
        let dist = Math.hypot(dx, dy);
        if (dist > 5) {
            let force = p.pull * (100 / (dist + 20));
            pkg.vx += (dx / dist) * force;
            pkg.vy += (dy / dist) * force;
        }
    });

    // Move Package
    pkg.x += pkg.vx;
    pkg.y += pkg.vy;

    // Air friction / space drag
    pkg.vx *= 0.99;
    pkg.vy *= 0.99;

    // Move Asteroids
    asteroids.forEach(a => {
        a.x += a.vx;
        a.y += a.vy;
        if (a.x < 20 || a.x > canvas.width - 20) a.vx *= -1;
        if (a.y < 20 || a.y > canvas.height - 20) a.vy *= -1;

        // Collision with Package
        let dist = Math.hypot(pkg.x - a.x, pkg.y - a.y);
        if (dist < pkg.radius + a.radius) {
            isGameOver = true;
        }
    });

    // Wall Bounds Collision
    if (pkg.x < 10 || pkg.x > canvas.width - 10 || pkg.y < 10 || pkg.y > canvas.height - 10) {
        isGameOver = true;
    }

    // Portal Reached Check
    let portalDist = Math.hypot(pkg.x - portal.x, pkg.y - portal.y);
    if (portalDist < pkg.radius + portal.radius) {
        levelWon = true;
        score += 100;
        level++;
    }
}

function drawGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw Space Background Stars
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(50, 50, 2, 2);
    ctx.fillRect(120, 300, 2, 2);
    ctx.fillRect(300, 100, 2, 2);
    ctx.fillRect(220, 380, 2, 2);

    // Draw Planets
    planets.forEach(p => {
        // Gravity Field Ring
        ctx.strokeStyle = p.color + '44';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius * 2, 0, Math.PI * 2);
        ctx.stroke();

        // Planet Core
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
    });

    // Draw Asteroids
    asteroids.forEach(a => {
        ctx.fillStyle = '#94a3b8';
        ctx.beginPath();
        ctx.arc(a.x, a.y, a.radius, 0, Math.PI * 2);
        ctx.fill();
    });

    // Draw Portal Goal
    ctx.strokeStyle = '#facc15';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.arc(portal.x, portal.y, portal.radius, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fillStyle = '#facc1533';
    ctx.fill();

    // Draw Package
    ctx.fillStyle = '#f97316';
    ctx.fillRect(pkg.x - pkg.radius, pkg.y - pkg.radius, pkg.radius * 2, pkg.radius * 2);
    ctx.strokeStyle = '#ffffff';
    ctx.strokeRect(pkg.x - pkg.radius, pkg.y - pkg.radius, pkg.radius * 2, pkg.radius * 2);

    document.getElementById('lvlCount').innerText = level;
    document.getElementById('scoreCount').innerText = score;

    if (isGameOver) {
        ctx.fillStyle = 'rgba(3, 7, 18, 0.85)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ef4444';
        ctx.font = 'bold 24px sans-serif';
        ctx.fillText('CRASHED INTO ASTEROID!', canvas.width / 2 - 130, canvas.height / 2 - 10);
        ctx.font = '14px sans-serif';
        ctx.fillStyle = '#a78bfa';
        ctx.fillText('Tap Screen to Try Again', canvas.width / 2 - 75, canvas.height / 2 + 25);
    } else if (levelWon) {
        ctx.fillStyle = 'rgba(3, 7, 18, 0.85)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#22c55e';
        ctx.font = 'bold 26px sans-serif';
        ctx.fillText('SUCCESSFUL DELIVERY!', canvas.width / 2 - 130, canvas.height / 2 - 10);
        ctx.font = '14px sans-serif';
        ctx.fillStyle = '#facc15';
        ctx.fillText('Tap Screen for Next Level', canvas.width / 2 - 80, canvas.height / 2 + 25);
    }
}

function resetGame() {
    pkg.x = 50;
    pkg.y = 350;
    pkg.vx = 2;
    pkg.vy = -3;
    isGameOver = false;
    levelWon = false;
}

function loop() {
    updatePhysics();
    drawGame();
    requestAnimationFrame(loop);
}

loop();
</script>
</body>
</html>
"""

components.html(game_html, height=600)

# BOTTOM BANNER AD
render_banner_ad("Bottom Footer")
