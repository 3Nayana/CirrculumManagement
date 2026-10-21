"""Verification scripts for the five AI exercises (synthetic, non-confidential)."""
import time, random, sqlite3, ipaddress, itertools

# ---- Ex1: CS203 DAA - two-sum existence ----
def pair_quadratic(a, t):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == t:
                return True
    return False

def pair_hash(a, t):
    seen = set()
    for x in a:
        if t - x in seen:
            return True
        seen.add(x)
    return False

random.seed(1)
mism = 0
for _ in range(2000):
    a = [random.randint(-20, 20) for _ in range(random.randint(0, 12))]
    t = random.randint(-30, 30)
    if pair_quadratic(a, t) != pair_hash(a, t):
        mism += 1
print("EX1 mismatches over 2000 random tests:", mism)
for n in (2000, 4000, 8000):
    a = list(range(n)); t = -1  # worst case: no pair
    s = time.perf_counter(); pair_quadratic(a, t); q = time.perf_counter() - s
    s = time.perf_counter(); pair_hash(a, t); h = time.perf_counter() - s
    print(f"EX1 n={n}: quadratic {q:.4f}s, hash {h:.6f}s")

# ---- Ex2: CS206 DBMS ----
con = sqlite3.connect(":memory:")
c = con.cursor()
c.executescript("""
CREATE TABLE course(course_id INTEGER PRIMARY KEY, title TEXT);
CREATE TABLE enrollment(student_id INTEGER, course_id INTEGER, grade_point REAL);
""")
random.seed(7)
rows = [(s, cid, random.choice([6,7,8,9,10])) for s in range(1, 41) for cid in random.sample(range(1, 7), 3)]
c.executemany("INSERT INTO course VALUES (?,?)", [(i, f"Course {i}") for i in range(1, 7)])
c.executemany("INSERT INTO enrollment VALUES (?,?,?)", rows)
q = """SELECT c.course_id, c.title, COUNT(*) AS n, ROUND(AVG(e.grade_point),2) AS avg_gp
FROM course c JOIN enrollment e ON e.course_id = c.course_id
GROUP BY c.course_id, c.title
HAVING COUNT(*) >= 3 AND AVG(e.grade_point) > 8.0
ORDER BY avg_gp DESC;"""
sql_res = c.execute(q).fetchall()
from collections import defaultdict
d = defaultdict(list)
for s, cid, g in rows: d[cid].append(g)
py_res = sorted([(cid, f"Course {cid}", len(v), round(sum(v)/len(v), 2)) for cid, v in d.items() if len(v) >= 3 and sum(v)/len(v) > 8.0], key=lambda r: -r[3])
print("EX2 SQL result:", sql_res)
print("EX2 Python result:", py_res)
print("EX2 match (as sets):", set(sql_res) == set(py_res))

# ---- Ex3: MA202 Discrete Math ----
cnt = sum(1 for bits in itertools.product("01", repeat=10) if "11" not in "".join(bits))
fib = [0, 1]
for _ in range(15): fib.append(fib[-1] + fib[-2])
print("EX3 brute force count n=10:", cnt, "| F(12) =", fib[12])
a = [0]*11; a[0] = 1; a[1] = 2
for n in range(2, 11): a[n] = a[n-1] + a[n-2]
print("EX3 recurrence a(10) =", a[10])

# ---- Ex4: CS306 Networks ----
net = ipaddress.ip_network("192.168.10.0/24")
subs = list(net.subnets(new_prefix=27))[:5]
for s in subs:
    h = list(s.hosts())
    print("EX4", s, "hosts:", len(h), "range", h[0], "-", h[-1], "broadcast", s.broadcast_address)

# ---- Ex5: CS302 OS Round Robin ----
def rr(procs, q):
    procs = sorted(procs, key=lambda p: p[1]); rem = {p[0]: p[2] for p in procs}
    arr = {p[0]: p[1] for p in procs}; t = 0; queue = []; done = {}; gantt = []; i = 0
    def admit(t):
        nonlocal i
        while i < len(procs) and procs[i][1] <= t:
            queue.append(procs[i][0]); i += 1
    admit(0)
    while len(done) < len(procs):
        if not queue:
            t = procs[i][1]; admit(t); continue
        p = queue.pop(0); run = min(q, rem[p]); gantt.append((p, t, t+run)); t += run; rem[p] -= run
        admit(t)  # arrivals up to t enter before the preempted process
        if rem[p] > 0: queue.append(p)
        else: done[p] = t
    return gantt, done, arr
P = [("P1",0,5),("P2",1,3),("P3",2,8),("P4",3,6)]
g, done, arr = rr(P, 4)
burst = {p[0]: p[2] for p in P}
print("EX5 gantt:", g)
wt = {p: done[p]-arr[p]-burst[p] for p in done}; tat = {p: done[p]-arr[p] for p in done}
print("EX5 completion", done, "TAT", tat, "WT", wt)
print("EX5 avg WT", sum(wt.values())/4, "avg TAT", sum(tat.values())/4)
