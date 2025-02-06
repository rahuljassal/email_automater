import pandas as pd
def create_email_content(name: str, company: str, profile: str, job_link: str) -> dict:
    # Check if job_link is NaN or None
    has_valid_link = job_link and not pd.isna(job_link)
    """Create personalized email subject and body"""
    subject = f"Job Application - {profile} - {company}"

    body = f"""
<html>
<body>
<p>Dear {name},</p>

<p>I hope this email finds you well. I am writing to express my interest in this opening  {f"<a href={job_link}><b>{profile}</b></a>" if has_valid_link else f"<b>{profile}</b>"} at <b>{company}</b> and would greatly appreciate your referral for this role.</p>

<p>About my background:</p>
<ul>
    <li><b>3.6+ years of professional experience in software development</b></li>
    <li>Technical expertise in:
        <ul>
            <li><b>Frontend:</b> React.js, JavaScript, TypeScript,Redux, HTML5, CSS3</li>
            <li><b>Backend:</b> Node.js, Python, SQL</li>
            <li><b>Tools & Others:</b> Data Structures & Algorithms, Git, Google Cloud Platform (GCP)</li>
        </ul>
    </li>
</ul>

<p>For your reference:</p>
<ul>
    <li>Resume: <a href="https://drive.google.com/file/d/1aSW1NXq41VzPtD9S9xYDIyJIM-Htwpxj/view?usp=sharing">Resume Drive Link</a></li>
    <li>Total Experience: <b>3.6+ years</b></li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/rahul-jassal-44ba75179">https://www.linkedin.com/in/rahul-jassal-44ba75179</a></li>
    <li>Portfolio: <a href="https://rahul-jassal.vercel.app/">https://rahul-jassal.vercel.app/</a></li>
    <li>GitHub: <a href="https://github.com/rahuljassal">https://github.com/rahuljassal</a></li>
    <li>Notice Period: <b>Serving (LWD - 07/02/2025 )</b></li>
    
</ul>

<p>I believe my technical skills and experience align well with {company}'s requirements, and I'm excited about the opportunity to contribute to the team.</p>

<p>I would greatly appreciate any insights you could provide about the role and the application process. Please let me know if you need any additional information to support the referral.</p>

<p>Thank you for your time and consideration.</p>

<p>Best regards,<br>
<b>Rahul Jassal</b><br>
<b>987788819</b></p>
</body>
</html>
"""
    return {"subject": subject, "body": body}
