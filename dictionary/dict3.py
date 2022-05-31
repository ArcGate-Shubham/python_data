zudio = {'men': {'name': 'Vijay',
                 'address': 'Udaipur',
                 'product': 'Pants'
                 },
         'women': {'name': 'shubham',
                   'address': 'Ajmer',
                   }
        }
for x, y in zudio.items():
    print(x, ":",)
    for a, b in y.items():
        print("\t", a, ":", b)
