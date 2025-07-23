from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Create new document
doc = Document()

def add_main_heading(text):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(18)
    para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

def add_sub_heading(text):
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(14)
    para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

def add_text_block(text):
    para = doc.add_paragraph(text)
    para.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

# Main Header
add_main_heading("KEMIDI MANISH")
add_text_block("📞 7036969854 | ✉️ kemidimanish04@gmail.com")
add_text_block("🌐 LinkedIn: https://www.linkedin.com/in/kemidimanish04")
add_text_block("💻 GitHub: https://github.com/manish2804-hub")
add_text_block("🏠 Address: Boduppal, Hyderabad")
GitHub: https://github.com/manish2804-hub


# Introduction
add_sub_heading("Hi! I'm Kemidi Manish")
add_text_block("""Motivated and detail-oriented Computer Science undergraduate with strong interests in Python, Web Development, and Cloud Computing. 
Currently focused on enhancing my technical and problem-solving abilities by building real-world projects and contributing to open-source. 
Eager to work in collaborative environments and drive innovative software solutions.

I’m looking forward to working with amazing teams and building impactful solutions.

Regards & Thank you,
Kemidi Manish""")

# Area of Interests
add_sub_heading("Area of Interests")
add_text_block("""• Web Development (Frontend & Backend) 
• Cloud Computing (Basics of AWS, Azure)
• Machine Learning & Data Science 
• Open Source Contributions 
• Git & Version Control 
• WordPress Development""")

# Skills
add_sub_heading("Skills")
add_text_block("""• Languages: Python, C (Basics), Java (Basics)
• Web Technologies: HTML, CSS, JavaScript, PHP
• Databases: SQL, MySQL
• Tools: Git, GitHub, TensorFlow, Scikit-learn
• Platforms: Windows OS, WordPress (Beginner)""")

# Education Qualification
add_sub_heading("Education Qualification")
add_text_block("""• B.Tech in CSE (2022–2026) – Kommuri Pratap Reddy Institute of Technology – CGPA: 8.0 (till 2nd year)
• Intermediate – MPC (2020–2022) – Narayana Junior College – GPA: 8.7/10
• SSC – SR Digi School – GPA: 9.5/10""")

# Projects
add_sub_heading("Projects")
add_text_block("""• Anomaly Detection in IoT Sensor Data using ML
  - Used Python, TensorFlow, Scikit-learn, NumPy, Pandas
  - Built a system to detect unusual patterns in sensor readings""")

# Certifications
add_sub_heading("Certifications")
add_text_block("""• Microsoft Copilot – Certified via LinkedIn
• Generative AI Course – Completed
• Machine Learning with IoT – SAK Informatics""")

# Achievements & Strengths
add_sub_heading("Achievements & Strengths")
add_text_block("""• Active participant in technical & non-technical college events
• Strong communication and collaboration skills
• Fast learner with a passion for problem-solving""")

# Declaration
add_sub_heading("Declaration")
add_text_block("""I hereby declare that the information provided above is true to the best of my knowledge and belief.

Signature: Kemidi Manish
Date:
Place: Hyderabad""")

# Save the document to Desktop
output_path = "C:/Users/Admin/Desktop/Kemidi_Manish_Resume.docx"
doc.save(output_path)
print("✅ Resume generated successfully at:", output_path)

