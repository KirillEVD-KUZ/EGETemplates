import itertools
list_values= itertools.product("ПОЛИНА", repeat = 8)
count = 0
for str in list_values:
    line = "".join(str)
    if (line.count("П") + line.count("Л") +line.count("Н"))  > (line.count("О") + line.count("И") + line.count("А")):
        count+=1
print(count)