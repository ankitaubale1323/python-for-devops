import psutil


def get_thresholds():
    print("Enter threshold values (in percentage):")
    cpu_threshold = float(input("CPU threshold (%): "))
    memory_threshold = float(input("Memory threshold (%): "))
    disk_threshold = float(input("Disk threshold (%): "))
    
    return cpu_threshold, memory_threshold, disk_threshold


def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    return cpu_usage, memory_usage, disk_usage


def check_health(cpu, memory, disk, cpu_t, memory_t, disk_t):
    print("\n--- System Health Report ---")
    
    if cpu > cpu_t:
        print(f"⚠️ CPU usage is HIGH: {cpu}%")
    else:
        print(f"✅ CPU usage is Normal: {cpu}%")
        
    if memory > memory_t:
        print(f"⚠️ Memory usage is HIGH: {memory}%")
    else:
        print(f"✅ Memory usage is Normal: {memory}%")
        
    if disk > disk_t:
        print(f"⚠️ Disk usage is HIGH: {disk}%")
    else:
        print(f"✅ Disk usage is Normal: {disk}%")


def main():
    cpu_t, memory_t, disk_t = get_thresholds()
    cpu, memory, disk = get_system_metrics()
    check_health(cpu, memory, disk, cpu_t, memory_t, disk_t)


if __name__ == "__main__":
    main()