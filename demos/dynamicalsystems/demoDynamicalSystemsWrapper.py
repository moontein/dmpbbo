# This file is part of DmpBbo, a set of libraries and programs for the 
# black-box optimization of dynamical movement primitives.
# Copyright (C) 2014 Freek Stulp, ENSTA-ParisTech
# 
# DmpBbo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# DmpBbo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with DmpBbo.  If not, see <http://www.gnu.org/licenses/>.


## \file demoDynamicalSystems.py
## \author Freek Stulp
## \brief  Visualizes results of demoDynamicalSystems.cpp
## 
## \ingroup Demos
## \ingroup DynamicalSystems

import matplotlib.pyplot as plt
import numpy
import os, sys

# dmpbbo/demos/dynamicalsystems => ../../python/
# dmpbbo/build_dir_debug/demos/dynamicalsystems => ../../../python
# dmpbbo/bin => ../python

for lib_path in ['../python/','../../python/','../../../python/']:
    sys.path.append(lib_path)

from executeBinary import executeBinary
from executeBinary import executeBinaryWithDirectory

from dynamicalsystems.dynamicalsystems_plotting import * 



if __name__=='__main__':
    
    # See if input directory was passed
    if (len(sys.argv)<2 or len(sys.argv)>3):
        print('\nUsage: '+sys.argv[0]+' <test1> [test2]\n')
        print('Available test labels are:')
        print('   rungekutta - Use 4th-order Runge-Kutta numerical integration.')
        print('   euler      - Use simple Euler numerical integration.')
        print('   analytical - Compute analytical solution (rather than numerical integration)')
        print('   tau        - Change the time constant "tau"')
        print('   attractor  - Change the attractor state during the integration')
        print('   perturb    - Perturb the system during the integration')
        print('')
        print('If you call with two tests, the results of the two are compared in one plot.\n')
        sys.exit()
        
    demo_labels = [];
    for arg in sys.argv[1:]:
      demo_labels.append(str(arg))
        
    
    # Call the executable with the directory to which results should be written
    directory = "/tmp/demoDynamicalSystems"
    arguments = directory
    for demo_label in demo_labels:
      arguments += " "+demo_label
     
    print("____________________________________________________________________")
    executeBinaryWithDirectory("../../bin/","demoDynamicalSystems", arguments, True)
    
    figure_number = 1;
    directories = os.listdir(directory) 
    for subdirectory in  directories:
        fig = plt.figure(figure_number)
        figure_number = figure_number+1

        data = numpy.loadtxt(directory+"/"+subdirectory+"/results_"+demo_labels[0]+".txt")
        if (len(demo_labels)==1):
          plotDynamicalSystem(data,[fig.add_subplot(1,2,1), fig.add_subplot(1,2,2)])
          fig.canvas.set_window_title(subdirectory+"  ("+demo_labels[0]+")") 
        else:
          data_compare = numpy.loadtxt(directory+"/"+subdirectory+"/results_"+demo_labels[1]+".txt")
          axs      =  [fig.add_subplot(2,2,1), fig.add_subplot(2,2,2)]
          axs_diff =  [fig.add_subplot(2,2,3), fig.add_subplot(2,2,4)]
          # Bit of a hack... We happen to know that SpringDamperSystem is only second order system
          if (subdirectory == "SpringDamperSystem"):
              axs      =  [fig.add_subplot(2,3,1), fig.add_subplot(2,3,2), fig.add_subplot(2,3,3)]
              axs_diff =  [fig.add_subplot(2,3,4), fig.add_subplot(2,3,5), fig.add_subplot(2,3,6)]
          plotDynamicalSystemComparison(data,data_compare,demo_labels[0],demo_labels[1],axs,axs_diff)
          fig.canvas.set_window_title(subdirectory+"  ("+demo_labels[0]+" vs "+demo_labels[1]+")") 
          axs[1].legend()
          
          
        
    plt.show()

