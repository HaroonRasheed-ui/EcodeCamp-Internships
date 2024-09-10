store_sections = {
    'produce': 1,
    'bakery': 2,
    'dairy': 3,
    'meat': 4,
    'miscellaneous': 5
}

def optimize_shopping_route(categorized_items):
    route = []
    for section in sorted(categorized_items.keys(), key=lambda sec: store_sections[sec]):
        route.append(section)
    return route
