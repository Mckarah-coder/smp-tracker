// SMP skills list
const skills = ["welding", "tiling", "copywriting", "phone repair", "beekeeping"];

console.log("Skills:", skills);
console.log("First:", skills[0]);
console.log("Last:", skills[skills.length - 1]);
console.log("Count:", skills.length);

// Add and remove items
skills.push("plumbing");          // add to end
const removed = skills.shift();  // remove from front
console.log("\nAfter push + shift:", skills);
console.log("Removed:", removed);

// Array methods that return new arrays
const stepLog = [8200, 11400, 6300, 10050, 9800, 12100, 7500];

const hitDays = stepLog.filter(s => s >= 10000);
const doubled = stepLog.map(s => s * 2);
const total   = stepLog.reduce((sum, s) => sum + s, 0);
const average = total / stepLog.length;
const sorted = [...stepLog].sort((a, b) => b - a);


console.log("\nStep log:", stepLog);
console.log("Hit days (>=10k):", hitDays);
console.log("Total steps:", total.toLocaleString());
console.log("Average:", Math.round(average).toLocaleString());
console.log("Sorted:", sorted);

// Check membership
console.log("\nIncludes 6300:", stepLog.includes(6300));
console.log("Index of 9800:", stepLog.indexOf(9800));
