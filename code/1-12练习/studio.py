# print("Hello World")#用于输出
# print("Hello Again")
# print("I like typing this.")
# print("This is fun.")
# print('Yay! Printing.')
# print("I'd much rather you 'not'.")
# print('I"said"do not touch this.')

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90

# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car, "in each car.")


# message = "hello world"
# print(message)

# message = "hello python world"
# print(message)


# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print("Hello,",full_name.title())


# favorite_language = ' t python t '
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())


# message = "eric"
# print("Hello",message.title(),",would you like to learn soime Python today?")


# message = "eric"
# aller = "ior"
# allur = f"{aller} {message}"
# print(allur.lower())
# print(allur.title())
# print(allur.upper())


# a = "albert"
# b = "Einstein once said,\"A person who never made a mistake never tried anything new.\""
# print(a.title(),b)


# a = "alberteinstein"
# b = "once said:\n\t\"A person who never made a mistake never tried anything new.\""
# print(a.title(),b)


# filename = "python_notes.txt"
# u = f"{filename.removesuffix('.txt')}"
# print(u)


# print(6+2)
# print(3.2+4.8)
# print(1_00-92.0)
# MEN = 300
# a,b = 298.0,4
# print((MEN-a)*b)


# MEN = 7
# print("我最喜欢的数字是",MEN)


# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(f"我最喜欢的自行车是{bicycles[-1].title()}")


# names = ['ben', 'ken', 'kily']
# print(names[0].title())
# print(names[1].title())
# print(names[-1].title())
# print(f"Hello,I\'m {names[0].title()}")


# names = ['ben', 'ken', 'lucy', 'kily']
# a = f"我希望可以邀请{names}来参加晚宴。"
# b = f"我知道了{names[1].title()}来不了了"
# names[1] = 'curry'
# c = f"所以我又邀请了{names[1].title()},所以最终名单是{names}"
# print(a,b,c)
# names.append('kd')
# names.insert(3, '汤普森')
# names.append('winson')
# d = f"我订到了一个更大的餐桌，所以我又邀请了{names[-1].title()},{names[-2].upper()},{names[3]}"
# print(d)
# names_pop = names.pop()
# e = f"{names_pop.title()}我很抱歉你不能来参加我的晚宴"
# print(e)
# names_pop = names.pop()
# e = f"{names_pop.title()}我很抱歉你不能来参加我的晚宴"
# print(e)
# names_pop = names.pop()
# e = f"{names_pop.title()}我很抱歉你不能来参加我的晚宴"
# print(e)
# names_pop = names.pop()
# e = f"{names_pop.title()}我很抱歉你不能来参加我的晚宴"
# print(e)
# names_pop = names.pop()
# e = f"{names_pop.title()}我很抱歉你不能来参加我的晚宴"
# print(e)
# f = f"{names}你们两个也不在在邀请名单中"
# del names[0]
# del names[0]
# g = f"所以我的邀请名单是{names}"
# print(f,g)
# h = len(names)
# print(h)


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)



# pizzas = ['er', 'erw', 'ert']
# for pizza in pizzas:
#     print(f"我喜欢的披萨是{pizza}")
# friend_like = pizzas[:]
# pizzas.append('sdfj')
# friend_like.append('fjie')
# print('My favorite pizzas are:')
# print(pizzas)
# print("My friend's favorite pizzas are:")
# print(friend_like)

    

# a = ['c三亚', 's西藏', 'b成都', 'g上海', 'a哈尔滨']
# print(a)
# print(sorted(a))
# print(a)
# print(sorted(a,reverse=True))
# print(a)
# a.reverse()
# print(a)
# a.reverse()
# print(a)


# for value in range(6):
#     print(value)


# a = list(range(0,20,5))
# print(a)



# squares = []
# for value in range(1,11):
#     print(value ** 2)


# for value in range(1,21):
#     print(value)


# a = []
# for a in range(1,1_000_000):
#     print(a)


# a = list(range(1,1_000_000))
# print(a)
# b = min(a)
# c = max(a)
# d = sum(a)
# print(b,c,d)


# for a in list(range(1,21,2)):
#     print(a)


# numbers = list(range(3, 31, 3))

# for number in numbers:
#     print(number)


# a = []
# for vallue in range(1,11):
#     vallues = vallue**3
#     a.append(vallues)
#     print(a)

# for vallue in range(1,11):
#     print(vallue**3)


