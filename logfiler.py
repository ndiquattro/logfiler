# Logfile maker
import os
import csv
import time

class logger(object):
    ''' Helper class for creating and writing to a logfile '''
    
    def __init__(self, subname, suffix, folder = 'data'):
        ''' Opens logfile, creating a data folder if need be. 
        
        Parameters
            subname -- Subject ID
            suffix  -- Tag placed at the end of the file. Typically experiment
                       name.
            folder  -- Name of folder to save data in. Will be created if it
                       doesn't exist. Defaults to 'data'.
        '''
        # Add datafolder if not found
        if not os.path.isdir(folder):
            os.mkdir(folder)
            
        # Get timestamp
        ts = int(time.time())
        
        # Make and open file name
        fname = '{}_{}_{}.csv'.format(subname, ts, suffix)
        self.file = open(os.path.join(folder, fname), 'wb')
        
        # Create writter
        self.log = csv.writer(self.file)
        
        # Tell write() to write headers
        self.hwrite = True
        
    def write(self, tdict):
        ''' Adds a row of data to logfile.
        
        Parameters
            tdict -- A python dictionary object. Keys are headers, values are
                     data.
        '''
        
        # Write header if need be
        if self.hwrite:
            self.log.writerow(tdict.keys())
            self.hwrite = False
            
        # Write trial data
        self.log.writerow(tdict.values())
        
    def close(self):
        ''' Closes logfile. '''
        
        # Close logfile
        self.file.close()