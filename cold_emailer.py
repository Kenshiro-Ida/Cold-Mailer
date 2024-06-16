import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Function to decode the obfuscated email
# Define email content
subject = "Why I am the best Intern for [Company]"
email_body_template = """\
Dear [Recipient Name],

I am writing to express my interest in [Company] as an Intern. I am currently [Your Current Status], and I believe this internship would provide me with valuable hands-on experience and help me grow in my field.

I have been following [Company] for a while now, and I am impressed by the innovative work you are doing in [Industry/Field]. Your commitment to [Company's Mission/Values] aligns with my own career goals, and I believe I would be a great fit for your team.

I have attached my resume for your consideration. In the Resume, I have highlighted my skills, experience, and achievements that make me an ideal candidate for the internship.

If you have any availability next week, I would greatly appreciate the chance to speak with you and learn more about your firm and the possibility of completing a [Time Period] internship there. I am available for a call [insert your availability].

Thank you for taking the time to read my email. I look forward to the opportunity to discuss further how I can contribute to the success of [Company].

Best regards,

[Your Name]

[Your Phone Number]

[Your Email Address]
"""

# Your email credentials
your_email = "your.email@gmail.com"
your_password = "pkad vbsa zygp xdwd"

# Load the HR details from the CSV file
with open('hr_details.csv', mode='r') as file:
    reader = csv.DictReader(file)
    hr_details = [row for row in reader]

# Set up the SMTP server
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
smtp_port = 587  # Replace with your SMTP port if different
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(your_email, your_password)

# Path to the resume file
resume_path = "resume.pdf"
i = 0
# Send the email to each recipient
for detail in hr_details:
    recipient_email = detail['Email']
    recipient_name = detail['Name']
    company_name = detail['Company']

    # Customize the email body for each recipient
    email_body = email_body_template.replace("[Recipient Name]", recipient_name)
    email_body = email_body.replace("[Company]", company_name)
    email_body = email_body.replace("[Your Current Status]", "a student at IIT Madras")  # Customize as needed
    email_body = email_body.replace("[Industry/Field]", "the tech industry")  # Customize as needed
    email_body = email_body.replace("[Company's Mission/Values]", "innovation and excellence")  # Customize as needed
    email_body = email_body.replace("[Time Period]", "6-month")  # Customize as needed
    email_body = email_body.replace("[insert your availability]", "next Monday to Friday")  # Customize as needed
    email_body = email_body.replace("[Your Name]", "Aditya Singh Rawat")  # Customize as needed
    email_body = email_body.replace("[Your Phone Number]", "+911234567890")  # Customize as needed
    email_body = email_body.replace("[Your Email Address]", your_email)  # Customize as needed

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = recipient_email
    msg['Subject'] = subject.replace("[Company]", company_name)
    msg.attach(MIMEText(email_body, 'plain'))

    # Attach the resume file
    with open(resume_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {resume_path}",
    )
    msg.attach(part)

    # Send the email
    server.sendmail(your_email, recipient_email, msg.as_string())
    print("Done" ,i)
    i+=1

# Close the SMTP server
server.quit()

print("Emails have been sent successfully.")
