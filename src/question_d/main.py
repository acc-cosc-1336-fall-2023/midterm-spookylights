import question_d

def local_variable_check():

    num = 100
    question_d.use_local_variable(num)
    
    print("The value of num in function local_variable_check is:", num)

local_variable_check()