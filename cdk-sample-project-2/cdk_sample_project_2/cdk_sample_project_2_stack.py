from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkSampleProject2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creates a VPC with two public subnets (10.0.0.0/16, 1 AZ)
        vpc = ec2.Vpc(self, 'DemoVPC',
            cidr='10.0.0.0/16',
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='PublicSubnet',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
        )

        # Defines a SG allowing HTTP (80) and SSH (22) from anywhere
        web_sg = ec2.SecurityGroup(self, 'WebSG',
            vpc=vpc,
            security_group_name='iac-demo-web-sg',
            description='Allow HTTP & SSH',
            allow_all_outbound=True
        )
        # Ingress rule: HTTP
        web_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description='Allow HTTP from anywhere'
        )
        # Ingress rule: SSH
        web_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description='Allow SSH from anywhere'
        )

        # Launches a t2.micro Amazon Linux 2 instance into a public subnet
        ec2.Instance(self, 'WebInstance',
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=web_sg,
            key_name='my-keypair'  # instruct viewers to replace or parameterize
        )


        # Output the VPC ID
        CfnOutput(self, 'VpcId',
            value=vpc.vpc_id,
            description='The ID of the created VPC'
        )

        # Output the Public Subnet IDs (comma-separated)
        CfnOutput(self, 'PublicSubnetIds',
            value=','.join([sub.subnet_id for sub in vpc.public_subnets]),
            description='Comma-separated list of public subnet IDs'
        )


        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkSampleProject2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
