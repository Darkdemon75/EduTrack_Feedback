import datetime

def collect_feedback():
    """Collects student feedback and saves it to a file."""
    student_id = input("Enter your Student ID: ")
    course_name = input("Enter the Course Name: ")
    feedback_text = input("Please provide your feedback: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    feedback_data = f"Timestamp: {timestamp}\n"
    feedback_data += f"Student ID: {student_id}\n"
    feedback_data += f"Course: {course_name}\n"
    feedback_data += f"Feedback: {feedback_text}\n"
    feedback_data += "---\n"

    try:
        with open("student_feedback.txt", "a") as f:
            f.write(feedback_data)
        print("Thank you for your feedback!")
    except Exception as e:
        print(f"Error saving feedback: {e}")

if __name__ == "__main__":
    collect_feedback()