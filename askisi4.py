def main(code):
    array = [0]*30000
    pointerLocation = 0
    i = 0
    c = 0
    print(code)
    while i < len(code):
        if code[i] == '<':
            if pointerLocation > 0:
                pointerLocation -= 1
        elif code[i] == '>':
            pointerLocation += 1
            if len(array) <= pointerLocation:
                array.append(0)
        elif code[i] == '+':
            array[pointerLocation] += 1
        elif code[i] == '-':
            if array[pointerLocation] > 0:
                array[pointerLocation] -= 1
        elif code[i] == '.':
            print(array[pointerLocation], chr(array[pointerLocation]))
        elif code[i] == ',':
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pointerLocation] = y
        elif code[i] == '[':
            if array[pointerLocation] == 0:
                open_braces = 1
                while open_braces > 0:
                    i += 1
                    if code[i] == '[':
                        open_braces += 1
                    elif code[i] == ']':
                        open_braces -= 1
        elif code[i] == ']':
			
            open_braces = 1
            while open_braces > 0:
                i -= 1
                if code[i] == '[':
                    open_braces -= 1
                elif code[i] == ']':
                    open_braces += 1
        i -= 1
main()

