// Session store (lives in memory for this page session)
const sessionLog = [];

const logEntry = (sleep, water, steps, hitGoal, confidence, score) => {
  const entry = {
    id:         sessionLog.length + 1,
    time:       new Date().toLocaleTimeString(),
    sleep, water, steps, hitGoal, confidence, score
  };
  sessionLog.push(entry);
  return entry;
};

const renderHistory = () => {
  const tableEl = document.querySelector('#historyTable');
  if (!sessionLog.length) {
    tableEl.innerHTML = '<tr><td colspan="6" style="color:var(--muted);text-align:center;padding:1rem;">No entries yet.</td></tr>';
    return;
  }
  tableEl.innerHTML = sessionLog.map(e => {
    const outcomeColor = e.hitGoal ? "#4ecca3" : "#f5a623";
    const outcome = e.hitGoal ? "HIT" : "MISS";
    return `<tr>
      <td style="color:#8b949e;font-size:0.8rem;">${e.time}</td>
      <td>${e.sleep}h</td>
      <td>${e.water} gl</td>
      <td>${e.steps.toLocaleString()}</td>
      <td style="color:${outcomeColor};font-weight:700;">${outcome}</td>
      <td style="color:#a0a0b0;">${(e.confidence * 100).toFixed(0)}%</td>
    </tr>`;
  }).join('');
};

// Hook into the existing coach form
const predictGoal = (sleep, water, steps) => {
  const s = Math.min(sleep / 8.0, 1.0) * 35;
  const w = Math.min(water / 10.0, 1.0) * 25;
  const st = Math.min(steps / 12000, 1.0) * 40;
  const total = s + w + st;
  const hit = total >= 60;
  const conf = Math.min(0.50 + Math.abs(total - 60) * 0.012, 0.95);
  return { hitGoal: hit, confidence: conf, score: Math.round(total) };
};

if (typeof document !== "undefined") {
  const form2 = document.querySelector('#coachForm2');
  form2.addEventListener('submit', (event) => {
    event.preventDefault();
    const sleep = parseFloat(document.querySelector('#h_sleep').value);
    const water = parseInt(document.querySelector('#h_water').value);
    const steps = parseInt(document.querySelector('#h_steps').value);

    if (isNaN(sleep) || isNaN(water) || isNaN(steps)) return;

    const result = predictGoal(sleep, water, steps);
    const entry  = logEntry(sleep, water, steps, result.hitGoal, result.confidence, result.score);

    renderHistory();
    console.log(`Entry #${entry.id} logged: ${result.hitGoal ? "HIT" : "MISS"} | score ${result.score}`);
    const hitRate = sessionLog.filter(e => e.hitGoal).length / sessionLog.length;
    // Reset inputs
    form2.reset();
  });

  renderHistory();
  console.log("History form wired. Submit entries using the form below.");
} else {
  const samples = [
    { sleep: 8, water: 10, steps: 12000 },
    { sleep: 5, water: 4, steps: 6000 },
    { sleep: 7.5, water: 8, steps: 10000 }
  ];

  console.log("Sample history:");
  samples.forEach(({ sleep, water, steps }) => {
    const result = predictGoal(sleep, water, steps);
    const entry = logEntry(sleep, water, steps, result.hitGoal, result.confidence, result.score);
    const outcome = result.hitGoal ? "HIT" : "MISS";
    console.log(
      `Entry #${entry.id}: ${sleep}h sleep | ${water} glasses | ${steps.toLocaleString()} steps | ` +
      `${outcome} | score ${result.score} | confidence ${(result.confidence * 100).toFixed(0)}%`
    );
  });
}
