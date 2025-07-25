import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_sample_project_2.cdk_sample_project_2_stack import CdkSampleProject2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_sample_project_2/cdk_sample_project_2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkSampleProject2Stack(app, "cdk-sample-project-2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
