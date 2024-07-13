# Cookie Baking Algorithm

The following flowchart describes the algorithm for baking cookies:

```mermaid
graph TD
    A[Start] --> B[Gather Ingredients]
    B --> C[Preheat Oven to 350°F]
    C --> D[Prepare Dough]
    D --> E[Form Cookies on Baking Sheet]
    E --> F[Bake for 8-10 minutes]
    F --> G[Cool and Serve]
    G --> H[End]

    subgraph Prepare Dough
        D1[Mix Dry Ingredients]
        D2[Cream Butter and Sugar]
        D3[Beat in Eggs and Vanilla]
        D4[Blend in Dry Ingredients]
        D5[Stir in Chocolate Chips]
        D1 --> D2
        D2 --> D3
        D3 --> D4
        D4 --> D5
        D5 --> E
    end