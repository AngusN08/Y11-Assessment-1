from testhelper import test

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,4,6,8,10,12,14,16,18]

def sum_number_lists():
    if len(list1) != len(list2):
        print('List length not equal.')
        return
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    print(list3)
sum_number_lists()

### TESTS - Run the code that calls the function to check it works.
# test("Sum number lists 1", [4,5,7,8,10,11,13], sum_number_lists([1,2,3,4,5,6,7], [3,3,4,4,5,5,6]))
# test("Sum number lists 2", [11,12,13,14,15,16,17], sum_number_lists([1,2,3,4,5,6,7], [10,10,10,10,10,10,10]))
