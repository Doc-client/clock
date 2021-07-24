from core.new import plugin

clockplugin = plugin.plugin("clock")


@clockplugin.command("c")
def clock(event):
    """live time clock"""
    import time, datetime
    try:
        while True:
            event.print("\r" + str(datetime.datetime.now().strftime("%H:%M:%S")), end="")
            time.sleep(1)

    except:
        event.print("", end="\n")
