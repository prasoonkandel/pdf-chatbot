def chunk(content: str, max_size: int = 500, overlap: int = 50):
    chunks = []
    temp_part = ""
    overlap_part = ""

    for piece in content.split("\n\n"):
        if len(piece) > max_size:
            chunks.append(temp_part)
            overlap_part = temp_part[-overlap:]
            temp_part = ""
            i = 0

            while i < len(piece):
                piece_part = piece[i : (i + max_size - overlap)]

                if len(piece_part) == 0:
                    chunk_part = piece[i:]
                    chunks.append(chunk_part)
                    overlap_part = chunk_part[-overlap:]
                    break

                current_part = overlap_part + piece_part
                chunk_part = ""

                if "\n" in current_part[len(overlap_part) :]:
                    before, newline, after = current_part.rpartition("\n")
                    chunk_part = before
                    i += len(before) - len(overlap_part)
                    overlap_part = before[-overlap:]
                elif ". " in current_part[len(overlap_part) :]:
                    before, newline, after = current_part.rpartition(". ")
                    chunk_part = before
                    i += len(before) - len(overlap_part)
                    overlap_part = before[-overlap:]
                elif " " in current_part[len(overlap_part) :]:
                    before, word_break, after = current_part.rpartition(" ")
                    chunk_part = before
                    i += len(before) - len(overlap_part)
                    overlap_part = before[-overlap:]
                else:
                    chunk_part = current_part
                    i += len(current_part) - len(overlap_part)
                    overlap_part = current_part[-overlap:]

                chunks.append(chunk_part)

            continue

        if len(temp_part + f"{piece}") >= max_size:
            chunks.append(temp_part)
            overlap_part = temp_part[-overlap:]
            temp_part = ""

        if temp_part == "":
            temp_part += overlap_part

        temp_part += f"{piece}"

    else:
        chunks.append(temp_part)

    return chunks
