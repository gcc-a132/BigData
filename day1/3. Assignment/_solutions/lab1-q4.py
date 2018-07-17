some_of_my_favorite_dogs = {"Plato": {'address':'1234 Dog Avenue', 'phone':'1800DOG5555'},
"Jamilla": {'address':'4321 Dog Avenue', 'phone':'1800DOG5555'}}

for dog,attributes in some_of_my_favorite_dogs.items():
    print(dog)
    for key in some_of_my_favorite_dogs[dog]:
        print('\t',key,": ",some_of_my_favorite_dogs[dog][key])