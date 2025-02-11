import sys
sys.stdout.reconfigure(encoding='utf-8')


def detectar_spam(email):

    if email.endswith("@xyz.com"):
        print(f"O email de {email} é spam.")
    else:
        print(f"O email de {email} não é spam.")


detectar_spam("usuario1@empresa.com")


detectar_spam("usuario2@xyz.com")