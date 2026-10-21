# Five AI exercises (Task 2)

**Tool / model:** Claude Sonnet 5.5 (free plan), session of 16 October 2026.
**Scope:** Each exercise is a small, generic, textbook-style problem with synthetic data. None uses graded, confidential or college-owned material.
**Verification:** Every answer was checked by running code (`verify_all.py`; log in `verification_log.txt`).


---

## Exercise 1: Design and Analysis of Algorithms (CS203)

**Task:** Analyse the time complexity of a nested-loop pair-sum check and improve it.

**Prompt:** "Here is a Python function `pair_quadratic(a, t)` that returns True if two different elements of list `a` sum to `t`, using two nested loops. State its time and space complexity, give a faster version, and state the new complexity and trade-off."

**Output (summary of the model's answer):**
- Nested loops run n(n-1)/2 comparisons, so the time is O(n²) and the space is O(1).
- A single pass with a hash set (check whether `t - x` was already seen, then add `x`) gives expected O(n) time and O(n) extra space.
- The trade-off is memory for time. Hash operations are O(1) on average, and the worst case depends on the hash function.

**Verification performed:**
- Compared both functions on 2000 random lists: **0 mismatches**.
- Timed the worst case (no pair exists): n=2000: 0.1665 s vs 0.0005 s; n=4000: 0.5595 s vs 0.0006 s; n=8000: 2.2247 s vs 0.0013 s.
- Doubling n roughly quadrupled the quadratic time (0.17 → 0.56 → 2.22 s), which is consistent with O(n²).

**What the model did:** The model derived the complexities and wrote the code. 

**Errors found:** None. No error is claimed.


---

## Exercise 2: Database Management Systems (CS206)

**Task:** Write an aggregate SQL query over a synthetic schema.

**Prompt:** "Tables: course(course_id, title), enrollment(student_id, course_id, grade_point). Write SQL for courses with at least 3 enrolled students and average grade point above 8.0, sorted by average descending. Suggest an index."

**Output (summary):**
```sql
SELECT c.course_id, c.title, COUNT(*) AS n, ROUND(AVG(e.grade_point),2) AS avg_gp
FROM course c JOIN enrollment e ON e.course_id = c.course_id
GROUP BY c.course_id, c.title
HAVING COUNT(*) >= 3 AND AVG(e.grade_point) > 8.0
ORDER BY avg_gp DESC;
```
- The model explained that the conditions on aggregates belong in `HAVING`, not `WHERE`.
- It suggested an index on `enrollment(course_id, grade_point)` to support the join and aggregation.

**Verification performed:** Ran the query in SQLite on 40 synthetic students × 3 random courses each (120 rows). Result: Course 6 (n=14, 8.36), Course 5 (n=23, 8.35), Course 2 (n=18, 8.28). An independent Python calculation gave **identical results**.



**Errors found:** None.


---

## Exercise 3: Discrete Mathematics (MA202)

**Task:** Count binary strings of length 10 with no two consecutive 1s.

**Prompt:** "How many binary strings of length 10 contain no two consecutive 1s? Derive a recurrence and give the answer."

**Output (summary):**
- Let a(n) be the count for length n. If the string ends in 0, the first n-1 symbols are any valid string, giving a(n-1) options. If it ends in 1, the previous symbol must be 0, giving a(n-2) options.
- So a(n) = a(n-1) + a(n-2), with a(1) = 2 and a(2) = 3 (equivalently a(0) = 1, a(1) = 2).
- Therefore a(10) = 144, which equals the Fibonacci number F(12).

**Verification performed:** Brute-force enumeration of all 1024 strings gave **144**. The recurrence computed in code also gave 144, and F(12) = 144.



**Errors found:* None.

---

## Exercise 4: Computer Networks (CS306)

**Task:** Subnetting.

**Prompt:** "Split 192.168.10.0/24 into at least 5 subnets with at least 25 usable hosts each. Give the prefix length and list the five subnets with their usable ranges and broadcast addresses."

**Output (summary):**
- 25 hosts need 5 host bits (2⁵ − 2 = 30 usable), so the prefix is /27.
- A /24 splits into 8 subnets of /27, so 5 subnets are available with 3 spare.
- Subnets: 192.168.10.0, .32, .64, .96, .128 (all /27). Usable hosts run from network+1 to broadcast−1; broadcasts are .31, .63, .95, .127, .159.

**Verification performed:** Python's `ipaddress` module confirmed /27, 30 usable hosts each, and the exact ranges and broadcasts above.


**Errors found:** None.


---

## Exercise 5: Operating Systems (CS302)

**Task:** Round Robin scheduling. This is a classic place for AI to slip on tie-breaking.

**Prompt:** "Round Robin, quantum 4. Processes (arrival, burst): P1(0,5), P2(1,3), P3(2,8), P4(3,6). Assume a process arriving while another is running enters the queue before the preempted process re-enters. Give the Gantt chart, completion, turnaround and waiting times and the averages."

**Output (summary):**
- Gantt: P1 0–4, P2 4–7, P3 7–11, P4 11–15, P1 15–16, P3 16–20, P4 20–22.
- Completion: P1 16, P2 7, P3 20, P4 22.
- Turnaround: 16, 6, 18, 19, average **14.75**.
- Waiting: 11, 3, 10, 13, average **9.25**.

**Verification performed:** A simulation using the same queue convention matched every number. Flipping the convention (preempted process re-enters first) would change the order, so the assumption must stay stated in the prompt and in any write-up.



**Errors found:** None. No error is claimed.


---

## Summary

| # | Subject | Result | Verified by | Error found |
|---|---|---|---|---|
| 1 | CS203 DAA | O(n²) → O(n) | 2000 tests + timing | None |
| 2 | CS206 DBMS | HAVING query | SQLite + Python cross-check | None |
| 3 | MA202 Discrete Maths | 144 | Brute force + recurrence | None |
| 4 | CS306 Networks | /27 ×5 subnets | `ipaddress` module | None |
| 5 | CS302 OS | Avg WT 9.25 | Simulation | None |

**Pattern across the five:** The model got all five right. The risk is not wrong arithmetic in these simple cases. It is **unstated assumptions** (duplicates in Ex. 1, base-case indexing in Ex. 3, subnet-zero in Ex. 4, queue tie-break in Ex. 5) and **unmeasured performance claims** (the index in Ex. 2).
