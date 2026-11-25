import os

LINE = "fix: removed the bug I wrote at 2am, replaced it with the one I wrote at 4am"

# Gate: one line, 1-200 chars, no trailing newline.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip() != ""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read back and confirm exactly what was written, with no trailing newline.
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