# a = [vallue**3 for vallue in range(1,11)]
# print(a)
# print("The first three items in the list are:")
# print(a[:3])
# print("Three items from the middle of the list are:")
# print(a[4:7])
# print("The last three items in the list are:")
# print(a[-3:])


# pizzas = ['food', 'fruit', 'jdij']
# for pizza in pizzas:
#     print(f'{pizza}')
# b_a = pizzas
# for b in b_a:
#     print(b)



# foods = ('water', 'apple', 'banana', 'hambergous', 'coke')
# for food in foods:
#     print(food)
# #foods[0] = 'chilcken'#无法更改
# foods = ('water', 'tomato', 'banana', 'milk', 'coke')
# print("the next are")
# for food in foods:
#     print(food)


# car = 'subaru'
# if car == 'subaru':
#     print("Is car == 'subaru'? I predict True")
# else:
#     print(car == 'subaru')


# age_1 = 19
# age_2 = 19
# if age_1 >= 20 or age_2 >=22:
#     print("True")
# else:
#     print("False")



# can_speak = ['ben', 'ken', 'kily']
# user_1 = 'Kd'
# if user_1.lower() in can_speak:
#     print("you can speak")
# else:
#     print("you can't speak in there")



# alien_color = ['green', 'red', 'yellow']
# monster = 'red'
# if monster in 'green':
#     print("you take 5 second")
# elif monster in 'red':
#     print("you take 8 second")
# elif monster in 'yellow':
#     print("you take 10 second")



# age = 0
# if age < 2:
#     print('baby')
# elif age < 4:
#     print('small children')
# elif age < 13:
#     print('children')
# elif age < 18:
#     print('teenager')
# elif age < 65:
#     print('emmmm')
# elif age >= 65:
#     print('old people')



# requested_toppings = ['tomato']

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")



# a = ['admin', 'ben', 'kily', 'kd', 'curry']
# user = 'jdifj'
# if user in a:
#     print(f"Hello {user.title()}")
# else:
#     print("Hello, jfdijfdi")



# current_users = ['ben', 'ken', 'jfid', 'fjidjf', 'jfijde']
# new_users = ['jfid', 'Jdifdj', 'iowej', 'Ben', 'djifjdi']
# for new_user in new_users:
#     print(new_user)
#     if new_user.lower() in current_users:
#         print("you can't")
#     else:
#         print("ok")



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for xushu in a:
#     if xushu == 1:
#         print(f"{xushu}st")
#     elif xushu == 2:
#         print(f"{xushu}nd")
#     elif xushu == 3:
#         print(f"{xushu}rd")
#     else:
#         print(f"{xushu}th")


# #第六章
# # #6.1,6.2.1，6.2.2
# alien_0 = {'color': 'gerrn', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# #6.2.3
# alien_0= {}
# alien_0['color']= 'green'
# alien_0['points'] = 5
# print(alien_0)


# #6.2.4
# alien_0 = {'color': 'green'}
# print(alien_0['color'])
# alien_0['color'] = 'yellow'
# print(alien_0['color'])

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(alien_0['x_position'])


# #6.2.5
# alien_0 = {'xlolr': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)


# # #6.2.6
# favorits_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'esward': 'rust',
#     'phil': 'python',
#     }
# language = favorits_languages['sarah'].title()
# print(language)
# for name in sorted(favorits_languages.keys()):
#     print(f"{name.title()},thank yyou for taking the poll.")
# print("The following languages have been mentioned:")
# for language in set(favorits_languages.values()):
#     print(language.title())


# alien_0 = {'color': 'green', 'speed': 'slow', 'points':2}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


# #练习
# a = {'name': 'Ben', 'age': 19, 'city': 'york'}
# print(a['name'],a['age'],a['city'])
# b = {'ben': 3,'ken': 4, 'kliy': 7}
# print(b['ben'],b['ken'], b['kliy'])


# #6.3.1
# user_0= {
#     'username': 'sfermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }
# for key, value in user_0.items():
#     print(f"\nKey{key}")
#     print(f"value{value}")
# for key in user_0:
#     print(key)



# #练习
# a = {'h': 'jidfjd', 'b': 'ifje','i': 'jefi', 'd': 'ifje'}
# for v in a.keys():
#     print(f"The {v.title()} runs thorough {v.title()}")
# for v in a:
#     print(v)
# for d in a.values():
#     print(d)
# for v,d in set(a.items()):
#     print(v,d)



# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)


# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color']
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of aliens: {len(aliens)}")

# #6.4.2
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")


