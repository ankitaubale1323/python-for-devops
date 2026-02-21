LOG_FILE = "app.log"
OUTPUT_FILE = "log_summary.txt"


def read_log_file(filename):
    """Read log file and return lines."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines:
            print("⚠️ Log file is empty.")
            return None

        return lines

    except FileNotFoundError:
        print("❌ Log file not found.")
        return None

    except Exception as error:
        print(f"❌ Unexpected error: {error}")
        return None


def analyze_logs(lines):
    """Count INFO, WARNING, ERROR messages."""
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        for level in log_counts:
            if level in line:
                log_counts[level] += 1

    return log_counts


def write_summary(summary, filename):
    """Write log summary to output file."""
    try:
        with open(filename, "w") as file:
            file.write("Log Analysis Summary\n")
            file.write("---------------------\n")
            for level, count in summary.items():
                file.write(f"{level}: {count}\n")

        print(f"✅ Summary written to {filename}")

    except Exception as error:
        print(f"❌ Failed to write summary: {error}")


def main():
    print("Reading log file...\n")

    lines = read_log_file(LOG_FILE)

    if not lines:
        print("⚠️ Exiting due to log file issue.")
        return

    summary = analyze_logs(lines)

    print("📊 Log Summary:")
    for level, count in summary.items():
        print(f"{level}: {count}")

    write_summary(summary, OUTPUT_FILE)


if __name__ == "__main__":
    main()