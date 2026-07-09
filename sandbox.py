import jupyter_client
import queue 

km = jupyter_client.KernelManager()
km.start_kernel()

kc = km.client()
kc.start_channels()

kc.execute("print('hi')")
