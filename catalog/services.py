from catalog.models import Product


def get_products_by_category(category_id):
    product_list = Product.objects.filter(category_id=category_id)
    return product_list
