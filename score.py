score = int(input("Give me your score: "))

if score > 100:
    print("wrong score")
elif 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
else:
    print("D")


