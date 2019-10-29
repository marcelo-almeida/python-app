from persistence.category_repository import CategoryRepository, Category

repository = CategoryRepository()


def add_category(category: Category):
    repository.add(category=category)


def update_category(category: Category):
    repository.update(category=category)


def delete_category(category: Category):
    repository.delete(category=category)


def count_categories() -> int:
    return repository.count()


def get_categories(limit=None, offset=None) -> list:
    return repository.get(limit=limit, offset=offset)


def get_category_by_id(category_id: int) -> Category:
    return repository.get_by_id(category_id=category_id)


def get_category_by_name(category_name: str) -> Category:
    return repository.get_by_name(category_name=category_name)
