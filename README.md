## Cold Mailer for Cold Mailing HR Representatives

This Python script is designed to automate the process of sending cold emails to HR representatives of different companies. The script reads HR details from a CSV file, customizes an email template for each recipient, and sends the emails with an attached resume using the SMTP protocol.
## Features

- Reads HR details (name, email, company) from a CSV file.
- Customizes the email body for each recipient using a template.
- Attach a resume file to each email.
- Sends the emails via an SMTP server.


## Installation

1. Clone the Repository

```bash
  git clone https://github.com/Kenshiro-Ida/Cold-Mailer
  cd https://github.com/Kenshiro-Ida/Cold-Mailer
```
2. Install Dependencies

No additional dependencies are required as the necessary libraries are part of the Python Standard Library.

3. Prepare the CSV File

Create a CSV file named hr_details.csv with the following columns:

- Name: The name of the HR representative.
- Email: The email address of the HR representative.
- Company: The name of the company.

I have also provided my own hr_details.csv

4. Prepare Your Resume 

Could you make sure you have your resume file named resume.pdf in the same directory as the script?

5. Set Up Your Email Credentials

Replace the your_email and your_password variables in the script with your actual email credentials. Use an application-specific password if using Gmail.

```bash
    your_email = "your.email@gmail.com"
    your_password = "rvyn srem errp xagd" 
```

## Usage/Examples

Run the script using the following command:

```bash
    python cold_emailer.py
```

The script will:

- Read the HR details from the hr_details.csv file.
- Customize the email template for each recipient.
- Attach the resume.pdf file to each email.
- Send the emails via the specified SMTP server.
- Print a confirmation message for each email sent.


## Email Template

The email body is customized for each recipient using the following template:

```plaintext
Dear [Recipient Name],

I am writing to express my interest in [Company] as an Intern. I am currently a student at IIT Madras, and I believe this internship would provide me with valuable hands-on experience and help me grow in my field.

I have been following [Company] for a while now, and I am impressed by the innovative work you are doing in the tech industry. Your commitment to innovation and excellence aligns with my own career goals, and I believe I would be a great fit for your team.

I have attached my resume for your consideration. In the Resume, I have highlighted my skills, experience, and achievements that make me an ideal candidate for the internship.

If you have any availability next week, I would greatly appreciate the chance to speak with you and learn more about your firm and the possibility of completing a 6-month internship there. I am available for a call next Monday to Friday.

Thank you for taking the time to read my email. I look forward to the opportunity to discuss further how I can contribute to the success of [Company].

Best regards,

[Your Name]

[Your Number]

[Your Email]
```
## Important Notes

- Ensure you have the correct permissions to send emails via your SMTP server.
- Be mindful of the email sending limits of your email provider to avoid being flagged for spam.
## Disclaimer

Use this script responsibly and ensure compliance with email marketing laws and regulations.
