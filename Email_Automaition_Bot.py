import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("SENDERS_EMAIL_ADDRESS", "********")
    email = EmailMessage()
    email['From'] = "SENDERS_EMAIL_ADDRESS"
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    # ADD THE KEY VALUE PAIR OF EMAIL 
    
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    talk('Do you want to send this mail ?')
    send_this = get_info()
    if 'yes' in send_this:
        send_email(receiver, subject, message)
        talk('Hey lazy ass. Your email is sent')
        talk('Do you want to send more email?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()


get_email_info()
