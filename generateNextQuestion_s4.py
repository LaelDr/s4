# s4.py

# ייבוא השאלות מקובץ questions.py
from questions import questions

# משתנה גלובלי לאינדקס השאלה הנוכחית
current_question_index = 0

# הגדרת מחלקה GlobalQuestionManager לניהול השאלות
class GlobalQuestionManager:
    def __init__(self):
        # כאן לא נאתחל את current_question_index בתוך המחלקה
        pass

    def get_next_question(self, include_options=False):
        # שימוש במשתנה הגלובלי
        global current_question_index

        # בדיקה אם יש עוד שאלות
        if current_question_index < len(questions):
            # שמירת השאלה הנוכחית
            question_data = questions[current_question_index]
            
            # עדכון האינדקס לשאלה הבאה
            current_question_index += 1

            # החזרת השאלה (עם או בלי האופציות לפי הצורך)
            if include_options:
                question_data['question_text'] = self.reverse_text(question_data['question_text'])
                return question_data
            else:
                return question_data['question_text']
        else:
            # אם נגמרו השאלות
            return "תודה רבה על השתתפותך"

    # פונקציה להיפוך הטקסט
    def reverse_text(self, text):
        return text[::-1]

# יצירת אובייקט גלובלי מהמחלקה
question_manager = GlobalQuestionManager()

# דוגמה לקריאה לפונקציה ללא אופציות
print(question_manager.get_next_question())

# דוגמה לקריאה לפונקציה עם אופציות
#print(question_manager.get_next_question(include_options=True))
