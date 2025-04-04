# Программа API_VK
## Назначение программы
Ваши фотографии из VK — это ценные воспоминания, но что, если соцсеть временно недоступна? **VK_API** — это надёжное решение для автоматического резервного копирования фотографий профиля (аватарок) из ВКонтакте в облачное хранилище **Яндекс.Диск**.

Программа гарантирует, что ваши фото всегда будут доступны, даже если VK оффлайн.


## Ключевые функции
✅ **Автоматическая загрузка фото** из профиля VK

✅ **Сохранение в Яндекс.Диск** — ваши фото в безопасности

✅ **Умные имена файлов**

+ Используется количество лайков (123.jpg)

+ Если лайков одинаково, добавляется дата (123_2024-05-20.jpg)

✅ **Логирование в JSON** — информация о каждой фотографии сохраняется в файл photos_info.json

## Как это работает?
### 1. Получение фото из VK
Программа подключается к **API ВКонтакте** и загружает фотографии профиля (аватарок) в максимальном качестве.

### 2. Генерация имён файлов
+ Если у фото 100 лайков → сохраняется как 100.jpg

+ Если у двух фото по 100 лайков → второе сохраняется как 100_2024-05-20.jpg

### 3. Загрузка в Яндекс.Диск
Фото автоматически отправляются в папку **Photos_VK** на вашем Яндекс.Диске.

### 4. Сохранение метаданных в JSON
Формат файла photos_info.json:

>[
  {
    "file_name": "100.jpg",
    "size": "z"  // Размер фото (z — максимальный)
  },
  {
    "file_name": "100_2024-05-20.jpg",
    "size": "z"
  }
]

## Техническая реализация
📌 **Язык:** Python

📌 **Используемые API:**

+ VK API (для получения фото)

+ Яндекс.Диск API (для загрузки в облако)

📌 **Библиотеки:** requests, json, datetime, os



## Почему это удобно?
🔹 **Автоматизация** — не нужно вручную сохранять фото

🔹 **Резервная копия** — защита от потери данных

🔹 **Удобный доступ** — фото всегда под рукой в Яндекс.Диске

🔹 **Гибкость** — можно настроить копирование других альбомов


## Пример использования
**Установка и настройка** (требуется только 1 раз)

**Запуск программы** → фото копируются в облако

**Готово!** Теперь ваши фото сохранены, даже если VK не работает.

## Заключение
**VK_API** — это не просто программа, а надёжный цифровой архив для ваших фотографий. Больше не нужно переживать о потере доступа к соцсети — ваши воспоминания в безопасности!

🚀 **Готовы попробовать?** Скачайте программу и настройте резервное копирование за 5 минут!