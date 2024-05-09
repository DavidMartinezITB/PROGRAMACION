vouels  = 'aeiou'
text    = input()

for t in text.lower():
    for v in vouels:
        if t == v:
            print(t, end='')

print()