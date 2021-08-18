#!/usr/bin/python3

import random

retries = 0
def randomNum():
    my_nums = []
    for i in range(4):
        my_nums.append(random.randint(1,10))
    
    # check duplicates here.
    if len(set(my_nums)) < len(my_nums):
        global retries
        retries+=1
        randomNum()
    else:
        lotto_number = 1
        for items in my_nums:
            print("Lotto number {}".format(lotto_number), items)
            lotto_number+=1
        print("The number of tries", retries)