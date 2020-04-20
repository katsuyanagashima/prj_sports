# -*- coding: utf-8 -*-

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import time
import shutil

temp_dir = "C:/pg/Python38-32/prj_sports/receive_autorace_temp"
save_dir = "C:/pg/Python38-32/prj_sports/receive_autorace"


class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sができました' % filename)
        shutil.move(filename, filepath)

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを変更しました' % filename)

    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを削除しました' % filename)


if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, temp_dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()