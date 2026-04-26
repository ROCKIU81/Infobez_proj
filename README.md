# Project Name

Этот проект представляет собой веб-приложение с FastAPI бэкендом и React фронтендом.

## Структура проекта
- `app/` - FastAPI бэкенд.
- `frontend/` - React фронтенд (на Vite).

## Запуск проекта

### Бэкенд
1. Перейдите в папку с проектом.
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux/macOS
   # .venv\Scripts\activate  # для Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите сервер:
   ```bash
   uvicorn app.main:app --reload
   ```

### Фронтенд
1. Перейдите в папку `frontend/`:
   ```bash
   cd frontend
   ```
2. Установите зависимости:
   ```bash
   npm install
   ```
3. Запустите сервер разработки:
   ```bash
   npm run dev
   ```

   пописить главное не забудьте
   
