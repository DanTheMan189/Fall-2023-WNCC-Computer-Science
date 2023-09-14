import time
import sys
import psutil

from rich.console import Console

from rich.panel import Panel

console = Console()

console.print(
    Panel.fit(
        " ---- Python Network IO Monitor ---- ",
        style="bold blue")
)

while True:
    try:
        net_io = psutil.net_io_counters()

        sent_1 = net_io.bytes_sent
        recv_1 = net_io.bytes_recv

        time.sleep(1)

        net_io = psutil.net_io_counters()

        sent_2 = net_io.bytes_sent
        recv_2 = net_io.bytes_recv

        sent = sent_2 - sent_1
        recv = recv_2 - recv_1

        sent = sent / 125000
        recv = recv / 125000

        console.print (
            f" Sent: {sent:,.1f} Kbps - Recv: {recv:,.1f} Kpbs "            , end="\r") 
    
    except KeyboardInterrupt:
        sys.exit(0)