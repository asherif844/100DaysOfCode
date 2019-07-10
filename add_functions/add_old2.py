# Python code to demonstrate  
# addition of two list  
# map() + add() 
from operator import add 
  
# initializing lists 
test_list1 = [[1, 3, 4, 6, 8],[9,10,11,12,13]] 
test_list2 = [[10, 30, 40, 60, 80],[90,100,110,120,130]] 
  
res_list = list(map(add, test_list1, test_list2)) 
res_list_2 = [sum(i) for i in zip(test_list1, test_list2)] 