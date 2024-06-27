def login(login, pswd):
    pass
    # with open('bank_clients/' + login + '.' + 'passwordhash.txt') as file_hash:
    #     if hash_funct(passw) == file_hash.readline():
    #                     file_hash.close()
    #             else:
    #                     print('\n*************\nIncorrect password')
    #                     return False
    #     except FileNotFoundError:
    #         print('A system error has occurred!\n Please contact an administrator.\n')
    #         return False
    #     return True
    # else:
    #  return False


# Create Hash for password
def hash_funct(pswd):
    summ = 0
    mult = 1
    CONST_FOR_HASH = 68429
    for i in range(len(pswd)):
        summ += ord(pswd[i])
        mult = mult * ord(pswd[i])
    summ = summ % CONST_FOR_HASH
    mult = mult % CONST_FOR_HASH
    return str(summ) + str(mult)