# Short-Circuiting in Python

## Introduction

Short-circuiting is a programming concept that occurs with logical operators in compound conditional expressions. In Python, the logical operators `and` and `or` exhibit short-circuit behavior. This means that the evaluation of the expression stops as soon as the result is determined, potentially avoiding unnecessary computation.

## Flowchart

### `and` Short-Circuiting

graph TD
    A1[Start] --> B1{condition1}
    B1 --|False|--> E1[Do nothing (short-circuit)]
    B1 --|True|--> C1{condition2}
    C1 --|True|--> D1[Do something]
    C1 --|False|--> E1[Do nothing]
