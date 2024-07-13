# Sample Project

This is a sample project to demonstrate Mermaid diagrams in PyCharm.

## Flowchart

```mermaid
graph TD;
    Start-->Determine_Number_of_Batches;
    Determine_Number_of_Batches-->Get_4_cups_of_flour_per_batch;
    Get_4_cups_of_flour_per_batch-->Get_1/3_cup_of_sugar_per_batch;
    Get_1/3_cup_of_sugar_per_batch-->Get_1/5_cup_of_butter_per_batch;
    Get_1/5_cup_of_butter_per_batch-->Get_1/4_Teaspoon_baking_powder_per_batch;
    Get_1/4_Teaspoon_baking_powder_per_batch-->Get_1_egg_per_batch;
    Get_1_egg_per_batch-->Get_2_Teaspoons_of_milk_per_batch;
    Get_2_Teaspoons_of_milk_per_batch-->More_Batches?;
    More_Batches?-->Mix_Ingredients;
    Mix_Ingredients-->Preheat_Oven_to_350°F;
    Preheat_Oven_to_350°F-->Shape_Cookies_on_Baking_Sheet;
    Shape_Cookies_on_Baking_Sheet-->Bake_for_10-12_Minutes;
    Bake_for_10-12_Minutes-->Cool_Cookies;
    Cool_Cookies-->Serve_and_Enjoy;
    Serve_and_Enjoy-->End;
    More_Batches?-->Determine_Number_of_Batches;