# #练习
# a = {'dog': 'ben', 'cat': 'ken', 'bear': 'kily'}
# for pet,name in a.items():
# #     print(pet,name)
# favorite_places = {'ben':['sanya','xizang','beijing'], 'ken': ['tianjin','shanghai','haikou'], 'kily':['everywhere']}
# for name,want_to_go in favorite_places.items():
#     print(f"{name} wang to go {want_to_go}")



# #7.1
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# name = input("Please enter your name:")
# print(f"\nHello, {name}!")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello,{name}!")


# #7.1.2
# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("True")
# elif age < 18:
#     print("no")


#7.1.3
# number = input("Enter a number, and I'll tell you if it's even or odd:")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"\nThe number {number} is odd.")


# #练习
# car = input("What car do you wang")
# # print(f"Let me see if I can find you a {car}")
# people = input("How many people will come on?")
# people = int(people)
# if people > 8 :
#     print("We can't have enoth table")
# else:
#     print("ok, wo have enoth table to give you")
# number = input("please give me a number?")
# number = int(number)
# n_1 = number % 10
# if n_1 == 0:
#     print("yes")
# else:
#     print("no")



# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


#7.2.2,7.2.3
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the propram."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         actiove = False
#     else:
#         print(message)


# #7.2.4
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# #7.2.5
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 ==0:
#         continue 
#     print(current_number)    



# x = 1
# while x <= 5:
#     print(x)



# message = ''
# while message != 'ok':
#     message = input('what do you want?')
#     if message != 'ok':
#         print(f"ok,I will take {message} in your pizza.")



# message = ''
# while True:
#     message = input("How old are you?")
#     message = int(message)
#     if message < 3:
#         print("you are free")
#     elif message < 10:
#         print("you should give 10 dollor")
#     elif message < 12:
#         print("you should give 15 dollor")
#     else:
#         print("sorry, this is children movie")


#7.3.1
# a = ['alice','ben','ken']
# b = []
# while a:
#     a_b = a.pop()
#     print(f"verifying user: {a_b.title()}")
#     b.append(a_b)
# print("\nThe following users have been confirmed:")
# for bs in b:
#     print(bs.title())



# #7.3.2
# pets = ['dog', 'cat','dog', 'goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)



# #7.3.3
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat id your name")
#     response = input("Whice mountain would you like to climb someday?")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond?(yes/no)")
#     if repeat == 'no':
#         polling_active = False
#     print("\n--- Poll Tesults ---")
#     for name, response in responses.items():
#         print(f"{name} would lik eto climb{response}")


# # 生成两个列表
# sandwich_orders = ['jfidj','jfdij','djfidk','djifjdfff','jfidj']
# finshid_sandwiches = []

# # 遍历并打印列表
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order} pizza")

# # 通过循环将jfidj从列表中删除
# while 'jfidj' in sandwich_orders:
#     sandwich_orders.remove('jfidj')

# # 打印语句
# print("I'm sorry, we not have jfidj")

# # 将第一个列表转移到第二个列表
# while sandwich_orders:
#     ad = sandwich_orders.pop()
#     finshid_sandwiches.append(ad)

# #遍历转移后的列表后打印
# for finshid_sandwich in finshid_sandwiches:
#     print(f"your {finshid_sandwich} is ok")



# def greet_user():
#     print("Hello!")
# greet_user()
# greet_user()


# c = []
# a = 1
# b = 1
# while b != 10:
#     c.append(f"{a}*{b}={a*b}")
#     if a==b:
#         a = 1
#         b += 1
#         print(c)
#         del c[:]
#     else:
#         a += 1



# c = []
# a = 1
# b = 1
# while a != 10:
#     while b <= 2:
#         b += 1
#     print(f"{a}*{b}={a*b}")



#8.1.1
# def greet_user(username):
#     print(f"Hello, {username.title()}")
# greet_user('jesse')


# def message(jidfj):
#     print(f"ji{jidfj}")
# message('函数')


# def favorite_book(book):
#     print(f"One of my favorite bools is {book} in Wonderland")
# favorite_book('Alice')


# def describe_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet('hamster','harry')
# describe_pet('idjjf','djifj')


# def d(pet_name,animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# d(pet_name='wolloe',animal_type='n')


# def make_shirt(a,b='I love Python'):
#     print(f"\nni de chima shi{a}")
#     print(f"ni de chi ma {a} ke yi ying {b}")
# make_shirt(123,'jidfjidj')
# make_shirt(b='jdifjdi',a=3223)
# make_shirt(a=3223)


