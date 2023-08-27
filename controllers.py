import datetime
from DB import Session
from models import clients



def create_client_if_not_exists(chat_id):
    """Проверяем наличие юзера в базе данных"""
    session = Session()
    if bool(session.query(clients).filter_by(chat_id=chat_id).first()):
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


def get_today_clients_count():
    """Все клиенты за сегодня"""
    date_list=0
    session = Session()
    for date in session.query(clients).filter(clients.date == datetime.date.today()):
        date_list= date_list+1
    return date_list
    session.close()


create_client_if_not_exists("Вася")
