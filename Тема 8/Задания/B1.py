import itertools
count=0
for p in itertools.product("012345678",repeat=5):
    st="".join(p)
    if st[0] not in ("0","1","3","5","7") and st[4]!="1" and st[4]!="8" and st.count("3")==1:
        count+=1
print(count)