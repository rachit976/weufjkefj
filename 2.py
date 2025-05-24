try:
    num1,num2 = eval(input("enter two numbers, separated by comma ;"))
    result= num1/ num2
    print("result is",result)

except ZeroDivisionError:
    print("Division by zero is error!!")
  

except SyntaxError:
    print("comma is missing. enter numbers seperted by comma like this 1, 2")
      

except :
    print("Wrong input")


else:
    print("No expections")


finally: 
    print('this will excute no matter what')   
    