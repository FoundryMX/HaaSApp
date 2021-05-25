#!/bin/bash
ppid=$(ps -ef | awk '$1 == "xrdp" {print $3}' | tail -1)

if [ -z $ppid ];then
   echo "XRDP is not working"
else
   echo "PPID: $ppid"
   if [ $ppid -eq 1 ]; then
      echo "XRDP is working but no one is connected"
   else
      echo "Someone is connected"
   fi
fi
