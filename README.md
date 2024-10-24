# Side Hustle Matcher

**Side Hustle Matcher** is a web application that helps users find the best side hustle opportunities based on their resume. By uploading their resume, users can get matched with relevant job descriptions using NLP techniques like cosine similarity.

## Features

- **Resume Upload:** Upload your resume in PDF or DOCX format.
- **Job Matching:** Automatically find side hustles that best match your resume using cosine similarity.
- **Cosine Similarity Algorithm:** The application uses NLP to compare resumes with job descriptions, finding the best match based on the context and terminology.

## How to Run the Project

### Prerequisites
- Python 3.x
- Virtual Environment (venv)

### Installation Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
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

## Project Structure

