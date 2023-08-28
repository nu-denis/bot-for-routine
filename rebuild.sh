docker build -t panda-bot:1.0 . &
PID=$!

wait $PID
docker stop panda_bot
docker run -d --name panda_bot panda-bot:1.0
