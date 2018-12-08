empty_list = [];
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
print(empty_list);
print(weekdays);
big_birds = ['emu','ostrich', 'cassowary'];
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael'];
print(first_names)

another_empty_list = list();
print(another_empty_list);

print(list('cat'));

a_tuple = ('ready', 'fire', 'aim');
print(list(a_tuple));
birthday = '1/6/1952';
print(birthday.split('/'));
splitme = 'a/b//c/d///e';
print(splitme.split('/'));

marxes = ['Groucho', 'Chico', 'Harpo'];
print(marxes[0]);
print(marxes[1]);
print(marxes[2]);
#print(marxes[3]);

print(marxes[-1]);
print(marxes[-2]);
print(marxes[-3]);

#list of list
small_birds = ['hummingbird', 'finch'];
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue'];
carol_birds = [3, 'French hens', 2, 'turtledoves'];
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds];
print(all_birds)
print(all_birds[0]);
print(all_birds[1])
print(all_birds[2])
print(all_birds[3])
print(all_birds[1][1]);

marxes = ['Groucho', 'Chico', 'Harpo'];
marxes[2] = 'Wanda';
print(marxes);

marxes = ['Groucho', 'Chico', 'Harpo'];
print('test:',marxes[0:2]);
print(marxes[::2]);
print(marxes[::-2]);
print(marxes[::-1])

marxes.append('Zeppo');
print(marxes);

others = ['Gummo', 'Karl']
marxes.extend(others);
print(marxes);

marxes += others;
print(marxes);

marxes.append(others);
print(marxes);
marxes = ['Groucho', 'Chico', 'Harpo'];
marxes.insert(3, 'Gummo');
print(marxes);

marxes.insert(10, 'Karl');
print(marxes);

del marxes[-1];
print(marxes);

marxes.remove('Gummo');
print(marxes);

marxes = ['Groucho', 'Chico', 'Harpo'];
marxes.pop();
print(marxes);

marxes = ['Groucho', 'Chico', 'Harpo'];
sorted_marxes = sorted(marxes);
print("sorted_marxes:{1}_{0}".format(sorted_marxes,"hello"));
marxes.sort(reverse=True);
print(marxes);

print(len(marxes));

#mutable
a = [1, 2, 3];
b = a.copy();
print(a);
#b = a;

a[0] = 'surprise';
print(a);
print(b);

#tuple
empty_tuple = ();
print(empty_tuple);


one_marx = "Groucho",
print(one_marx);

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

(a, b, c) = marx_tuple;
print(a);
print(b);
print(c);




