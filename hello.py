def main() -> None:
    with open("sample-submodule/message.txt", "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()