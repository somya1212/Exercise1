**Targets**
- `eval/p05_candidate.py` (two_sum)
- `eval/p09_candidate.py` (roman_to_int)

**New tests**
- `tests_added/test_p05_llm_iter2.py`: multiple valid pairs → first-by-index, no-solution variants, duplicates/zeros clarified.
- `tests_added/test_p09_llm_iter2.py`: composite subtractive numerals (XLII, XCIX, CDXLIV, MCMXCIV) + mixed cases.

**Result**
- P05: ✅ all tests pass. Coverage unchanged (100% line/branch).
- P09: ❌ expected failures on subtractive & composite cases (IV, IX, XL, XC, CD, CM, XLII, XCIX, CDXLIV, MCMXCIV). Implementation still sums symbols only.

**Takeaway**
- Tests now clearly document the roman subtractive-rule requirement without modifying code.


| **Iteration (i)** | **Line Coverage %** | **Branch Coverage %** | **Δ (vs previous)** | **Δ (vs i − 2)** | **Notes**                                                                              |
| :---------------: | :-----------------: | :-------------------: | :-----------------: | :--------------: | :------------------------------------------------------------------------------------- |
|     **i = 1**     |         14 %        |          14 %         |          —          |         —        | Initial baseline (before adding LLM tests)                                             |
|     **i = 2**     |         14 %        |          14 %         |         +0 %        |         —        | No change after first set of tests                                                     |
|     **i = 3**     |         41 %        |          41 %         |        +27 %        |       +27 %      | Significant increase after adding cumulative LLM-generated tests (p05 and p09 → 100 %) |

