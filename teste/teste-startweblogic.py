import os
def startweblogic():
    DOMAIN_HOME = os.environ.get('DOMAIN_HOME')
    STARTWEBLOGIC='nohup '+ DOMAIN_HOME +'/bin/startWebLogic.sh &'
    print(STARTWEBLOGIC)
    #os.system(STARTWEBLOGIC)

startweblogic()