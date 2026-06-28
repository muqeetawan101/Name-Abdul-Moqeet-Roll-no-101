
import os
import json
from datetime import datetime

DATA_FOLDER = "data"

FILES = {
    "cases": "cases.json",
    "hearings": "hearings.json",
    "firs": "firs.json",
    "orders": "orders.json",
    "users": "users.json",
    "timeline": "timeline.json",
    "audit": "audit.json",
    "notifications": "notifications.json"
}

# ---------------- STORAGE ----------------

def init_storage():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    for f in FILES.values():
        path = os.path.join(DATA_FOLDER, f)
        if not os.path.exists(path):
            with open(path, "w") as file:
                json.dump([], file)

def load_data(name):
    with open(os.path.join(DATA_FOLDER, FILES[name]), "r") as f:
        return json.load(f)

def save_data(name, data):
    with open(os.path.join(DATA_FOLDER, FILES[name]), "w") as f:
        json.dump(data, f, indent=4)

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------------- LOGIN ----------------

def initialize_default_admin():
    users = load_data("users")

    if not any(u.get("username") == "admin" for u in users):
        users.append({
            "username": "admin",
            "password": "admin123",
            "role": "Admin"
        })
        save_data("users", users)

def login():
    username = input("Username: ")
    password = input("Password: ")

    users = load_data("users")

    for u in users:
        if u["username"] == username and u["password"] == password:
            return u

    return None

def create_user():
    users = load_data("users")

    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (Judge/Lawyer/Client): ")

    users.append({
        "username": username,
        "password": password,
        "role": role
    })

    save_data("users", users)
    print("User Created")

def view_users():
    users = load_data("users")

    print("\nUSERS")
    for u in users:
        print(f"{u['username']} | {u['role']}")

def delete_user():
    username = input("Username To Delete: ")

    users = load_data("users")
    users = [u for u in users if u["username"] != username]

    save_data("users", users)
    print("User Deleted")

def reset_password():
    username = input("Username: ")
    new_password = input("New Password: ")

    users = load_data("users")

    for u in users:
        if u["username"] == username:
            u["password"] = new_password

    save_data("users", users)
    print("Password Updated")

# ---------------- AUDIT/TIMELINE ----------------

def add_timeline(case_id, event):
    t = load_data("timeline")
    t.append({
        "case_id": case_id,
        "event": event,
        "date": now()
    })
    save_data("timeline", t)

def add_audit(user, action):
    a = load_data("audit")
    a.append({
        "user": user,
        "action": action,
        "date": now()
    })
    save_data("audit", a)

# ---------------- CASES ----------------

def dashboard():
    print("\n===== DASHBOARD =====")
    print("Cases:", len(load_data("cases")))
    print("Hearings:", len(load_data("hearings")))
    print("Orders:", len(load_data("orders")))
    print("Users:", len(load_data("users")))

def add_case():
    cases = load_data("cases")

    cid = max([c["id"] for c in cases], default=0) + 1

    case = {
        "id": cid,
        "title": input("Title: "),
        "description": input("Description: "),
        "category": input("Category: "),
        "priority": input("Priority: "),
        "status": "Filed",
        "judge": "",
        "lawyer": "",
        "client": input("Client: "),
        "filing_date": now()
    }

    cases.append(case)
    save_data("cases", cases)

    add_timeline(cid, "Case Filed")

    print("Case Added")

def show_cases():
    cases = load_data("cases")

    if not cases:
        print("No Cases Found")
        return

    for c in cases:
        print(f"{c['id']} | {c['title']} | {c['status']} | {c['category']}")

def search_case():
    key = input("Search: ").lower()

    for c in load_data("cases"):
        if key in c["title"].lower():
            print(c)

def assign_judge():
    cid = int(input("Case ID: "))
    judge = input("Judge Name: ")

    cases = load_data("cases")

    for c in cases:
        if c["id"] == cid:
            c["judge"] = judge
            add_timeline(cid, f"Judge Assigned: {judge}")

    save_data("cases", cases)

def assign_lawyer():
    cid = int(input("Case ID: "))
    lawyer = input("Lawyer Name: ")

    cases = load_data("cases")

    for c in cases:
        if c["id"] == cid:
            c["lawyer"] = lawyer
            add_timeline(cid, f"Lawyer Assigned: {lawyer}")

    save_data("cases", cases)

