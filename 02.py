mevalar = ['olma', 'anor', ' bana', 'uzum']
meva = input('meva krit: ')

if meva in mevalar:
    print("bu meva mavjud")
else:
    mevalar.append(meva)

print(mevalar)