def task1(a, n):
       if a>n:
              return a, ' is greater'
       elif n>a:
              return n, ' is greater'
       else:
              return 'Numbers are equal'


def task2(n):
       if n>0:
              return n, ' is positive'
       elif n<0:
              return n, ' is negative'
       else:
              return n, ' is zero'


def task3(n):
       if n%2==0:
              return n, ' is even'
       else:
              return n, ' is odd'


def task4(score):
       if score>100 or score<0:
              return  "Invalid score"
       elif score>90:
              return 'A'
       elif score > 80:
              return 'B'
       elif score > 70:
              return 'C'
       elif score>60:
              return 'D'
       elif score > 50:
              return 'E'
       else:
              return 'F'


def task5(a, b, n):
       if a>b and a>n:
              return a, ' is greatest'
       elif b>a and b>n:
              return b, ' is greatest'
       else:
              return n, ' is greatest'


def task6(a, b, n):
       op=['+', '-', '*', '/', '%', '**', '//']
       if not n in op:
              return "Invalid operation"
       else:
              if n=='+':
                     return a+b
              elif n=='-':
                     return a-b
              elif n=='*':
                     return a*b
              elif b!=0 and n=='/':
                     return a/b
              elif b==0 and n=='/':
                     return 'Error'
              elif b!=0 and n=='%':
                     return a%b
              elif a==0 and b==int(b) and n=='**':
                     return 'Error'
              elif n=='**':
                     return a**b
              elif b!=0 :
                     return a//b
              else:
                     return 'Error'


def task7(age):
       if age<0:
              return "Invalid age"
       elif age>65:
              return 'Senior'
       elif age>18:
              return 'Adult'
       elif age>13:
              return 'Teen Titans Go'
       else:
              return 'Child'


def task8(money):
       if money<0:
              return "Invalid money"
       elif money <100:
              discount=0
       elif money<300:
              discount=10
       elif money <500:
              dircount = 15
       else:
              discount=20
       return money*(100-discount)


def task9(a, b, n):
       if a>b and a>n:
              if b>n:
                     return a, ' ', b, ' ', n
              else:
                     return a, ' ', n, ' ', b
       elif b>a and b>n:
              if a>n:
                     return b, ' ', a, ' ', n
              else:
                     return b, ' ', n, ' ', a
       else:
              if a>b:
                     return n, ' ', a, ' ', b
              else:
                     return n, ' ', b, ' ', a


def task10(amount):
       balance=1000
       if amount<=0:
              return 'Invlaid amount'
       elif amount>balance:
              return 'Insufficient balance'
       else:
              return balance- amount


def task11(usage):
       if usage<0:
              return "invalid usage"
       elif usage<100:
              rate=0.08
       elif usage<300:
              rate=0.12
       else:
              rate=0.15
       return usage, rate, usage*rate



def task12(distance):
       starting_fee=2
       if distance<0:
              return 'Invalid distance'
       elif distance<5:
              fee=0.7
       elif distance<15:
              fee=0.6
       else:
              fee=0.5
       total=distance*fee+starting_fee
       return starting_fee, distance*fee, total



def task13(age, salary, amount):
       if age<0 or salary<0 or amount<=0:
              return 'Invlid input'
       elif age<18 or salary<500 or amount>10*salary:
              return 'Rejected'
       else:
              return 'Approved'



def task14(a, b, n):
       if a<0 or b<0 or n<0:
              return 'Invlaid input'
       elif a+b<c or a+c<b or b+c<a:
              return 'Triangle cannot be created'
       elif a==b==c:
              return 'Equilateral'
       elif a==b or a==n or b==n:
              return "Isosceles"
       else:
              return 'Scalene'



def task15(exam_score, school_score, age):
       if age<0 or 0<=exam_score<=700 or 0<=school_score<=100:
              return 'Invalid input'
       elif age<16:
              return 'Rejected'
       elif 600<=exam_score<=700:
              return 'Accepted, Scholarship'
       elif 450<=exam_score<600:
              return "Accepted"
       elif 300<=exam_score<450:
              if school_score>=80:
                     return 'Accepted'
              else:
                     return 'Rejected'
       else:
              return 'Rejected'



