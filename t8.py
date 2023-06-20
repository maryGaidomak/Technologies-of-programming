def check_bracket_balance(text):
    stack = []
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    for char in text:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # Закрывающая скобка без соответствующей открывающей
            if len(stack) == 0:
                return False
            last_opening_bracket = stack.pop()
            # Несоответствие открывающей и закрывающей скобок
            if bracket_pairs[last_opening_bracket] != char:
                return False

    return len(stack) == 0


def test_check_bracket_balance():
    print(check_bracket_balance("(a [b c {(x q b)}] d r)") == True)
    print(check_bracket_balance("(a [b c x (q) b] {d} r)") == True)
    print(check_bracket_balance("(a [b (c {(x q) b)}] d r)") == False)


test_check_bracket_balance()



