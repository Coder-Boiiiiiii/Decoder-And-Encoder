String = str(input("Sentence to encode: "))
String_To_Encode = list(String)

def convertToList(string):
    str1 = " "
    return(str1.join(string))

for i in range(len(String_To_Encode)):
    String_To_Encode[i] = String_To_Encode[i].lower()

for x in range(len(String_To_Encode)):
    if "a" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("a")] = "@"

    elif "b" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("b")] = "#"

    elif "c" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("c")] = "!"

    elif "d" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("d")] = "^"

    elif "e" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("e")] = "$"

    elif "f" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("f")] = "%"

    elif "g" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("g")] = "&"

    elif "h" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("h")] = "("

    elif "i" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("i")] = "*"

    elif "j" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("j")] = ")"

    elif "k" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("k")] = "_"

    elif "l" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("l")] = "-"

    elif "m" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("m")] = "+"

    elif "n" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("n")] = "="

    elif "o" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("o")] = "~"

    elif "p" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("p")] = "`"

    elif "q" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("q")] = "|"
        
    elif "r" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("r")] = "/"

    elif "s" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("s")] = "?"

    elif "t" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("t")] = ">"

    elif "u" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("u")] = "<"

    elif "v" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("v")] = ":"

    elif "w" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("w")] = ";"

    elif "x" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("x")] = "."

    elif "y" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("y")] = ","

    elif "z" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("z")] = "}"

print(convertToList(String_To_Encode), end = "")
