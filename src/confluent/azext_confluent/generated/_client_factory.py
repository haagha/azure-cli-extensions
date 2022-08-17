# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=import-outside-toplevel


def cf_confluent_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_confluent.vendored_sdks.confluent import ConfluentManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   ConfluentManagementClient)


def cf_marketplace_agreement(cli_ctx, *_):
    return cf_confluent_cl(cli_ctx).marketplace_agreements


def cf_organization(cli_ctx, *_):
    return cf_confluent_cl(cli_ctx).organization
