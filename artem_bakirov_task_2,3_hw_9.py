def decorator(func):
    def counter():
        text = input("Введите любой текст: ")
        result = func()
        counter2 = len(result)
        return f'{result}\n{text} {counter2}'

    return counter()


@decorator
def methods():

    name_obj = input("Введите тип объекта: ")
    if name_obj == "tuple":
        name_obj = tuple(name_obj)
    if name_obj == "set":
        name_obj = set(name_obj)
    if name_obj == "list":
        name_obj = list(name_obj)
    if name_obj == "str":
        name_obj = "str"
    if name_obj == "int":
        name_obj = 1
    if name_obj == "float":
        name_obj = 1.0
    if name_obj == "bool":
        name_obj = True
    dir_of_obj = dir(name_obj)
    my_list = list(dir_of_obj)
    dir_list = [i for i in my_list if not i.startswith("__")]
    return dir_list


print(methods)
