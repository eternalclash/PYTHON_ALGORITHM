while True:
    n=input()
    stack=[]
    t=True
    if n==".":
        break
    else:
        for i in range (len(n)):
            if n[i]=="(" or n[i]=="[":
                stack.append(n[i])
            elif n[i]==")" or n[i]=="]":
                if stack:
                    if n[i]==")" and stack[-1]=="(":
                        stack.pop()
                    elif n[i]=="]" and stack[-1]=="[":
                       stack.pop()
                    else:
                      t=False
                      break
                else:
                    t=False
                    break
    if not t:
        print("no")
    else:
        if len(stack)==0:
            print("yes")
        else:
            print("no")