def task16(score):
       if not 0<score<100:
              return 'Rejected'
       elif score>=51:
              return "Pass"
       else:
              return 'Fail'



def task17(money, membership):
       if money<0 or membership.lower()!='no' or membership.lower()!='yes':
              return 'Invalid input'
       elif money>50 or membership.lower()=='yes':
              delivery=0
       else:
              delivery=5
       return delivery, delivery+money



def task18(day):
       study='Study day'
       end='Weekend'
       match day:
              case 1:
                     return 'Monday '+study
              case 2:
                     return 'Tuesday '+study
              case 3:
                     return 'Wednesday '+study
              case 4:
                     return 'Thursday '+study
              case 5:
                     return 'Friday '+study
              case 6:
                     return 'Saturday '+end
              case 7:
                     return 'Sunday '+end
              case _:
                     return 'Invalid number'



def task19():
       print('T = Tea (2 AZN),C = Coffee (4 AZN), J = Juice (3 AZN).')
       drink=input('Choose drink: ')
       quantity=int(input('Choose quantity'))
       match drink:
              case 'T':
                     drink='Tea'
                     fee=2
              case 'C':
                     drink='Coffee'
                     fee=4
              case 'J':
                     drink='Juice'
                     fee=3
              case _:
                     return 'Invalid input'
       return drink, quantity, quantity*fee



def task20(ID):
       if len(ID)!=8 or not ID.isdecimal():
              return 'Invalid input'
       return 'Student Accepted'



def task21(pin):
       stored_pin='0427'
       if pin=='':
              return 'PIN is required'
       elif len(pin)!=4:
              return  "PIN must have 4 digits"
       elif not pin.isdecimal():
              return  "Digits only"
       if pin == stored_pin:
              return "Access granted"
       else:
              return 'Incorrect PIN'



def task22(num):
       l=['050', '051', '055', '070', '077', '099']
       if num[0]!='0':
              return 'Number doesnt start with 0'
       elif len(num)!=10:
              return 'Number must contain 10 digits'
       elif not num.isdecimal():
              return 'Number must only contain digits'
       elif not num[:3] in l:
              return 'Error'
       else:
              match num[:3]:
                     case '050'|'051'|'055'|'070'|'077'|'099':
                            return 'Phone number accepted'
                     case _:
                            return 'Error'
       


def task23(pin, amount):
       balance=1000
       stored_pin='0427'
       if len(pin)!=4 or not pin.isdecimal():
              return 'Invalid pin'
       elif len(amount)==0 or not amount.isdecimal():
              return 'Invalid amount'
       elif not 10<amount<500 and not amount%10==0:
              return 'Wrong amount'
       if amount > 200:
              fee=0
       else:
              fee=2
       if amount+fee>balance:
              return 'You cant withdraw'
       else:
              return amount+fee, fee, balance-(amonut+fee)



def task24(code, quantity, cupon_code, delivery_code):
       cupon='SAVE10'
       match code:
              case 'K':
                     product='Keyboard'
                     money=40
              case 'M':
                     product='Mouse'
                     money=20
              case 'H':
                     product='Headphones'
                     money=60
              case _:
                     return 'Invalid product request'
       if not 1<=quantity<=5 or not quantity.isdecimal():
              return 'Invalid quantity input'
       if cupon_code==cupon:
              discount=10
       elif cupon_code=='NONE':
              discount=0
       else:
              return 'Invalid cupon'
       subtotal=money*(100-discount)
       match delivery_code:
              case 'P':
                     delivery_fee=0
              case 'S':
                     if subtotal>=80:
                            delivery_fee=0
                     else:
                            delivery_fee=5
              case _:
                     return 'Invalid delivery input'
       return product, quantity, subtotal, discount, delivery_fee
       
       
       
       
       
       
              










