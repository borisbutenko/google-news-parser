#!/bin/bash

action=$1
msg="Activate env"

case ${action} in
    "activate"):
        source env/bin/activate
        ;;
    "deactivate"):
        msg="Deactivate env"
        deactivate
        ;;
    *):
        source env/bin/activate
esac

echo ${msg}
