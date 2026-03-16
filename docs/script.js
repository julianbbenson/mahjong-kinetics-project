// CONSTANTS FROM YOUR PYTHON ANALYSIS
const VMAX = 1.38;
const KM = 63.9;

const slider = document.getElementById('wallSlider');
const tilesDisplay = document.getElementById('tilesDisplay');
const regimeDisplay = document.getElementById('regimeDisplay');
const sValue = document.getElementById('sValue');
const vValue = document.getElementById('vValue');
const canvas = document.getElementById('wallCanvas');
const ctx = canvas.getContext('2d');

let chart;

// --- 1. TILE DRAWING ENGINE ---
function drawTile(x, y, opacity) {
    // Tile Body (Back of tile)
    ctx.fillStyle = `rgba(253, 242, 208, ${opacity})`; // Bone white
    ctx.strokeStyle = `rgba(150, 150, 150, ${opacity})`;
    ctx.beginPath();
    ctx.roundRect(x, y, 18, 26, 3);
    ctx.fill();
    ctx.stroke();

    // Tile Back (Blue/Green typical in Japan)
    ctx.fillStyle = `rgba(40, 60, 140, ${opacity})`; 
    ctx.beginPath();
    ctx.roundRect(x+2, y+2, 14, 22, 2);
    ctx.fill();
}

function drawWall(tilesLeft) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw 70 slots (2 rows of 35)
    // We visually represent the wall shrinking.
    const startX = 35;
    const startY = 40;
    const gap = 20;

    for (let i = 0; i < 70; i++) {
        let row = Math.floor(i / 35);
        let col = i % 35;
        let x = startX + (col * 18); // Tight packing
        let y = startY + (row * 35);
        
        // If the tile is "gone", draw it as a ghost
        let isPresent = i < tilesLeft;
        let opacity = isPresent ? 1.0 : 0.1;
        
        drawTile(x, y, opacity);
    }
}

// --- 2. MATH ---
function calculateRate(s) {
    return (VMAX * s) / (KM + s);
}

function update(s) {
    // Update Text
    sValue.innerText = s;
    tilesDisplay.innerText = s + " Tiles Left";
    
    // Update Win Rate
    let v = calculateRate(s);
    vValue.innerText = (v * 100).toFixed(1) + "%";

    // Update Regime Visuals
    if (s > KM) {
        regimeDisplay.innerText = "SATURATED REGIME";
        regimeDisplay.className = "status-green";
    } else if (s > 20) {
        regimeDisplay.innerText = "LINEAR PHASE";
        regimeDisplay.className = "status-yellow";
    } else {
        regimeDisplay.innerText = "STARVATION REGIME";
        regimeDisplay.className = "status-red";
    }

    // Redraw Canvas
    drawWall(s);

    // Update Chart
    if (chart) {
        chart.data.datasets[1].data = [{x: s, y: v}];
        chart.update();
    }
}

// --- 3. CHART SETUP ---
function initChart() {
    const chartCtx = document.getElementById('kineticsChart').getContext('2d');
    const sPoints = Array.from({length: 71}, (_, i) => i);
    const vPoints = sPoints.map(calculateRate);

    chart = new Chart(chartCtx, {
        type: 'line',
        data: {
            labels: sPoints,
            datasets: [{
                label: 'Michaelis-Menten Curve',
                data: vPoints,
                borderColor: '#f43f5e',
                borderWidth: 2,
                pointRadius: 0
            }, {
                label: 'Current State',
                data: [{x: 70, y: calculateRate(70)}],
                backgroundColor: 'white',
                borderColor: 'white',
                pointRadius: 6,
                type: 'scatter'
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: {display:true, text:'[S] Tiles Remaining'}, reverse: true },
                y: { title: {display:true, text:'[V] Win Probability'}, min: 0, max: 0.8 }
            },
            animation: false
        }
    });
}

slider.addEventListener('input', (e) => update(parseInt(e.target.value)));

initChart();
update(70);