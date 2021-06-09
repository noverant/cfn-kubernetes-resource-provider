# Kubernetes Resource Types for AWS CloudFormation

This project provides extensions to AWS CloudFormation that enable the management of kubernetes resources in CloudFormation. By example:

Kubernetes manifest:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-cm
data:
  example_key: example_value
```

Can be added to a CloudFormation template:
 ```yaml
Resources:
  ExampleCm:
    Type: "AWSQS::Kubernetes::Resource"
    Properties:
      ClusterName: my-eks-cluster-name
      Namespace: default
      Manifest: | 
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: example-cm
        data:
          example_key: example_value
```
At this time EKS is supported by providing the `ClusterName`, with plans for support for more kubernetes distributions coming soon. 

## Prerequisites

### IAM role
An IAM role is used by CloudFormation to execute the resource type handler code provided by this project. A CloudFormation template to create the exeecution role is available [here](^https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/execution-role.template.yaml) 

### Create an EKS cluster and provide CloudFormation access to the Kubernetes API
EKS clusters use IAM to allow access to the kubernetes API, as the CloudFormation resource types in this project interact with the kubernetes API, the IAM execution role must be granted access to the kubernetes API. This can be done in one of two ways: 
 * Create the cluster using CloudFormation: Currently there is no native way to manage EKS auth using CloudFormation (+1 [this GitHub issue](^https://github.com/aws/containers-roadmap/issues/554) to help prioritize native support). For this reason we have published `AWSQS::EKS::Cluster`. Instructions on activation and usage can be found [here](^https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md).
 * Manually: to allow these resource types to access the kubernetes API, follow the [instructions in the EKS documentation](^https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html) adding the IAM execution role created above to the `system:masters` group. (Note: you can scope this down if you plan to use the resource type to only perform specific operations on the kubernetes cluster)

## Registering the Resource type
To privately register the resource types provided in this project into your account a CloudFromation template has been provided [here](^https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/register-type.template.yaml). Note that this must be run in each region yo plan to use this project in.

## Usage
The properties and return values are documented here:
* [`AWSQS::Kubernetes::Resource`](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/apply/docs/README.md)
* [`AWSQS::Kubernetes::Get`](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/get/docs/README.md)

## Examples

### Create a Kubernetes ConfigMap in the default namespace
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  MyConfigMap:
    Type: "AWSQS::Kubernetes::Resource"
    Properties:
      ClusterName: my-eks-cluster-name
      Namespace: default
      Manifest: | 
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: example-cm
        data:
          example_key: example_value
```

### Get the cluster IP for the kube-dns service and add it to stack outputs
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  GetKubeDnsClusterIp:
    Type: "AWSQS::Kubernetes::Get"
    Properties:
      ClusterName: my-eks-cluster-name
      Namespace: kube-system
      Name: svc/kube-dns
      JsonPath: '{.spec.clusterIP}'
Outputs:
  KubeDnsClusterIp:
    Value: !GetAtt GetKubeDnsClusterIp.Response
```