# def describe_city(city_name,f='china'):
#     print(f"{city_name.title()} is in {f.title()}")
# describe_city(city_name='shanghai')
# describe_city('beijing')
# describe_city(f='new york',city_name='america')



# def get_formatted_name(first_name,last_name,middle_name=''):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)



# def build_person(first_name,last_name, age=None):
#     person={'first': first_name, 'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix',age=27)
# print(musician)



# def get_formatted_name(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def city_country(name,country):
#     answer = f"{name},{country}"
#     return answer.title()
# a = city_country('shanghai','china')
# print(a)


# def make_album(name,music,number):
#     a = {'first':name,'second':music,'third':number}
#     return a 
#     while True:
#       print("\nPlease tell me his/her name and music ,and you can tell me number")
#       print("(enter 'q' at any time to quit)")
#       n = input()
#       if n == "q":
#           break
#       m = input("second")
#       if m == "q":
#           break
#       n2 = input("third")
#       if n2 == "q":
#           break
#       b = make_album(n,m,n2)
#       print(b)
    



# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)




# def print_models(unprinted_desiges,completed_models):
#     while unprinted_desiges:
#         current_design = unprinted_desiges.pop()
#         print(f"Printing model:{current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_desiges,completed_models)
# show_completed_models(completed_models)




# def make_pizza(*toppings):
#     print(toppings)
# make_pizza('peperoni')
# make_pizza('mushrooms', 'green pepers', 'extra cheese')



# def make_album(name,music,number=""):
#     if number:
#         return {'f': name ,'d':music,'q':number}
#     else:
#         return {'f': name ,'d':music}
# while True:
#     print("if you want to break,please attack 'o'.")
#     s = input("name")
#     if s == 'o':
#         break
#     p = input("music:")
#     if p == 'o':
#         break
#     w = input("number")
#     if w == 'o':
#         break
#     a = make_album(s.title(),p,w)
#     print(a)




# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)



# def show_message(things,sent):
#     for thing in things:
#         print(thing)
#     a = things[:]
#     print(f"我转移了{a}")
#     sent.append(a)
# def sent_messages(sent):
#     print("\nThe following models have been printed")
#     for sen in sent:
#         print(sen)
#     print(f"原列表{things}")
# things = ['djfi', 'jfdisfjd', 'djfifjdi','dfijsjf', 'eifwiufhuhr']
# sent = []
# show_message(things,sent)
# sent_messages(sent)




# def make_pizza(*toppings):
#     print("\nMaking a pozza with the following topping:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushroomas', 'green peppers', 'extra cheese')



# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f"{b}*{a}={a*b}",end=' ')
#     print()


# def print_message(message):
#     print(message)
#     print_message(message+1)

# m = 23
# print_message(m)


# def number_manager():
#     num = []
#     h = []
#     while True:
#         print("输入整数，当输入0时停止")
#         number = int(input("请输入："))
#         if number == 0:
#             break
#         else:
#             if number % 2 == 0:
#                 h.append(number)
#             num.append(number)

#     a = 0
#     while a < len(num):
#         print(num[a])
#         a += 1

#     total = 0
#     count = 0
#     i = 0
#     while i < len(num):
#         total += num[i]
#         count += 1
#         i += 1
#     print(total,count)
# number_manager()



# def login_system():
#     a = {'小明':"123",'小美':"abc"}
#     while True:
#         name = input("请输入用户名：")
#         if name not in a:
#             print("用户名错误，请重新输入：")
#             continue
#         i = 0
#         while i < 3:
#             ne = input(f"{name}，请输入密码：")
#             if a[name] == ne:
#                 print("密码正确")
#                 return
#             else:
#                 i += 1
#                 b = 3-i
#                 print("密码错误")
#                 if b > 0:
#                     print(f"你还有{b}次机会")
#         print("已锁定")
#         break
# login_system()






# def login_system():
#     name = ['小明',"123",'小美',"abc"]
#     while True:
#         a = input("请输入用户名")
#         if a == '小明':
#             i = 0
#             while i < 3:
#                 num = input("请输入密码")
#                 if num == "123":
#                     print("密码正确")
#                     i = 3
#                     return   
#                 else:
#                     print("密码错误，请重试")
#                     i += 1
#             print("账户已锁定")
#             break
#         elif a == '小美':
#             i = 0
#             while i < 3:
#                 num = input("请输入密码")
#                 if num == "abc":
#                     print("密码正确")
#                     return
#                 else:
#                     print("密码错误，请重试")
#                     i += 1
#             print("账户已锁定")
#             break
#         else:
#             print("用户名错误")
# login_system()





