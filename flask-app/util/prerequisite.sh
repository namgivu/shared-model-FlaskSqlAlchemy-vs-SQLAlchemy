#!/usr/bin/env bash

echo 'Require `python` installed'
echo 'Require `virtualenv` installed'
echo 'Require `pip` installed'
echo

#get APP_HOME path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME=$s
a="$SCRIPT_HOME/.." ; a=$(cd "$a" && pwd) ; APP_HOME=$a
e="$APP_HOME/.." ; e=$(cd "$e" && pwd) ; VENV_HOME="$e/venv"

echo "Steps to install prerequisite
1.  Install venv
    virtualenv $VENV_HOME

2.  Activate venv
    . $VENV_HOME/bin/activate

3.  Install pip packages
    pip install -r $APP_HOME/requirements.txt
"
