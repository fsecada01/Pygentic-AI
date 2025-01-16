#!/bin/bash

#set -o errexit
#set -o nounset

rm -f './celerybeat.pid'

cd /opt/pygentic_ai
source .venv/bin/activate

#apt-get install supervisor -y
#
#echo user=nobody >> /etc/supervisor/supervisord.conf
#service supervisor stop
#service supervisor start
#supervisorctl start celeryd
#supervisorctl start celerybeat

celery -A cworker --workdir /opt/pygentic_ai/src worker -l INFO --detach
celery -A cworker --workdir \
/opt/pygentic_ai/src beat \
--scheduler celery.beat.Scheduler \
-l INFO \
--detach

sleep 10

worker_ready() {
    celery -A cworker --workdir /opt/pygentic_ai/src inspect ping
}



until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

celery -A cworker --workdir /opt/pygentic_ai/src flower --basic-auth=${FLOWER_USERNAME}:${FLOWER_PASSWORD} --port=${CELERY_PORT} -l INFO
