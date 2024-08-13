# 1. ორ მნიშვნელობას შორის თანაბარობა
print(5 == 5)      # True
print(10 == 5)     # False

# 2. ორ მნიშვნელობას შორის განსხვავება
print(5 != 5)      # False
print(10 != 5)     # True

# 3. ერთი მნიშვნელობა მეტია მეორეაზე
print(10 > 5)      # True
print(5 > 10)      # False

# 4. ერთი მნიშვნელობა ნაკლებია მეორეაზე
print(5 < 10)      # True
print(10 < 5)      # False

# 5. ერთი მნიშვნელობა მეტია ან თანაბარია მეორეაზე
print(10 >= 10)    # True
print(10 >= 5)     # True
print(5 >= 10)     # False

# 6. ერთი მნიშვნელობა ნაკლებია ან თანაბარია მეორეაზე
print(5 <= 10)     # True
print(10 <= 10)    # True
print(10 <= 5)     # False

# 7. ცვლადების შედარება
a = 20
b = 25
print(a == b)      # False
print(a != b)      # True
print(a > b)       # False
print(a < b)       # True
print(a >= b)      # False
print(a <= b)      # True

# 8. სია შედარებები
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [4, 5, 6]
print(list1 == list2)  # True
print(list1 != list3)  # True
print(list1 < list3)   # True (ვადების შედარება თანმიმდევრობით)
print(list1 <= list2)  # True
print(list1 > list3)   # False

# 9. სტრინგების შედარება
str1 = "apple"
str2 = "banana"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 > str2)   # False (ბოლო სიტყვა არსებითად სიტყვების შედარება)
print(str1 < str2)   # True
print(str1 >= str2)  # False
print(str1 <= str2)  # True

# 10. ლოგიკური ტიპის შედარებები
bool1 = True
bool2 = False
print(bool1 == bool2)  # False
print(bool1 != bool2)  # True
print(bool1 > bool2)   # True (True უფრო დიდია False-ზე)
print(bool1 < bool2)   # False
print(bool1 >= bool2)  # True
print(bool1 <= bool2)  # False

# 11. სია შედარებები სხვადასხვა სიგრძე
list4 = [1, 2]
list5 = [1, 2, 3]
print(list4 < list5)   # True
print(list4 > list5)   # False

# 12. სიის შედარება ცალკე ელემენტებზე
list6 = [1, 2, 3]
list7 = [1, 2, 4]
print(list6 < list7)   # True (პირველი განსხვავება არის მესამე ელემენტში)

# 13. სტრინგების სიგრძის შედარება
str3 = "apple"
str4 = "apples"
print(len(str3) == len(str4))  # False
print(len(str3) < len(str4))   # True

# 14. ტიპების შედარება
print(type(5) == type(10))     # True
print(type(5) != type("text")) # True

# 15. ცვლადების შედარება კალკულაციით
x = 10
y = 20
print(x + 5 == y)     # True
print(x - 5 != y)     # True
print(x * 2 > y)      # False

# 16. სტრინგების შედარება ინტეგერებზე
print("123" == str(123))  # True
print("123" != str(124))  # True

# 17. ცვლადების შედარება `None`-თან
a = None
b = 5
print(a == b)       # False
print(a != b)       # True
print(a is None)    # True
print(a is not None) # False

# 18. სიის ელემენტების შედარება
list8 = [1, 2, 3]
list9 = [1, 2, 3, 4]
print(list8 < list9)   # True
print(list8 == list9)  # False

# 19. ცვლადების შედარება ლოგიკური ოპერატორებით
a = 15
b = 10
print(a > 5 and b < 15)  # True
print(a > 20 or b < 15)  # True
print(not (a > 20))      # True

# 20. სტრინგების შედარება რეგულარული ნიმუშების მიხედვით
import re
print(re.match("^[a-zA-Z]*$", "Hello"))  # True (ხართ მხოლოდ ასოები)
print(re.match("^[0-9]*$", "1234"))     # True (ხართ მხოლოდ ციფრები)

# 21. ჩარჩოს შედარება
list10 = [1, 2, 3]
print(len(list10) >= 3)   # True

# 22. მარტივი ცვლადების შედარება
a = 10
b = 10.0
print(a == b)       # True (10-ის ინტეგერი და ფლოტი ერთნაირია)

# 23. ტექსტური ცვლადების შედარება
text1 = "abc"
text2 = "a" + "bc"
print(text1 == text2)  # True

# 24. ცვლადების შედარება შორის ლოგიკური ოპერატორები
x = 5
y = 10
print(x <= 5 and y > 8)  # True
print(x > 5 or y == 10) # True

# 25. ცვლადების შედარება ერთობლივი ოპერატორებით
a = 8
b = 16
print(a * 2 == b)  # True
print(a + b != 30) # True

# 26. სია შედარება სტრინგებთან
list11 = ["apple", "banana"]
list12 = ["apple", "banana", "cherry"]
print(list11 < list12)  # True
print(list11 > list12)  # False

# 27. ცვლადების შედარება სტრინგის ტიპით
x = "10"
y = "20"
print(x < y)    # True (სტრინგების შედარება ასოების მიხედვით)

# 28. `is` ოპერატორი
a = [1, 2, 3]
b = a
print(a is b)     # True (ორივე ვარიაბლი მითითებულია იმავე სიაში)

# 29. შედარებითი ოპერატორების გამოყენება ლოგიკური ფუნქციებით
def compare_values(x, y):
    return x < y

print(compare_values(5, 10))   # True
print(compare_values(10, 5))   # False

# 30. ცვლადების შედარება რეგულარული გამოხატულებებით
import re
pattern = re.compile(r'\d+')  # ციფრების ნიმუში
print(pattern.match("1234") is not None)  # True
print(pattern.match("abc") is None)  
