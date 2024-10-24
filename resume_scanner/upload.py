import PyPDF2
import docx
import os
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    return text

# Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])

# Download job description from URL
def download_job_description(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract job description (look for text under sections like "requirements" or "qualifications")
            for header in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
                if "requirements" in header.text.lower() or "qualifications" in header.text.lower():
                    requirements_section = header.find_next("ul")
                    if requirements_section:
                        return ' '.join(li.text for li in requirements_section.find_all("li"))
            return soup.get_text()
        return None
    except Exception as e:
        print(f"Error fetching job description from {url}: {e}")
        return None

# List of Web Developer Jobs URLs
web_dev_jobs = [
    {
        "title": "Shopify Website Development for Healthcare ePharmacy",
        "url": "https://www.upwork.com/freelance-jobs/apply/Shopify-Website-Development-for-Healthcare-ePharmacy_~021847949972282521574/"
    },
    {
        "title": "Experienced WordPress Developer Needed",
        "url": "https://www.upwork.com/freelance-jobs/apply/Experienced-WordPress-Developer-Needed-for-Custom-Website-Design-and-Functionality-Enhancements_~021847951768940266071/"
    },
    {
        "title": "Website Needs Some Reconfiguring - WordPress",
        "url": "https://www.upwork.com/freelance-jobs/apply/website-needs-some-reconfiguring-Wordpress_~021847946452263221222/"
    }
]

# Function to calculate cosine similarity
def calculate_cosine_similarity(resume_text, job_texts):
    # Vectorize the texts (resume + all job descriptions)
    vectorizer = TfidfVectorizer()
    all_texts = [resume_text] + job_texts  # Resume is the first text
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Calculate cosine similarity between the resume and each job description
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return cosine_similarities[0]

# Match resume to jobs based on cosine similarity
def match_resume_to_jobs(resume_file_path):
    # Extract resume text
    file_extension = os.path.splitext(resume_file_path)[1].lower()
    if file_extension == ".pdf":
        resume_text = extract_text_from_pdf(resume_file_path)
    elif file_extension == ".docx":
        resume_text = extract_text_from_docx(resume_file_path)
    else:
        return None, "Unsupported file type"

    # Extract job descriptions
    job_texts = []
    for job in web_dev_jobs:
        job_description = download_job_description(job["url"])
        if job_description:
            job_texts.append(job_description)
        else:
            print(f"Warning: No description found for {job['title']}.")
            job_texts.append("")  # If no description found, use an empty string

    # Calculate cosine similarities between resume and job descriptions
    similarities = calculate_cosine_similarity(resume_text, job_texts)

    # Find the job with the highest cosine similarity
    best_match_index = similarities.argmax()  # Get the index of the highest similarity
    best_match = web_dev_jobs[best_match_index]
    best_similarity_score = similarities[best_match_index]

    return best_match, best_similarity_score

# Example usage with user input for the resume file
if __name__ == "__main__":
    # Ask user for the path to their resume
    resume_file_path = input("Please enter the path to your resume file (.pdf or .docx): ")

    # Check if the file exists before proceeding
    if not os.path.isfile(resume_file_path):
        print(f"Error: The file '{resume_file_path}' does not exist.")
    else:
        # Match the resume to jobs
        best_job, similarity_score = match_resume_to_jobs(resume_file_path)

        if best_job:
            print(f"Best Match: {best_job['title']}")
            print(f"Job URL: {best_job['url']}")
            print(f"Cosine Similarity Score: {similarity_score * 100:.2f}%")
        else:
            print("No matching job found.")
            
def match_resume_to_jobs_from_file(resume_file_path):
    # Match the resume to jobs
    best_job, similarity_score = match_resume_to_jobs(resume_file_path)

    if best_job:
        return {
            "title": best_job['title'],
            "url": best_job['url'],
            "score": similarity_score * 100  # Return score as a percentage
        }
    else:
        return None
