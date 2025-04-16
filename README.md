# Автоматический анализ рекламной кампании Яндекс Директ

## Что находится в репозитории

Данный репозиторий содержит автоматически сгенерированный отчет по анализу эффективности рекламной кампании Яндекс Директ для сервиса Gooroo.tools. Отчет включает в себя анализ ключевых метрик, визуализации данных и рекомендации по оптимизации рекламной кампании.

**[👉 Просмотреть готовый интерактивный отчет](https://amoneron.github.io/Auto-Report-Sample/yandex_direct_analysis.html)**

Основные компоненты репозитория:
- Исходные данные рекламной кампании
- Python-скрипт для анализа данных
- Интерактивный HTML-отчет с визуализациями
- Модульные компоненты для построения отчета

## Последовательность построения отчета

### 1. Загрузка данных

Исходные данные находятся в файле [data.csv](data.csv). Файл содержит детальную информацию о показах рекламных объявлений, кликах, конверсиях и других метриках рекламной кампании.

### 2. Описание данных

В файле содержатся данные о результатах рекламной кампании (по поиску) Яндекс Директ сервиса [https://gooroo.tools](https://gooroo.tools). Данные включают информацию о поисковых запросах, группах объявлений, показах, кликах, CTR, стоимости и конверсиях.

### 3. Вопросы для анализа

Отчет строится с целью ответить на следующие вопросы:

1. Какое объявление работает лучше всего?
2. Корректно ли настроены объявления по ЦА сервиса? 
3. Какие поисковые фразы надо убрать, а какие добавить?
4. На что еще важно обратить внимание?
5. Дай рекомендации.

### 4. Обработка данных с помощью AI

Для обработки данных используется Python-скрипт [analyze_data.py](analyze_data.py), автоматически созданный связкой Claude 3.7 + Gemini 2.5 Pro. Скрипт анализирует данные исходя из поставленных вопросов, что позволяет избежать ошибок и галлюцинаций. Результаты анализа сохраняются в файл [results.json](results.json).

### 5. Построение отчета

AI-модели (Claude 3.7 + Gemini 2.5 Pro) строят отчет по блокам. Отчет может быть представлен в различных форматах:
- Интерактивный (HTML) - текущая версия
- Статичный (PDF)
- Редактируемый (XLS/Google Sheets)

Компоненты отчета находятся в директории [report_components](report_components/).

### 6. Финализация отчета

Все блоки верифицируются и собираются в итоговый отчет [yandex_direct_analysis.html](yandex_direct_analysis.html). Весь процесс создания отчета занимает от 1 до 5 минут.

## Итоговый отчет

Основные выводы и результаты анализа:
- Общий расход на рекламную кампанию: 14 168,25 ₽
- Получено 17 конверсий из 286 переходов (5,9%)
- Средняя цена конверсии: 833,43 ₽
- Выявлены наиболее эффективные поисковые запросы
- Предложены рекомендации по оптимизации бюджета и настройке таргетинга

## Как использовать

Готовый интерактивный отчет можно просмотреть онлайн по ссылке: [https://amoneron.github.io/Auto-Report-Sample/yandex_direct_analysis.html](https://amoneron.github.io/Auto-Report-Sample/yandex_direct_analysis.html)

Для локального просмотра откройте файл [yandex_direct_analysis.html](yandex_direct_analysis.html) в любом современном браузере. 

Для повторного анализа с обновленными данными запустите скрипт `analyze_data.py`.