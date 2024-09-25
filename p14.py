tu=(1,2,3,4,5,6,7,8,9)
if len(tu)<2:
    mod=tu
else:
    mod=(tu[-1],)+tu[1:-1]+(tu[0],)
print(mod)