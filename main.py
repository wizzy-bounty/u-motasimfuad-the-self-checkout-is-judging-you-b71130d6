import os

LINE = "Please place the ice cream in the bagging area; denial is not a reusable bag."
OUTPUT_FILENAME = "entry.txt"


def resolve_output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, OUTPUT_FILENAME)


def main() -> None:
    with open(resolve_output_path(), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
