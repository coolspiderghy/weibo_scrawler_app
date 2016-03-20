#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import config

reload(sys)
sys.setdefaultencoding('utf-8')

import logging
from controller2 import Controller
from unslib import *
if __name__ == '__main__':
    logging.basicConfig(filename='log/weibo.log', filemode='w',
                        format='[%(asctime)s] - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    filepath = config.UID_FILEPATH
    uns = get_uns_uids(filepath)[0]
    Controller.let_us_go(uns)
    def runControl():
        uid_len_beforerun=len_uns(filepath)
        Controller.let_us_go(uns)
        uid_len_afterrun=len_uns(filepath)
        if uid_len_afterrun>uid_len_beforrun:
            runControl()
    #runControl()
            
