#!/usr/bin/python
import random


#NOTE : Using random generator, please run multiple times if you dont see result as some random may not generate given sum

class Zignage:
	
	# O(n) time complexity implementaion of pair search function

        @staticmethod
        def TwoSum(arr, num):
            found = {}
            for i in range(len(arr)):
                find = num - arr[i]
                if((find in arr)):
                    found[find] = arr[i]
                    print(arr[i], find)
            return  found

        @staticmethod
        def count(arr, num):
            print ("Total Length is ->",len(Zignage.TwoSum(arr,num)))


a = []
for i in range(100):
    val = random.randrange(1000)
    #print (val)
    a.append(val)
print ("Result follows")

Zignage.count(a, 50)
