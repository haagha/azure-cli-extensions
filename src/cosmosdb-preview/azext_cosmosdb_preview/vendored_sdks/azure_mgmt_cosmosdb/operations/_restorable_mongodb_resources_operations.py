# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    subscription_id: str,
    location: str,
    instance_id: str,
    *,
    restore_location: Optional[str] = None,
    restore_timestamp_in_utc: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-02-15-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableMongodbResources")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "location": _SERIALIZER.url("location", location, 'str'),
        "instanceId": _SERIALIZER.url("instance_id", instance_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if restore_location is not None:
        _query_parameters['restoreLocation'] = _SERIALIZER.query("restore_location", restore_location, 'str')
    if restore_timestamp_in_utc is not None:
        _query_parameters['restoreTimestampInUtc'] = _SERIALIZER.query("restore_timestamp_in_utc", restore_timestamp_in_utc, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class RestorableMongodbResourcesOperations(object):
    """RestorableMongodbResourcesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cosmosdb.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        location: str,
        instance_id: str,
        restore_location: Optional[str] = None,
        restore_timestamp_in_utc: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.RestorableMongodbResourcesListResult"]:
        """Return a list of database and collection combo that exist on the account at the given timestamp
        and location. This helps in scenarios to validate what resources exist at given timestamp and
        location. This API requires
        'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission.

        :param location: Cosmos DB region, with spaces between words and each word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database account.
        :type instance_id: str
        :param restore_location: The location where the restorable resources are located. Default value
         is None.
        :type restore_location: str
        :param restore_timestamp_in_utc: The timestamp when the restorable resources existed. Default
         value is None.
        :type restore_timestamp_in_utc: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RestorableMongodbResourcesListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.RestorableMongodbResourcesListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-02-15-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestorableMongodbResourcesListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    location=location,
                    instance_id=instance_id,
                    api_version=api_version,
                    restore_location=restore_location,
                    restore_timestamp_in_utc=restore_timestamp_in_utc,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    location=location,
                    instance_id=instance_id,
                    api_version=api_version,
                    restore_location=restore_location,
                    restore_timestamp_in_utc=restore_timestamp_in_utc,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RestorableMongodbResourcesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableMongodbResources"}  # type: ignore
