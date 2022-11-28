# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.container import gapic_version as package_version

__version__ = package_version.__version__


from .services.cluster_manager import ClusterManagerAsyncClient, ClusterManagerClient
from .types.cluster_service import (
    AcceleratorConfig,
    AddonsConfig,
    AdvancedMachineFeatures,
    AuthenticatorGroupsConfig,
    Autopilot,
    AutoprovisioningNodePoolDefaults,
    AutoUpgradeOptions,
    BinaryAuthorization,
    BlueGreenSettings,
    CancelOperationRequest,
    ClientCertificateConfig,
    CloudRunConfig,
    Cluster,
    ClusterAutoscaling,
    ClusterUpdate,
    CompleteIPRotationRequest,
    CompleteNodePoolUpgradeRequest,
    ConfidentialNodes,
    ConfigConnectorConfig,
    CostManagementConfig,
    CreateClusterRequest,
    CreateNodePoolRequest,
    DailyMaintenanceWindow,
    DatabaseEncryption,
    DatapathProvider,
    DefaultSnatStatus,
    DeleteClusterRequest,
    DeleteNodePoolRequest,
    DnsCacheConfig,
    DNSConfig,
    FastSocket,
    GatewayAPIConfig,
    GcePersistentDiskCsiDriverConfig,
    GcfsConfig,
    GcpFilestoreCsiDriverConfig,
    GetClusterRequest,
    GetJSONWebKeysRequest,
    GetJSONWebKeysResponse,
    GetNodePoolRequest,
    GetOpenIDConfigRequest,
    GetOpenIDConfigResponse,
    GetOperationRequest,
    GetServerConfigRequest,
    GkeBackupAgentConfig,
    GPUSharingConfig,
    HorizontalPodAutoscaling,
    HttpLoadBalancing,
    IdentityServiceConfig,
    ILBSubsettingConfig,
    IntraNodeVisibilityConfig,
    IPAllocationPolicy,
    IPv6AccessType,
    Jwk,
    KubernetesDashboard,
    LegacyAbac,
    LinuxNodeConfig,
    ListClustersRequest,
    ListClustersResponse,
    ListNodePoolsRequest,
    ListNodePoolsResponse,
    ListOperationsRequest,
    ListOperationsResponse,
    ListUsableSubnetworksRequest,
    ListUsableSubnetworksResponse,
    LoggingComponentConfig,
    LoggingConfig,
    LoggingVariantConfig,
    MaintenanceExclusionOptions,
    MaintenancePolicy,
    MaintenanceWindow,
    ManagedPrometheusConfig,
    MasterAuth,
    MasterAuthorizedNetworksConfig,
    MaxPodsConstraint,
    MeshCertificates,
    MonitoringComponentConfig,
    MonitoringConfig,
    NetworkConfig,
    NetworkPolicy,
    NetworkPolicyConfig,
    NetworkTags,
    NodeConfig,
    NodeConfigDefaults,
    NodeKubeletConfig,
    NodeLabels,
    NodeManagement,
    NodeNetworkConfig,
    NodePool,
    NodePoolAutoConfig,
    NodePoolAutoscaling,
    NodePoolDefaults,
    NodePoolLoggingConfig,
    NodePoolUpdateStrategy,
    NodeTaint,
    NodeTaints,
    NotificationConfig,
    Operation,
    OperationProgress,
    PrivateClusterConfig,
    PrivateClusterMasterGlobalAccessConfig,
    PrivateIPv6GoogleAccess,
    RecurringTimeWindow,
    ReleaseChannel,
    ReservationAffinity,
    ResourceLabels,
    ResourceLimit,
    ResourceUsageExportConfig,
    RollbackNodePoolUpgradeRequest,
    SandboxConfig,
    SecurityBulletinEvent,
    ServerConfig,
    ServiceExternalIPsConfig,
    SetAddonsConfigRequest,
    SetLabelsRequest,
    SetLegacyAbacRequest,
    SetLocationsRequest,
    SetLoggingServiceRequest,
    SetMaintenancePolicyRequest,
    SetMasterAuthRequest,
    SetMonitoringServiceRequest,
    SetNetworkPolicyRequest,
    SetNodePoolAutoscalingRequest,
    SetNodePoolManagementRequest,
    SetNodePoolSizeRequest,
    ShieldedInstanceConfig,
    ShieldedNodes,
    StackType,
    StartIPRotationRequest,
    StatusCondition,
    TimeWindow,
    UpdateClusterRequest,
    UpdateMasterRequest,
    UpdateNodePoolRequest,
    UpgradeAvailableEvent,
    UpgradeEvent,
    UpgradeResourceType,
    UsableSubnetwork,
    UsableSubnetworkSecondaryRange,
    VerticalPodAutoscaling,
    VirtualNIC,
    WorkloadIdentityConfig,
    WorkloadMetadataConfig,
)

