c = int(input())

for _ in range(c):
    name, force = input().split()
    
    if name == "Thor":
        print("Y")
    else:
        print("N")