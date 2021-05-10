String = str(input("Sentence to decode: "))
String_To_Encode = list(String)

def convertToList(string):
    str1 = " "
    return(str1.join(string))

for i in range(len(String_To_Encode)):
    String_To_Encode[i] = String_To_Encode[i].lower()

for x in range(len(String_To_Encode)):
    if "@" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("@")] = "a"

    elif "#" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("#")] = "b"

    elif "!" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("!")] = "c"

    elif "^" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("^")] = "d"

    elif "$" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("$")] = "e"

    elif "%" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("%")] = "f"

    elif "&" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("&")] = "g"

    elif "(" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("(")] = "h"

    elif "*" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("*")] = "i"

    elif ")" in String_To_Encode:
        String_To_Encode[String_To_Encode.index(")")] = "j"

    elif "_" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("_")] = "k"

    elif "-" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("-")] = "l"

    elif "+" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("+")] = "m"

    elif "=" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("=")] = "n"

    elif "~" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("~")] = "o"

    elif "`" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("`")] = "p"

    elif "|" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("|")] = "q"
        
    elif "/" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("/")] = "r"

    elif "?" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("?")] = "s"

    elif ">" in String_To_Encode:
        String_To_Encode[String_To_Encode.index(">")] = "t"

    elif "<" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("<")] = "u"

    elif ":" in String_To_Encode:
        String_To_Encode[String_To_Encode.index(":")] = "v"

    elif ";" in String_To_Encode:
        String_To_Encode[String_To_Encode.index(";")] = "w"

    elif "." in String_To_Encode:
        String_To_Encode[String_To_Encode.index(".")] = "x"

    elif "," in String_To_Encode:
        String_To_Encode[String_To_Encode.index(",")] = "y"

    elif "}" in String_To_Encode:
        String_To_Encode[String_To_Encode.index("}")] = "z"

print(convertToList(String_To_Encode), end = "")
