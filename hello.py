
def profile(name, age, *language):
    print("이름: {0} 나이: {1}\t".format(name,age), end="")
    for lang in language:
        print(lang)
    print()


profile("노현우", 25, "파이썬", "자바", "C", "C++", "C#")
profile("박기훈", 24, "코틀린", "스위프트","", "", "")