# ---------------- HEARINGS ----------------

def schedule_hearing():
    hearings = load_data("hearings")

    cid = int(input("Case ID: "))

    hearings.append({
        "case_id": cid,
        "date": input("Date: "),
        "time": input("Time: "),
        "courtroom": input("Courtroom: "),
        "remarks": input("Remarks: ")
    })

    save_data("hearings", hearings)
    add_timeline(cid, "Hearing Scheduled")



def issue_order():
    orders = load_data("orders")

    cid = int(input("Case ID: "))

    orders.append({
        "case_id": cid,
        "order": input("Order: "),
        "date": now()
    })

    save_data("orders", orders)
    add_timeline(cid, "Order Issued")



def reports():
    cases = load_data("cases")

    print("\n===== REPORT =====")
    print("Total Cases:", len(cases))

    status = {}

    for c in cases:
        status[c["status"]] = status.get(c["status"], 0) + 1

    print(status)

# ---------------- DETAILS ----------------

def case_details():
    cid = int(input("Case ID: "))

    print("\nCASE INFO")
    for c in load_data("cases"):
        if c["id"] == cid:
            print(c)

    print("\nTIMELINE")
    for t in load_data("timeline"):
        if t["case_id"] == cid:
            print(t)

    print("\nHEARINGS")
    for h in load_data("hearings"):
        if h["case_id"] == cid:
            print(h)

    print("\nORDERS")
    for o in load_data("orders"):
        if o["case_id"] == cid:
            print(o)

# ---------------- PANELS ----------------

def admin_panel():
    while True:
        print("\nADMIN PANEL")
        print("1 Dashboard")
        print("2 Add Case")
        print("3 View Cases")
        print("4 Search Case")
        print("5 Assign Judge")
        print("6 Assign Lawyer")
        print("7 Reports")
        print("8 Create User")
        print("9 View Users")
        print("10 Delete User")
        print("11 Reset Password")
        print("12 Logout")

        ch = input("> ")

        if ch == "1": dashboard()
        elif ch == "2": add_case()
        elif ch == "3": show_cases()
        elif ch == "4": search_case()
        elif ch == "5": assign_judge()
        elif ch == "6": assign_lawyer()
        elif ch == "7": reports()
        elif ch == "8": create_user()
        elif ch == "9": view_users()
        elif ch == "10": delete_user()
        elif ch == "11": reset_password()
        elif ch == "12": break

def judge_panel():
    while True:
        print("\nJUDGE PANEL")
        print("1 View Cases")
        print("2 Schedule Hearing")
        print("3 Issue Order")
        print("4 Case Details")
        print("5 Logout")

        ch = input("> ")

        if ch == "1": show_cases()
        elif ch == "2": schedule_hearing()
        elif ch == "3": issue_order()
        elif ch == "4": case_details()
        elif ch == "5": break

def lawyer_panel():
    while True:
        print("\nLAWYER PANEL")
        print("1 File Case")
        print("2 Search Case")
        print("3 Track Case")
        print("4 Logout")

        ch = input("> ")

        if ch == "1": add_case()
        elif ch == "2": search_case()
        elif ch == "3": case_details()
        elif ch == "4": break

def client_panel():
    while True:
        print("\nCLIENT PANEL")
        print("1 View Cases")
        print("2 Track Case")
        print("3 Logout")

        ch = input("> ")

        if ch == "1": show_cases()
        elif ch == "2": case_details()
        elif ch == "3": break

# ---------------- MAIN ----------------

def main():
    init_storage()
    initialize_default_admin()

    while True:
        print("\nCOURT CASE MANAGEMENT SYSTEM")
        print("1 Login")
        print("2 Exit")

        choice = input("Choice: ")

        if choice == "2":
            break

        user = login()

        if not user:
            print("Invalid Username or Password")
            continue

        role = user["role"]

        if role == "Admin":
            admin_panel()
        elif role == "Judge":
            judge_panel()
        elif role == "Lawyer":
            lawyer_panel()
        elif role == "Client":
            client_panel()

if __name__ == "__main__":
    main()
