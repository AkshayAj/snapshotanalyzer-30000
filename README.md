# snapshotanalyzer-30000
Demo project to manage AWS EC2 instance snapshots

##About
This project is a study project which uses boto3 to manage AWS EC2 instance snapshots

shotty uses the configuration file created by AWS cli
eg:

`aws configure profile shotty`

##Running
`pipenv run python shotty/shotty.py <command> <--project=Project>`

*command* is list, start or stop
*project* is optional
