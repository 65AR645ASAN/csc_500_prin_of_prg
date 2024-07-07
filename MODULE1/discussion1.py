def gather_ingredients():
    """
    Gather all the ingredients needed for baking cookies.
    
    Returns:
        dict: A dictionary containing the ingredients and their quantities.
    """
    ingredients = {
        'flour': '2 cups',
        'sugar': '1 cup',
        'butter': '1/2 cup',
        'eggs': '2',
        'baking_powder': '1 tsp',
        'vanilla_extract': '1 tsp',
        'chocolate_chips': '1 cup (optional)'
    }
    return ingredients


def preheat_oven(temp=350):
    """
    Preheat the oven to a specified temperature.
    
    Args:
        temp (int, optional): The temperature to preheat the oven to. Defaults to 350°F.
    """
    print(f"Preheating the oven to {temp}°F...")


def prepare_dough(ingredients):
    """
    Prepare the cookie dough by mixing the ingredients in the correct order.
    
    Args:
        ingredients (dict): A dictionary containing the ingredients and their quantities.
    
    Returns:
        list: A list representing the mixed dough.
    """
    # Step 1: Mix dry ingredients
    dry_ingredients = [ingredients['flour'], ingredients['baking_powder']]
    print("Mixing dry ingredients:", dry_ingredients)

    # Step 2: Cream together butter and sugar
    wet_ingredients = [ingredients['butter'], ingredients['sugar']]
    print("Creaming butter and sugar:", wet_ingredients)

    # Step 3: Beat in eggs and vanilla extract
    wet_ingredients += [ingredients['eggs'], ingredients['vanilla_extract']]
    print("Adding eggs and vanilla extract:", wet_ingredients)

    # Step 4: Blend in dry ingredients
    dough = wet_ingredients + dry_ingredients
    print("Blending in dry ingredients:", dough)

    # Step 5: Stir in chocolate chips if using
    if 'chocolate_chips' in ingredients:
        dough.append(ingredients['chocolate_chips'])
        print("Stirring in chocolate chips:", ingredients['chocolate_chips'])

    return dough


def form_cookies(dough):
    """
    Form the cookie dough into individual cookies on a baking sheet.
    
    Args:
        dough (list): The mixed dough ready to be formed into cookies.
    """
    print("Forming cookies on the baking sheet...")


def bake_cookies(time=10):
    """
    Bake the cookies in the oven for a specified amount of time.
    
    Args:
        time (int, optional): The baking time in minutes. Defaults to 10 minutes.
    """
    print(f"Baking cookies for {time} minutes...")


def cool_and_serve():
    """
    Cool the cookies on the baking sheet and then transfer them to wire racks to cool completely.
    """
    print("Cooling cookies on the baking sheet...")
    print("Transferring to wire racks to cool completely...")


def bake_cookies_algorithm():
    """
    The main algorithm for baking cookies, which includes gathering ingredients,
    preheating the oven, preparing the dough, forming cookies, baking, and cooling.
    """
    # Step 1: Gather ingredients
    ingredients = gather_ingredients()
    print("Ingredients gathered:", ingredients)

    # Step 2: Preheat the oven
    preheat_oven()

    # Step 3: Prepare the dough
    dough = prepare_dough(ingredients)

    # Step 4: Form cookies on baking sheet
    form_cookies(dough)

    # Step 5: Bake
    bake_cookies()

    # Step 6: Cool and serve
    cool_and_serve()
    print("Cookies are ready to serve!")


# Run the baking cookies algorithm
bake_cookies_algorithm()
