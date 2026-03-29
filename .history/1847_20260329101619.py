#take 3 days temperature
A, B, C = map(int, input().split())

#define emojis
happy_emoji = ":)"
sad_emoji = ":("

#compare the temepratures and print the emoji

if A > B and B <= C:
    print(happy_emoji)

elif A < B and B >= C:
    print(sad_emoji)

elif A < B and B < C and (C - B) < (B - A):
    print(sad_emoji)

elif A < B and B < C and (C - B) > (B - A):
    print(happy_emoji)

elif A > sercond and B > C and (B - C) < (A - B):
    print(happy_emoji)

elif A > B and B > C and (B - C) < (A - B):
    print(sad_emoji)

elif A ==B and B < C:
    print(happy_emoji)

elif A == B and B > C:
    print(sad_emoji)

