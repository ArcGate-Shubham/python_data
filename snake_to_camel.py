# snake = "All_is_well"
# camel = snake.title().replace("_","")
# print(camel)
# x = camel[0].lower()
# print(camel.replace("[0]", x))





txt1 = "hello_this_city_is_udaipur_city"
li= txt1.split('_')
for x in range(1,len(li)):
    li[x] = li[x].title()
new_text =''.join(li)
print(new_text)