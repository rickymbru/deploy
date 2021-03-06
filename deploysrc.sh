#!/bin/sh
#Variaveis
APP=src
export DOMAIN_HOME=/u01/domains/cedae
SCRIPT=$(readlink -f "$0")
BASEDIR=$(dirname $(readlink -f $0))
DEPLOY="/var/weblogic-external-data/$APP/deploy"
VERSIONDIR=$DEPLOY/versoes
CONTROL=$BASEDIR/$APP"_control.txt"
LOG=$DEPLOY"/log-"$APP".txt"
MOUNT=/var/weblogic-external-data
USERCONFIG='/home/oracle/oracle-WebLogicConfig.properties'
USERKEY='/home/oracle/oracle-WebLogicKey.properties'
PATH=$PATH:$HOME/.local/bin:$HOME/bin
export CLASSPATH='/u01/middleware/fmw12c/wlserver/server/lib/weblogic.jar'
export MW_HOME=/u01/middleware/wls12c
export WLS_HOME=$MW_HOME/wlserver
export WL_HOME=$WLS_HOME
export JAVA_HOME=/u01/middleware/jdk
export PATH=$JAVA_HOME/bin:$PATH
export URL=`grep ADMIN_URL $DOMAIN_HOME/bin/stopWebLogic.sh  | grep t3  | cut -d '=' -f2 | sed -e 's/"//g'`
PID=$BASEDIR/$APP.pid

# Cria o subdiretorio versoes caso não exista
if [ ! -d $VERSIONDIR ] ;then
	mkdir $VERSIONDIR
fi	

#verifica se o Deploy já está em andamento
if [ -f "$PID" ]; then
        #echo `date` - Deploy já em andamento, saindo... >>$LOG
        exit 1
else touch $PID		
fi

# Verifica se o /weblogic-external-data está montado.
if ! mountpoint -q $MOUNT;
then
	rm $PID -rf
        exit 1
fi

#Seleciona o arquivo mais recente em $DEPLOY
unset NEWEST
for filename in $DEPLOY/*.ear; do
    if [ -f "$filename" ] && [ "$filename" -nt "$NEWEST" ]; then
        NEWEST=$filename
    fi
done

# Sai do programa caso não tenha arquivo ear
if [ -z $NEWEST ]
    then
		rm $PID	-rf 
        exit 0
fi

#Validação do formato do arquivo ear, se possui $APP-versão
if [[ ! $NEWEST =~ $APP ]]
then
   "Arquivo ear fora do formato: "$APP"_versão"
   rm $PID	-rf
   exit 1
fi

NEWESTDATA=`date --reference "$NEWEST" +%Y%m%d%H%M%S`

# Obtem a versão do ear armazenada
if [ -f $CONTROL ]
 then
	CONTROLDATA=`cat "$CONTROL"`
fi

# Executa o Redeploy em caso de um ear mais atual
if [ "$NEWESTDATA" != "$CONTROLDATA" ]; then
		if [[ "$NEWESTDATA" > "$CONTROLDATA" ]]; then
			java -cp $CLASSPATH weblogic.Deployer -adminurl $URL -userconfigfile $USERCONFIG -userkeyfile $USERKEY -redeploy -name $APP -source $NEWEST -usenonexclusivelock >>$LOG && echo $NEWESTDATA > $CONTROL
			mv $NEWEST $VERSIONDIR
		fi
fi
rm $PID	-rf   


