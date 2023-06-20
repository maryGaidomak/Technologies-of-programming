def pack_string(line:str):
    result = ""
    current_length = 1

    for i in range(0, len(line) - 1):
        # Для конца строки добавляем последнюю группу
        if i + 1 == len(line) - 1:
            # Если последний символ отличается добавляем его как новую группу размера 1
            if line[i] != line[i + 1]:
                result += f"@1{line[i + 1]}"
            # Иначе последний символ входит в последнюю группу
            else:
                result += f"@{current_length+1}{line[i]}"

        elif line[i] != line[i + 1]:
            result += f"@{current_length}{line[i]}"
            current_length = 1

        else:
            current_length += 1
    return result;


def test_pack_string():
    print(pack_string("XXXZZRRVBVVVVVWW") == "@3X@2Z@2R@1V@1B@5V@2W")
    print(pack_string("AABBBBHHHOOOWW") == "@2A@4B@3H@3O@2W")
    print(pack_string("ABCDEFG") == "@1A@1B@1C@1D@1E@1G")


#test_pack_string()


def unpack_string(line: str):
    result = ""
    packs = line.split('@')
    for p in packs:
        if p == "":
            continue
        symbol = p[-1]
        count = int(p[0:-1])
        result += symbol * count
    return result


def test_unpack_string():
    print(unpack_string("@3X@2Z@2R@1V@1B@5V@2W") == "XXXZZRRVBVVVVVWW")
    print(unpack_string("@2A@4B@3H@3O@2W") == "AABBBBHHHOOOWW")
    print(unpack_string("@1A@1B@1C@1D@1E@1F@1G") == "ABCDEFG")


test_unpack_string()





