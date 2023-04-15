# AWSQS::Kubernetes::Resource

Kubernetes Resource Types for AWS CloudFormation

This project has been deprecated, and is no longer supported. You are free to fork the code in the main branch and use it as a private resource type, but no support will be given by the AWS I&A or Cloudformation Teams.

**USE AT YOUR OWN RISK**

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AWSQS::Kubernetes::Resource",
    "Properties" : {
    }
}
</pre>

### YAML

<pre>
Type: AWSQS::Kubernetes::Resource
Properties:
</pre>

## Properties

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### ID

Primary identifier for Cloudformation

