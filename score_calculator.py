import json

def calculate_average_scores(filename="student_feedback.json"):
    """Calculates the average overall and instructor ratings from the feedback data."""
    overall_scores = []
    instructor_scores = []

    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    feedback = json.loads(line.strip())
                    if "overall_rating" in feedback and isinstance(feedback["overall_rating"], int):
                        overall_scores.append(feedback["overall_rating"])
                    if "instructor_rating" in feedback and isinstance(feedback["instructor_rating"], int):
                        instructor_scores.append(feedback["instructor_rating"])
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line: {line.strip()}")

        avg_overall = sum(overall_scores) / len(overall_scores) if overall_scores else 0
        avg_instructor = sum(instructor_scores) / len(instructor_scores) if instructor_scores else 0

        return avg_overall, avg_instructor

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

if name == "main":
    avg_overall, avg_instructor = calculate_average_scores()
    print("\n--- Average Scores ---")
    print(f"Average Overall Rating: {avg_overall:.2f}")
    print(f"Average Instructor Rating: {avg_instructor:.2f}")