# arrays programs
# Author- Siba prasad Pradhan

numbers = [10,20,30,40,50];

print(numbers[1]);

print(numbers[4]);


#numbers[4]='siba';

for num in numbers:
	print(num);

for i in range(len(numbers)):
	print(numbers[i]);

print(numbers[0:2]);


print(numbers[:]);

print(numbers[:-1]);

print(numbers[:-2]);

maximum=numbers[0];
for num in numbers:
	if num > maximum:
		maximum=num;
print (maximum);





