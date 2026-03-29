#take 3 days temperature
first, second, third = map(int, input().split())

#define emojis
happy_emoji = ":)"
sad_emoji = ":("

#compare the temepratures and print the emoji

if first > second and second <= third:
    print(happy_emoji)

elif first < second and second >= third:
    print(sad_emoji)

elif first < second and second < third and (third - second) < (second - first):
    print(sad_emoji)

elif first < second and second < third and (third - second) > (second - first):
    print(happy_emoji)

elif first > sercond and second > third and (second - third) < (first - second):
    print(happy_emoji)

elif first > second and second > third and (second - third) < (first - second):
    print(sad_emoji)

elif first ==second and second < third:
    print(happy_emoji)

elif first == second and second > third:
    print(sad_emoji)

