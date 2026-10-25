max_chars = 500


def chunk(content: str) -> list[str]:
    chunks = []

    temp = ""

    for word in content.split():
        if len(temp) >= max_chars:
            if word == "\n\n":
                chunks.append(temp)
                temp = ""
        elif len(temp) >= max_chars:
            if word == "\n":
                chunks.append(temp)
                temp = ""
        elif len(temp) >= max_chars:
            if word == " " and temp.strip()[-1]:
                chunks.append(temp)
                temp = ""
        else:
            temp += f" {word}"

    return chunks
