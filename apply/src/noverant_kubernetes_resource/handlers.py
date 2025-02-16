import logging
import json
import requests
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
    identifier_utils,
)

from .models import ResourceHandlerRequest, ResourceModel, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Noverant::Kubernetes::Resource"

resource = Resource(TYPE_NAME, ResourceModel, TypeConfigurationModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    config = request.typeConfiguration
    model.Notes = None

    try:
        print('Kubernetes Resource Types for AWS CloudFormation')

    except Exception as e:
        raise exceptions.InternalFailure(f"{e}")

    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.DELETE)
def delete_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    LOG.error("delete handler invoked")
    model = request.desiredResourceState
    ssm = session.client('ssm')
    try:
        print('Kubernetes Resource Types for AWS CloudFormation')

    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=None,
    )




