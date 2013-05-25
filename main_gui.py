#!/usr/bin/env python

import asr, guiboard
from multiprocessing import Process, Queue
import gobject


class ResultListener(asr.Listener):
    def handle(self, params):
        print "Comando: %s"  % params["text"]
        q.put(params["text"])



if __name__ == "__main__":
    recognizer = asr.Recognizer()
    board = guiboard.GuiBoard()
    q = Queue()

    recognizer.add_result_listener(ResultListener())
    
    p = Process(target=board.draw, args=(q,))
    p.start()
    
    gobject.threads_init()
    gobject.MainLoop().run()
