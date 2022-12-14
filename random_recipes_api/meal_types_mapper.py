from typing import Dict, List


mapper:Dict[str, str] = {'sniadania': 'breakfasts',
          'przystawki': 'starters',
          'ciasta-i-desery': 'cakes_and_desserts',
          'do-chleba':'spreads',
          'zupy': 'soups',
          'napoje': 'beverages',
          'lunche-do-pracy':'work_lunches',
          'dania-glowne':'main_courses',
          'sosy-i-dodatki': 'sauces_and_etceteras'}


def get_possible_meal_types() -> List[str]:
    return list(mapper.values())