graph TD
    A2[Start] --> B2{condition1}
    B2 --|True|--> D2[Do something (short-circuit)]
    B2 --|False|--> C2{condition2}
    C2 --|True|--> D2[Do something]
    C2 --|False|--> E2[Do nothing]
