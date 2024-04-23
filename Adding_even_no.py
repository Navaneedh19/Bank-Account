#target = int(input())
# even_sum = 0
# for n in range (2, target, 2):
#    print(n)
#    even_sum += n
# print(even_sum)

target = int(input())
alternative_sum = 0
for n in range(1, target+1):
   if n % 2 == 0:
    alternative_sum += n
print(alternative_sum)
