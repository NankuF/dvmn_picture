# Получить аватарку из изображения.
Получает аватарку с новыми цветами, смешивая цвета RGB.

## Окружение
### Подготовка Linux:<br>

Скачать git:
```bash
sudo apt-get install git
```
Сделать fork репозитория:
```bash
git clone https://github.com/NankuF/dvmn_picture.git
```
Перейти в директорию со скриптом:
```bash
cd ~ && cd dvmn_picture/
```
Создать виртуальное окружение:
```bash
python -m venv venv
```
Активировать виртуальное окружение:
```bash
. ./venv/bin/activate
```
Установить зависимости:
```bash
pip install -r requirements.txt 
```

## Запуск: <br>

1. Положить картинку в формате jpg в директорию, рядом с main.py

2. Ввести в консоли код:
```bash
python main.py
```

## Результат:
Появится 2 картинки:
1. Аватарка в пределах 80 пикселей
2. Полноразмерное изображение

![avatar_monro.jpg](avatar_monro.jpg)
![new_monro.jpg](new_monro.jpg)
