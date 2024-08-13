# 1. და სექვენციაში
x = True
y = False
print(x and y)   # False (საჭიროა ორივე ჭეშმარიტი, მაგრამ მეორე არის ფალსიური)

# 2. ან სექვენციაში
x = True
y = False
print(x or y)    # True (ერთ-ერთი მაინც ჭეშმარიტია)

# 3. არა სექვენციაში
x = True
print(not x)     # False (დააბრუნებს True-ს წინააღმდეგობას)

# 4. ორი პირობის ერთად გადაწყვეტა
a = True
b = True
c = False
print(a and b)    # True (ორივე ჭეშმარიტია)
print(a and c)    # False (ერთ-ერთი ფალსიური)

# 5. ორი ან პირობის გაწვდვა
a = False
b = True
c = True
print(a or b)     # True (ერთ-ერთი ჭეშმარიტია)
print(a or c)     # True (ერთ-ერთი ჭეშმარიტია)
print(a or (b and c))  # True (b და c ორივე ჭეშმარიტია, ამიტომ ან-ით ჭეშმარიტია)

# 6. გაწვდვა ეჭვიანი პირობების ჩართვით
a = True
b = False
c = True
print(not (a and b))  # True (a and b არის False, და არა იმავლის ჭეშმარიტია)
print(not (a or b))   # False (a or b არის True, და არა False)

# 7. მრავალპიროვნული პირობის გამოცდა
x = True
y = False
z = True
print(x and (y or z))   # True (y or z არის True, x and (y or z) ასევე True)

# 8. პირობის შეჯამება ერთვის მაგისტრატიურ პირობებს
a = True
b = True
print((a or b) and (not b))  # False ((a or b) არის True, მაგრამ (not b) არის False)

# 9. სრული შეცდომა
x = False
y = False
print(not (x or y))   # True (x or y არის False, ამიტომ არა ჭეშმარიტია)

# 10. ან-თან პარალელური პირობების გაწვდვა
x = True
y = False
z = True
print((x and y) or z)    # True (x and y არის False, მაგრამ z არის True)
