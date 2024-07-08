## Flowchart for Managing Student Grades

```mermaid
graph TD
    A1[Start] --> B1[Initialize StudentGrades class with student_grades array]
    B1 --> C1[Call calculate_average]
    C1 --> D1[Return average_grade]
    D1 --> E1[Print average_grade]
    E1 --> F1[Call find_highest]
    F1 --> G1[Return highest_grade]
    G1 --> H1[Print highest_grade]
    H1 --> I1[Call find_lowest]
    I1 --> J1[Return lowest_grade]
    J1 --> K1[Print lowest_grade]
    K1 --> L1[End]
