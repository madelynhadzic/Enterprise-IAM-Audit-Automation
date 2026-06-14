import csv

def run_user_access_audit():
    print("[-] Launching Cyber Risk & Internal Audit Automation Script...\n")
    
    # 1. Load HR Data into a dictionary and clean spaces
    hr_status = {}
    with open('hr_list.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emp_id = row['employee_id'].strip()
            hr_status[emp_id] = {
                'name': row['name'].strip(),
                'status': row['status'].strip()
            }
            
    # 2. Audit the IT Access list against the HR status
    flagged_exceptions = []
    
    with open('it_access_list.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emp_id = row['employee_id'].strip()
            
            # Check if the person with IT access is marked as "Terminated"
            if emp_id in hr_status and hr_status[emp_id]['status'] == 'Terminated':
                flagged_exceptions.append({
                    'id': emp_id,
                    'name': hr_status[emp_id]['name'],
                    'username': row['username'].strip(),
                    'risk_level': 'CRITICAL' if row['access_level'].strip() == 'Admin' else 'HIGH'
                })

    # 3. Output the Clean Audit Findings Report
    if flagged_exceptions:
        print(f"[!] ALERT: Found {len(flagged_exceptions)} unauthorized active accounts for terminated employees!\n")
        print(f"{'Emp ID':<8} | {'Employee Name':<15} | {'Username':<10} | {'Risk Level':<10}")
        print("-" * 55)
        for bug in flagged_exceptions:
            print(f"{bug['id']:<8} | {bug['name']:<15} | {bug['username']:<10} | {bug['risk_level']:<10}")
            
        # Save exceptions to a separate file for management review
        with open('audit_exceptions_report.csv', mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=['id', 'name', 'username', 'risk_level'])
            writer.writeheader()
            writer.writerows(flagged_exceptions)
        print("\n[+] Audit report automatically saved to 'audit_exceptions_report.csv'.")
    else:
        print("[+] Audit complete. No access compliance exceptions found.")

if __name__ == "__main__":
    run_user_access_audit()
