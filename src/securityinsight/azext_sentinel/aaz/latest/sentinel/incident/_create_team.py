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
    "sentinel incident create-team",
    is_experimental=True,
)
class CreateTeam(AAZCommand):
    """Create a Microsoft team to investigate the incident by sharing information and insights between participants.
    """

    _aaz_info = {
        "version": "2022-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/providers/microsoft.securityinsights/incidents/{}/createteam", "2022-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.incident_id = AAZStrArg(
            options=["--incident-id"],
            help="Incident ID",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            is_experimental=True,
        )

        # define Arg Group "TeamProperties"

        _args_schema = cls._args_schema
        _args_schema.group_ids = AAZListArg(
            options=["--group-ids"],
            arg_group="TeamProperties",
            help="List of group IDs to add their members to the team",
        )
        _args_schema.member_ids = AAZListArg(
            options=["--member-ids"],
            arg_group="TeamProperties",
            help="List of member IDs to add to the team",
        )
        _args_schema.team_description = AAZStrArg(
            options=["--team-description"],
            arg_group="TeamProperties",
            help="The description of the team",
        )
        _args_schema.team_name = AAZStrArg(
            options=["--team-name"],
            arg_group="TeamProperties",
            help="The name of the team",
            required=True,
        )

        group_ids = cls._args_schema.group_ids
        group_ids.Element = AAZStrArg()

        member_ids = cls._args_schema.member_ids
        member_ids.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.IncidentsCreateTeam(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IncidentsCreateTeam(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents/{incidentId}/createTeam",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "incidentId", self.ctx.args.incident_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01-preview",
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
            _builder.set_prop("groupIds", AAZListType, ".group_ids")
            _builder.set_prop("memberIds", AAZListType, ".member_ids")
            _builder.set_prop("teamDescription", AAZStrType, ".team_description")
            _builder.set_prop("teamName", AAZStrType, ".team_name", typ_kwargs={"flags": {"required": True}})

            group_ids = _builder.get(".groupIds")
            if group_ids is not None:
                group_ids.set_elements(AAZStrType, ".")

            member_ids = _builder.get(".memberIds")
            if member_ids is not None:
                member_ids.set_elements(AAZStrType, ".")

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
            _schema_on_200.description = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.primary_channel_url = AAZStrType(
                serialized_name="primaryChannelUrl",
                flags={"read_only": True},
            )
            _schema_on_200.team_creation_time_utc = AAZStrType(
                serialized_name="teamCreationTimeUtc",
                flags={"read_only": True},
            )
            _schema_on_200.team_id = AAZStrType(
                serialized_name="teamId",
                flags={"read_only": True},
            )

            return cls._schema_on_200


__all__ = ["CreateTeam"]
