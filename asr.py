#!/usr/bin/env python

import os

import gobject
import pygst
pygst.require('0.10')
gobject.threads_init()
import gst


__all__ = [ "Recognizer" ]


MODEL_HOME = os.path.join(os.getcwd(), "adapted-model")

class Recognizer(object):
    """Recognizer class"""
    def __init__(self):
        """Initialize a  object"""
        self.init_gst()

    def init_gst(self):
        """Initialize the speech components"""
        self.pipeline = gst.parse_launch('gconfaudiosrc ! audioconvert ! audioresample '
                                         + '! vader name=vad auto-threshold=true '
                                         + '! pocketsphinx name=asr')
                                         #+ '! pocketsphinx name=asr ! fakesink')
        asr = self.pipeline.get_by_name('asr')
        
        asr.set_property('hmm', os.path.join(MODEL_HOME, "default-model", "adapted")) 
        asr.set_property('lm', os.path.join(MODEL_HOME, "lm", "step-14.lm.DMP"))
        asr.set_property('dict', os.path.join(MODEL_HOME, "step-14.dic")) 
        asr.set_property('configured', True)
        
        asr.connect('partial_result', self.asr_partial_result)
        asr.connect('result', self.asr_result)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message::application', self.application_message)

        #self.pipeline.set_state(gst.STATE_PAUSED)
        self.pipeline.set_state(gst.STATE_PLAYING)

    def asr_partial_result(self, asr, text, uttid):
        """Forward partial result signals on the bus to the main thread."""
        struct = gst.Structure('partial_result')
        struct.set_value('hyp', text)
        struct.set_value('uttid', uttid)
        asr.post_message(gst.message_new_application(asr, struct))

    def asr_result(self, asr, text, uttid):
        """Forward result signals on the bus to the main thread."""
        struct = gst.Structure('result')
        struct.set_value('hyp', text)
        struct.set_value('uttid', uttid)
        asr.post_message(gst.message_new_application(asr, struct))

    def application_message(self, bus, msg):
        """Receive application messages from the bus."""
        msgtype = msg.structure.get_name()
        if msgtype == 'partial_result':
            self.partial_result(msg.structure['hyp'], msg.structure['uttid'])
        elif msgtype == 'result':
            self.final_result(msg.structure['hyp'], msg.structure['uttid'])
            self.pipeline.set_state(gst.STATE_PAUSED)
            #self.button.set_active(False)

    def partial_result(self, hyp, uttid):
        """Delete any previous selection, insert text and select it."""
        # All this stuff appears as one single action
        pass

    def final_result(self, hyp, uttid):
        """Insert the final result."""
        # All this stuff appears as one single action
        print hyp

    #def button_clicked(self, button):
        #"""Handle button presses."""
        #if button.get_active():
            #button.set_label("Stop")
            #self.pipeline.set_state(gst.STATE_PLAYING)
        #else:
            #button.set_label("Speak")
            #vader = self.pipeline.get_by_name('vad')
            #vader.set_property('silent', True)