# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test, rg):
    pass


# EXAMPLE: KustoClustersCreateOrUpdate
@try_manual
def step_kustoclusterscreateorupdate(test, rg):
    test.cmd('az kusto cluster create '
             '--name "{myCluster}" '
             '--identity-type "SystemAssigned" '
             '--location "westus" '
             '--enable-double-encryption false '
             '--enable-purge true '
             '--enable-streaming-ingest true '
             '--sku name="Standard_L8s" capacity=2 tier="Standard" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myCluster}", case_sensitive=False),
                 test.check("identity.type", "SystemAssigned", case_sensitive=False),
                 test.check("location", "westus", case_sensitive=False),
                 test.check("enableDoubleEncryption", False),
                 test.check("enablePurge", True),
                 test.check("enableStreamingIngest", True),
                 test.check("sku.name", "Standard_L8s", case_sensitive=False),
                 test.check("sku.capacity", 2),
                 test.check("sku.tier", "Standard", case_sensitive=False),
             ])
    test.cmd('az kusto cluster wait --created '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasesCreateOrUpdate
@try_manual
def step_kustodatabasescreateorupdate(test, rg):
    test.cmd('az kusto database create '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--parameters "{{\\"location\\":\\"westus\\",\\"properties\\":{{\\"softDeletePeriod\\":\\"P1D\\"}}}}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsCreateOrUpdate
@try_manual
def step_kustodataconnectionscreateorupdate(test, rg):
    test.cmd('az kusto data-connection event-hub create '
             '--cluster-name "{myCluster}" '
             '--name "{myDataConnection}" '
             '--database-name "KustoDatabase8" '
             '--location "westus" '
             '--consumer-group "testConsumerGroup1" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHu'
             'b/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: AttachedDatabaseConfigurationsCreateOrUpdate
@try_manual
def step_attacheddatabaseconfigurationscreateorupdate(test, rg):
    test.cmd('az kusto attached-database-configuration create '
             '--name "{myAttachedDatabaseConfiguration2}" '
             '--cluster-name "{myCluster}" '
             '--location "westus" '
             '--cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/Clu'
             'sters/{myCluster3}" '
             '--database-name "kustodatabase" '
             '--default-principals-modification-kind "Union" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "westus", case_sensitive=False),
                 test.check("clusterResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Micros"
                            "oft.Kusto/Clusters/{myCluster3}", case_sensitive=False),
                 test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
             ])
    test.cmd('az kusto attached-database-configuration wait --created '
             '--name "{myAttachedDatabaseConfiguration2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: AttachedDatabaseConfigurationsGet
@try_manual
def step_attacheddatabaseconfigurationsget(test, rg):
    test.cmd('az kusto attached-database-configuration show '
             '--name "{myAttachedDatabaseConfiguration2}" '
             '--cluster-name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "westus", case_sensitive=False),
                 test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
             ])


# EXAMPLE: KustoDataConnectionsGet
@try_manual
def step_kustodataconnectionsget(test, rg):
    test.cmd('az kusto data-connection show '
             '--cluster-name "{myCluster}" '
             '--name "{myDataConnection}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "westus", case_sensitive=False),
                 test.check("consumerGroup", "testConsumerGroup1", case_sensitive=False),
                 test.check("eventHubResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Micro"
                            "soft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1", case_sensitive=False),
             ])


# EXAMPLE: KustoDatabasesListByCluster
@try_manual
def step_kustodatabaseslistbycluster(test, rg):
    test.cmd('az kusto database list '
             '--cluster-name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoAttachedDatabaseConfigurationsListByCluster
@try_manual
def step_kustoattacheddatabaseconfigurationslistbyclus(test, rg):
    test.cmd('az kusto attached-database-configuration list '
             '--cluster-name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: KustoDatabasesGet
@try_manual
def step_kustodatabasesget(test, rg):
    test.cmd('az kusto database show '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasesListByCluster
@try_manual
def step_kustodatabaseslistbycluster(test, rg):
    test.cmd('az kusto database list '
             '--cluster-name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersListResourceSkus
@try_manual
def step_kustoclusterslistresourceskus(test, rg):
    test.cmd('az kusto cluster list-sku '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersGet
@try_manual
def step_kustoclustersget(test, rg):
    test.cmd('az kusto cluster show '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myCluster}", case_sensitive=False),
                 test.check("identity.type", "SystemAssigned", case_sensitive=False),
                 test.check("location", "westus", case_sensitive=False),
                 test.check("enableStreamingIngest", True),
                 test.check("sku.name", "Standard_L8s", case_sensitive=False),
                 test.check("sku.capacity", 2),
                 test.check("sku.tier", "Standard", case_sensitive=False),
             ])


# EXAMPLE: KustoClustersListByResourceGroup
@try_manual
def step_kustoclusterslistbyresourcegroup(test, rg):
    test.cmd('az kusto cluster list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: KustoClustersList
@try_manual
def step_kustoclusterslist(test, rg):
    test.cmd('az kusto cluster list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: KustoClustersListSkus
@try_manual
def step_kustoclusterslistskus(test, rg):
    test.cmd('az kusto cluster list-sku '
             '-g ""',
             checks=[])


# EXAMPLE: KustoOperationsList
@try_manual
def step_kustooperationslist(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: KustoDataConnectionsUpdate
@try_manual
def step_kustodataconnectionsupdate(test, rg):
    test.cmd('az kusto data-connection event-hub update '
             '--cluster-name "{myCluster}" '
             '--name "{myDataConnection}" '
             '--database-name "KustoDatabase8" '
             '--location "westus" '
             '--consumer-group "testConsumerGroup1" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHu'
             'b/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionValidation
@try_manual
def step_kustodataconnectionvalidation(test, rg):
    test.cmd('az kusto data-connection event-hub data-connection-validation '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--name "{myDataConnection}" '
             '--consumer-group "testConsumerGroup1" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHu'
             'b/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsCheckNameAvailability
@try_manual
def step_kustodataconnectionschecknameavailability(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: KustoDatabaseRemovePrincipals
@try_manual
def step_kustodatabaseremoveprincipals(test, rg):
    test.cmd('az kusto database remove-principal '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--value name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser role="Admin" '
             '--value name="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup role="Viewer" '
             '--value name="SomeApp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp role="Admin" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabaseListPrincipals
@try_manual
def step_kustodatabaselistprincipals(test, rg):
    test.cmd('az kusto database list-principal '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabaseAddPrincipals
@try_manual
def step_kustodatabaseaddprincipals(test, rg):
    test.cmd('az kusto database add-principal '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--value name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser role="Admin" '
             '--value name="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup role="Viewer" '
             '--value name="SomeApp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp role="Admin" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasesUpdate
@try_manual
def step_kustodatabasesupdate(test, rg):
    test.cmd('az kusto database update '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--parameters "{{\\"properties\\":{{\\"softDeletePeriod\\":\\"P1D\\"}}}}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClusterDetachFollowerDatabases
@try_manual
def step_kustoclusterdetachfollowerdatabases(test, rg):
    test.cmd('az kusto cluster detach-follower-database '
             '--name "{myCluster}" '
             '--attached-database-configuration-name "{myAttachedDatabaseConfiguration}" '
             '--cluster-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto/clu'
             'sters/{myCluster2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabaseCheckNameAvailability
@try_manual
def step_kustodatabasechecknameavailability(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: KustoClusterListFollowerDatabases
@try_manual
def step_kustoclusterlistfollowerdatabases(test, rg):
    test.cmd('az kusto cluster list-follower-database '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersStart
@try_manual
def step_kustoclustersstart(test, rg):
    test.cmd('az kusto cluster start '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersStop
@try_manual
def step_kustoclustersstop(test, rg):
    test.cmd('az kusto cluster stop '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersUpdate
@try_manual
def step_kustoclustersupdate(test, rg):
    test.cmd('az kusto cluster update '
             '--name "{myCluster}" '
             '--identity-type "SystemAssigned" '
             '--location "westus" '
             '--enable-purge true '
             '--enable-streaming-ingest true '
             '--engine-type "V2" '
             '--key-vault-properties key-name="keyName" key-vault-uri="https://dummy.keyvault.com" '
             'key-version="keyVersion" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myCluster}", case_sensitive=False),
                 test.check("identity.type", "SystemAssigned", case_sensitive=False),
                 test.check("location", "westus", case_sensitive=False),
                 test.check("enablePurge", True),
                 test.check("enableStreamingIngest", True),
                 test.check("engineType", "V2", case_sensitive=False),
                 test.check("keyVaultProperties.keyName", "keyName", case_sensitive=False),
                 test.check("keyVaultProperties.keyVaultUri", "https://dummy.keyvault.com", case_sensitive=False),
                 test.check("keyVaultProperties.keyVersion", "keyVersion", case_sensitive=False),
             ])


# EXAMPLE: KustoClustersCheckNameAvailability
@try_manual
def step_kustoclusterschecknameavailability(test, rg):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: AttachedDatabaseConfigurationsDelete
@try_manual
def step_attacheddatabaseconfigurationsdelete(test, rg):
    test.cmd('az kusto attached-database-configuration delete -y '
             '--name "{myAttachedDatabaseConfiguration2}" '
             '--cluster-name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsDelete
@try_manual
def step_kustodataconnectionsdelete(test, rg):
    test.cmd('az kusto data-connection delete -y '
             '--cluster-name "{myCluster}" '
             '--name "{myDataConnection2}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasesDelete
@try_manual
def step_kustodatabasesdelete(test, rg):
    test.cmd('az kusto database delete -y '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClustersDelete
@try_manual
def step_kustoclustersdelete(test, rg):
    test.cmd('az kusto cluster delete -y '
             '--name "{myCluster}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasePrincipalAssignmentsGet
@try_manual
def step_kustodatabaseprincipalassignmentsget(test, rg):
    test.cmd('az kusto database-principal-assignment show '
             '--cluster-name "{myCluster}" '
             '--database-name "Kustodatabase8" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasePrincipalAssignmentsCreateOrUpdate
@try_manual
def step_kustodatabaseprincipalassignmentscreateorupda(test, rg):
    test.cmd('az kusto database-principal-assignment create '
             '--cluster-name "{myCluster}" '
             '--database-name "Kustodatabase8" '
             '--principal-id "87654321-1234-1234-1234-123456789123" '
             '--principal-type "App" '
             '--role "Admin" '
             '--tenant-id "12345678-1234-1234-1234-123456789123" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDatabasePrincipalAssignmentsDelete
@try_manual
def step_kustodatabaseprincipalassignmentsdelete(test, rg):
    test.cmd('az kusto database-principal-assignment delete -y '
             '--cluster-name "{myCluster}" '
             '--database-name "Kustodatabase8" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClusterPrincipalAssignmentsGet
@try_manual
def step_kustoclusterprincipalassignmentsget(test, rg):
    test.cmd('az kusto cluster-principal-assignment show '
             '--cluster-name "{myCluster}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClusterPrincipalAssignmentsCreateOrUpdate
@try_manual
def step_kustoclusterprincipalassignmentscreateorupdat(test, rg):
    test.cmd('az kusto cluster-principal-assignment create '
             '--cluster-name "{myCluster}" '
             '--principal-id "87654321-1234-1234-1234-123456789123" '
             '--principal-type "App" '
             '--role "AllDatabasesAdmin" '
             '--tenant-id "12345678-1234-1234-1234-123456789123" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoClusterPrincipalAssignmentsDelete
@try_manual
def step_kustoclusterprincipalassignmentsdelete(test, rg):
    test.cmd('az kusto cluster-principal-assignment delete -y '
             '--cluster-name "{myCluster}" '
             '--principal-assignment-name "kustoprincipal1" '
             '--resource-group "{rg}"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg):
    pass


# Testcase
@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step_kustoclusterscreateorupdate(test, rg)
    step_kustodatabasescreateorupdate(test, rg)
    step_kustodataconnectionscreateorupdate(test, rg)
    step_attacheddatabaseconfigurationscreateorupdate(test, rg)
    step_attacheddatabaseconfigurationsget(test, rg)
    step_kustodataconnectionsget(test, rg)
    step_kustodatabaseslistbycluster(test, rg)
    step_kustoattacheddatabaseconfigurationslistbyclus(test, rg)
    step_kustodatabasesget(test, rg)
    step_kustodatabaseslistbycluster(test, rg)
    step_kustoclusterslistresourceskus(test, rg)
    step_kustoclustersget(test, rg)
    step_kustoclusterslistbyresourcegroup(test, rg)
    step_kustoclusterslist(test, rg)
    step_kustoclusterslistskus(test, rg)
    step_kustooperationslist(test, rg)
    step_kustodataconnectionsupdate(test, rg)
    step_kustodataconnectionvalidation(test, rg)
    step_kustodataconnectionschecknameavailability(test, rg)
    step_kustodatabaseremoveprincipals(test, rg)
    step_kustodatabaselistprincipals(test, rg)
    step_kustodatabaseaddprincipals(test, rg)
    step_kustodatabasesupdate(test, rg)
    step_kustoclusterdetachfollowerdatabases(test, rg)
    step_kustodatabasechecknameavailability(test, rg)
    step_kustoclusterlistfollowerdatabases(test, rg)
    step_kustoclustersstart(test, rg)
    step_kustoclustersstop(test, rg)
    step_kustoclustersupdate(test, rg)
    step_kustoclusterschecknameavailability(test, rg)
    step_attacheddatabaseconfigurationsdelete(test, rg)
    step_kustodataconnectionsdelete(test, rg)
    step_kustodatabasesdelete(test, rg)
    step_kustoclustersdelete(test, rg)
    step_kustodatabaseprincipalassignmentsget(test, rg)
    step_kustodatabaseprincipalassignmentscreateorupda(test, rg)
    step_kustodatabaseprincipalassignmentsdelete(test, rg)
    step_kustoclusterprincipalassignmentsget(test, rg)
    step_kustoclusterprincipalassignmentscreateorupdat(test, rg)
    step_kustoclusterprincipalassignmentsdelete(test, rg)
    cleanup(test, rg)


@try_manual
class KustoManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    def test_kusto(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myCluster4': 'default',
            'myAttachedDatabaseConfiguration3': 'default',
            'myCluster2': 'leader4',
            'myCluster3': 'KustoClusterLeader',
            'myCluster': 'kustoclusterrptest4',
            'myAttachedDatabaseConfiguration': 'myAttachedDatabaseConfiguration',
            'myAttachedDatabaseConfiguration2': 'attachedDatabaseConfigurations1',
            'myDataConnection': 'DataConnections8',
            'myDataConnection2': 'kustoeventhubconnection1',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
