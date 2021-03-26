import os
import time
import argparse
from termcolor import colored

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def build():
    os.system('pdflatex main')
    os.system('biber main')
    os.system('pdflatex main')

def show():
    os.system('evince main.pdf &')

def clear():
    os.system('rm *.aux *.bbl *.bcf *.blg *.log *.run.xml *.glo *.acn *.ist *.nav *.out *.snm *.toc')

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.latest_build = time.time()

    def on_modified(self, event):
        t = time.time()
        if event.src_path.endswith('.tex') and (t - self.latest_build) > 3:
            delta_t = t - self.latest_build
            text = '{} {} {}'.format(delta_t, event.key, event.src_path)
            print(colored(text, 'green'))
            build()
            self.latest_build = t

def monitor():
    handler = Handler()
    observer = Observer()
    observer.schedule(handler, path='.', recursive=True)
    observer.start()

    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        clear()
        observer.stop()
    observer.join()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--build', action='store_true')
    # parser.add_argument('--clear', action='store_true')
    # parser.add_argument('--show', action='store_true')

    # args = parser.parse_args()

    # if args.build:
    #     build()
    # elif args.clear:
    #     clear()
    # elif args.show:
    #     show()
    # else:
    #     monitor()

    clear()
