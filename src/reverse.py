from collections import deque


def solution(input_string):
    stack = deque()
    last_letter = None

    if len(input_string) < 2:
        return input_string

    for char in input_string:
        if last_letter is None:
            last_letter = char
        else:
            if char == 'A':
                if last_letter == 'B':
                    last_letter = stack.pop() if stack else None
                else:

                    stack.append(last_letter)
                    last_letter = char
                continue

            if char == 'B':
                if last_letter == 'A':
                    last_letter = stack.pop() if stack else None
                else:
                    stack.append(last_letter)
                    last_letter = char
                continue

            if char == 'C':
                if last_letter == 'D':
                    last_letter = stack.pop() if stack else None
                else:
                    stack.append(last_letter)
                    last_letter = char
                continue

            if char == 'D':
                if last_letter == 'C':
                    last_letter = stack.pop() if stack else None
                else:
                    stack.append(last_letter)
                    last_letter = char
                continue

    stack.append(last_letter)
    return ''.join(char for char in stack if char is not None)


if __name__ == "__main__":
    print(solution("AB"))
