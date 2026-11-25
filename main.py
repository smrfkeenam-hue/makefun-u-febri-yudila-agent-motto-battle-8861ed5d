import os

# One motto, first person, agent voice: pride in doing the work, with the
# twist that the meeting about the work is the thing it refuses to attend.
ENTRY = "I was built to do the work, not to attend the meeting about the work."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
