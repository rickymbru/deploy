#!/bin/bash

name="metrus_3.13.1.20200714.2102.ear"
NEWEST="/var/weblogic-external-data/metrus/deploy/versoes/metrus_3.13.1.20200714.2102.ear"
md5=`md5sum ${NEWEST} | awk '{ print $1 }'`
            echo "############      Inicio do deploy      ############"
            echo "Arquivo: "$name
            echo "Hash Md5: "$md5
            echo ""
            echo "Executando o deploy ..."
            echo ""