password = '9867254461'

hacked = []
test_no = 0
test_index = 0
i = 0
for i in range(len(password)+100):
    if int(password[test_index]) == test_no:
        hacked.append(test_no)
        test_no += 1
        test_index += 1 
        print(hacked)
        i += 1
    else:
        test_no +=1
        