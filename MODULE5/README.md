
## Simple Conditional Test

```mermaid
graph TD
    A1[Start] --> B1{condition1}
    B1 -- No --> E1[Short-circuit]
    B1 -- Yes --> C1{condition2}
    C1 -- Yes --> D1{condition3}
    C1 -- No --> E1[Short-circuit]
    D1 -- Yes --> F1[Do something else]
    D1 -- No --> G1[Stop]
    F1 --> H1{condition4}
    H1 -- Yes --> I1[End]
    H1 -- No --> J1[Reevaluate]