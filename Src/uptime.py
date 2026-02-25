def get_uptime():
    with open("/proc/uptime") as page:
        seconds = float(page.readline().split()[0])

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)

    return hours, minutes
