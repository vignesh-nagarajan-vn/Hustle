import docx as python_docx
from PyPDF2 import PdfReader


# Side hustle dictionary
side_hustles = {
    "Scriptwriter": ["Creative writing", "Screenwriting", "Story development", "Dialogue creation", "Narrative structure", "Plot development", "Character arcs", "World-building", "Genre writing", "Subtext", "English", "Content", "Media"],
    "Prompt Engineer": ["Natural language processing", "AI", "Model optimization", "GPT-3/4", "Data analysis", "Machine learning", "Algorithm design", "Data preprocessing", "Text generation", "Python", "Computer Science", "Programming", "Technical"],
    "Medium Content Writer": ["Blog writing", "SEO optimization", "Content strategy", "Article development", "Copywriting", "Social media marketing", "Keyword research", "Content curation", "Content marketing", "Email marketing", "English", "Content", "Media"],
    "Graphic Designer": ["Adobe Creative Suite", "Branding", "Visual communication", "Typography", "Layout design", "Illustration", "UI/UX design", "Wireframing", "Print design", "Logo creation", "Creativity", "Art", "Technical"],
    "Animator": ["2D/3D animation", "Motion graphics", "Storyboarding", "After Effects", "Character design", "Keyframe animation", "Rigging", "Visual effects (VFX)", "Compositing", "3D modeling", "Programming", "Computer science", "Technical"],
    "Photographer": ["Photo editing", "Lightroom", "Event photography", "Composition", "Lighting techniques", "Photojournalism", "Commercial photography", "Studio lighting", "Portrait photography", "Editing workflow", "Entrepreneurship", "Content", "Media"],
    "3D Printing Specialist": ["CAD", "Additive manufacturing", "3D modeling", "Prototyping", "AutoCAD", "FDM/SLA printing", "Product design", "Slicing software", "Material science", "Reverse engineering", "Graphic Design", "Technical", "Math"],
    "Virtual Bookkeeper": ["QuickBooks", "Accounts payable/receivable", "Financial reporting", "Reconciliation", "Data entry", "Tax preparation", "Invoicing", "Payroll management", "Expense tracking", "Financial statements", "Analysis", "Management", "Technical"],
    "Podcast Host": ["Public speaking", "Audio editing", "Content creation", "Interviewing skills", "Audience engagement", "Podcast production", "Social media promotion", "Audio engineering", "Guest outreach", "Scriptwriting", "Communication", "Content", "Media"],
    "Online Tutor": ["Curriculum development", "Lesson planning", "Subject expertise", "Virtual teaching platforms", "Student engagement", "Assessment creation", "Test preparation", "Learning management systems (LMS)", "STEM", "Educational psychology", "Honor Roll", "High School", "Education"],
    "Voiceover Artist": ["Voice modulation", "Audio recording", "Diction", "Script interpretation", "Studio equipment", "Commercial voiceovers", "Audiobook narration", "Character voices", "Breathing techniques", "Sound engineering", "Content", "Media", "Editing"],
    "Web Developer": ["HTML/CSS/JavaScript", "Full-stack development", "Responsive design", "API integration", "Front-end/back-end development", "React.js", "Node.js", "Version control (Git)", "Database management", "Web performance optimization", "Bootstrap", "VSCode", "Django"],
    "Babysitter": ["Childcare", "CPR certification", "Time management", "Conflict resolution", "Activity planning", "Child development", "First aid", "Emotional intelligence", "Meal preparation", "Behavior management", "Customer Service", "Organization", "Adaptability"],
    "Content Editor": ["Proofreading", "Copy editing", "Grammar and syntax", "Style guides", "Attention to detail", "Fact-checking", "Content management systems", "Research skills", "Headlines optimization", "SEO for content", "Content", "Media", "Writing"],
    "Video Editor": ["Final Cut Pro", "Storytelling", "Color grading", "Video transitions", "Timeline management", "Motion graphics", "Audio syncing", "Green screen editing", "Video effects", "Multi-camera editing", "Software", "Technical", "Media"],
    "Dog Walker": ["Pet care", "Time management", "Route planning", "Animal behavior", "Reliability", "Pet first aid", "Exercise planning", "Pet safety", "Client communication", "Weather preparedness", "Organization", "Customer Service", "Adaptability"]
}

# Returns text if uploaded file extension is .docx
def process_docx(file_path):
    try:
        doc = python_docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error reading DOCX resume: {e}")

# Returns text if uploaded file extension is .txt
def process_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading TXT resume: {e}")
        return ""

# Returns text if uploaded file extension is .pdf
def process_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF resume: {e}")
        return ""

# Processes the resume and calculates the highest matching side hustle percentage
def process_resume(file_path):
    side_hustle_scores = {side_hustle: 0 for side_hustle in side_hustles}

    # Extract text based on file type
    resume_text = ""
    if file_path.endswith('.docx'):
        resume_text = process_docx(file_path)
    elif file_path.endswith('.txt'):
        resume_text = process_txt(file_path)
    elif file_path.endswith('.pdf'):
        resume_text = process_pdf(file_path)
    
    # Count keyword matches for each side hustle
    if resume_text:
        for line in resume_text.splitlines():
            line = line.strip()
            for side_hustle, keywords in side_hustles.items():
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        side_hustle_scores[side_hustle] += 1

    # Calculate percentage scores and find the highest matching side hustle
    percentage_scores = {}
    for side_hustle, score in side_hustle_scores.items():
        total_keywords = len(side_hustles[side_hustle])
        if total_keywords > 0:
            percentage_scores[side_hustle] = (score / total_keywords) * 100
    
    if percentage_scores:
        highest_hustle = max(percentage_scores, key=percentage_scores.get)
        highest_score = percentage_scores[highest_hustle]
        print(f"Highest Hustle: {highest_hustle}, Score: {highest_score:.2f}%")
        return highest_hustle, highest_score, percentage_scores

    return None, None, None
