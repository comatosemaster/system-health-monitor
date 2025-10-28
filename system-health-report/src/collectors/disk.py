import psutil
from humanfriendly import format_size

def get_disk_info():
    """
    Collects total, used, and free disk space for all drives.
    Returns a list of dictionaries (one per partition).
    """

    # access to all partitions in the device
    partitions = psutil.disk_partitions(all=False)
    disks = []

    # go through all partitions and collect total, used, free and percentage of the disk usage, append dict into disks list
    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue

        disks.append(
            {
                "device": part.device,
                "mountpoint": part.mountpoint,
                "total": format_size(usage.total),
                "used": format_size(usage.used),
                "free": format_size(usage.free),
                "percent": usage.percent
            }
        )
    # return list of dicts containing detailed info regarding each partition
    return disks
