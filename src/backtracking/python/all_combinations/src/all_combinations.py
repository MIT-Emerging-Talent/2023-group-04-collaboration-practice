#generate all possible combinations of k integers from 0 to n (inclusive)
def allComb(n,k):
    # combList is a list of all possible combinations
    combList=[]
    # subList is a combination
    subList = []
    # generateList is a helper function that generate all combination
    generateList(n,k, subList, combList)
    return combList

"""helper function
n: the upper limit of the range of integers from which the combinations are drawn.
k: the length of the combinations.
subList:empty list and adding elements to it one at a time in helper function
For each iteration of the loop, the function can call itself recursively with n, k
and subList + [i] (to add the current integer to the combination) until 
the lenght of a subList be equal to k"""
def generateList(n,k, subList,combList):
    if len(subList) == k:
        combList.append(subList)
    else:
        if len(subList) == 0:
            maxS = 0
        else:
            maxS = max(subList)+1
        for i in range(maxS,n+1):
            generateList(n, k, subList+[i], combList)
    return combList
  
