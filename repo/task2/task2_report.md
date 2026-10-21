# Task 2: Audit and Redesign My Own Curriculum

**Question:** What should my degree keep, update, reduce or add to prepare graduates for work in 2030?
**Status:** Student proposal. This is not an official ICFAI syllabus revision.
**Chosen role:** Entry-level software engineer (backend / full-stack, with AI exposure).

## 1. Starting point

| Item | Value |
|---|---|
| Campus / degree / branch | ICFAI Tech / B. Tech / CSE. The transcript shows a computing programme with AI, Software Developer and Data Science courses. |
| Batch | Transcript starts 2023-24 (admission batch 2023) |
| Curriculum version | Taken from my own transcript (semesters I-VI) plus the semester VII-VIII details I supplied. **No official syllabus document has been checked for my batch.** |
| Official references | The assignment lists four ICFAITech pages [1]-[4]. I did not open them for this report. My automated search returned other universities' pages, not the ICFAI ones, so nothing here relies on them. I used ICFAI SIS: http://111.93.16.209/sz/login.aspx

**Why the official reference example does not replace my transcript:** The assignment's example structure names CS309 Cloud Computing and CS311 Software Testing. My transcript has CS307 Cloud Computing and no Software Testing course. Course codes and contents therefore differ by programme or batch, and my own transcript is the baseline.

### 1.1 Baseline credits (from my transcript and your semester VII-VIII details)

| Semester | Credits | Notes |
|---|---:|---|
| I | 20 | |
| II | 24 | |
| III | 23 | |
| IV | 24 | |
| Summer term II (IP201 Internship-I) | 3 | |
| V | 21 | |
| VI | 21 | |
| VII | 16 | Deep Learning 4; NLP, Ethical Hacking, Intro to Entrepreneurship, HCI 3 each. **Course codes unavailable.** |
| VIII | 15 | Internship. **Code unavailable.** |
| **Total programme** | **167** | Cumulative units on the transcript (136 after semester VI) agree with my sums. |

Unavailable details: semester VII and VIII codes, whether any semester VII courses are electives or alternatives, and the contents (syllabi) of every course. When I write "present", I mean the title suggests coverage.

The full map is in `course_map.csv` and the interactive view.

## 2. Evidence: three dated job descriptions

| # | Employer / role | Date given | Type of source |
|---|---|---|---|
| J1 | Alaan, Full Stack Engineering Intern (backend focus) | 13 Oct 2026 | Full job description text |
| J2 | Tescra (posting for ACHNET), Software Engineer, Bangalore/Remote | 15 Oct 2026 | Job description PDF |
| J3 | Amazon, SDE-I for 2027 batch | 28 Aug 2026 | **Resume-building tips that summarize the JD's themes, not the JD itself.** Its keyword list is useful but secondary evidence. |

### 2.1 Requirement-to-curriculum comparison

"Absent" means no course in my transcript appears to cover it. "Present, needs practice" means a relevant course exists but its title alone does not show whether this skill is taught or assessed.

| Requirement | Source | Existing teaching | Finding | Proposed change |
|---|---|---|---|---|
| Data structures, algorithms, complexity | J1, J2, J3 | CS102, CS203 | Present | KEEP |
| OOP / object-oriented design | J2, J3 | CS201 | Present, needs practice (design patterns not evident from title) | UPDATE CS201 |
| HTML/CSS/JavaScript | J2 | CS205 | Present | UPDATE CS205 |
| TypeScript, Node.js, Express/NestJS | J1 | None evident | **Absent** | UPDATE CS205 + ADD Studio |
| React / Next.js | J1 | None evident | **Absent** | ADD Studio |
| REST APIs, microservices | J1, J3 | CS205, CS307 | Present, needs practice | UPDATE CS205, CS307 |
| SQL / PostgreSQL / MySQL, indexing | J1, J3 | CS206 | Present, needs practice (engine, indexing depth unknown) | UPDATE CS206 |
| NoSQL (MongoDB, Redis) | J2 | DS307 (possible) | Unverified | UPDATE CS206 |
| Git, version control, code review | J1 | CS304 (possible) | Present, needs practice | UPDATE CS304 |
| Agile/Scrum | J1, J2, J3 | CS304 | Present | UPDATE CS304 |
| ML models (YOLO, LLM, NER) | J2 | DS304, CS305, Deep Learning, NLP | Present | KEEP |
| Distributed systems, scalable systems, fault tolerance | J3 | DS307, CS307, DS303 (partial) | **Absent as a dedicated subject** | ADD Distributed Systems |
| Operating systems | J3 | CS302 | Present | KEEP |
| CI/CD, Docker, unit testing | J3 | None evident | **Absent** | ADD DevOps; UPDATE CS304, CS307 |
| Linear programming / optimization | J3 | None evident | **Absent**. Weakest evidence (secondary source); **not addressed** in this proposal. | Note only |
| Portfolio / Git profile, deployed projects | J1, J2, J3 | SP301, internships | Present but not assessed as a portfolio | ADD Studio deliverable |
| Working in ambiguity, ownership | J1, J3 | Internships | Present | KEEP |

