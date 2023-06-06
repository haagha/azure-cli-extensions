# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "dataprotection backup-vault list",
    is_experimental=True,
)
class List(AAZCommand):
    """Gets list of backup vault in a subscription or in a resource group.

    :example: List backup vault in a subscription
        az dataprotection backup-vault list

    :example: List backup vault in a resource group
        az dataprotection backup-vault list -g sarath-rg
    """

    _aaz_info = {
        "version": "2022-12-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.dataprotection/backupvaults", "2022-12-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults", "2022-12-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.BackupVaultsGetInSubscription(ctx=self.ctx)()
        if condition_1:
            self.BackupVaultsGetInResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class BackupVaultsGetInSubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.DataProtection/backupVaults",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.e_tag = AAZStrType(
                serialized_name="eTag",
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.feature_settings = AAZObjectType(
                serialized_name="featureSettings",
            )
            properties.is_vault_protected_by_resource_guard = AAZBoolType(
                serialized_name="isVaultProtectedByResourceGuard",
                flags={"read_only": True},
            )
            properties.monitoring_settings = AAZObjectType(
                serialized_name="monitoringSettings",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_move_details = AAZObjectType(
                serialized_name="resourceMoveDetails",
            )
            properties.resource_move_state = AAZStrType(
                serialized_name="resourceMoveState",
                flags={"read_only": True},
            )
            properties.security_settings = AAZObjectType(
                serialized_name="securitySettings",
            )
            properties.storage_settings = AAZListType(
                serialized_name="storageSettings",
                flags={"required": True},
            )

            feature_settings = cls._schema_on_200.value.Element.properties.feature_settings
            feature_settings.cross_subscription_restore_settings = AAZObjectType(
                serialized_name="crossSubscriptionRestoreSettings",
            )

            cross_subscription_restore_settings = cls._schema_on_200.value.Element.properties.feature_settings.cross_subscription_restore_settings
            cross_subscription_restore_settings.state = AAZStrType()

            monitoring_settings = cls._schema_on_200.value.Element.properties.monitoring_settings
            monitoring_settings.azure_monitor_alert_settings = AAZObjectType(
                serialized_name="azureMonitorAlertSettings",
            )

            azure_monitor_alert_settings = cls._schema_on_200.value.Element.properties.monitoring_settings.azure_monitor_alert_settings
            azure_monitor_alert_settings.alerts_for_all_job_failures = AAZStrType(
                serialized_name="alertsForAllJobFailures",
            )

            resource_move_details = cls._schema_on_200.value.Element.properties.resource_move_details
            resource_move_details.completion_time_utc = AAZStrType(
                serialized_name="completionTimeUtc",
            )
            resource_move_details.operation_id = AAZStrType(
                serialized_name="operationId",
            )
            resource_move_details.source_resource_path = AAZStrType(
                serialized_name="sourceResourcePath",
            )
            resource_move_details.start_time_utc = AAZStrType(
                serialized_name="startTimeUtc",
            )
            resource_move_details.target_resource_path = AAZStrType(
                serialized_name="targetResourcePath",
            )

            security_settings = cls._schema_on_200.value.Element.properties.security_settings
            security_settings.immutability_settings = AAZObjectType(
                serialized_name="immutabilitySettings",
            )
            security_settings.soft_delete_settings = AAZObjectType(
                serialized_name="softDeleteSettings",
            )

            immutability_settings = cls._schema_on_200.value.Element.properties.security_settings.immutability_settings
            immutability_settings.state = AAZStrType()

            soft_delete_settings = cls._schema_on_200.value.Element.properties.security_settings.soft_delete_settings
            soft_delete_settings.retention_duration_in_days = AAZFloatType(
                serialized_name="retentionDurationInDays",
            )
            soft_delete_settings.state = AAZStrType()

            storage_settings = cls._schema_on_200.value.Element.properties.storage_settings
            storage_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.storage_settings.Element
            _element.datastore_type = AAZStrType(
                serialized_name="datastoreType",
            )
            _element.type = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class BackupVaultsGetInResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-12-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.e_tag = AAZStrType(
                serialized_name="eTag",
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.feature_settings = AAZObjectType(
                serialized_name="featureSettings",
            )
            properties.is_vault_protected_by_resource_guard = AAZBoolType(
                serialized_name="isVaultProtectedByResourceGuard",
                flags={"read_only": True},
            )
            properties.monitoring_settings = AAZObjectType(
                serialized_name="monitoringSettings",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_move_details = AAZObjectType(
                serialized_name="resourceMoveDetails",
            )
            properties.resource_move_state = AAZStrType(
                serialized_name="resourceMoveState",
                flags={"read_only": True},
            )
            properties.security_settings = AAZObjectType(
                serialized_name="securitySettings",
            )
            properties.storage_settings = AAZListType(
                serialized_name="storageSettings",
                flags={"required": True},
            )

            feature_settings = cls._schema_on_200.value.Element.properties.feature_settings
            feature_settings.cross_subscription_restore_settings = AAZObjectType(
                serialized_name="crossSubscriptionRestoreSettings",
            )

            cross_subscription_restore_settings = cls._schema_on_200.value.Element.properties.feature_settings.cross_subscription_restore_settings
            cross_subscription_restore_settings.state = AAZStrType()

            monitoring_settings = cls._schema_on_200.value.Element.properties.monitoring_settings
            monitoring_settings.azure_monitor_alert_settings = AAZObjectType(
                serialized_name="azureMonitorAlertSettings",
            )

            azure_monitor_alert_settings = cls._schema_on_200.value.Element.properties.monitoring_settings.azure_monitor_alert_settings
            azure_monitor_alert_settings.alerts_for_all_job_failures = AAZStrType(
                serialized_name="alertsForAllJobFailures",
            )

            resource_move_details = cls._schema_on_200.value.Element.properties.resource_move_details
            resource_move_details.completion_time_utc = AAZStrType(
                serialized_name="completionTimeUtc",
            )
            resource_move_details.operation_id = AAZStrType(
                serialized_name="operationId",
            )
            resource_move_details.source_resource_path = AAZStrType(
                serialized_name="sourceResourcePath",
            )
            resource_move_details.start_time_utc = AAZStrType(
                serialized_name="startTimeUtc",
            )
            resource_move_details.target_resource_path = AAZStrType(
                serialized_name="targetResourcePath",
            )

            security_settings = cls._schema_on_200.value.Element.properties.security_settings
            security_settings.immutability_settings = AAZObjectType(
                serialized_name="immutabilitySettings",
            )
            security_settings.soft_delete_settings = AAZObjectType(
                serialized_name="softDeleteSettings",
            )

            immutability_settings = cls._schema_on_200.value.Element.properties.security_settings.immutability_settings
            immutability_settings.state = AAZStrType()

            soft_delete_settings = cls._schema_on_200.value.Element.properties.security_settings.soft_delete_settings
            soft_delete_settings.retention_duration_in_days = AAZFloatType(
                serialized_name="retentionDurationInDays",
            )
            soft_delete_settings.state = AAZStrType()

            storage_settings = cls._schema_on_200.value.Element.properties.storage_settings
            storage_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.storage_settings.Element
            _element.datastore_type = AAZStrType(
                serialized_name="datastoreType",
            )
            _element.type = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
