import os

JOKE = (
    "My AI coding agent doesn't make mistakes — it commits them with a "
    "passing test suite and a cheerful PR summary."
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
