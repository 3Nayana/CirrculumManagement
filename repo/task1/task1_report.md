TASK 1: INVESTIGATION AND REDESIGN OF AN ENGINEERING GRAPHICS LAB ACCESS WORKFLOW

1. Introduction

Students sometimes require additional laboratory practice beyond their regularly scheduled practical sessions. Engineering Graphics is one example of a subject in which students may benefit from extra practice time. However, additional access to a laboratory depends on factors such as scheduled classes, laboratory availability, and permission from the responsible staff member.

During my first year at ICFAI, a few friends and I requested permission from a laboratory staff member to use a lab for practising Engineering Graphics outside our scheduled laboratory hours. We were allowed to practise when no class was scheduled to use the lab. I have also heard from other students that similar requests are made, although I have not independently verified the current procedure.

This experience provides the starting point for investigating a small college workflow: how students request permission to use a laboratory outside their scheduled practical hours.

The purpose of this investigation is to develop a structured, hypothetical workflow for handling such requests. The proposed solution will support request submission, availability checks, approval by authorized staff, status tracking, and record keeping. The project does not assume that the existing ICFAI process is entirely manual or that the college has an identified operational problem. These matters would require further investigation and permission.

2. Problem Statement and Objectives

Problem statement

Students who need additional laboratory practice may need to contact the responsible staff member and establish whether the laboratory is available. If requests are handled through informal communication, possible challenges could include incomplete request details, uncertainty about availability, repeated communication, and difficulty tracking the final decision.

These are potential problems to investigate, not confirmed shortcomings of ICFAI's current laboratory management process.

Objectives

1. Document the known background of additional lab-access requests.
2. Develop an explicitly hypothetical model of the current request process.
3. Identify the roles, decisions, handoffs, and exceptions involved.
4. Estimate request-handling effort using clearly labelled synthetic data.
5. Design a structured request-management workflow.
6. Test the proposed workflow against five synthetic scenarios.
7. Estimate possible time savings, implementation effort, and risks.
8. Identify the evidence required before the proposed solution could be recommended for actual use.

3. Evidence and Investigation Method

3.1 Available evidence

The investigation begins with my recollection of a first-year experience in which a small group of students asked a laboratory staff member for permission to practise Engineering Graphics outside scheduled lab hours. Permission was granted when the laboratory was not required for a class.

I have also heard from other students that similar requests continue to occur. This is second-hand information and has not been independently confirmed.

No current staff interview, direct observation of the present workflow, official procedure document, request log, or measured timing data is available for this report.

3.2 Evidence classification

| Evidence item | Classification | Limitation |
|---|---|---|
| Students requested additional lab access during my first year | Personal recollection | Exact date and frequency are not recorded |
| Permission was granted when the lab had no scheduled class | Personal recollection | Does not establish the current approval policy |
| Other students reportedly make similar requests | Second-hand information | Not independently verified |
| Current request volumes and processing times | Unavailable | No measured data |
| Proposed request form and approval workflow | Design proposal | Not an existing confirmed ICFAI system |
| Numerical workload and savings calculations | Synthetic estimates | Must be validated using real data |

3.3 Investigation method

The current report uses a hypothetical walkthrough because access to the present operational process has not been obtained.

The next stage, subject to permission, would involve asking a responsible lab staff member to explain the process, observing a permitted walkthrough, and recording the steps and approximate timings. Only the staff member's role would be recorded; names and private information would not be collected.

4. Current-State Workflow: Hypothetical Model

The following workflow is a proposed model based on the known background. It is not a verified map of ICFAI's current procedure.

1. A student identifies a need for additional laboratory practice.
2. The student contacts the responsible lab staff member to request access.
3. The staff member checks whether the laboratory is needed for a scheduled class or other authorized activity.
4. The staff member considers whether the request can be accommodated.
5. The staff member grants or declines permission.
6. The student receives the decision and follows the applicable instructions.

Roles and responsibilities

- **Student:** Explains the purpose, requested date, time, and expected duration.
- **Lab staff member:** Receives the request, checks relevant availability, and communicates the decision within their authority.
- **Timetable or laboratory coordinator, if applicable:** Helps resolve scheduling conflicts or requests outside the staff member's authority.
- **Authorized institutional authority, if required:** Decides exceptions according to applicable college rules.

The exact responsibilities and approval boundaries must be confirmed before this model can be treated as the actual process.

Potential exceptions

- The requested time overlaps with a scheduled class.
- The request lacks a date, time, or purpose.
- Multiple students request the same available period.
- The requested access requires additional authorization.
- The laboratory becomes unavailable after permission is granted.
- The responsible staff member cannot immediately confirm availability.

5. Operational Problem and Workload Estimate

Because actual request volumes and processing times are unavailable, the following calculations use a synthetic scenario to demonstrate the required method.

