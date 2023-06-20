def symbol_rearrangement(line: str):
    symbols_count = {}
    for symbol in line:
        # если символ не найден возвращаем 0
        symbols_count[symbol] = symbols_count.get(symbol, 0) + 1

    sorted_symbols = sorted(symbols_count, key=lambda x: symbols_count[x], reverse=True)

    result = ""
    for symbol in sorted_symbols:
        result += symbol * symbols_count[symbol]

    return result


def test_symbol_rearrangement():
    print(symbol_rearrangement("барракуда") == "аааррбкуд")
    print(symbol_rearrangement("сказка") == "ккаасз")
    print(symbol_rearrangement("тест") == "ттес")


test_symbol_rearrangement()