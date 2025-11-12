import json
import csv
# import pandas as pd
# import os

with open('recipes.json', 'r') as file:
    data = json.load(file)

# 12 recipe categories
recipe_categories = [
                      "Lunch recipes",
                      "Dinner recipes",
                      "Breakfast recipes",
                      "Storecupboard",
                      "Cheese recipes",
                      "Desserts",
                      "Fish and seafood",
                      "Pasta",
                      "Chicken",
                      "Meat",
                      "Vegan",
                      "Vegetarian"
                    ]

recipes_array = []
counter = 0
data = data['recipes']
# categories shown above
for category in recipe_categories:
    # each category has a subcategory ("quick lunch recipes", etc.)
    sub_category = data[category]
    for _, recipes in sub_category.items():
        # columns we want in our new category
        # we should save and export the columns we want this into a new csv
        for recipe in recipes:
            counter += 1
            # recipes_array.append({
            #     "id": recipe["id"],
            #     "name": recipe.get("name", ""),
            #     "ingredients": recipe.get("ingredients", []),
            #     "steps": recipe.get("steps", []),
            #     "description": recipe.get("description", ""),
            #     "times": recipe.get("times", {}),
            #     "difficulty": recipe.get("difficulty", ""),
            # })
            description = recipe.get('description', '')
            ingredients = ",".join(recipe.get('ingredients', []))
            steps = recipe.get("steps", [])
            prep_time = recipe.get('times', {}).get('preparation', '')
            cook_time = recipe.get('times', {}).get('cooking', '')
            difficult = recipe.get('difficult', '')
            text = f"{recipe.get('name', '')}. {description}. {ingredients}.\n"
            text += f"{steps}. Prep Time: {prep_time} Cook Time: {cook_time}."
            text += f"\nDifficulty: {difficult}."
            recipes_array.append([recipe["id"], text])
            if counter > 500:
                break

headers = ["id", "text"]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(recipes_array)

# print(recipes_array)