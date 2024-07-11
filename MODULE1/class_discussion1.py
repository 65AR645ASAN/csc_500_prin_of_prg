class CookieBaking:
    def __init__(self):
        """
        Initialize the CookieBaking class and gather all the ingredients needed for baking cookies.
        """
        self.ingredients = {
            'flour': '2 cups',
            'sugar': '1 cup',
            'butter': '1/2 cup',
            'eggs': '2',
            'baking_powder': '1 tsp',
            'vanilla_extract': '1 tsp',
            'chocolate_chips': '1 cup'
        }

    @staticmethod
    def preheat_oven(temp=350):
        """
        Preheat the oven to a specified temperature.

        Args:
            temp (int, optional): The temperature to preheat the oven to. Defaults to 350°F.
        """
        print(f"Preheating the oven to {temp}°F...")

    def prepare_dough(self):
        """
        Prepare the cookie dough by mixing the ingredients in the correct order.

        Returns:
            list: A list representing the mixed dough.
        """
        # Step 1: Mix dry ingredients
        dry_ingredients = [self.ingredients['flour'], self.ingredients['baking_powder']]
        print("Mixing dry ingredients:", dry_ingredients)

        # Step 2: Cream together butter and sugar
        wet_ingredients = [self.ingredients['butter'], self.ingredients['sugar']]
        print("Creaming butter and sugar:", wet_ingredients)

        # Step 3: Beat in eggs and vanilla extract
        wet_ingredients += [self.ingredients['eggs'], self.ingredients['vanilla_extract']]
        print("Adding eggs and vanilla extract:", wet_ingredients)

        # Step 4: Blend in dry ingredients
        dough = wet_ingredients + dry_ingredients
        print("Blending in dry ingredients:", dough)

        # Step 5: Stir in chocolate chips if using
        if 'chocolate_chips' in self.ingredients:
            dough.append(self.ingredients['chocolate_chips'])
            print("Stirring in chocolate chips:", self.ingredients['chocolate_chips'])

        return dough

    @staticmethod
    def form_cookies(dough):
        """
        Form the cookie dough into individual cookies on a baking sheet.

        Args:
            dough (list): The mixed dough ready to be formed into cookies.
        """
        print("Forming cookies on the baking sheet...")

    @staticmethod
    def bake_cookies(time=10):
        """
        Bake the cookies in the oven for a specified amount of time.

        Args:
            time (int, optional): The baking time in minutes. Defaults to 10 minutes.
        """
        print(f"Baking cookies for {time} minutes...")

    @staticmethod
    def cool_and_serve():
        """
        Cool the cookies on the baking sheet and then transfer them to wire racks to cool completely.
        """
        print("Cooling cookies on the baking sheet...")
        print("Transferring to wire racks to cool completely...")

    def run(self):
        """
        The main algorithm for baking cookies, which includes preheating the oven, preparing the dough,
        forming cookies, baking, and cooling.
        """
        print("Ingredients gathered:", self.ingredients)
        self.preheat_oven()
        dough = self.prepare_dough()
        self.form_cookies(dough)
        self.bake_cookies()
        self.cool_and_serve()
        print("Cookies are ready to serve!")


# Run the baking cookies algorithm
if __name__ == "__main__":
    cookie_baking = CookieBaking()
    cookie_baking.run()
