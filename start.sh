if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/JadejaShu/valentinaa.git /valentinaa
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /valentinaa
fi
cd /valentinaa
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