__all__ = (
    "ClusterManagerAsyncClient",
    "AcceleratorConfig",
    "AddonsConfig",
    "AdvancedMachineFeatures",
    "AuthenticatorGroupsConfig",
    "AutoUpgradeOptions",
    "Autopilot",
    "AutoprovisioningNodePoolDefaults",
    "BinaryAuthorization",
    "BlueGreenSettings",
    "CancelOperationRequest",
    "ClientCertificateConfig",
    "CloudRunConfig",
    "Cluster",
    "ClusterAutoscaling",
    "ClusterManagerClient",
    "ClusterUpdate",
    "CompleteIPRotationRequest",
    "CompleteNodePoolUpgradeRequest",
    "ConfidentialNodes",
    "ConfigConnectorConfig",
    "CostManagementConfig",
    "CreateClusterRequest",
    "CreateNodePoolRequest",
    "DNSConfig",
    "DailyMaintenanceWindow",
    "DatabaseEncryption",
    "DatapathProvider",
    "DefaultSnatStatus",
    "DeleteClusterRequest",
    "DeleteNodePoolRequest",
    "DnsCacheConfig",
    "FastSocket",
    "GPUSharingConfig",
    "GatewayAPIConfig",
    "GcePersistentDiskCsiDriverConfig",
    "GcfsConfig",
    "GcpFilestoreCsiDriverConfig",
    "GetClusterRequest",
    "GetJSONWebKeysRequest",
    "GetJSONWebKeysResponse",
    "GetNodePoolRequest",
    "GetOpenIDConfigRequest",
    "GetOpenIDConfigResponse",
    "GetOperationRequest",
    "GetServerConfigRequest",
    "GkeBackupAgentConfig",
    "HorizontalPodAutoscaling",
    "HttpLoadBalancing",
    "ILBSubsettingConfig",
    "IPAllocationPolicy",
    "IPv6AccessType",
    "IdentityServiceConfig",
    "IntraNodeVisibilityConfig",
    "Jwk",
    "KubernetesDashboard",
    "LegacyAbac",
    "LinuxNodeConfig",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListNodePoolsRequest",
    "ListNodePoolsResponse",
    "ListOperationsRequest",
    "ListOperationsResponse",
    "ListUsableSubnetworksRequest",
    "ListUsableSubnetworksResponse",
    "LoggingComponentConfig",
    "LoggingConfig",
    "LoggingVariantConfig",
    "MaintenanceExclusionOptions",
    "MaintenancePolicy",
    "MaintenanceWindow",
    "ManagedPrometheusConfig",
    "MasterAuth",
    "MasterAuthorizedNetworksConfig",
    "MaxPodsConstraint",
    "MeshCertificates",
    "MonitoringComponentConfig",
    "MonitoringConfig",
    "NetworkConfig",
    "NetworkPolicy",
    "NetworkPolicyConfig",
    "NetworkTags",
    "NodeConfig",
    "NodeConfigDefaults",
    "NodeKubeletConfig",
    "NodeLabels",
    "NodeManagement",
    "NodeNetworkConfig",
    "NodePool",
    "NodePoolAutoConfig",
    "NodePoolAutoscaling",
    "NodePoolDefaults",
    "NodePoolLoggingConfig",
    "NodePoolUpdateStrategy",
    "NodeTaint",
    "NodeTaints",
    "NotificationConfig",
    "Operation",
    "OperationProgress",
    "PrivateClusterConfig",
    "PrivateClusterMasterGlobalAccessConfig",
    "PrivateIPv6GoogleAccess",
    "RecurringTimeWindow",
    "ReleaseChannel",
    "ReservationAffinity",
    "ResourceLabels",
    "ResourceLimit",
    "ResourceUsageExportConfig",
    "RollbackNodePoolUpgradeRequest",
    "SandboxConfig",
    "SecurityBulletinEvent",
    "ServerConfig",
    "ServiceExternalIPsConfig",
    "SetAddonsConfigRequest",
    "SetLabelsRequest",
    "SetLegacyAbacRequest",
    "SetLocationsRequest",
    "SetLoggingServiceRequest",
    "SetMaintenancePolicyRequest",
    "SetMasterAuthRequest",
    "SetMonitoringServiceRequest",
    "SetNetworkPolicyRequest",
    "SetNodePoolAutoscalingRequest",
    "SetNodePoolManagementRequest",
    "SetNodePoolSizeRequest",
    "ShieldedInstanceConfig",
    "ShieldedNodes",
    "StackType",
    "StartIPRotationRequest",
    "StatusCondition",
    "TimeWindow",
    "UpdateClusterRequest",
    "UpdateMasterRequest",
    "UpdateNodePoolRequest",
    "UpgradeAvailableEvent",
    "UpgradeEvent",
    "UpgradeResourceType",
    "UsableSubnetwork",
    "UsableSubnetworkSecondaryRange",
    "VerticalPodAutoscaling",
    "VirtualNIC",
    "WorkloadIdentityConfig",
    "WorkloadMetadataConfig",
)
