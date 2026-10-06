import platform
import psutil

def get_laptop_info():
    # Sistem operasi
    os_name = platform.system()
    os_version = platform.version()

    # CPU
    cpu = platform.processor()

    # RAM
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024 ** 3), 2)
    ram_used = round(ram.used / (1024 ** 3), 2)

    # Storage
    disk = psutil.disk_usage("/")
    disk_total = round(disk.total / (1024 ** 3), 2)
    disk_used = round(disk.used / (1024 ** 3), 2)

    return {
        "os": f"{os_name} {os_version}",
        "cpu": cpu,
        "ram_total": f"{ram_total} GB",
        "ram_used": f"{ram_used} GB",
        "storage_total": f"{disk_total} GB",
        "storage_used": f"{disk_used} GB"
    }


