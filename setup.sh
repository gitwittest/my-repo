#!/bin/bash
cd ~/Desktop

echo  '.......... starting redis  .......... '
redis-server &
echo ''
echo  '.......... redis done .......... '

echo  '.......... starting celery worker .......... '
celery -A sound worker --loglevel=info &
echo  '.......... celery done .......... '
echo ''

echo  '.......... starting flask server .......... '
python webapp.py &
echo  '.......... flask done .......... '

echo  '...100% Init completed , visit localhost to start the app'