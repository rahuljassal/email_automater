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
   RESUME_FILENAME=Your_Name_Resume.pdf
   ```

5. **Prepare your Excel file**
   Create an Excel file with the following required columns:
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
- The `.gitignore` file is configured to exclude sensitive files (_.xlsx, _.pdf, .env)
- Never share your email credentials or sensitive information

## 📊 Logging

The application creates detailed logs in the `logs` directory with:

- Timestamp for each action
- Success/failure status for each email sent
- Error details if any
- Email sending progress and completion status

## ⚠️ Important Notes

- Ensure you comply with Gmail's sending limits (typically 500 per day)
- Default delay between emails is 2 seconds to avoid spam filters
- Keep your contact list up to date
- Test with a small list first
- Make sure to use a Gmail account with "Less secure app access" or App Password enabled
- The script uses HTML formatting for emails for better presentation

## 🛠️ Technical Details

- Python 3.9+ required
- Uses pandas for Excel file handling
- SMTP configuration preset for Gmail
- HTML email template support
- Automatic error logging and reporting
- Built-in rate limiting with configurable delays

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🐛 Troubleshooting

If you encounter issues:

1. Check your Gmail settings and ensure App Password is correctly set
2. Verify Excel file format matches requirements
3. Check logs in the `logs` directory for detailed error messages
4. Ensure all environment variables are correctly set in `.env`
