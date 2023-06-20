def print_hex_dump(filename, offset, length):
    with open(filename, "rb") as f:
        f.seek(offset)  # смещение на длину offset
        block = f.read(length)

    # печать
    for i in range(0, len(block), 16):
        row = block[i:i + 16]
        hex_dump = " ".join([f"{byte:02X}" for byte in row])
        ascii_dump = "".join([chr(byte) for byte in row])
        print(f"{offset + i:08X}: {hex_dump.ljust(48)} | {ascii_dump}")


print_hex_dump('data/21example.bin', 5, 40)
