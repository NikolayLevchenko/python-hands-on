phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)

###################################### version 1
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)

###################################### version 2
# plist = plist[1:8]
# plist.remove("'")
# plist.insert(2, plist.pop(3))
# plist.insert(4, plist.pop())

###################################### version 3
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

# new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

# book = "The Hitchhiker's Guide to the Galaxy"
# booklist = list(book)
# print(booklist)
# backwards = booklist[::-1]
# print(''.join(backwards))
