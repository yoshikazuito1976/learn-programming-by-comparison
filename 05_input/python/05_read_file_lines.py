with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        print(f"読み込んだ単語: {word}")
