lines=[]
while True:
    try:
        num=input()
        if num.isdigit():
            lines.append(int(num))
    except EOFError:
        break

num=lines.pop(0)
for _ in range(num):
    amplitude=lines.pop(0)
    frequency=lines.pop(0)
    for f in range(frequency):
        for a in range(1,amplitude*2):
            if a > amplitude:
                count=abs(amplitude*2-a)
            else:
                count=a
            for _ in range(count):
                print(count,end='')
            print()
        if not(f==frequency-1 and not lines):
            print()