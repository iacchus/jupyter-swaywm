#!/usr/bin/env python

import os

import i3ipc

SWAYSOCK = os.environ['SWAYSOCK']

sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()
#  focused = sway.get_tree().find_focused()
focused = root.find_focused()
windows = root.descendants()

window_id_list = [window.id for window in windows
                  if window.type in ("con", "floating_con")]

print(windows)

print(window_id_list)

#  print(focused)
print("FOCUSED:", focused.ipc_data, end="\n\n")

for window in windows:
    if window.type in ("con", "floating_con"):
        print("WINDOW:", window.ipc_data, end="\n\n")

sway.main()
