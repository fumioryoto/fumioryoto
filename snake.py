import os
from datetime import datetime, timedelta
import json

# Repo path
repo_path = os.getcwd()
state_file = "snake_state.json"

# Grid configuration (GitHub contribution graph has 7 rows, 52 weeks)
rows = 7
cols = 52

# Load last head position
if os.path.exists(state_file):
    with open(state_file, "r") as f:
        state = json.load(f)
    head_pos = state["head_pos"]
else:
    head_pos = 0  # start at the first column

# Save new head position for next run
head_pos = (head_pos + 1) % cols
with open(state_file, "w") as f:
    json.dump({"head_pos": head_pos}, f)

# Create commits for this frame
start_date = datetime.today() - timedelta(days=rows*cols)
for y in range(rows):
    x = (head_pos + y) % cols  # diagonal snake effect
    filename = f"snake-{y}-{x}.txt"
    with open(filename, "w") as f:
        f.write(f"Snake at row {y}, col {x}")
    commit_date = start_date + timedelta(days=y*cols + x)
    os.system(f'git add {filename}')
    os.system(f'git commit -m "Snake commit at row {y}, col {x}" --date="{commit_date.isoformat()}"')