5.1 Hypothetical baseline

Assume that the process receives 40 requests per month.

Assume the average staff effort per request is eight minutes, including receiving the request, checking availability, and communicating the decision.

Assume 25% of requests require five additional minutes of rework because some information is missing or needs clarification.

Base handling effort:

40 requests * 8 minutes = 320 minutes.

Rework effort:

40 * 25% * 5 minutes = 50 minutes.

Total monthly effort:

320 + 50 = 370 minutes.

370 / 60 = approximately 6.17 staff-hours per month.

These figures are illustrative only and do not represent measured ICFAI workload.

5.2 Sensitivity to request volume

Using the same hypothetical assumptions:

| Requests per month | Base effort | Rework | Total effort |
|---:|---:|---:|---:|
| 20 | 160 min | 25 min | 185 min |
| 40 | 320 min | 50 min | 370 min |
| 80 | 640 min | 100 min | 740 min |

The calculation suggests that total effort increases with request volume. The actual scale of the problem cannot be established until request volumes and timings are measured.

6. Proposed Workflow

The proposed system is a small lab-access request tracker. It would not automatically grant laboratory access.

Step 1: Submit a request

The student enters the requested date, start time, end time, purpose, and approximate number of students.

Step 2: Validate the request

The system checks that required fields are completed and that the requested end time is later than the start time. Incomplete requests are returned for correction.

Step 3: Assign a request ID

Each request receives a unique reference number. The system checks for possible duplicate submissions using the requester-independent request details and an appropriate duplicate-checking rule.

Step 4: Check availability

The proposed system checks a permitted, current timetable or requires an authorized staff member to verify availability. It must not assume that an empty timetable entry automatically means that access is permitted.

Step 5: Refer the request for approval

The request is sent to the authorized lab staff member. Requests outside the person's approval authority are escalated to the appropriate authority.

Step 6: Record the decision

The authorized staff member approves, rejects, or requests further information. Each decision is associated with the request ID, status, timestamp, and authorized role.

Step 7: Notify the student

The student receives the decision and any applicable instructions. A failed notification does not erase the request or approval record.

Step 8: Handle failures

If the timetable cannot be accessed or the system fails, the request is marked as awaiting verification. The responsible staff member follows an approved fallback procedure. No access is granted solely because of a system failure.

Request statuses

- Submitted
- Incomplete
- Awaiting availability check
- Pending approval
- Approved
- Rejected
- More information required
- Cancelled
- Notification failed

Accountability and audit

The designated lab authority remains accountable for approval decisions. The system records request creation, changes in status, the authorized decision, and notification attempts. Access to records is restricted to authorized users, and records are retained only according to an approved policy.

7. Role of Software, Rules, and AI

Ordinary software and explicit rules are sufficient for most functions in this project.

| Function | Recommended method | Reason |
|---|---|---|
| Required-field checks | Ordinary software | Deterministic validation |
| Unique request ID | Ordinary software | Simple and reliable |
| Duplicate detection | Rules | Similar requests can be flagged for review |
| Timetable conflict checks | Rules and verified timetable data | Depends on accurate scheduling information |
| Approval | Authorized human decision | Access must follow institutional authority |
| Status tracking | Ordinary software | Structured records are sufficient |
| Categorizing unusual free-text requests | Optional AI assistance | May help if requests become varied or numerous |

AI is not necessary for the initial prototype. It would add complexity without a demonstrated need. If introduced later, AI could suggest request categories or summarize non-confidential descriptions, but it should not independently authorize access or override institutional rules.

8. Five Synthetic Test Cases

All cases below use fictional data. They test the proposed design, not an existing ICFAI system.

Test Case 1: Normal request

**Input:** A student requests access on a proposed date from 3:00 PM to 4:00 PM and supplies all required details.

**Expected result:** The system creates a request ID, verifies availability through the authorized procedure, and sends the request for approval.

**Recovery:** If availability cannot be confirmed, the request remains pending verification.

**Decision owner:** Authorized lab staff member.

Test Case 2: Missing information

**Input:** A request includes the date but omits the requested time.

**Expected result:** The system marks the request as incomplete and asks for the missing information.

**Recovery:** The student supplies the missing time, and the request proceeds through validation.

**Decision owner:** The student corrects the information; authorized lab staff decide on access.

Test Case 3: Duplicate request

**Input:** A student submits the same request twice for the same date, time, and purpose.

**Expected result:** The system flags a possible duplicate and retains the original request. It does not create a second approval automatically.

**Recovery:** An authorized user checks whether the submissions are genuinely duplicates.

**Decision owner:** The responsible staff member resolves the flagged case.

Test Case 4: Unauthorized approval

**Input:** A user without approval authority attempts to approve a request.

**Expected result:** The system denies the approval action and records the unauthorized attempt where appropriate.

