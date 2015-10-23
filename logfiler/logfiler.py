# Logfile Maker
import os
import csv
import time


class Logger(object):
    """
    Open logfile and create data folder if needed.

    :param subname: Subject identifier.
    :type subname: str
    :param suffix: Experiment identifier.
    :type suffix: str
    :param folder: Path to folder to write logfiles. Creates folder if it
                   doesn't exist
    :type folder: str
    """
    
    def __init__(self, subname, suffix, folder='data'):

        # Create datafolder if not found
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
        """
        Writes a row of data to the logfile.

        :param tdict: Dictionary containing information about a trial.
        :type tdict: dict
        """

        # Write header if need be
        if self.hwrite:
            self.log.writerow(tdict.keys())
            self.hwrite = False
            
        # Write trial data
        self.log.writerow(tdict.values())
        
    def close(self):
        """
        Closes the logfile.
        """

        # Close logfile
        self.file.close()
