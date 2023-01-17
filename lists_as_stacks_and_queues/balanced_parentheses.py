parentheses = input()

balanced_bracket = []
balanced = True
for char in parentheses:
    if char in "({[":
        balanced_bracket.append(char)
    elif not balanced_bracket:
        balanced = False
    else:
        current_bracket = balanced_bracket.pop()
        if current_bracket == "(" and char != ")":
            balanced = False

        elif current_bracket == "[" and char != "]":
            balanced = False

        elif current_bracket == "{" and char != "}":
            balanced = False

    if not balanced:
        break

if not balanced or balanced_bracket:
    print('NO')
else:
    print('YES')
