# def add():

list1 = [[1,2,3],[4,5,6]]
list2 = [[10,20,30],[40,50,60]]

    
    # return [sum(list1[i]+list2[i]) for i in range(len(list1))]


# a = [[5,6,7], [8,9,10]]
# b = [[50,60,70], [80,90,100]]

[list1[i]+list2[i] for i in range(len(list1))]
[list1[i] for i in range(len(list1))]
[list2[i] for i in range(len(list1))]

[list1[0]+list2[0] for i in range(1)]

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()