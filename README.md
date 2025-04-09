# EduTrack
EduTrack is a educational tools development and this team is assigned to develop Student Feedback Manager

## Features

- **Feedback Submission (CLI):** Students can provide feedback through a simple command-line script (`feedback_entry.py`).
- **Data Storage (JSON):** Feedback data is currently stored in a local JSON file (`student_feedback.json`).
- **Basic Analysis (CLI):** Administrators can run a command-line script (`score_calculator.py`) to calculate the average overall and instructor ratings from the collected feedback.
- **Automated Testing:** Basic unit tests for the `score_calculator.py` are implemented using `pytest` (`test_score_calculator.py`).
- **Automated Testing Workflow:** A GitHub Actions workflow (`.github/workflows/test.yml`) is set up to automatically run `pytest` tests on code pushes and pull requests.
- **Version Control:** The project is managed using Git, with collaboration facilitated through GitHub.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git
- `pytest` (for running tests)

### Installation

1. Clone the repository:
   ```bash
   git clone [YOUR_REPOSITORY_URL_HERE]
