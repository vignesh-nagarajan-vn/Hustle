# Side Hustle Matcher

**HUSTLE** is a flask web application that helps users find the best side hustle opportunities based on their resume. By uploading their resume, users can get matched with a relevant, specific side hustle and recieve a job on a freelancing site, like Fiverr or Upwork, that they can started on immediately.

## Features

- **Resume Upload:** Upload your resume in PDF, DOCX or txt format and recieve a personalized side hustle
- **Side Hustle Database:** Browse and filter through a vast databse of detailed side hustle
- **Job Matching:** Recieve a job that you can get started on immediately based on the skills and experiences mentioned in your resume

## How to Run the Project

### Prerequisites
- Python 3.x
- Virtual Environment (venv)
- VSCode

### Installation Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # For Mac or Linux OS
    source venv/bin/activate
    # For Windows
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    flask run
    ```

5. Open the app in your browser at `http://127.0.0.1:5000/`.
