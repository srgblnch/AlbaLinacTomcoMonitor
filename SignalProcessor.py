#!/usr/bin/env python

##############################################################################
## license : GPLv3+
##============================================================================
##
## File :        SignalProcessor.py
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
    Given a signal proceed with the calculations the user have requested.
"""

import numpy as np
from taurus import Logger


class Signal(Logger):
    """
        This class can receive as input an array. It divides this input in 
        N subsignals and over each of them takes a subsampling (starting in the
        offset with the given length).
        With this provide statistical data (mean and std) on each of these 
        subsamplings, then finally calculate an upper level statistics over
        the intermediate ones.
    """
    def __init__(self,name,nsubsignals=3,offset=25,length=1,
                 logLevel=Logger.Info):
        self._name = name
        Logger.__init__(self,self._name)
        self.setLogLevel(logLevel)
        self._nsubsignals = nsubsignals
        self._offset = offset
        self._length = length
        self._array = None
        self._means = \
        np.array([float("NaN")]*self.nsubsignals,dtype=np.float64)
        self._stds = \
        np.array([float("NaN")]*self.nsubsignals,dtype=np.float64)
        self._composedMean = float("NaN")
        self._composedStd = float("NaN")

    @property
    def nsubsignals(self):
        """
            The received array to process is divided in a number of subsignals.
        """
        return self._nsubsignals

    @nsubsignals.setter
    def nsubsignals(self,value):
        self._nsubsignals = value

    @property
    def offset(self):
        """
            Form each of the subsignals, use the offset to define the first 
            element to study.
            Then use length to define how many will be used in this first part.
        """
        return self._offset

    @offset.setter
    def offset(self,value):
        self._offset = value

    @property
    def length(self):
        """
            Form each of the subsignals, use the offset to define the first 
            element to study.
            Then use length to define how many will be used in this first part.
        """
        return self._length

    @length.setter
    def length(self,value):
        self._length = value

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self,value):
        self._array = value
        self.__process()

    def __process(self):
        """
            - Cut the array in subsignals. 
            - For each of them take a subsample of the 'length' elements after 
              the 'offset' index.
            - Calculate mean & std for each of those subsamples of the 
              subsignals.
        """
        subsignals = self._array.reshape(\
                    [self.nsubsignals,len(self._array)/self.nsubsignals])
        subsamples = np.array([[float("NaN")]*self.length]*self.nsubsignals,
                              dtype=np.float64)
        self._means = \
        np.array([float("NaN")]*self.nsubsignals,dtype=np.float64)
        self._stds = \
        np.array([float("NaN")]*self.nsubsignals,dtype=np.float64)
        for i,signal in enumerate(subsignals):
            subsamples[i] = signal[self.offset:self.offset+self.length]
            self._means[i] = subsamples[i].mean()
            self._stds[i] = subsamples[i].std()
            self.info("subsignal %d: %s (%g,%g)"
                      %(i,subsamples[i],self._means[i],self._stds[i]))
        self.info("means %s (stds %s)"
                   %(self.subsignalMeans,self.subsignalStds))
        self._composedMean = self._means.mean()
        self._composedStd = self._means.std()
        self.info("composed mean %g (std %g)"
                   %(self._composedMean,self._composedStd))

    @property
    def subsignalMeans(self):
        return self._means

    @property
    def subsignalStds(self):
        return self._stds

    @property
    def composedMean(self):
        return self._composedMean

    @property
    def composedStd(self):
        return self._composedStd

#---- #Testing area

def getOptions():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('',"--log-level",default="info",
                      help="Define the logging level to print out. Allowed "\
                      "values error|warning|info|debug, being info the "\
                      "default")
    (options, args) = parser.parse_args()
    logLevel = {'error':Logger.Error,
                'warning':Logger.Warning,
                'info':Logger.Info,
                'debug':Logger.Debug
               }[options.log_level.lower()]
    options.log_level = logLevel
    return options


def test(log_level):
    from SignalSample import s1
    s = Signal("sample1",logLevel=log_level)
    #try with lenght 1
    s.array = s1
    #try with lenght 3
    s.offset = 24
    s.length = 3
    s.array = s1
    #try with lenght 5
    s.offset = 23
    s.length = 5
    s.array = s1


def main():
    options = getOptions()
    test(options.log_level)


if __name__ == "__main__":
    import sys
    main()
