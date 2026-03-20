cl = 'aabbccddeefgghhi'
print([a for a in cl if cl.count(a)==1])
# cl2 ={}
# for str in cl:
#     if str not in cl2:
#         cl2[str] = 1
#     else:
#         cl2[str]+=1
# print(cl2)        

# print({a for a in cl2 if cl2.get(a)==1})
# lst = []
# for key,value in cl2.items():
#     if cl2[key] == 1:
#         lst.append(key)
# print(lst)        

