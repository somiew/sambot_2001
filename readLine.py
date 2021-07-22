# Read discord token from token.txt
def read_line(document, i):
    with open(document, "r") as f:
        lines = f.readlines()
        return lines[i].strip()
