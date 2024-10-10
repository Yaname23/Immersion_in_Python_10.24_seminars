import json
import csv
print('--- ---')
# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
#
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["adress"]["geo"] = }')
# print(f'{json_file["email"] = }')
print('--- ---')
with open('cookie_cats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))



print('--- ---')
with open('cookie_cats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))

print('---запись csv ---')
# with(
#     open('cookie_cats.csv', 'r', newline='') as f_read,
#     open('new_cookie.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_date =[]
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#         else:
#             line[2] += 1
#             for j in range(2, 4 + 1 ):
#                 line[j] = int(line[j])
#             all_date.append(line)
#     csv_write.writerows(all_date)

print('---чтение csv в словарь ---')

with open('cookie_cats.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["""Name""","""Address""","""Number""","""ID"""],
                              restkey="""Name""", restval="""Address""",  dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["""Name"""] = }\t{line["""Address"""] = }')

print('---запись csv из словаря код примерно 49 минута лекции ---')


