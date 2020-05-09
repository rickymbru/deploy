import os

def startweblogic():
    DOMAIN_HOME = os.environ.get('DOMAIN_HOME')
    STARTWEBLOGIC='nohup '+ DOMAIN_HOME +'/bin/startWebLogic.sh > /dev/null 2>&1 &'
    os.system(STARTWEBLOGIC)

startweblogic()