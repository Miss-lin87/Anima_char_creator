import charstats

def new_char(new):
    new = {}
    new = charstats.emptydic.copy()
    f = open(new,"x")
    f = open(new, "a")
    return new


print(new_char(new="test"))

print("new direct made")