#!/usr/bin/env bash

echo "Require 'pip packages' installed"
echo

#get APP_HOME path
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME=$s
a="$SCRIPT_HOME/.." ; a=$(cd "$a" && pwd) ; APP_HOME=$a

python $APP_HOME/application.py