import pickle

def func(a, b, c):
    return a + b + c

my_dict = {'numbers': [42, 4.1415, 7+3j],
           'functions': (func, sum, max),
           'others': {True, False, 'Hello words!'}}

with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)

print('-------')

def func(a, b, c):
    return a * b * c

with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)

print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')

