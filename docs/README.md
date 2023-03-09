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
        "<a href="#id" title="ID">ID</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: AWSQS::Kubernetes::Resource
Properties:
    <a href="#id" title="ID">ID</a>: <i>String</i>
</pre>

## Properties

#### ID

Primary identifier for Cloudformation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the ID.
