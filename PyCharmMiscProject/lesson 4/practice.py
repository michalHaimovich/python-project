import csv
import json


# def countWords(str):
#     with open(str, 'r') as file_text:
#         content = file_text.readlines()
#         count = 0
#         for line in content:
#             count += len(line.split())
#     return count
#
#
# # with open('')
#
# print(countWords('text'))
#
#
# def write_csv(mat):
#     with open('file.csv', 'w') as file_csv:
#         writer = csv.writer(file_csv)
#         for li in mat:
#             writer.writerow(li)
#
#
# a = [["michal", "ha", 2, "fds"], ["michal", "haa", 5, "fdsa"], ["midwachal", "asdas", 23, "ftewtwe"]]
# write_csv(a)


def write_json(dict):
    with open('data.json', 'w') as file_json:
        json.dump(dict, file_json)
    with open('data.json','r') as file_json:
        data=json.load(file_json)
        print(data)

d={"name":"michal","age":20,"last":"haimovich"}
write_json(d)