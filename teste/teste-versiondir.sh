#!/bin/sh


BASEDIR=$(dirname $(readlink -f $0))
VERSIONDIR=$BASEDIR/versoes

echo $BASEDIR
echo $VERSIONDIR

if [ ! -d $VERSIONDIR ] ;then
	mkdir $VERSIONDIR
fi	
	
	
		
		
