# read_my_table.py
# Part of Lab 09 — feature/read-recipe branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Recipe_Book"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_recipe(recipe_book):
    recipe = recipe_book.get("Recipe", "Unknown Recipe")
    servings = recipe_book.get("Servings", "Unknown Servings")

    print(f"  Recipe  : {recipe}")
    print(f"  Servings   : {servings}")
    print()


def print_all_recipes():
    """Scan the entire Recipe_Book table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No recipes found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} recipe(s):\n")
    for recipe in items:
        print_recipe(recipe)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_recipes()


if __name__ == "__main__":
    main()