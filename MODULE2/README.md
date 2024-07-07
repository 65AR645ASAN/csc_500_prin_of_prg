# Short-Circuiting in Python

## Introduction

Short-circuiting is a programming concept that occurs with logical operators in compound conditional expressions. In Python, the logical operators `and` and `or` exhibit short-circuit behavior. This means that the evaluation of the expression stops as soon as the result is determined, potentially avoiding unnecessary computation.

## Flowchart

### `and` Short-Circuiting

```mermaid
graph TD
    A[Start] --> B{condition1}
    B -- False --> E[Do nothing (short-circuit)]
    B -- True --> C{condition2}
    C -- True --> D[Do something]
    C -- False --> E[Do nothing]
