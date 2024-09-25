Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}
v=list(Company.values())
k=list(Company.keys())
print(k[v.index(max(v))])