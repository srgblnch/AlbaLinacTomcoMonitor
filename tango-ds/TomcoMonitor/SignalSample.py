#!/usr/bin/env python

##############################################################################
## license : GPLv3+
##============================================================================
##
## File :        SignalSample.py
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
    This file is made for unit test purposes.
"""

import numpy as np

s1 = \
np.array([ -6.10351562e-04,   8.54492188e-03,   7.20214844e-02,
            1.02355957e+00,   1.54724121e+00,   1.74957275e+00,
            1.82159424e+00,   1.84600830e+00,   1.85333252e+00,
            1.85455322e+00,   1.85394287e+00,   1.85302734e+00,
            1.85211182e+00,   1.85058594e+00,   1.84967041e+00,
            1.85119629e+00,   1.85058594e+00,   1.84906006e+00,
            1.85058594e+00,   1.84631348e+00,   1.85211182e+00,
            1.85180664e+00,   1.85089111e+00,   1.85058594e+00,
            1.85058594e+00,   1.85089111e+00,   1.85180664e+00,
            1.85180664e+00,   1.85302734e+00,   1.84997559e+00,
            1.84448242e+00,   1.74011230e+00,   1.13403320e+00,
            4.98657227e-01,   2.00805664e-01,   7.99560547e-02,
            3.20434570e-02,   1.15966797e-02,   1.83105469e-03,
            1.83105469e-03,   1.83105469e-03,   1.83105469e-03,
            1.22070312e-03,   0.00000000e+00,   6.10351562e-04,
            9.15527344e-04,   1.22070312e-03,  -3.05175781e-04,
           -9.15527344e-04,   0.00000000e+00,   9.15527344e-04,
            7.62939453e-03,   7.17163086e-02,   1.02355957e+00,
            1.54968262e+00,   1.75231934e+00,   1.82495117e+00,
            1.84875488e+00,   1.85729980e+00,   1.85821533e+00,
            1.85668945e+00,   1.85607910e+00,   1.85394287e+00,
            1.85516357e+00,   1.85211182e+00,   1.85455322e+00,
            1.85241699e+00,   1.85241699e+00,   1.85180664e+00,
            1.85363770e+00,   1.85424805e+00,   1.85241699e+00,
            1.85455322e+00,   1.85150146e+00,   1.85302734e+00,
            1.85333252e+00,   1.85241699e+00,   1.85241699e+00,
            1.85455322e+00,   1.85241699e+00,   1.84631348e+00,
            1.73950195e+00,   1.13525391e+00,   4.98352051e-01,
            2.00500488e-01,   7.84301758e-02,   3.14331055e-02,
            1.09863281e-02,   5.18798828e-03,   1.83105469e-03,
            9.15527344e-04,   2.44140625e-03,   0.00000000e+00,
            0.00000000e+00,   0.00000000e+00,   3.05175781e-04,
            3.05175781e-04,   1.22070312e-03,   3.05175781e-04,
            3.05175781e-04,   6.10351562e-04,   7.93457031e-03,
            6.50024414e-02,   1.01806641e+00,   1.54907227e+00,
            1.75384521e+00,   1.82861328e+00,   1.85180664e+00,
            1.85943604e+00,   1.86035156e+00,   1.85791016e+00,
            1.85668945e+00,   1.85546875e+00,   1.85791016e+00,
            1.85546875e+00,   1.85363770e+00,   1.85455322e+00,
            1.85333252e+00,   1.85394287e+00,   1.85363770e+00,
            1.85363770e+00,   1.85241699e+00,   1.85333252e+00,
            1.85241699e+00,   1.85333252e+00,   1.85394287e+00,
            1.85241699e+00,   1.85211182e+00,   1.85333252e+00,
            1.85333252e+00,   1.84600830e+00,   1.74377441e+00,
            1.14471436e+00,   5.03540039e-01,   2.02331543e-01,
            8.02612305e-02,   3.17382812e-02,   1.15966797e-02,
            5.79833984e-03,   2.74658203e-03,   0.00000000e+00,
            9.15527344e-04,  -6.10351562e-04,   0.00000000e+00,
            6.10351562e-04,  -3.05175781e-04,   3.05175781e-04,
            9.15527344e-04,  -3.05175781e-04,   3.05175781e-04])
