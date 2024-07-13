# Baking Cookies Algorithm for Multiple Batches

```mermaid
graph TD
    A[Start] --> B[Determine Number of Batches]
    B --> C[Get Flour]
    C --> D[Get Sugar]
    D --> E[Get Butter]
    E --> F[Get Baking Powder]
    F --> G[Get Eggs]
    G --> H[Get Milk]
    H --> I[Mix Ingredients]
    I --> J[Preheat Oven to 350 degrees]
    J --> K[Put Cookies on the Baking Sheet]
    K --> L[Bake Cookies for 15 minutes]
    L --> M[Cool Cookies]
    M --> N[Serve]
    N --> O[End]

    subgraph Get Flour
        C1[Get 4 cups of flour per batch]
        B --> C1
    end
    
    subgraph Get Sugar
        D1[Get 1/3 cup of sugar per batch]
        C --> D1
    end
    
    subgraph Get Butter
        E1[Get 1/5 cup of butter per batch]
        D --> E1
    end
    
    subgraph Get Baking Powder
        F1[Get 1/4 Teaspoon baking powder per batch]
        E --> F1
    end
    
    subgraph Get Eggs
        G1[Get 1 egg per batch]
        F --> G1
    end
    
    subgraph Get Milk
        H1[Get 2 Teaspoons of milk per batch]
        G --> H1
    end
