#!/usr/bin/env bash

echo "Below steps to kill the running app
- Current Python-related process
  ps aux | grep python

- Kill process command (fill in the process id in 'P01 P02 ...'
  processIdList='P01 P02' ; kill -9 \$processIdList
"
