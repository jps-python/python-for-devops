import boto3
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-12345678',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print("EC2 Instance Created:", instance[0].id)
