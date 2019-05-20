############################################################################################
#
# Project:       Peter Moss Acute Myeloid/Lymphoblastic Leukemia AI Research Project
# Repository:    AML/ALL Detection System
# Project:       AML/ALL Detection System
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Data Augmentation Helper Class
# Description:   Helper functions for the AML/ALL Detection System Augmentation Class.
# License:       MIT License
# Last Modified: 2019-05-09
#
############################################################################################

import json
import time

from datetime import datetime


class Helpers():
    """ AML/ALL Detection System Movidius NCS1 Classifier Helper Class

    Common helper functions for the AML/ALL Detection System Movidius NCS1 Classifier. 
    """

    def __init__(self):
        """ Initializes the AML/ALL Detection System Helper Class. """

        pass

    def loadConfs(self):
        """ Loads the AML/ALL Detection System configuration. """

        confs = {}
        with open('Required/confs.json') as confs:
            confs = json.loads(confs.read())
        return confs

    def currentDateTime(self):
        """ Gets the current date and time in words. """

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def timerStart(self):
        """ Starts the timer. """

        return str(datetime.now()), time.time()

    def timerEnd(self, start):
        """ Ends the timer. """

        return time.time(), (time.time() - start), str(datetime.now())

    def setLogFile(self, path):
        """ Ends a log file path. """

        return path + datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S') + ".txt"

    def logMessage(self, logfile, process, messageType, message, hide=False):
        """ Logs a message to a log file. """

        logString = datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d %H:%M:%S') + "|" + process + "|" + messageType + ": " + message
        with open(logfile, "a") as logLine:
            logLine.write(logString+'\r\n')
        if hide == False:
            print(logString)
