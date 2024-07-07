graph TD
    A[Start] --> B{condition1}
    B -- True --> C[Evaluate condition2]
    C -- True --> D[Do something]
    C -- False --> E[Do nothing]
    B -- False --> E[Do nothing]

    subgraph OR Short-Circuiting
        A1[Start] --> B1{condition1}
        B1 -- True --> D1[Do something]
        B1 -- False --> C1[Evaluate condition2]
        C1 -- True --> D1[Do something]
        C1 -- False --> E1[Do nothing]
    end
