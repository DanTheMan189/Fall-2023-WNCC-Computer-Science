import psutil
import time

while True:
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

    print (f"Sent: {sent:,.2f} Mbps - Recv: {recv:,.2f} Mpbs")