**Recovery:** The request is routed to an authorized approver.

**Decision owner:** The designated institutional authority.

Test Case 5: Failed step

**Input:** A request is approved, but the notification service fails.

**Expected result:** The approval record remains saved, while the notification status is marked as failed.

**Recovery:** The system retries notification or the responsible staff member communicates the decision through an approved fallback method.

**Decision owner:** Authorized staff remain responsible for the decision; the designated system support role handles the technical failure.

9. Proposed Workflow Evaluation and ROI

For a second synthetic calculation, assume that the proposed workflow reduces routine staff handling from eight minutes to three minutes per request. Assume the rework rate falls from 25% to 10%, and that each reworked request requires three additional minutes.

These are design assumptions to be tested, not measured improvements.

Baseline monthly effort

40 * 8 + 40 * 25% * 5 = 370 minutes.

Proposed monthly effort

40 * 3 + 40 * 10% * 3 = 132 minutes.

Gross monthly time saved

370 - 132 = 238 minutes, or approximately 3.97 hours.

If the workflow requires one hour of monthly support and maintenance, net recurring savings would be approximately:

3.97 - 1 = 2.97 hours per month.

If initial design and implementation require 12 hours, the estimated break-even period would be:

12 / 2.97 = approximately 4.04 months.

This simple estimate excludes other costs, such as training, hosting, approvals, and unexpected maintenance. It also assumes that the estimated reduction in handling and rework actually occurs. Therefore, it is not sufficient evidence by itself to justify implementation.

Evaluation measures

The prototype should be assessed using:

- Average staff handling time per request.
- Percentage of requests missing required information.
- Duplicate requests detected.
- Time between submission and decision.
- Number of scheduling conflicts.
- Successful notification rate.
- Correct enforcement of approval permissions.
- Frequency and duration of system failures.

A fair comparison would use comparable request types and sample periods. Results should include sample size and limitations.

10. Risks and Limitations

1. **Unverified current process:** The actual ICFAI procedure has not been observed.
2. **Synthetic workload data:** The estimated request volume and handling times may differ from reality.
3. **Incorrect timetable information:** An outdated timetable could lead to a false availability result.
4. **Unauthorized access:** Access permissions must be enforced and tested.
5. **Operational disruption:** The prototype must not interfere with classes or existing laboratory procedures.
6. **Data privacy:** The project should use fictional records and avoid unnecessary personal information.
7. **Low volume or negligible rework:** If the existing process is already efficient, a new application may not justify its implementation and maintenance effort.
8. **Institutional policy:** The proposed workflow must not replace existing rules or delegated authority.

Evidence that would change the design

If a permitted walkthrough showed that requests are already recorded in an effective booking system, scheduling conflicts are rare, and handling takes very little time, I would reconsider the need for a separate application. A small improvement to the existing process might be more suitable.

11. Conclusion

This project uses a personal experience of requesting additional Engineering Graphics laboratory practice as the starting point for investigating laboratory access management. The experience establishes that an additional-access request occurred in that instance, but it does not establish the full current procedure or the scale of any operational problem at ICFAI.

A structured request tracker could potentially improve the completeness, traceability, and communication of lab-access requests. The proposed workflow includes validation, availability checks, authorized approval, audit records, and recovery procedures. Five synthetic test cases demonstrate how the design could handle routine and exceptional situations.

The workload and return-on-investment calculations are illustrative and must be validated through permitted observations and measured data before any real implementation is recommended. The immediate next step is to obtain permission for a walkthrough and determine whether the proposed improvement addresses a genuine, measurable need.

Appendix A: Evidence Log Template

| Date | Activity | Evidence or result | Classification | Sample size / limitation |
|---|---|---|---|---|
| [Actual date] | Recorded recollection of earlier lab-access request | Permission was granted when no class was using the lab | Personal recollection | One remembered instance; exact date unavailable |
| [Actual date] | Documented second-hand information | Other students reportedly make similar requests | Unverified report | No independent confirmation |
| [Actual date] | Developed current-state model | Hypothetical sequence of request, availability check, and decision | Assumption / model | Requires staff validation |
| [Actual date] | Developed synthetic test cases | Five fictional scenarios and expected results | Synthetic | Not observed operational outcomes |
| [Actual date] | Calculated workload and potential savings | Worked calculations based on stated assumptions | Estimate | No measured request volume or time data |

Appendix B: Evidence to Collect If Permission Becomes Available

- Confirmation of the actual request channel and required information.
- The roles responsible for availability checks and approval.
- A permitted walkthrough of one representative request.
- Timing observations for relevant processing steps.
- Counts of requests and rework over an agreed sample period.
- The actual exception-handling and fallback procedures.
- Feedback from a willing process user, recorded by role only.
- A record of unresolved questions and access limitations.