class Recipe:
    def __init__(self, name, images, ingredients, author,
                 date, rating, ingredient_quantities, preperation_time,
                 instructions, category, unique_id, cook_time, recipe_yield,
                 servings, description, reviews=list):
        self.__name = name
        self.__images = images
        self.__ingredients = ingredients
        self.__author = author
        self.__date = date
        self.__rating = rating
        self.__ingredient_quantities = ingredient_quantities
        self.__preparation_time = preperation_time
        self.__instructions = instructions
        self.__category = category
        self.__ID = unique_id
        self.__cook_time = cook_time
        self.__recipe_yield = recipe_yield
        self.__servings = servings
        self.__description = description
        self.__reviews = reviews

    def __repr__(self):
        return (f"Recipe {self.__name} with id: {self.__ID} was created by {self.__author}"
                f"on {self.__date}")


