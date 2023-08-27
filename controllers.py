import datetime
from DB import Session
from models import clients



def check_client(chat_id):
    """Проверяем наличие юзера в базе данных"""
    session = Session()
    for user in session.query(clients).filter(clients.chat_id==chat_id):
        if user:
            session.close()
            return False
    session.close()
    create_clients(chat_id)
    return True


def create_clients(chat_id):
    """Создаем нового пользователя"""
    session = Session()
    new_с = clients(chat_id=chat_id,date=datetime.date.today())
    session.add(new_с)
    session.commit()
    session.close()
    print("Я добавил новичка!")

def get_today_client():
    """Все клиенты за сегодня"""
    date_list=0
    session = Session()
    for date in session.query(clients).filter(clients.date == datetime.date.today()):
        date_list= date_list+1
    return date_list
    session.close()



