# gives access to live system stats (CPU, RAM, disk, etc.)
import psutil
# turns numbers like 4281794560 → 4.28 GB
from humanfriendly import format_size

def get_cpu_mem_info():
    """
    Collects current CPU and memory usage.
    Returns a dictionary with readable values.
    """

    # waits 1 second, measures CPU load, returns something like 17.3
    cpu_percent = psutil.cpu_percent(interval=1)

    # returns a small object with memory stats (total, used, free, etc.)
    mem = psutil.virtual_memory()

    # .total and .used are numbers in bytes, that’s why we pass them into format_size
    total_ram = format_size(mem.total)
    used_ram = format_size(mem.used)
    percent_ram = mem.percent

    # The function returns a dictionary (a box of key:value pairs) with 4 values:
    return {
        "cpu_percent": cpu_percent,
        "ram_total": total_ram,
        "ram_used": used_ram,
        "ram_percent": percent_ram
    }

