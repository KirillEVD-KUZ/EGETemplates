text=open("ЕКСР.txt").readline()
while "--" in text or "**" in text or "-*" in text or "*-" in text:
    if "--" in text:
        text=text.replace("--","^")
    if "**" in text:
        text=text.replace("**", "^")
    if "*-" in text:
        text=text.replace("*-", "^")
    if "-*" in text:
        text = text.replace("-*", "^")
parts=text.split("^")
