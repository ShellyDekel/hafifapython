from datetime import datetime

# 6
def happyBirthdayIn(birthdayDate: datetime):
    birthdate = birthdayDate.replace(year=datetime.now().year)

    return (birthdate.date() - datetime.now().date()).days % 365