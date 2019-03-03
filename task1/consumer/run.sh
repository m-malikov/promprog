#! /bin/bash

until timeout 1 bash -c "cat < /dev/null > /dev/tcp/rabbitmq/5672"; do
  sleep 1
done

python consumer.py
