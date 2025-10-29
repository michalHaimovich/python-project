# #1
# from itertools import count
#
#
# def filter_alphanumeric(str):
#     return "".join(char for char in str if char.isalnum())
#
# print(filter_alphanumeric("f45#$%54gf"))
# #2
# def most_p(str):
#     maxC=0;
#     maxW=''
#     list=str.split();
#     for l in list:
#         if(str.count(l)>maxC):
#             maxC=str.count(l)
#             maxW=l
#
#     return maxW
#
# print(most_p("ab ab gfd d dd "))
#
# #3
#
# def initials(str):
#     list=str.split();
#     initial=""
#     for i in list:
#         initial+=i[0]
#     return initial
#
#
# print(initials("michal haimovich"))

#1
def analyze_list(lst):
    count=0
    sum=0;
    min=lst[0]
    max=lst[0]
    my_set=set()
    for i in lst:
        if(i< min):
            min=i
        if(i>max):
            max=i
        count+=1
        sum+=i
        my_set.add(i)
    return {
        "set":my_set,
        "avg":sum/count,
        "min":min,
        "max":max
    }


# print(analyze_list([1,2,3,4,5,6,7,8,5,3,2,6]))
 #2

def filter_dict(d, threshold):
    li=[]
    for i in d.values():
        if(i>threshold):
            li.append(i)
    return li

d={"a":231,"f":453}
print(filter_dict(d,500))