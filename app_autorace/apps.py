# -*- coding: utf-8 -*-
from django.apps import AppConfig
from logging import getLogger
import os
import subprocess

logger = getLogger('command')

class AppAutoraceConfig(AppConfig):
    name = 'app_autorace'

    run_already = False 

    def call_shell(self):
        path = os.getcwd()
        logger.info(path)
        cmd = 'mkdir test'
        logger.info(cmd)
        res = subprocess.call(cmd, shell=True)
        logger.info(res)

    # docker-compose up -d docker-compose stop 呼ばれる？
    def ready(self):
        logger.info('command Start:')

        if AppAutoraceConfig.run_already: 
            return 
        AppAutoraceConfig.run_already = True 
        # self.call_shell()
        logger.info('command End:')