## 3. Proposal

### 3.1 Credit result

| Measure | Credits |
|---|---:|
| Baseline total | 167 |
| Credits removed (REDUCE) | 8 |
| Credits added (ADD) | 8 |
| **Proposed total** | **167** (balanced) |
| Credits in UPDATE courses (content rewrite, credits unchanged) | 22 |
| **Affected credits = added + removed + UPDATE** | 8 + 8 + 22 = **38** |
| **Share of programme** | 38 / 167 = **22.8%** (inside 20-25%) |

The definition of "affected" is my own choice and is stated so reviewers can check it. Counting differently would change the percentage.

### 3.2 Changes

**REDUCE (8 credits removed; subjects kept, not called obsolete)**

| Course | Now → Proposed | Reason |
|---|---|---|
| PHY101 Physics | 5 → 3 | Largest single credit weight among first-year foundation courses (R1) |
| MT102 Engineering Graphics | 3 → 2 | Overlaps with MT101 (R2) |
| MT101 Digital Fabrication | 3 → 2 | Overlaps with MT102 (R2) |
| EC101 Basic Electronics | 4 → 3 | EC201 IoT and EC102 revisit the topics (R3) |
| CH101 Chemistry | 4 → 3 | Basic-science weight is high for a computing degree (R4) |
| EC102 Signal Processing | 3 → 2 | Core transforms retained; weight shifted to systems skills (R5) |
| DS303 Blockchain | 3 → 2 | Consensus content moves to Distributed Systems (R6) |

All reductions that touch basic-science or engineering-science courses are **conditional** on the regulatory minimum for those categories, which I could not check. If a regulation blocks a reduction, the alternative is to keep the credits and make the new course an elective from the same slot.

**ADD (8 credits)**

| Course | Credits | Semester | Prerequisites |
|---|---:|---|---|
| Full-Stack Engineering Studio (includes the Task 1 capstone) | 3 | V | CS201, CS205, CS206 |
| Distributed Systems and System Design | 3 | VI | CS302, CS306, CS206 |
| DevOps, CI/CD and Testing Practice | 2 | VII | CS304, CS307 |

**UPDATE (22 credits, no credit change):** CS201 (design patterns, OOD), CS205 (TypeScript, Node, React basics), CS206 (PostgreSQL, indexing, NoSQL module), CS304 (Git workflow, Scrum, code review, testing), CS307 (containers, microservices), DS307 (streaming, storage and indexing).

**KEEP:** The remaining 120 credits, including all mathematics, core CS (CS102, CS202, CS203, CS204, CS302, CS306), the AI/ML sequence (DS101, DS201, DS304, CS305, Deep Learning, NLP), security (CS301, Ethical Hacking), internships and the project.

### 3.3 Credits by semester

| Semester | Before | After | Change | Driver |
|---|---:|---:|---:|---|
| I | 20 | 17 | -3 | PHY101 -2, MT102 -1 |
| II | 24 | 21 | -3 | EC101 -1, CH101 -1, MT101 -1 |
| III | 23 | 23 | 0 | UPDATE only |
| IV | 24 | 23 | -1 | EC102 -1 |
| Summer II | 3 | 3 | 0 | |
| V | 21 | 23 | +2 | DS303 -1, Studio +3 |
| VI | 21 | 24 | +3 | Distributed Systems +3 |
| VII | 16 | 18 | +2 | DevOps +2 |
| VIII | 15 | 15 | 0 | |
| **Total** | **167** | **167** | **0** | |

Semester VI at 24 credits equals the existing peak (semester IV at 24), so the load stays inside the range already in the programme.

**Feasibility for my own batch:** I have already completed semesters I-VI, so none of this can apply to my batch beyond a possible elective in semester VII-VIII. It is a proposal for a future cohort.

### 3.4 Reasons (course-referenced)

