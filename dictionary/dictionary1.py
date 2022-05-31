person = {'name': 'Shubham',
          'address': 'Bhopal',
          'DOB': '24/08/1998',
          'contact': {
              'home': 5757347896,
              'personal': 7854646854,
              'office': 3546132547
          }
          }
for x, y in person.items():
    if(x == 'contact'):
        print(x, ":")
        for a, b in y.items():
            print("\t", a, ":", b)
    else:
        print(x, ":", y)
