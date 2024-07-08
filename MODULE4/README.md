# Flowchart for Short-Circuiting `and` Operator

```mermaid
graph TD
    A1[Start] --> B1{condition1}
    B1 -- No --> E1["False: One condition is False"]
    B1 -- Yes --> C1{condition2}
    C1 -- Yes --> D1["True: Both conditions are True"]
    C1 -- No --> E1["False: One condition is False"]
