# Kubernetes Resource Types for AWS CloudFormation

This project provides extensions to AWS CloudFormation that enable the creation of kubernetes resources. By example:

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
At this time EKS is supported by providing the `ClusterName`, with plans for support for more kubernetes ditributions coming soon. 

