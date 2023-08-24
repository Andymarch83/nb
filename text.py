main_menu = '''\nГлавное меню:
		1. Открыть блокнот • 
		2. Запомнить изменения  •
		3. Смотреть записии •
		4. Новая запись •
		5. Искать запись •
		6. Исправить запись •
		7. Удалить запись •
		8. Выход •\n '''

input_choice = 'Выберите действие: '
JSON_PATH = 'data_notes.json'

load_successful = 'Блокнот открыт'
save_successful = 'Изменения запомнены'

load_error = 'Блокнот закрыт или записи отсутствуют'

input_new_note = 'Добавьте запись: '
new_notes = {'title': 'Назовите запись: ',
             'note': 'Напишите что-нибудь: '}


def new_note_successful(title: str):
    return f'Ваша {title}  добавлена.'


cancel_input = 'Отмена ввода'

index_del_note = 'Выберите индекс записи для удаления: '


def del_note(title: str):
    return f'Ваша {title}  больше нет'


input_change = 'Измените запись: '
input_index = 'Введите индекс записи: '

change_note = 'Введите информацию или оставьте поле пустым, чтобы не менять: '


def change_successful(title: str | dict) -> str:
    return f'Ваша {title}  изменена!'


input_search = 'Что ищем? '


def empty_search(word) -> str:
    return f'Записи с "{word}" не найдены!'
