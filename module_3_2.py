def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient  or not (recipient.endswith(".ru")
                                                        or recipient.endswith(".com")
                                                        or recipient.endswith(".net")):
        print(f"невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif "@" not in sender or not (sender.endswith(".ru")
                                        or sender.endswith(".com")
                                        or sender.endswith(".net")):
        print(f"невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender}  на адрес {recipient} с собщением: {message}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')


