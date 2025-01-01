# Pinger

A simple health checker that sends an alert via a Telegram bot if something is wrong.

## Setup

1. Add your Telegram bot token and chat ID to a .env file:

```bash
echo "BOT_TOKEN=your_bot_token" > .env
echo "BOT_OWNER_ID=your_chat_id" >> .env
```

2. Open the crontab editor:

```bash
crontab -e
```

3. Add entries for each service you want to monitor. For example:

```bash
# Check every minute and send an alert only if the service is unavailable:
*/1 * * * * cd $pinger_dir && poetry run python -m pinger https://example.com &>> /dev/null

# Check every week and send a message even if everything is fine. This ensures you know the pinger itself is running.
0 12 * * 7 cd $pinger_dir && poetry run python -m pinger https://example.com --send-ok &>> /dev/null

```

Replace `https://example.com` with the URL of the service you want to monitor, and `$pinger_dir` with the directory
where the Pinger script is located.