List = ["Spiderman 2", "Joker", "Infinity War", "Conjuring", "Horrible Bosses 2"]
print(List)
x = input('Enter your Favorite Movie too add to the list:')
List.append(x)
print(List)
print("That's your Movie List")
# code written here is to add movie to list
for x in range(len(List)):
    print(f"movie # {x}. Selection Choice: {List[x]}.")
m = input('Enter another movie ')
y = input('which movie do you want to remove: select # from 0-5 ')
for x in range(len(List)):
    if (x == int(y)):
        string = List[x]
        print(f"movie # {x}. Selection Choice: {string.replace(List[x], m)}.")

    elif (x != int(y)):
        print(f"movie # {x}. Selection Choice: {List[x]}.")

# code written below is to remove movie from list
for x in range(len(List)):
    print(f"movie # {x}. Selection Choice: {List[x]}.")
#m = input('Enter another movie ')
y = input('which movie do you want to replace: select # from 0-5 ')
for x in range(len(List)):
    if (x == int(y)):
        string = List[x]
        print(f"movie # {x}. Selection Choice: {string.replace(List[x], '')}.")

    elif (x != int(y)):
        print(f"movie # {x}. Selection Choice: {List[x]}.")

