txt1 = "hello_this_city_is_udaipur_city"
li= txt1.split('_')
for x in range(1,len(li)):
    li[x] = li[x].title()
new_text =''.join(li)
print(new_text)