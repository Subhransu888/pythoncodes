lloyd={"name":"lloyd",
"homework":[90.0,97.0,75.0,92.0],
"quizzes":[88.0,40.0,92.0],
"tests":[75.0,90.0]}
alice={"name":"alice",
"homework":[100,92,98,100],
"quizzes":[82,83,91],
"tests":[89,97]}
tyler={"name":"tyler",
"homework":[0,87,75,22],
"quizzes":[0,75,78],
"tests":[100,100]}
list=[lloyd,alice,tyler]
for list in list:
    print(f"student name: {list['name']}")
    print(f"homework: {list['homework']}")
    print(f"quizzes: {list['quizzes']}")
    print(f"tests: {list['tests']}")