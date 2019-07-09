list1 = [[1,2,3],[4,5,6]]
list2 = [[10,20,30],[40,50,60]]


def add(list1, list2):
    
    
    if len(list1) == len(list2):

        result = list1


        for i in range(len(list1)):
            for j in range(len(list1[0])):
                result[i][j] = list1[i][j] + list2[i][j]

        return result
    else:

        print("ValueError: Given matrices are not the same size.")
        

add(list1, list2)