1. **R1 (PHY101):** Physics carries 5 credits, more than any computing course, while J1-J3 request none of it. I am proposing 3 credits, not removal.
2. **R2 (MT101, MT102):** Engineering Graphics and Digital Fabrication are adjacent design-skills courses. A one-credit trim each keeps the hands-on content.
3. **R3 (EC101):** Basic Electronics (4) is followed by EC201 IoT and EC102 Signal Processing, so one credit can move.
4. **R4 (CH101):** Chemistry (4) plus CH102 Environmental Sciences (2) gives six credits of chemistry-flavoured content. This is conditional on regulations.
5. **R5 (EC102):** DS-side transform content partly appears in MA201; keep the core and trim one credit.
6. **R6 (DS303):** J3 stresses distributed systems and fault tolerance; consensus belongs there, so Blockchain can shrink.
7. **R7 (CS205, J1):** Web-Enabled Technologies exists, but J1 requires TypeScript, Node.js, Express/NestJS and React/Next.js. This is a **depth gap**, not a missing subject, so it is an UPDATE plus a project-based Studio.
8. **R8 (CS206, J1/J3):** DBMS exists; J1 and J3 name PostgreSQL/MySQL and indexing. UPDATE, not ADD.
9. **R9 (J3 vs DS307/CS307/CS302/CS306):** The pieces of distributed systems exist across four courses, but no course ties them together or teaches system design. This is the strongest "absent subject" finding.
10. **R10 (CS304, J1/J3):** Software Engineering should assess Git, code review, Scrum and testing, which are named by all three descriptions. The official example lists a separate Software Testing course I do not have.
11. **R11 (CR201-CR302):** The Power Skills courses are a natural place for portfolio and GitHub profile work (J1-J3 all reward demonstrable projects). I propose no credit change.
12. **R12 (DS304, CS305, NLP, Deep Learning):** J2's "good to have" ML models (YOLO, LLM, NER) are already covered, so I propose **no** AI addition. This matters because it shows I am not adding AI by default.

## 4. Task 1 as a capstone

**Host course:** Full-Stack Engineering Studio (new, 3 credits, semester V).
**Project:** Lab-access request tracker from Task 1 (hypothetical, synthetic data only).
**Prerequisite knowledge:** OOP (CS201), web basics (CS205), SQL (CS206).

**Learning outcomes**
1. Build a REST API (Node/Express or equivalent) with validation, statuses and an audit table in PostgreSQL.
2. Enforce role-based approval so only an authorized role can approve.
3. Handle a failed notification without losing the approval record.
4. Measure and report the value claimed in Task 1 with explicit assumptions.

**Synthetic dataset:** 200 fictional requests with missing fields, duplicates, timetable clashes and injected notification failures. It contains no real names, IDs or timetables.

**Milestone:** Working API plus a React form and an approver view, deployed to a free tier and linked from the student's portfolio.

**Acceptance tests (from the five Task 1 test cases)**

| Test | Pass condition |
|---|---|
| Normal request | Request ID created; status moves to pending approval |
| Missing information | Status "Incomplete"; nothing sent for approval |
| Duplicate | Flagged; no second approval created |
| Unauthorized approval | Action rejected; attempt logged |
| Failed step | Approval stays saved; notification marked failed; retry works |

**How students demonstrate the three required controls**
- **Approval control:** A test suite shows an unauthorized role is denied.
- **Failure recovery:** Fault injection on the notification service, with recovery shown.
- **Measured value:** Handling time and incomplete-request rate measured on the synthetic dataset, reported with sample size and limits. It must **not** be presented as proof of savings at a real college.

## 5. Validation and AI exercises

**Validation with a faculty member or recent graduate:** **Not done.** I had no access. Nothing in this report is attributed to a faculty member or graduate. I could not validate these findings with a faculty member or recent graduate. Therefore, the proposed changes to CS205 and CS304 need to be checked against the actual course syllabi or through feedback from someone familiar with the programme. Their answer to that single question would confirm or overturn R7 and R10.

**AI exercises:** Five exercises (CS203, CS206, MA202, CS306, CS302) are in `ai_exercises/ai_exercises.md`. All five answers were verified by code, and **no model errors were found**. The remaining risk is unstated assumptions and unmeasured performance claims.

## 6. Limits, and what could prove me wrong

- Course content is judged from titles only. If the syllabi show that CS205 already teaches Node.js and React, R7 weakens, and the Studio shrinks to a project course.
- Three job descriptions, one of them secondary (J3), are a small sample, and two are for internship-level or entry roles. They do not represent 2030.
- Credit reductions may be blocked by regulation, and that is why they are marked conditional.
- The weakest claim is R9. A dedicated distributed-systems subject could be disproved if DS307 or CS307 syllabi already cover consensus, replication and system design.
- **What changed my mind while drafting:** I first considered adding an AI/LLM engineering course because of J2. I dropped it because DS304, CS305, Deep Learning and NLP already cover what J2 lists.
- Linear programming/optimization (J3) is unaddressed because the evidence is secondary and a new course could not be justified from one source.

## Appendices
- A: `course_map.csv`, the full course map with status and credits
- B: `interactive/index.html`, a course filter, current-versus-proposed comparison and credit calculator
- C: `ai_exercises/`, the exercise log and verification script
- D: Job descriptions J1-J3 (supplied by the student/me).

## Distinguishing official facts from the proposal
**Official or student-record facts:** Transcript courses, codes and credits for semesters I-VI; semester VII-VIII details supplied by the student.
**My proposal:** Everything in Section 3 and Section 4.
