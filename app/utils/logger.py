import logging


def set_log():
    logger = logging.getLogger('my_logger')  # Дай уникальное имя
    logger.setLevel(logging.INFO)

    # ПРОВЕРКА: если хэндлеры уже есть, не добавляем их снова (защита от дублей)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler('fileHand.log', encoding='utf-8')
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # Отключаем передачу логов выше (в логгер FastAPI)
        logger.propagate = False

    return logger