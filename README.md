# Enterprise-IAM-Audit-Automation
A Python-based automation script for Identity and Access Management (IAM) cyber risk compliance auditing.
# Enterprise Cyber Risk & IAM Controls Automation

## Project Overview
This technical risk automation tool simulates an Identity and Access Management (IAM) internal audit control used within regulated financial services institutions. Developed using **Python**, the script enforces the security principle of *least privilege* by cross-examining enterprise HR status records against active IT application access logs to detect and mitigate critical "ghost account" vulnerabilities.

## Cyber Risk Addressed
When employees are terminated, manual de-provisioning workflows occasionally fail, leaving active credentials exposed. This script automates continuous compliance monitoring by programmatically flagging active system accounts belonging to terminated personnel, prioritizing exceptions by administrative access privileges.

## How It Works
1. **Data Ingestion**: Parses separate data pipelines (`hr_list.csv` and `it_access_list.csv`) utilizing clean data-stripping logic to eliminate formatting anomalies.
2. **Exception Analysis**: Cross-references employee unique identifiers to verify organizational status.
3. **Risk Scoring**: Implements conditional logic to automatically assign `CRITICAL` risk tiers to unauthorized administrator profiles and `HIGH` risk tiers to standard user profiles.
4. **Automated Reporting**: Outputs a formatted terminal dashboard and saves compliance findings to a tracking file (`audit_exceptions_report.csv`) for executive management remediation.
