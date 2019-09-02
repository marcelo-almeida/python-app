from api.category.service import add_category, update_category, get_categories, get_category_by_id, \
    get_category_by_name, delete_category
from persistence.model import Category

CATEGORY_NAME = 'a better name'
CATEGORY_NAME_UPDATED = 'a better changed name'


def create():
    category = Category()
    category.name = CATEGORY_NAME
    add_category(category)


def method_one():
    create()
    category = get_category_by_name(CATEGORY_NAME)
    if category:
        print(category.serialize)
    else:
        print('not found')
    category.name = CATEGORY_NAME_UPDATED
    update_category(category)
    category = get_category_by_name(CATEGORY_NAME_UPDATED)
    if category:
        print(category.serialize)
    else:
        print('not found')
    delete_category(category)


if __name__ == '__main__':
    method_one()
    categories = get_categories()
    print([i.serialize for i in categories])