#     def cart_calculator():
#     prices = {"苹果": 5, "香蕉": 3, "可乐": 4}
#     cart = []
#     while True:
#         info = input("请输入 商品名 数量: ")
#         if info == "结束":
#             break
#         parts = info.split() 
#         if len(parts) != 2:
#             print("格式不对")
#             continue
#         name = parts[0]
#         if not parts[1].isdigit():
#             print("数量必须是数字")
#             continue
#         qty = int(parts[1])
#         if name not in prices:
#             print("无此商品")
#         else:
#             cart.append((name, qty))
#             print(f"已加入 {name} x {qty}")
#     i = 0
#     total = 0
#     print("\n购物清单")
#     while i < len(cart):
#         name, qty = cart[i]
#         price = prices[name]
#         subtotal = price * qty
#         total += subtotal
#         print(f"{name} 单价{price}元 x {qty} = {subtotal}元")
#         i += 1
#     print(f"总价: {total}元")
# cart_calculator()



# def split_number():
#     i = 0
#     a = []
#     b = []
#     c = []
#     while i < 11:
#         f = int(input("请输入一个整数："))
#         try:
#             d = int(f)
#         except:
#             print("输入错误，请重新输入")
#             return
#         if d < 0 :
#             a.append(d)

#             i += 1
#         elif d > 0:
#             b.append(d)
#             i +=1 
#         elif d == 0:
#             b.append(c)
#             i += 1
#     print("ok")
#     print(a,sum(a))
#     print()
#     print(b,sum(a))
#     print()
#     print(c,len(c))
# split_number()




# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f"{b}*{a}={a*b}",end=' ')
#     print()


# def phone_book():
#     c = {'小明': "13800001111", "小红": "13800002222"}
#     while True:
#         a = input("请输入用户名：，或添加，退出")
#         if a == "退出":
#             return
#         elif a in c:
#             print(c[a])
#             phone_book()
#         elif a == "添加":
#             b = input("请输入用户名：")
#             while True:
#                 d = (input("请输入号码："))
#                 try:
#                     s = float(d)
#                     c[b] = s
#                     print("添加成功")
#                     break
#                 except ValueError:
#                     print("输入错误，请重试")
#         else:
#             print("查无此人")
#             phone_book()
# phone_book()




# a = 1000

# def check_balance():
#     print(f"当前余额为：{a}")

# def deposit():
#     global a
#     b = int(input("你想存多少钱："))
#     if b <= 0:
#         print("错误")
#     else:
#         a += b
#         print(f"存钱成功,存入金额为{b},余额为{a}")

# def withdraw():
#     c = int(input("你想取多少钱："))
#     global a
#     if c <= 0 :
#         print("错误")
#     else:
#         if c <= a:
#             a -= c
#             print("取款成功")
#         else:
#             print("余额不足")

# def exit_atm():
#     print("感谢使用")

# while True:
#     d = input("1.查询余额\n2.存钱\n3.取钱\n4.退出\n请选择")
#     # 查询余额
#     if d == "1":
#         check_balance()

#     # 存钱
#     elif d == "2":
#         deposit()

#     # 取钱 
#     elif d == "3":
#         withdraw()

#     # 退出
#     elif d == "4":
#         exit_atm()
#         break



# name = '勇者'
# hp = 100
# max_hp = 100
# atk = 20
# defense = 5
# level = 1
# exp = 0
# exp_to_next = 30

# def show_status():
#     print(f"----角色状态-----\n{name}\n等级：{level}\n血量：{hp}\n攻击力：{atk}\n防御力：{defense}\n经验值：{exp}/{exp_to_next}")

# def rest():
#     global hp
#     hp = max_hp
#     print(f"{name}休息了一下，血量已回满")

# def gain_exp(amount):
#     global exp
#     exp += amount
#     if exp >= exp_to_next:
#         new_exp = exp % exp_to_next
#         level_count = (exp - new_exp)/exp_to_next
#         exp = new_exp
#         level_up(level_count)
#     return

#     #     a = exp % exp_to_next
#     #     q = exp
#     #     exp = a
#     #     q -= a
#     #     w = q/exp_to_next
#     #     level_up()
#     # return

# def level_up(level_count):
#     global level,atk,max_hp,defense
#     level += level_count
#     atk += 5
#     max_hp += 20
#     defense += 2
#     print(f"恭喜升级，当前等级为{level}")

