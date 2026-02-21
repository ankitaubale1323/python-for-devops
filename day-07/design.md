
# Day 07 – Design Thinking (Log Analyzer CLI Tool)

## 1️ What Problem Am I Solving?

In production systems, logs are large and difficult to analyze manually.

When an issue happens:
- We need to quickly check how many ERROR or WARNING logs occurred.
- We need a summary without manually reading the whole file.

This script helps automate log analysis.

It reduces:
- Manual effort
- Debugging time
- Human mistakes


------------------------------------------------------------------------------------

## 2️ What Input Does My Script Need?

The script needs:

- Log file path (required)
    Example: app.log

Optional inputs:
- Output file path (where summary will be saved)
- Log level filter (INFO / WARNING / ERROR)

User will provide input using CLI arguments:
    --file app.log
    --out summary.txt
    --level ERROR


-------------------------------------------------------------------------

## 3️ What Output Should My Script Give?

Output should be:

1. Terminal Summary:
    Example:
        INFO: 10
        WARNING: 5
        ERROR: 2

OR if filtered:
        ERROR: 2

2. Output File (if --out is given):
    log_summary.txt containing the same summary.


------------------------------------------------------

## 4️ What Are the Main Steps?

Step 1: Parse CLI arguments using argparse  
Step 2: Validate that log file exists  
Step 3: Read log file  
Step 4: Count occurrences of:
        - INFO
        - WARNING
        - ERROR  
Step 5: If level filter is given, show only that level  
Step 6: Print summary to terminal  
Step 7: Write summary to output file (if provided)  


----------------------------------------------------------------

## 5️ What Errors Should Be Handled?

- Log file not found
- Empty log file
- Invalid log level
- Permission issues while writing file


-------------------------------------------------

## 6️ Future Improvements 

- Add threshold alert (example: ERROR > 10 → show warning)
- Generate JSON output
- Send email alert
- Add timestamp filtering
- Convert tool into installable CLI package

```
-------------------------------------------------------------------------

# What You Just Practiced


* Problem decomposition
* Requirement analysis
* Logical breakdown
* Pre-implementation planning

