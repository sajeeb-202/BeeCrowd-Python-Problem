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

elif A < B and B < C:
    if (C - B) < (B - A):
        print(sad_emoji)
    else:
        print(happy_emoji)

elif A > B and B > C:
    if (B - C) < (A - B):
        print(happy_emoji)
    else:
        print(sad_emoji)

else:  # A == B
    if C > B:
        print(happy_emoji)
    else:
        print(sad_emoji)