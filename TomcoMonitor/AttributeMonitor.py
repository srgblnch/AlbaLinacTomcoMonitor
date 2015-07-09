#!/usr/bin/env python

##############################################################################
## license : GPLv3+
##============================================================================
##
## File :        AttributeMonitor.py
## 
## Project :     TomcoMonitor
##
## This file is part of Tango device class.
## 
## Tango is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Tango is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Tango.  If not, see <http://www.gnu.org/licenses/>.
## 
##
## $Author :      sblanch$
## Copyright 2013 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## $Revision :    $
##
## $Date :        $
##
## $HeadUrl :     $
##############################################################################

"""
    Given an attribute, monitor it to process its value when needed to provide
    output information to the upper layer.
"""

from SignalProcessor import Signal
import PyTango
from taurus import Logger


class AttributeMonitor(Logger):
    """
    """
    #TODO: collect in a cyclic buffer the signal mean outputs to allow the 
    #      user to have more than the part 3 subsignal mean
    def __init__(self,devName,attrName,groupName=None,callback=None,
                 logLevel=Logger.Info):
        self._name = "%s/%s"%(devName,attrName)
        Logger.__init__(self,self._name)
        self.setLogLevel(logLevel)
        self._devName = devName
        self._devProxy = None
        self.buildProxy()
        self._attrName = attrName
        self._eventID = None
        self.debug("build Monitor")
        self._signal = Signal(self._name)
        self._signalCT = self._signal.nsubsignals
        self.groupName = groupName
        self._callback = callback
        self.subscribe()

    def __del__(self):
        self.unsubscribe()

    @property
    def name(self):
        return self._name

    @property
    def devName(self):
        return self._devName

    @property
    def attrName(self):
        return self._attrName

    def buildProxy(self):
        try:
            self._devProxy = PyTango.DeviceProxy(self._devName)
            #TODO: has to change subscription
        except Exception,e:
            self.error("Cannot build a device proxy with the name %s: %s"
                       %(self._devName,e))

    def read(self):
        self._signal.array = self._devProxy[self._attrName].value
        self.info("Subsignal means %s, composed mean %s"
                  %(self._signal.subsignalMeans,self._signal.composedMean))

    def subscribe(self):
        eventType = PyTango.EventType.CHANGE_EVENT
        self._eventID = self._devProxy.subscribe_event(\
                        self._attrName,eventType,self)
        self.info("Subscribed to %s with id %d (type %s)"
                  %(self._attrName,self._eventID,eventType))

    def unsubscribe(self):
        self._attr.unsubscribe_event(self._eventID)

    def push_event(self,event):
        try:
            if event != None:
                if event.attr_value != None and event.attr_value.value != None:
                    self._signalCT = \
                    (self._signalCT + 1)%self._signal.nsubsignals
                    if self._signalCT != 0:
                        self.debug("Discarting until all subsignals has "\
                                   "changed")
                        return
                    self.debug("%s::PushEvent() %s: %s"
                               %(self._name,event.attr_name,
                                 event.attr_value.value))
                    self._signal.array = event.attr_value.value
                    self.debug("Subsignal means %s, composed mean %s"
                               %(self._signal.subsignalMeans,
                                 self._signal.composedMean))
                    #TODO: push to the cyclic buffer
                    self._callback(self)
                else:
                    self.warn("%s::PushEvent() %s: value has None type"
                               %(self._name,event.attr_name))
        except Exception,e:
            self.error("%s::PushEvent() exception %s:"%(self._name,e))

    @property
    def subsignals(self):
        return self._signal.subsignalMeans
    
    @property
    def composed(self):
        return self._signal.composedMean

#---- #Testing area

def getOptions():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('',"--log-level",default="info",
                      help="Define the logging level to print out. Allowed "\
                      "values error|warning|info|debug, being info the "\
                      "default")
    parser.add_option('',"--device",default=None,
                      help="Name of the device with the signal")
    parser.add_option('',"--attribute",default=None,
                      help="Name of the attribute signal")
    (options, args) = parser.parse_args()
    logLevel = {'error':Logger.Error,
                'warning':Logger.Warning,
                'info':Logger.Info,
                'debug':Logger.Debug
               }[options.log_level.lower()]
    options.log_level = logLevel
    return options


def main():
    options = getOptions()
    atm = AttributeMonitor(options.device,options.attribute,options.log_level)
    import time
    i = 0
    while i < 10:
        t0 = time.time()
        #atm.read()
        time.sleep(1-(time.time()-t0))
        i+=1


if __name__ == "__main__":
    import sys
    main()
