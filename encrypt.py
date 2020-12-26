def encode(txt):
    ans = []
    c=1
    for i in txt:
        if i == "@":
            ans.append("-")
            continue
        if i == "$":
            ans.append("|")
            continue
        if i == "&":
            ans.append("`")
            continue
        if i == ".":
            ans.append(":")
            continue
        if i == ",":
            ans.append(";")
            continue
        temp = i
        temp = (ord(temp) + c - 97) % 26 
        ans.append(chr(int(temp + 97)))
        c = c*2

    ans = "".join(ans)
    print(ans)
    return ans

def decode(txt):
    s = []
    c=1
    for i in txt:
        if i == "-":
            s.append("@")
            continue
        if i == "|":
            s.append("$")
            continue
        if i == "`":
            s.append("&")
            continue
        if i == ":":
            s.append(".")
            continue
        if i == ";":
            s.append(",")
            continue
        temp = i
        temp = (ord(temp) - c - 97) % 26 
        s.append(chr(int(temp + 97)))
        c = c*2

    ss= []
    for i in range(len(s)):
        if i == len(s):
            break
        ss.append(s[i])
    s = "".join(ss)
    print(s)
    return(s)