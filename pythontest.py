#Q1
# s='hello world'
# a='hello Universe'
# for i in s:
#     s=s.replace(s,a)
# print(s)



#Q2
# names=['apple','google','yahoo','walmart']
# l=[]
# for i in names[::-1]:
#     l.append(i[::-1])
# print(l)

# Q3
# l=[3,4,1,7,2,12,8,9,11,16,13]
# l1=[]
# l2=[]
# for i in l:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# l=l2+l1
# print(l)


# Q4
# numbers=[18,15,20,25,30,35,40,5,10,15]
# numbers.sort()
# print(numbers)
# sum1=numbers[0]+numbers[1]+numbers[2]
# sum2=numbers[-1]+numbers[-2]+numbers[-3]
# print(f"Min Sum = {sum1}")
# print(f"Max Sum= {sum2}")




# Q5
# l=[1,2,3,4,1,2,3,4,4,5]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)
# print(l)



# Q6
# from abc import *
# class Q(ABC):
#     @abstractmethod
#     def enter(self):
#         ...
#     @abstractmethod
#     def valid(self):
#         ...
#     @abstractmethod
#     def validate(self):
#         ...
#
# class Login(Q):
#     def enter(self):
#         print("Welcome To Qspiders")
#         self.type=['mail','phone']
#         self.t=str(input(f"Choose Your Username Type: {self.type}"))
#         if self.t=='mail':
#             self.mail=str(input("Enter Your Mail"))
#         elif self.t=='phone':
#             self.phone=str(input("Enter Your Phone"))
#         self.pwd=str(input('Enter Your Password'))
#
#     def valid(self):
#         if self.t=='mail':
#             if self.mail.count('@')==1 and self.mail.count('.')<=2 and self.mail.endswith('.com'):
#                 print("Username is valid")
#         elif self.t=='phone':
#             if len(self.phone)==13:
#                 if self.phone.count('+')==1:
#                     print("Username is valid")
#         else:
#             print("Enter valid username")
#         if len(self.pwd)>=8:
#             for i in self.pwd:
#                 if i.isupper():
#                     if i.islower():
#                         if i.isdigit():
#                             if ord(i) in range(32,57) or (58,64) or (91,96) or (123,126):
#                                 print("Password is valid")
#         else:
#             print("Enter valid Password")
#     def validate(self):
#         if self.t=='mail':
#             print(f"Welcome Back: {self.mail}")
#         else:
#             print(f"Welcome Back {self.phone}")
#
# x=Login()
# x.enter()
# x.valid()
# x.validate()


# Q7(Doubt)
# l=['sun flower','lilly flower','Marigold flower','lion animal','tiger animal','eagle bird','snake animal','lotus flower','pigeon bird']
# d={}
# for i in range(0,len(l)):
#     a=l[i].split()
#     if a[1] not in d:
#         d[a[1]]=a[0]
#     if a[1] in d:
#         i+=1
# print(d)


# Q8
# l1=[2,3,5,7,5,2]
# l2=[5,4,2,7,8,4,5]
# a=[]
# for i in l1:
#     if i not in a:
#         a.append(i)
#     if i in a:
#         i+=1
# for j in l2:
#     if j not in a:
#         a.append(j)
#     if j in a:
#         j+=1
# print(a)



#Q9 (Doubt)
# s='hello guys good morning welcome to programming class'
# d={}
# for i in range(0,len(s)):
#     if s[i] in ('a','e','i','o','u'):
#         d['vowels']=[s[i]]
#         i+=1
#     else:
#         d['conso']=[s[i]]
#         i+=1
# print(d)


#Q10
# from abc import *
# class Student(ABC):
#     lst = ['QSP', 'JSP', 'PSPY']
#     names = ['Testing', 'Development']
#     @abstractmethod
#     def std_details(self,full_name,location,qualification,percentage):
#         ...
#     def std_intrest(self):
#         ...
#     def course(self):
#         ...
#     def final(self):
#         ...
#
# class Coaching(Student):
#     def __init__(self):
#         print("Welcome to Qspiders Counselling")
#     def std_details(self,full_name,location,qualification,percentage):
#         self.name=full_name
#         self.loc=location
#         self.qual=qualification
#         self.perc=percentage
#
#     def std_intrest(self):
#         i = str(input("Are you aware about any programming language?"))
#         if i in ('yes','y'):
#             self.j=str(input("Which language do you know?"))
#
#     def course(self):
#         print(f"We have 3 branches : {super().lst}")
#         self.b=str(input('Enter the branch you want : '))
#         print(f"We have 2 domains : {super().names}")
#         self.d=str(input("Enter The Domain : "))
#         if self.b in super().lst and self.d in super().names:
#             if self.b in ('QSP','qsp'):
#                 self.sub1=['manual testing','automation testing']
#                 print(f"In QSPY we have batches for: {self.sub1}")
#             elif self.b in ('jsp','JSP'):
#                 self.sub2=['Java Full Stack','Java Selenium']
#                 print(f"In JSP we have batches for: {self.sub2}")
#             elif self.b in ('pspy','PSPY'):
#                 self.sub3=['Python Full Stack','Python Selenium']
#                 print(f"In PSPY we have batches for: {self.sub3}")
#             else:
#                 print("Enter Valid Details!!!!")
#             self.c = str(input("Enter the preferred batch from above"))
#     def final(self):
#         print(f"Congratulations {self.name} For Joining {self.b}")
#         if 'Testing' in self.c:
#             print(f"Your Domain is : Testing")
#         else:
#             print(f"Your Domain is : Development")
#         print(f"Your batch is : {self.c}")
# x=Coaching()
# x.std_details("Akshay Warhade","Pune","MCA","80%")
# x.std_intrest()
# x.course()
# x.final()