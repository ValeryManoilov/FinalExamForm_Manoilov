#INTRO TO IT 2nd COURSE
s = input("Введите строку: ").replace(' ', '').lower()
if s == s[::-1]:
    print("Строка является палиндромом")
else:
     print("Строка не является палиндромом")
