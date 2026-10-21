import json, csv
from pathlib import Path

# (sem, code, title, cur_credits, status, new_credits, note)
C = [
("I","CS101","Computer Programming",4,"KEEP",4,""),
("I","MT102","Engineering Graphics",3,"REDUCE",2,"Overlaps with Digital Fabrication; keep core drawing skills in 2 credits"),
("I","EG101","English Language Skills",3,"KEEP",3,""),
("I","CH102","Environmental Sciences",2,"KEEP",2,"Likely regulatory requirement"),
("I","HS101","Essence of Indian Traditional Knowledge",0,"KEEP",0,""),
("I","MA101","Linear Algebra and ODE",3,"KEEP",3,"Foundation for ML/DL"),
("I","PHY101","Physics",5,"REDUCE",3,"Conditional: basic-science minimum must be checked"),
("II","EC101","Basic Electronics",4,"REDUCE",3,"Conditional: engineering-science minimum must be checked"),
("II","CH101","Chemistry",4,"REDUCE",3,"Conditional: basic-science minimum must be checked"),
("II","CS102","Data Structures",4,"KEEP",4,"Core of all three JDs"),
("II","MT101","Digital Fabrication",3,"REDUCE",2,"Hands-on content kept"),
("II","MA102","Higher Calculus",3,"KEEP",3,""),
("II","DS101","Introduction to AI and DS",3,"KEEP",3,""),
("II","EG102","Professional Communication",3,"KEEP",3,""),
("III","CS203","Design and Analysis of Algorithms",3,"KEEP",3,"Amazon: algorithms, complexity"),
("III","MA202","Discrete Mathematics",3,"KEEP",3,""),
("III","MG201","Engineering Economics and Management",3,"KEEP",3,""),
("III","MA201","Integral Transforms and Probability & Statistics",3,"KEEP",3,""),
("III","EC201","Introduction to IoT",3,"KEEP",3,""),
("III","CS201","Object Oriented Programming Concepts",4,"UPDATE",4,"Add OOD: SOLID, Factory/Observer patterns, unit-tested projects"),
("III","CR201","Power Skills-I",1,"KEEP",1,""),
("III","CS202","Theory of Computation",3,"KEEP",3,""),
("IV","CS204","Computer Organization and Architecture",3,"KEEP",3,""),
("IV","DS203","Data Science",3,"KEEP",3,""),
("IV","CS206","Database Management Systems",4,"UPDATE",4,"Add PostgreSQL practice, indexing/query plans, MongoDB/Redis module"),
("IV","HS201","Dynamics of Social Change",3,"KEEP",3,""),
("IV","EC102","Fundamentals of Signal Processing",3,"REDUCE",2,"Conditional: keep core transforms; confirm prerequisites for DS courses"),
("IV","DS202","Industry Coding Practice (Python/R)",3,"KEEP",3,""),
("IV","CR202","Power Skills-II",1,"KEEP",1,""),
("IV","CS205","Web-Enabled Technologies",4,"UPDATE",4,"Add TypeScript, Node/Express, React basics, REST design"),
("ST","IP201","Internship-I",3,"KEEP",3,""),
("V","DS303","Blockchain Technology",3,"REDUCE",2,"Consensus content moved into Distributed Systems; ledger basics retained"),
("V","HS301","Constitution of India",0,"KEEP",0,""),
("V","DS304","Machine Learning",4,"KEEP",4,"Tescra: ML models"),
("V","CS302","Operating Systems",4,"KEEP",4,"Amazon: OS fundamentals"),
("V","CR301","Power Skills-III",1,"KEEP",1,""),
("V","CS301","Principles of Cryptography",3,"KEEP",3,""),
("V","CS303","Programming Language and Compiler Construction",3,"KEEP",3,""),
("V","CS304","Software Engineering",3,"UPDATE",3,"Add Git workflow, Scrum, code review, unit/integration testing"),
("V","NEW-A","Full-Stack Engineering Studio (incl. Task 1 capstone)",0,"ADD",3,"Prereqs: CS201, CS205, CS206"),
("VI","DS307","Big Data Systems",3,"UPDATE",3,"Add stream processing, storage/indexing"),
("VI","CS307","Cloud Computing",4,"UPDATE",4,"Add containers (Docker) and microservices lab"),
("VI","CS306","Computer Networks",4,"KEEP",4,""),
("VI","CS305","Computer Vision",3,"KEEP",3,"Tescra: YOLO-type models"),
("VI","CR302","Power Skills-IV",1,"KEEP",1,""),
("VI","SP301","Special Project",3,"KEEP",3,""),
("VI","DS201","Artificial Intelligence",3,"KEEP",3,""),
("VI","NEW-B","Distributed Systems and System Design",0,"ADD",3,"Prereqs: CS302, CS306, CS206"),
("VII","SEM7-1","Deep Learning",4,"KEEP",4,"Code not available"),
("VII","SEM7-2","Natural Language Processing",3,"KEEP",3,"Tescra: LLM/NER"),
("VII","SEM7-3","Ethical Hacking",3,"KEEP",3,""),
("VII","SEM7-4","Introduction to Entrepreneurship",3,"KEEP",3,""),
("VII","SEM7-5","Human Computer Interaction",3,"KEEP",3,""),
("VII","NEW-C","DevOps, CI/CD and Testing Practice",0,"ADD",2,"Prereqs: CS304, CS307"),
("VIII","SEM8","Internship",15,"KEEP",15,"Code not available"),
]

cur = sum(c[3] for c in C)
new = sum(c[5] for c in C)
add = sum(c[5] for c in C if c[4] == "ADD")
rem = sum(c[3] - c[5] for c in C if c[4] == "REDUCE")
upd = sum(c[3] for c in C if c[4] == "UPDATE")
keep = sum(c[3] for c in C if c[4] == "KEEP")
print("current", cur, "proposed", new, "add", add, "removed", rem, "update", upd, "keep", keep)

aff = add + rem + upd
print("affected", aff, round(100 * aff / cur, 2))

order = ["I", "II", "III", "IV", "ST", "V", "VI", "VII", "VIII"]
sem = {}
for s in order:
    sem[s] = (sum(c[3] for c in C if c[0] == s), sum(c[5] for c in C if c[0] == s))
print(sem)

assert cur == 167 and new == 167 and add == rem == 8 and aff == 38

# Output paths: relative to this script's folder (works on Windows)
out_dir = Path(__file__).resolve().parent
build_dir = out_dir / "build"
build_dir.mkdir(exist_ok=True)

with open(out_dir / "course_map.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["semester", "code", "title", "current_credits", "status", "proposed_credits", "note"])
    for c in C:
        w.writerow(c)

with open(build_dir / "c.json", "w", encoding="utf-8") as f:
    json.dump(C, f, indent=2)

print("Wrote:", out_dir / "course_map.csv")
print("Wrote:", build_dir / "c.json")