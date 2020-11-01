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

## AWS Cloud9 environment

In order to setup a Cloud9 env, follows the steps to create it using `aws cli`.  
Requirements:
- AWS account
- AWS CLI properly configured

1. Creates the environment:
```sh
$ aws cloudformation create-stack --stack-name python-cloud9 --template-body file://automation/cloud9.yml
{
    "StackId": "arn:aws:cloudformation:us-east-1:11111111:stack/python-cloud9/e380a640-1c51-11eb-8c00-0e69ad9c0de11"
}
```

2. Get the URL to access the environment:

```sh
$ aws cloudformation describe-stacks --stack-name python-cloud9 --query "Stacks[0].Outputs[0].OutputValue"
"https://us-east-1.console.aws.amazon.com/cloud9/ide/d96025f784e84b50a59daf55190e4bd1"
```