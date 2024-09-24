from menu import data
from ui import components, utils


def create(route: str):
    routes = route.split("/")
    items = [
        item for item in data.items
        if item.route == route
    ]
    
    render(routes, items)
    item = prompt(items)

    if item == None:
        return create(route)
    
    if type(item.action) == str:
        return create(item.action)
    
    return item.action
        


def render(routes: list[str], items: list[data.Item]):
    utils.clear()
    components.put_head(routes[-1] if routes[-1] != "" else "can sim")


def prompt(items: list[data.Item]):
    response = components.get_select([item.name for item in items])

    if int(response) not in range(0, len(items)):
        return None
    
    return items[int(response)]