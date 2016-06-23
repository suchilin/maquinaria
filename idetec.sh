#!/bin/bash
set -e
LOGFILE=/home/proagro/idetec/idetec.log
NUM_WORKERS=3
# user/group to run as
USER=proagro
ADDRESS=127.0.0.1:8002
TIMEOUT=1200
cd /home/proagro/idetec
source /home/proagro/.virtualenvs/idetec/bin/activate
exec gunicorn idetec.wsgi:application -w $NUM_WORKERS --bind=$ADDRESS \
  --timeout $TIMEOUT \
  --user=$USER --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE  
