def create_email_content(name: str, company: str) -> dict:
    """Create personalized email subject and body"""
    subject = f"Job Application - Software Developer - {company}"

    body = f"""
<html>
<body>
<p>Dear {name},</p>

<p>I hope this email finds you well. I am writing to express my interest in the Software Developer position at <b>{company}</b> and would greatly appreciate your referral for this role.</p>

<p>About my background:</p>
<ul>
    <li><b>X+ years of professional experience in software development</b></li>
    <li>Technical expertise in:
        <ul>
            <li><b>Frontend:</b> React.js, JavaScript, TypeScript, HTML5, CSS3</li>
            <li><b>Backend:</b> Node.js, Python, SQL</li>
            <li><b>Tools & Others:</b> Git, AWS, Docker</li>
        </ul>
    </li>
</ul>

<p>For your reference:</p>
<ul>
    <li>Resume: [Attached]</li>
    <li>Total Experience: <b>X+ years</b></li>
    <li>LinkedIn: <a href="YOUR_LINKEDIN_URL">YOUR_LINKEDIN_URL</a></li>
    <li>Portfolio: <a href="YOUR_PORTFOLIO_URL">YOUR_PORTFOLIO_URL</a></li>
    <li>GitHub: <a href="YOUR_GITHUB_URL">YOUR_GITHUB_URL</a></li>
</ul>

<p>I believe my technical skills and experience align well with {company}'s requirements, and I'm excited about the opportunity to contribute to the team.</p>

<p>I would greatly appreciate any insights you could provide about the role and the application process. Please let me know if you need any additional information to support the referral.</p>

<p>Thank you for your time and consideration.</p>

<p>Best regards,<br>
<b>YOUR_NAME</b><br>
<b>YOUR_PHONE</b></p>
</body>
</html>
"""
    return {"subject": subject, "body": body}
