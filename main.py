#!/usr/bin/env python

import gobject

import asr, board

class ResultListener(asr.Listener):
    def handle(self, params):
        print "Comando: %s"  % params["text"]
        board.move(params["text"])
        board.draw()



if __name__ == "__main__":
    recognizer = asr.Recognizer()
    board = board.Board()
    
    recognizer.add_result_listener(ResultListener())
    
    board.draw()
    
    gobject.threads_init()
    gobject.MainLoop().run()
