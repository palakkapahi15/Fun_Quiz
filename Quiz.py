import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.load(content)

score = 0
for question_text in data:
    print(question_text["Question"])
    for index, options in enumerate(question_text["Options"]):
         print(index + 1,"-",options)
    user_choice = int(input("Enter your answer : "))
    question_text["user_coice"] = user_choice
    if question_text["user_choice"] == question_text["Correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    
    message = f"Your answer: {question_text['user_choice']},\n Correct answer: {question_text['Correct_answer']}"
    print(message)


print(data)
print(score, "/", len(data))