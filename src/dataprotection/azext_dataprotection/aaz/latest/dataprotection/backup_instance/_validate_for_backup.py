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
    "dataprotection backup-instance validate-for-backup",
    is_experimental=True,
)
class ValidateForBackup(AAZCommand):
    """Validate whether adhoc backup will be successful or not
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults/{}/validateforbackup", "2023-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the backup vault.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.backup_instance = AAZObjectArg(
            options=["--backup-instance"],
            arg_group="Parameters",
            help="Backup Instance",
            required=True,
        )

        backup_instance = cls._args_schema.backup_instance
        backup_instance.data_source_info = AAZObjectArg(
            options=["data-source-info"],
            help="Gets or sets the data source information.",
            required=True,
        )
        backup_instance.data_source_set_info = AAZObjectArg(
            options=["data-source-set-info"],
            help="Gets or sets the data source set information.",
        )
        backup_instance.datasource_auth_credentials = AAZObjectArg(
            options=["datasource-auth-credentials"],
            help="Credentials to use to authenticate with data source provider.",
        )
        backup_instance.friendly_name = AAZStrArg(
            options=["friendly-name"],
            help="Gets or sets the Backup Instance friendly name.",
        )
        backup_instance.object_type = AAZStrArg(
            options=["object-type"],
            required=True,
        )
        backup_instance.policy_info = AAZObjectArg(
            options=["policy-info"],
            help="Gets or sets the policy information.",
            required=True,
        )
        backup_instance.validation_type = AAZStrArg(
            options=["validation-type"],
            help="Specifies the type of validation. In case of DeepValidation, all validations from /validateForBackup API will run again.",
            enum={"DeepValidation": "DeepValidation", "ShallowValidation": "ShallowValidation"},
        )

        data_source_info = cls._args_schema.backup_instance.data_source_info
        data_source_info.datasource_type = AAZStrArg(
            options=["datasource-type"],
            help="DatasourceType of the resource.",
        )
        data_source_info.object_type = AAZStrArg(
            options=["object-type"],
            help="Type of Datasource object, used to initialize the right inherited type",
        )
        data_source_info.resource_id = AAZStrArg(
            options=["resource-id"],
            help="Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure resources, this will be the ID created by backup service via Fabric/Vault.",
            required=True,
        )
        data_source_info.resource_location = AAZStrArg(
            options=["resource-location"],
            help="Location of datasource.",
        )
        data_source_info.resource_name = AAZStrArg(
            options=["resource-name"],
            help="Unique identifier of the resource in the context of parent.",
        )
        data_source_info.resource_type = AAZStrArg(
            options=["resource-type"],
            help="Resource Type of Datasource.",
        )
        data_source_info.resource_uri = AAZStrArg(
            options=["resource-uri"],
            help="Uri of the resource.",
        )

        data_source_set_info = cls._args_schema.backup_instance.data_source_set_info
        data_source_set_info.datasource_type = AAZStrArg(
            options=["datasource-type"],
            help="DatasourceType of the resource.",
        )
        data_source_set_info.object_type = AAZStrArg(
            options=["object-type"],
            help="Type of Datasource object, used to initialize the right inherited type",
        )
        data_source_set_info.resource_id = AAZStrArg(
            options=["resource-id"],
            help="Full ARM ID of the resource. For azure resources, this is ARM ID. For non azure resources, this will be the ID created by backup service via Fabric/Vault.",
            required=True,
        )
        data_source_set_info.resource_location = AAZStrArg(
            options=["resource-location"],
            help="Location of datasource.",
        )
        data_source_set_info.resource_name = AAZStrArg(
            options=["resource-name"],
            help="Unique identifier of the resource in the context of parent.",
        )
        data_source_set_info.resource_type = AAZStrArg(
            options=["resource-type"],
            help="Resource Type of Datasource.",
        )
        data_source_set_info.resource_uri = AAZStrArg(
            options=["resource-uri"],
            help="Uri of the resource.",
        )

        datasource_auth_credentials = cls._args_schema.backup_instance.datasource_auth_credentials
        datasource_auth_credentials.secret_store_based_auth_credentials = AAZObjectArg(
            options=["secret-store-based-auth-credentials"],
        )

        secret_store_based_auth_credentials = cls._args_schema.backup_instance.datasource_auth_credentials.secret_store_based_auth_credentials
        secret_store_based_auth_credentials.secret_store_resource = AAZObjectArg(
            options=["secret-store-resource"],
            help="Secret store resource",
        )

        secret_store_resource = cls._args_schema.backup_instance.datasource_auth_credentials.secret_store_based_auth_credentials.secret_store_resource
        secret_store_resource.secret_store_type = AAZStrArg(
            options=["secret-store-type"],
            help="Gets or sets the type of secret store",
            required=True,
            enum={"AzureKeyVault": "AzureKeyVault", "Invalid": "Invalid"},
        )
        secret_store_resource.uri = AAZStrArg(
            options=["uri"],
            help="Uri to get to the resource",
        )
        secret_store_resource.value = AAZStrArg(
            options=["value"],
            help="Gets or sets value stored in secret store resource",
        )

        policy_info = cls._args_schema.backup_instance.policy_info
        policy_info.policy_id = AAZStrArg(
            options=["policy-id"],
            required=True,
        )
        policy_info.policy_parameters = AAZObjectArg(
            options=["policy-parameters"],
            help="Policy parameters for the backup instance",
        )

        policy_parameters = cls._args_schema.backup_instance.policy_info.policy_parameters
        policy_parameters.backup_datasource_parameters_list = AAZListArg(
            options=["backup-datasource-parameters-list"],
            help="Gets or sets the Backup Data Source Parameters",
        )
        policy_parameters.data_store_parameters_list = AAZListArg(
            options=["data-store-parameters-list"],
            help="Gets or sets the DataStore Parameters",
        )

        backup_datasource_parameters_list = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list
        backup_datasource_parameters_list.Element = AAZObjectArg()

        _element = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element
        _element.blob_backup_datasource_parameters = AAZObjectArg(
            options=["blob-backup-datasource-parameters"],
        )
        _element.kubernetes_cluster_backup_datasource_parameters = AAZObjectArg(
            options=["kubernetes-cluster-backup-datasource-parameters"],
        )

        blob_backup_datasource_parameters = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.blob_backup_datasource_parameters
        blob_backup_datasource_parameters.containers_list = AAZListArg(
            options=["containers-list"],
            help="List of containers to be backed up during configuration of backup of blobs",
            required=True,
        )

        containers_list = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.blob_backup_datasource_parameters.containers_list
        containers_list.Element = AAZStrArg()

        kubernetes_cluster_backup_datasource_parameters = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters
        kubernetes_cluster_backup_datasource_parameters.excluded_namespaces = AAZListArg(
            options=["excluded-namespaces"],
            help="Gets or sets the exclude namespaces property. This property sets the namespaces to be excluded during restore.",
        )
        kubernetes_cluster_backup_datasource_parameters.excluded_resource_types = AAZListArg(
            options=["excluded-resource-types"],
            help="Gets or sets the exclude resource types property. This property sets the resource types to be excluded during restore.",
        )
        kubernetes_cluster_backup_datasource_parameters.include_cluster_scope_resources = AAZBoolArg(
            options=["include-cluster-scope-resources"],
            help="Gets or sets the include cluster resources property. This property if enabled will include cluster scope resources during restore.",
            required=True,
        )
        kubernetes_cluster_backup_datasource_parameters.included_namespaces = AAZListArg(
            options=["included-namespaces"],
            help="Gets or sets the include namespaces property. This property sets the namespaces to be included during restore.",
        )
        kubernetes_cluster_backup_datasource_parameters.included_resource_types = AAZListArg(
            options=["included-resource-types"],
            help="Gets or sets the include resource types property. This property sets the resource types to be included during restore.",
        )
        kubernetes_cluster_backup_datasource_parameters.label_selectors = AAZListArg(
            options=["label-selectors"],
            help="Gets or sets the LabelSelectors property. This property sets the resource with such label selectors to be included during restore.",
        )
        kubernetes_cluster_backup_datasource_parameters.snapshot_volumes = AAZBoolArg(
            options=["snapshot-volumes"],
            help="Gets or sets the volume snapshot property. This property if enabled will take volume snapshots during restore.",
            required=True,
        )

        excluded_namespaces = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters.excluded_namespaces
        excluded_namespaces.Element = AAZStrArg()

        excluded_resource_types = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters.excluded_resource_types
        excluded_resource_types.Element = AAZStrArg()

        included_namespaces = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters.included_namespaces
        included_namespaces.Element = AAZStrArg()

        included_resource_types = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters.included_resource_types
        included_resource_types.Element = AAZStrArg()

        label_selectors = cls._args_schema.backup_instance.policy_info.policy_parameters.backup_datasource_parameters_list.Element.kubernetes_cluster_backup_datasource_parameters.label_selectors
        label_selectors.Element = AAZStrArg()

        data_store_parameters_list = cls._args_schema.backup_instance.policy_info.policy_parameters.data_store_parameters_list
        data_store_parameters_list.Element = AAZObjectArg()

        _element = cls._args_schema.backup_instance.policy_info.policy_parameters.data_store_parameters_list.Element
        _element.azure_operational_store_parameters = AAZObjectArg(
            options=["azure-operational-store-parameters"],
        )
        _element.data_store_type = AAZStrArg(
            options=["data-store-type"],
            help="type of datastore; Operational/Vault/Archive",
            required=True,
            enum={"ArchiveStore": "ArchiveStore", "OperationalStore": "OperationalStore", "VaultStore": "VaultStore"},
        )

        azure_operational_store_parameters = cls._args_schema.backup_instance.policy_info.policy_parameters.data_store_parameters_list.Element.azure_operational_store_parameters
        azure_operational_store_parameters.resource_group_id = AAZStrArg(
            options=["resource-group-id"],
            help="Gets or sets the Snapshot Resource Group Uri.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BackupInstancesValidateForBackup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class BackupInstancesValidateForBackup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}/validateForBackup",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

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
                **self.serialize_url_param(
                    "vaultName", self.ctx.args.vault_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("backupInstance", AAZObjectType, ".backup_instance", typ_kwargs={"flags": {"required": True}})

            backup_instance = _builder.get(".backupInstance")
            if backup_instance is not None:
                backup_instance.set_prop("dataSourceInfo", AAZObjectType, ".data_source_info", typ_kwargs={"flags": {"required": True}})
                backup_instance.set_prop("dataSourceSetInfo", AAZObjectType, ".data_source_set_info")
                backup_instance.set_prop("datasourceAuthCredentials", AAZObjectType, ".datasource_auth_credentials")
                backup_instance.set_prop("friendlyName", AAZStrType, ".friendly_name")
                backup_instance.set_prop("objectType", AAZStrType, ".object_type", typ_kwargs={"flags": {"required": True}})
                backup_instance.set_prop("policyInfo", AAZObjectType, ".policy_info", typ_kwargs={"flags": {"required": True}})
                backup_instance.set_prop("validationType", AAZStrType, ".validation_type")

            data_source_info = _builder.get(".backupInstance.dataSourceInfo")
            if data_source_info is not None:
                data_source_info.set_prop("datasourceType", AAZStrType, ".datasource_type")
                data_source_info.set_prop("objectType", AAZStrType, ".object_type")
                data_source_info.set_prop("resourceID", AAZStrType, ".resource_id", typ_kwargs={"flags": {"required": True}})
                data_source_info.set_prop("resourceLocation", AAZStrType, ".resource_location")
                data_source_info.set_prop("resourceName", AAZStrType, ".resource_name")
                data_source_info.set_prop("resourceType", AAZStrType, ".resource_type")
                data_source_info.set_prop("resourceUri", AAZStrType, ".resource_uri")

            data_source_set_info = _builder.get(".backupInstance.dataSourceSetInfo")
            if data_source_set_info is not None:
                data_source_set_info.set_prop("datasourceType", AAZStrType, ".datasource_type")
                data_source_set_info.set_prop("objectType", AAZStrType, ".object_type")
                data_source_set_info.set_prop("resourceID", AAZStrType, ".resource_id", typ_kwargs={"flags": {"required": True}})
                data_source_set_info.set_prop("resourceLocation", AAZStrType, ".resource_location")
                data_source_set_info.set_prop("resourceName", AAZStrType, ".resource_name")
                data_source_set_info.set_prop("resourceType", AAZStrType, ".resource_type")
                data_source_set_info.set_prop("resourceUri", AAZStrType, ".resource_uri")

            datasource_auth_credentials = _builder.get(".backupInstance.datasourceAuthCredentials")
            if datasource_auth_credentials is not None:
                datasource_auth_credentials.set_const("objectType", "SecretStoreBasedAuthCredentials", AAZStrType, ".secret_store_based_auth_credentials", typ_kwargs={"flags": {"required": True}})
                datasource_auth_credentials.discriminate_by("objectType", "SecretStoreBasedAuthCredentials")

            disc_secret_store_based_auth_credentials = _builder.get(".backupInstance.datasourceAuthCredentials{objectType:SecretStoreBasedAuthCredentials}")
            if disc_secret_store_based_auth_credentials is not None:
                disc_secret_store_based_auth_credentials.set_prop("secretStoreResource", AAZObjectType, ".secret_store_based_auth_credentials.secret_store_resource")

            secret_store_resource = _builder.get(".backupInstance.datasourceAuthCredentials{objectType:SecretStoreBasedAuthCredentials}.secretStoreResource")
            if secret_store_resource is not None:
                secret_store_resource.set_prop("secretStoreType", AAZStrType, ".secret_store_type", typ_kwargs={"flags": {"required": True}})
                secret_store_resource.set_prop("uri", AAZStrType, ".uri")
                secret_store_resource.set_prop("value", AAZStrType, ".value")

            policy_info = _builder.get(".backupInstance.policyInfo")
            if policy_info is not None:
                policy_info.set_prop("policyId", AAZStrType, ".policy_id", typ_kwargs={"flags": {"required": True}})
                policy_info.set_prop("policyParameters", AAZObjectType, ".policy_parameters")

            policy_parameters = _builder.get(".backupInstance.policyInfo.policyParameters")
            if policy_parameters is not None:
                policy_parameters.set_prop("backupDatasourceParametersList", AAZListType, ".backup_datasource_parameters_list")
                policy_parameters.set_prop("dataStoreParametersList", AAZListType, ".data_store_parameters_list")

            backup_datasource_parameters_list = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList")
            if backup_datasource_parameters_list is not None:
                backup_datasource_parameters_list.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]")
            if _elements is not None:
                _elements.set_const("objectType", "BlobBackupDatasourceParameters", AAZStrType, ".blob_backup_datasource_parameters", typ_kwargs={"flags": {"required": True}})
                _elements.set_const("objectType", "KubernetesClusterBackupDatasourceParameters", AAZStrType, ".kubernetes_cluster_backup_datasource_parameters", typ_kwargs={"flags": {"required": True}})
                _elements.discriminate_by("objectType", "BlobBackupDatasourceParameters")
                _elements.discriminate_by("objectType", "KubernetesClusterBackupDatasourceParameters")

            disc_blob_backup_datasource_parameters = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:BlobBackupDatasourceParameters}")
            if disc_blob_backup_datasource_parameters is not None:
                disc_blob_backup_datasource_parameters.set_prop("containersList", AAZListType, ".blob_backup_datasource_parameters.containers_list", typ_kwargs={"flags": {"required": True}})

            containers_list = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:BlobBackupDatasourceParameters}.containersList")
            if containers_list is not None:
                containers_list.set_elements(AAZStrType, ".")

            disc_kubernetes_cluster_backup_datasource_parameters = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}")
            if disc_kubernetes_cluster_backup_datasource_parameters is not None:
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("excludedNamespaces", AAZListType, ".kubernetes_cluster_backup_datasource_parameters.excluded_namespaces")
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("excludedResourceTypes", AAZListType, ".kubernetes_cluster_backup_datasource_parameters.excluded_resource_types")
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("includeClusterScopeResources", AAZBoolType, ".kubernetes_cluster_backup_datasource_parameters.include_cluster_scope_resources", typ_kwargs={"flags": {"required": True}})
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("includedNamespaces", AAZListType, ".kubernetes_cluster_backup_datasource_parameters.included_namespaces")
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("includedResourceTypes", AAZListType, ".kubernetes_cluster_backup_datasource_parameters.included_resource_types")
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("labelSelectors", AAZListType, ".kubernetes_cluster_backup_datasource_parameters.label_selectors")
                disc_kubernetes_cluster_backup_datasource_parameters.set_prop("snapshotVolumes", AAZBoolType, ".kubernetes_cluster_backup_datasource_parameters.snapshot_volumes", typ_kwargs={"flags": {"required": True}})

            excluded_namespaces = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}.excludedNamespaces")
            if excluded_namespaces is not None:
                excluded_namespaces.set_elements(AAZStrType, ".")

            excluded_resource_types = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}.excludedResourceTypes")
            if excluded_resource_types is not None:
                excluded_resource_types.set_elements(AAZStrType, ".")

            included_namespaces = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}.includedNamespaces")
            if included_namespaces is not None:
                included_namespaces.set_elements(AAZStrType, ".")

            included_resource_types = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}.includedResourceTypes")
            if included_resource_types is not None:
                included_resource_types.set_elements(AAZStrType, ".")

            label_selectors = _builder.get(".backupInstance.policyInfo.policyParameters.backupDatasourceParametersList[]{objectType:KubernetesClusterBackupDatasourceParameters}.labelSelectors")
            if label_selectors is not None:
                label_selectors.set_elements(AAZStrType, ".")

            data_store_parameters_list = _builder.get(".backupInstance.policyInfo.policyParameters.dataStoreParametersList")
            if data_store_parameters_list is not None:
                data_store_parameters_list.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".backupInstance.policyInfo.policyParameters.dataStoreParametersList[]")
            if _elements is not None:
                _elements.set_prop("dataStoreType", AAZStrType, ".data_store_type", typ_kwargs={"flags": {"required": True}})
                _elements.set_const("objectType", "AzureOperationalStoreParameters", AAZStrType, ".azure_operational_store_parameters", typ_kwargs={"flags": {"required": True}})
                _elements.discriminate_by("objectType", "AzureOperationalStoreParameters")

            disc_azure_operational_store_parameters = _builder.get(".backupInstance.policyInfo.policyParameters.dataStoreParametersList[]{objectType:AzureOperationalStoreParameters}")
            if disc_azure_operational_store_parameters is not None:
                disc_azure_operational_store_parameters.set_prop("resourceGroupId", AAZStrType, ".azure_operational_store_parameters.resource_group_id")

            return self.serialize_content(_content_value)

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
            _schema_on_200.job_id = AAZStrType(
                serialized_name="jobId",
            )
            _schema_on_200.object_type = AAZStrType(
                serialized_name="objectType",
                flags={"required": True},
            )

            return cls._schema_on_200


class _ValidateForBackupHelper:
    """Helper class for ValidateForBackup"""


__all__ = ["ValidateForBackup"]
