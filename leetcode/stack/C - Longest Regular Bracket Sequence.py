brack = input().strip()
st = []

for c in brack:
    if c == ")":
        if st and isinstance(st[-1], int):
            if len(st) > 1 and st[-2] == "(":
                curr = st.pop()
                st.pop()  # remove '('
                val = curr + 2

                if st and isinstance(st[-1], int):
                    val += st.pop()

                st.append(val)
            else:
                st.append(c)

        elif st and st[-1] == "(":
            st.pop()

            if st and isinstance(st[-1], int):
                st[-1] += 2
            else:
                st.append(2)

        else:
            st.append(c)

    else:
        st.append(c)

max_len = 0
count = 0

for x in st:
    if isinstance(x, int):
        if x > max_len:
            max_len = x
            count = 1
        elif x == max_len:
            count += 1

if max_len:
    print(max_len, count)
else:
    print(0, 1)
