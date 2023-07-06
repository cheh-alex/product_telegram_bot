import requests



def get_all_categories():
    ans = requests.get('https://dummyjson.com/products/categories')
    return ans.json()


def get_products_of_category(category):
    url = f'https://dummyjson.com/products/category/{category}'
    response = requests.get(url)
    return response.json()['products']
