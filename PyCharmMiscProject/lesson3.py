#1

def filter_alphanumeric(str):
    return "".join(char for char in str if char.isalnum())

print(filter_alphanumeric("f45#$%54gf"))
#2
def most_p(str):
    maxC=0;
    maxW=''
    list=str.split();
    for l in list:
        if(str.count(l)>maxC):
            maxC=str.count(l)
            maxW=l

    return maxW

print(most_p("ab ab gfd d dd "))

#3

def initials(str):
    list=str.split();
    initial=""
    for i in list:
        initial+=i[0]
    return initial


print(initials("michal haimovich"))