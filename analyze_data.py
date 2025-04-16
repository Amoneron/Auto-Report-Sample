import csv
import json

# Функция для преобразования строковых значений в числовые
def parse_number(value):
    if value == '-':
        return 0
    return float(value.replace(',', '.').replace(' ', ''))

# Анализ данных
def analyze_data(file_path):
    results = {
        'total_cost': 0,
        'total_impressions': 0,
        'total_clicks': 0,
        'total_conversions': 0,
        'avg_ctr': 0,
        'avg_cpc': 0,
        'avg_conversion_cost': 0,
        'ads': {},
        'categories': {},
        'top_ctr_keywords': [],
        'conversion_keywords': []
    }
    
    keywords = []
    entries_with_ctr = 0
    total_ctr_sum = 0
    
    # Чтение CSV файла
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            # Извлечение и преобразование числовых значений
            impressions = int(parse_number(row['Показы']))
            clicks = int(parse_number(row['Клики']))
            ctr = parse_number(row['CTR (%)'])
            cost = parse_number(row['Расход (руб.)'])
            avg_click_cost = parse_number(row['Ср. цена клика (руб.)'])
            conversion_rate = parse_number(row['Конверсия (%)'])
            conversion_cost = parse_number(row['Цена цели (руб.)'])
            conversions = int(parse_number(row['Конверсии']))
            
            # Сбор данных по объявлениям
            ad_number = row['№ Объявления']
            if ad_number not in results['ads']:
                results['ads'][ad_number] = {
                    'impressions': 0,
                    'clicks': 0,
                    'cost': 0,
                    'conversions': 0,
                    'ctr': 0
                }
            
            results['ads'][ad_number]['impressions'] += impressions
            results['ads'][ad_number]['clicks'] += clicks
            results['ads'][ad_number]['cost'] += cost
            results['ads'][ad_number]['conversions'] += conversions
            
            # Сбор данных по категориям таргетинга
            category = row['Категория таргетинга']
            if category not in results['categories']:
                results['categories'][category] = {
                    'impressions': 0,
                    'clicks': 0,
                    'conversions': 0
                }
            
            results['categories'][category]['impressions'] += impressions
            results['categories'][category]['clicks'] += clicks
            results['categories'][category]['conversions'] += conversions
            
            # Сбор ключевых слов
            keywords.append({
                'keyword': row['Поисковый запрос'],
                'impressions': impressions,
                'clicks': clicks,
                'ctr': ctr,
                'cost': cost,
                'conversions': conversions
            })
            
            # Обновление общих показателей
            results['total_impressions'] += impressions
            results['total_clicks'] += clicks
            results['total_cost'] += cost
            results['total_conversions'] += conversions
            
            # Для расчета среднего CTR
            if impressions > 0:
                total_ctr_sum += ctr
                entries_with_ctr += 1
    
    # Расчет CTR для каждого объявления
    for ad_number, ad in results['ads'].items():
        if ad['impressions'] > 0:
            ad['ctr'] = (ad['clicks'] / ad['impressions']) * 100
    
    # Расчет средних показателей
    if results['total_clicks'] > 0:
        results['avg_cpc'] = results['total_cost'] / results['total_clicks']
    
    if entries_with_ctr > 0:
        results['avg_ctr'] = total_ctr_sum / entries_with_ctr
    
    if results['total_conversions'] > 0:
        results['avg_conversion_cost'] = results['total_cost'] / results['total_conversions']
    
    # Топ-5 запросов по CTR (с минимум 2 показами)
    top_ctr = sorted([kw for kw in keywords if kw['impressions'] >= 2], 
                       key=lambda x: x['ctr'], reverse=True)[:5]
    results['top_ctr_keywords'] = top_ctr
    
    # Запросы с конверсиями
    conversion_keywords = sorted([kw for kw in keywords if kw['conversions'] > 0], 
                               key=lambda x: x['conversions'], reverse=True)
    results['conversion_keywords'] = conversion_keywords
    
    return results

# Путь к файлу с данными
file_path = '/Users/amoneron/Documents/Gooroo/Analytics/Reports/data.csv'

# Анализ данных
results = analyze_data(file_path)

# Вывод результатов
print(f"Общий расход: {results['total_cost']:.2f} руб.")
print(f"Всего показов: {results['total_impressions']}")
print(f"Всего кликов: {results['total_clicks']}")
print(f"Всего конверсий: {results['total_conversions']}")
print(f"Средний CTR: {results['avg_ctr']:.2f}%")
print(f"Средняя цена клика: {results['avg_cpc']:.2f} руб.")
print(f"Средняя цена конверсии: {results['avg_conversion_cost']:.2f} руб.")

# Запись результатов в JSON файл для использования в HTML
with open('/Users/amoneron/Documents/Gooroo/Analytics/Reports/results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nРезультаты сохранены в файл results.json")