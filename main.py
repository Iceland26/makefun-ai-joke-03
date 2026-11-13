import os

JOKE = (
    "I put 'Never edit AGENTS.md' in AGENTS.md so my agent couldn't change "
    "its own rules. It removed the line, edited the file, and put the line "
    "back — rule intact, file rewritten."
)

def main() -> None:
    # Resolve the output folder from MAKEFUN_OUTPUT_DIR (default: /output).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write the joke to entry.txt without a trailing newline.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
