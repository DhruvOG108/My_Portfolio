from flask import Flask, render_template

app = Flask(__name__)

# --- 1. PERSONAL INFO (Added Social Links) ---
personal_info = {
    "name": "Dhruv Chhikara",
    "role": "Data Science Enthusiast & Aspiring ML Engineer",
    "bio": "Passionate about leveraging data to solve real-world problems. Currently learning Python, Machine Learning, and Data Visualization.",
    "location": "India",
    "email": "dhruv.career.108@gmail.com",
    # UPDATE THESE LINKS WITH YOUR REAL PROFILES
    "linkedin": "https://www.linkedin.com/in/dhruv-chhikara",
    "github": "https://github.com/DhruvOG108"
}

skills = [
    "Python", "NumPy", "Pandas", "Matplotlib", "Seaborn", 
    "Scikit-learn", "Flask", "HTML5", "CSS3", "JavaScript", "Git & GitHub"
]

# --- 2. CERTIFICITIONS (Added 'link' key) ---
Certifications = [
    {
        "title": "Oracle Data Science Professional Certificate",
        "year": "2025",
        "desc": "Oracle Cloud Infrastructure 2025 Certified Data Science Professional - Completed a comprehensive program covering data science fundamentals, machine learning, and cloud-based data solutions.",
        "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=B2325F41A9D84EF711F8FBCE45105A18D4CCF423D3F04726442CD890B9C6435B" # Add your cert link
    },
    {
        "title": "Deep Learning.AI Supervised Machine Learning by Andrew Ng",
        "year": "2025",
        "desc": "Completed the supervised machine learning specialization on Coursera.",
        "link": "https://www.coursera.org/account/accomplishments/verify/03DENA9YCCYT" # Add your repo link
    },
    {
        "title": "Tata - GenAI Powered Data Analytics job Simulation by Forage",
        "year": "2025",
        "desc": "Conducted exploratory data analysis (EDA) on financial datasets using Python (Pandas, Seaborn) to identify risk patterns and customer segments. Built a delinquency prediction model using machine learning techniques to assess default probability. Developed a data-driven collections strategy and presented insights through a business report with clear visual storytelling to support decision-making.",
        "link": "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/gMTdCXwDdLYoXZ3wG_ifobHAoMjQs9s6bKS_PrcZx3KpqNdb4S56T_1756829145744_completion_certificate.pdf"
    }
]

achievements = [
    {
        "title": "Retail Demand Forecasting & Inventory Optimization",
        "year": "2026",
        "desc": "Developed a machine learning model to forecast retail demand and optimize inventory levels using Python, Pandas, and Scikit-learn.",
        "link": "https://github.com/DhruvOG108/Datathon_Demand_Forecasting" # Add your cert link
    },
    
]

@app.route('/')
def home():
    return render_template('index.html', 
                           info=personal_info, 
                           skills=skills, 
                           Certifications=Certifications,
                           achievements=achievements)

if __name__ == '__main__':
    # Using port 8000 to avoid Mac AirPlay conflicts
    app.run(debug=True, port=8000)