# Email Automater 📧

🚀 Automate Your Job Hunt: A sleek Python script that simplifies outreach by reading HR details from an Excel file and sending personalized emails effortlessly. Perfect for job seekers looking to save time and make a professional first impression! 📧📋

## 🎯 Purpose

This tool was created to help job seekers efficiently manage their outreach process by:

- Automating personalized email sending to multiple HR contacts
- Maintaining professional consistency in communications
- Saving time during the job application process
- Automatically attaching resumes to each email
- Tracking successful and failed email attempts through logging

## ⚙️ Features

- Excel-based contact management
- Customizable email templates with HTML support
- Automatic resume attachment
- Built-in delay system to prevent spam filtering
- Comprehensive logging system
- Error handling and reporting
- Support for Gmail SMTP

## 🚀 Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/rahuljassal/email_automater.git
   cd email_automater
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory with:

   ```
   EMAIL_ADDRESS=your.email@gmail.com
   EMAIL_PASSWORD=your_app_password
   RESUME_PATH=path/to/your/resume.pdf
   FILE_PATH=path/to/your/contacts.xlsx
   ```

5. **Prepare your Excel file**
   Create an Excel file with the following columns:
   - email
   - name
   - company

## 📝 Usage

1. **Update Email Template**
   Customize the email template in `src/templates/email_template.py` with your:

   - Professional experience
   - Technical skills
   - LinkedIn URL
   - Portfolio URL
   - GitHub URL
   - Contact information

2. **Run the Script**
   ```bash
   python main.py
   ```

## 📋 Excel File Format

Your Excel file should be structured as follows:

| email            | name | company  |
| ---------------- | ---- | -------- |
| hr@company.com   | John | Tech Co  |
| recruit@firm.com | Jane | Firm Inc |

## 🔒 Security Notes

- Use Gmail App Passwords instead of your main account password
- Keep your `.env` file secure and never commit it to version control
- The `.gitignore` file is configured to exclude sensitive files

## 📊 Logging

The application creates detailed logs in the `logs` directory with:

- Timestamp for each action
- Success/failure status
- Error details if any
- Email sending progress

## ⚠️ Important Notes

- Ensure you comply with email sending limits of your email provider
- Use appropriate delays between emails to avoid spam filters
- Keep your contact list up to date
- Test with a small list first

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
