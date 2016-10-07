#!/usr/bin/python
import os, time, glob, subprocess

files = glob.glob('*.png')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
        w = subprocess.Popen(['convert', f,
            os.path.splitext(f)[0]+'.jpg'])
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
