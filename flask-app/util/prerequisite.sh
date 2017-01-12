#!/usr/bin/env bash

echo 'Require `python` installed'
echo 'Require `virtualenv` installed'
echo 'Require `pip` installed'
echo

#get APP_HOME path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME=$s
a="$SCRIPT_HOME/.." ; a=$(cd "$a" && pwd) ; APP_HOME=$a

echo "Steps to install prerequisite
1.  Install venv
    virtualenv $APP_HOME/venv

2.  Activate venv
    . $APP_HOME/venv/bin/activate

3.  Install pip packages
    pip install -r $APP_HOME/flask-app/requirements.txt
"