# def attack_enemy(enemy_defense,enemy_atk,enemy_hp):
#     global atk,hp
#     while True:
#         damage = atk - enemy_defense
#         if damage < 1:
#             damage = 1
#         enemy_hp -= damage
#         if enemy_hp <= 0:
#             print("击败敌人，获得20经验值！")
#             b = 20
#             gain_exp(20)
#             return
#         else:
#             enemy_damage = enemy_atk - defense
#             if enemy_damage < 1:
#                 enemy_damage = 1
#             hp -= enemy_damage
#             print(f"你造成了{damage}的伤害，受到了{enemy_damage}的伤害，敌人剩余血量为{enemy_hp}")
#             if hp <= 0:
#                 print("你被击败了")
#                 return
            

# def battle_loop():
#     while True:
#         if hp <= 0:
#             print("游戏结束")
#             break
#         s = input("1.查看状态\n2.休息\n3.攻击敌人\n4.退出游戏\n请选择：")
#         if s == "1":
#             show_status()
#         elif s == "2":
#             rest()
#         elif s == "3":
#             enemy_hp = 30 + level*10
#             enemy_damage = 8 + level*3
#             enemy_defense = 2 + level*1
#             print(f"你遇到了一个敌人血量为：{enemy_hp}，攻击力为：{enemy_damage}，防御力为：{enemy_defense}")
#             attack_enemy(enemy_defense,enemy_damage,enemy_hp)
#         elif s == "4":
#             print("感谢游玩")
#             break
#         else:
#             print("无效输入")

# battle_loop()




# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is new sitting.")
#     def roll_over(self):
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog('ifjdji', 9)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old")
# print(f"\nYour dog's name is {your_dog.name}")
# print(f"Your dog is {your_dog.age} years old.")

# my_dog.sit()
# my_dog.roll_over()

# your_dog.sit()




# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type =cuisine_type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print(self.restaurant_name,self.cuisine_type)
#     def open_restaurant(self):
#         print(f"{self.restaurant_name}正在营业")
#     def read_number(self):
#         print(f"have {self.number_served} people")
#     def upper(self,number_upper):
#         self.number_served = number_upper
#     def increment_number_served(self,miles):
#         self.number_served += miles

# my = Restaurant('djfijd','jidjfid')
# my.describe_restaurant()
# my.open_restaurant()
# my.upper(10)
# my.read_number()
# my.increment_number_served(50)
# my.read_number()


# class User:
#     def __init__ (self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print(f"{self.first_name},{self.last_name}")
#     def greet_user(self):
#         print(f"{self.first_name},Hello")
#         print(self.last_name)

# m = User('jidfjf','djifjd')
# m.describe_user()
# m.greet_user()



# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

# class Battery:
#     def __init__(self, battery_size=40):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")    

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = Battery()
#     # def describe_battery(self):
#     #     print(f"This car has a {self.battery_size}")
# # my_new_car = Car('ausi', 'a4', 2024)
# # print(my_new_car.get_descriptive_name())
# # my_new_car.update_odometer(23)
# # my_new_car.read_odometer()

# # class Battery:
# #     def __init__(self, battery_size = 40):
# #         self.battery_size = battery_size
# #         super.battery = Battery()
# #     def describe_battery(self):
# #         print(f"This car has a {self.battery_size}—lWh battery.")
# #     def get_range(self):
# #         if self.battery_size == 40:
# #             range = 150
# #         elif self.battery_size == 65:
# #             range = 225
# #         print(f"This car can go about {range} miles on a full charge.")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# # my_leaf.battery.get_range()



# from pathlib import Path
# path = Path('text_files/filename.txt')
# contents = path.read_text()
# contents = contents.rstrip()
# print(contents) 


# from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# for line in lines:
#     print(line)


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")



# while True:
#     try:
#         a = int(input("请输入第一个整数："))
#         b = int(input("请输入第二个整数："))
#         print(f"结果为：{a/b}")
#     except ValueError:
#         print("你输入的不是整数")

# try:
#     from pathlib import Path
#     path = Path('dogs.txt')
#     a = path.read_text()
#     path = Path('cats.txt')
#     b = path.read_text()
#     print(a,b)
# except FileNotFoundError:
#     pass



# from pathlib import Path
# import json
# def get_stored_username(path):
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads 



# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def m_c(self):
#         print("fachushengyin")
# class Dog(Animal):
#     def __init__(self, name     , bread):
#         super().__init__(name)
#         self.bread = bread     

   



#     def m_c(self):
#         print(self.bread,self.name)

# dog = Dog("jidfj","jidffjd")
# dog.m_c()

