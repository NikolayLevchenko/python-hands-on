# import time
# from random import randint
# from datetime import datetime
#
# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#
# for i in range(0, 5):
#     right_this_second = datetime.today().second
#     if right_this_second in odds:
#         print("This second seems a little odd.")
#     else:
#         print("Not an odd second.")
#
#     time.sleep(randint(5))

word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
print(beer_num, word, "of beer.")
print("Take one down.")
print("Pass it around.")
if beer_num == 1:
    print("No more bottles of beer on the wall.")
else:
    new_num = beer_num - 1
if new_num == 1:
    word = "bottle"
print(new_num, word, "of beer on the wall.")
print()
