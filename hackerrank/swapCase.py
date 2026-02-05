def swap_case(s):
    out=""
    for ch in s:
        if ch.islower():
            out+=ch.upper()
        else:
            out+=ch.lower()
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)