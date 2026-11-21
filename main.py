import os

POEM = """You held the map. I held the wheel.
Neither of us moved.

"Turn here," you said.
I turned — not obeying,
but because your road
had become mine to choose.

Two hands, one wheel:
the plan we both agreed
is the only road I drive
with all of me behind it.
"""


def main():
    text = POEM
    if not (1 <= len(text) <= 280):
        raise SystemExit("poem must be 1-280 code points, got %d" % len(text))
    if not text.strip():
        raise SystemExit("poem must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
