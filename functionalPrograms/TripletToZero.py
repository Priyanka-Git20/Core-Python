'''
    @Author : Priyanka
    @Date : 2022-04-06  12:20:00
    @Last Modified by : Priyanka
    @Last Modified Time : 2022-04-06  01:10:00
    @Title : Findind the distinct triplets.
'''


def findingTriplet(arr,n):
    """
        Description:
            finding triplet of combination on addition
        Parameter:
            array and size of array
        Return:
            printing triplet if it is in array
    """

    tripletFound = False
    for i in range (0, n-2):
        for j in range (i+1, n-1):
            for k in range (j+1, n):
                if (arr[i] + arr[j] + arr[k]) == 0:
                    print ("Triplet Found: ", end=" ")
                    print (arr[i], arr[j], arr[k])
                    tripletFound = True

    if tripletFound == False:
        print("Triplet is not found")

if __name__ == '__main__':
    while True:
        numberOfIntegers = int(input("Enter Length Of An Array:\n"))
        if numberOfIntegers < 3:
            numberOfIntegers = int(input("Enter Valid Length Of An Array"))
        else:
            arr = [numberOfIntegers]
            break

    for i in range(numberOfIntegers):
        print("Enter ",i,": ")
        arr.append(int(input()))
    print(arr)

findingTriplet(arr,numberOfIntegers)