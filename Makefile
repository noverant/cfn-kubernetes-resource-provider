.PHONY: build publish clean

REGION ?= us-east-1
BUCKET ?= jmmccon-uno-dev
EX_ROLE ?= arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>
LOG_ROLE ?= arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>

build:
	docker build . -t k8s-cfn-build
	docker run -i --name k8s-cfn-build k8s-cfn-build
	docker cp k8s-cfn-build:/output/. ./build/
	docker rm k8s-cfn-build

publish:
	aws s3 cp ./build/awsqs_kubernetes_apply.zip s3://$(BUCKET)/
	aws cloudformation register-type --type "RESOURCE" --type-name  "AWSQS::Kubernetes::Resource" --schema-handler-package s3://$(BUCKET)/awsqs_kubernetes_apply.zip --logging-config LogRoleArn=$(LOG_ROLE),LogGroupName=/cloudformation/uno-beta/test --execution-role-arn $(EX_ROLE) --region $(REGION)

clean:
	rm -rf build/