# Part 1 – Baseline Coverage

This section establishes baseline line and branch coverage for all problems (P01 – P10).  
Problems **P05** and **P09** were selected for deeper analysis in Parts 2 and 3.

| Problem | Tests Passed? | Line % | Branch % | Notes |
|:--------:|:--------------:|:------:|:---------:|:------|
| P01 | ✓ | 100 | N/A | No branches in file. |
| P02 | ✓ | 100 | N/A | No branches in file. |
| P03 | ✓ | 100 | 100 | 6 branches – all covered (partial = 0). |
| P04 | ✓ | 100 | 100 | 4 branches – all covered (partial = 0). |
| P05 | ✓ | **83** | < 100 | 4 branches with partial = 1 ⇒ at least one branch path untested. Good Part 2 candidate. |
| P06 | ✓ | 100 | N/A | No branches in file. |
| P07 | ✓ | 100 | N/A | No branches in file. |
| P08 | ✓ | 100 | 100 | 2 branches – all covered (partial = 0). |
| P09 | ✗ | 100 | 100 | 2 branches covered, but functional bug: `roman_to_int("IV") → 6`. Keep for Part 3. |
| P10 | ✓ | 100 | 100 | 8 branches – all covered (partial = 0). |
