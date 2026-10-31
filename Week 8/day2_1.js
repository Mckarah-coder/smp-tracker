// Wire up the buttons in the live demo below
const addBtn    = document.querySelector('#d3addBtn');
const clearBtn  = document.querySelector('#d3clearBtn');
const logInput  = document.querySelector('#d3input');
const logList   = document.querySelector('#d3list');
const countEl   = document.querySelector('#d3count');

let count = 0;

const addEntry = (value) => {
  const li = document.createElement('li');
  li.textContent = `${new Date().toLocaleDateString()} - ${value}`;
  li.style.padding = "4px 0";
  li.style.borderBottom = "1px solid #30363d";
  logList.appendChild(li);

  count++;
  countEl.textContent = `Entries: ${count}`;
  console.log(`Added: "${value}"`);
};

addBtn.addEventListener('click', () => {
  const value = logInput.value.trim();
  if (!value) {
    console.log("No input to add.");
    return;
  }

  addEntry(value);
  logInput.value = "";
  logInput.focus();
});

[
  "Step 1: Gather the materials",
  "Step 2: Measure and mark the pieces",
  "Step 3: Assemble the parts",
  "Step 4: Check the finished work",
].forEach(addEntry);

clearBtn.addEventListener('click', () => {
  logList.innerHTML = "";
  count = 0;
  countEl.textContent = "Entries: 0";
  console.log("Log cleared.");
});

// Keyboard shortcut: Enter key submits
logInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    addBtn.click();
  }
});

console.log("Event listeners attached. Use the panel below.");