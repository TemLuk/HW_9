def my_number():
    my_num = '838372893'

    def user_telephone():
        user_tel = '+044'
        print(user_tel + my_num)

    return user_telephone()


print(my_number())
