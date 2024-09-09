from typing import List, Dict, Any

def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, у которых ключ state=EXECUTED"""
    return [d for d in data if d.get('state') == state]

def sort_by_date():
    pass