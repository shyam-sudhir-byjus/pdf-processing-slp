import re

def clean_questions_beginning(questions):
    remove_serial_nums_alphas = r"^(?:\d+[\).]|[\w]+[).])\s*"  
    
    for i, question in enumerate(questions):
        question = re.sub(remove_serial_nums_alphas, "", question)
        questions[i] = question

    return questions

if __name__ == "__main__":        
    questions = [
        "1) What is your name?",
        "2. How old are you?",
        "i) Where were you born?",
        "ii. What is your favorite color?",
        "a) Have you traveled abroad?",
        "b. Do you like to read?",
    ]

    print(clean_questions_beginning(questions))