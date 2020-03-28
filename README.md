# Awesome Python App

App created to test several features on the cloud.  
for now, it is just a simple API.

## Stack

- Python 3.7
- Flask
- Boto3


## Deployment

Follow steps to simple deploy on an instance.

### Amazon Linux

Use this script as `User data` script (simplest way)

```sh
sudo yum update
wget https://github.com/rgalba/flask-app/archive/master.zip
unzip master.zip
cd flask-app-master/
sudo chmod +x scripts/amaz-linux.sh
sudo cp scripts/flask-app.service /etc/systemd/system/flask-app.service
sudo pip install -r requirements.txt
sudo systemctl daemon-reload
sudo systemctl enable flask-app.service
sudo systemctl start flask-app
sudo systemctl status flask-app -l
```