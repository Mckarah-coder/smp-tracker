// Arrow function with default parameter
const assessDay = (steps, goal = 10000) => {
  if (steps >= goal) return "HIT";
  return "MISS";
};

const weeksummary = (stepcounts) => {
  const total = stepcounts.reduce((sum, steps) => sum + steps, 0);
  const average = total / stepcounts.length;
  const hitcount = stepcounts.filter((steps) => steps >= 10000).length;
  return { total, average, hitcount };
};

// Function returning an object
const analyzeDay = (sleep, water, steps) => {
  const hitGoal = steps >= 10000;
  let rating;
  if (sleep >= 7.5 && water >= 8 && hitGoal) {
    rating = "Excellent";
  } else if (hitGoal) {
    rating = "Good";
  } else if (sleep >= 7.0) {
    rating = "Average";
  } else {
    rating = "Below target";
  }
  return { sleep, water, steps, hitGoal, rating };
};

// Test with SMP data
const days = [
  [8.0, 10, 12100],
  [5.5,  4,  7800],
  [7.2,  8, 10050],
  [6.0,  5,  9200],
];

days.forEach(([sleep, water, steps]) => {
  const result = analyzeDay(sleep, water, steps);
  console.log(`Sleep:${result.sleep}h  Water:${result.water}gl  Steps:${result.steps.toLocaleString()}  --> ${result.rating}`);
});

// for...of loop
console.log("\nGoal assessments:");
const stepLog = [9800, 11400, 6300, 10050];
for (const steps of stepLog) {
  console.log(`  ${steps.toLocaleString()} --> ${assessDay(steps)}`);
}
console.log("Week summary:", weeksummary(stepLog));