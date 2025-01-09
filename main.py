"""
Gstreamer is a C library, so we use binding to use it in python

PyGObject is a Python package which provides bindings for GObject based 
libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more. Here it is --->>> import gi
"""
import gi
import time

from threading import Thread
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib

Gst.init()

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()
"""
ksvideosrc is input stream form the laptop web camera, it is next gets decoded to binary by decodebin and 
"""
pipeline = Gst.parse_launch("ksvideosrc ! decodebin ! videoconvert ! edgetv ! videoconvert ! autovideosink")

pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()