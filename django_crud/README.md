# Django CRUD (шаблон)

Готовый CRUD на Django: приложение `crud`, модель `Item`, CBV-вьюхи, Bootstrap-шаблоны, поиск, пагинация, админка, тесты.

## Запуск
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # по желанию, для /admin/
python manage.py runserver
```
Открыть: http://127.0.0.1:8000/

## URL-ы
| URL | Действие |
|---|---|
| `/` | список + поиск `?q=` |
| `/create/` | создать |
| `/<id>/` | просмотр |
| `/<id>/edit/` | изменить |
| `/<id>/delete/` | удалить |
| `/admin/` | админка |

## Как под новую задачу
1. `crud/models.py` — поменять поля модели.
2. `crud/forms.py` — обновить `fields` и `widgets`.
3. Шаблоны в `crud/templates/crud/` — поправить колонки/поля.
4. `python manage.py makemigrations && python manage.py migrate`.
5. Тесты: `python manage.py test`.
