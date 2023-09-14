import psutil

net_io = psutil.net_io_counters()

sent = net_io.bytes_sent

recv = net_io.bytes_recv

print (f"Sent: {sent:,.1f} Bytes")
print (f"Recv: {recv:,.1f} Bytes")