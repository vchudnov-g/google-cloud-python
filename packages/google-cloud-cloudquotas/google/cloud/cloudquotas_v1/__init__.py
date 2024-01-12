# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.cloud.cloudquotas_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_quotas import CloudQuotasAsyncClient, CloudQuotasClient
from .types.cloudquotas import (
    CreateQuotaPreferenceRequest,
    GetQuotaInfoRequest,
    GetQuotaPreferenceRequest,
    ListQuotaInfosRequest,
    ListQuotaInfosResponse,
    ListQuotaPreferencesRequest,
    ListQuotaPreferencesResponse,
    UpdateQuotaPreferenceRequest,
)
from .types.resources import (
    DimensionsInfo,
    QuotaConfig,
    QuotaDetails,
    QuotaIncreaseEligibility,
    QuotaInfo,
    QuotaPreference,
    QuotaSafetyCheck,
)

__all__ = (
    "CloudQuotasAsyncClient",
    "CloudQuotasClient",
    "CreateQuotaPreferenceRequest",
    "DimensionsInfo",
    "GetQuotaInfoRequest",
    "GetQuotaPreferenceRequest",
    "ListQuotaInfosRequest",
    "ListQuotaInfosResponse",
    "ListQuotaPreferencesRequest",
    "ListQuotaPreferencesResponse",
    "QuotaConfig",
    "QuotaDetails",
    "QuotaIncreaseEligibility",
    "QuotaInfo",
    "QuotaPreference",
    "QuotaSafetyCheck",
    "UpdateQuotaPreferenceRequest",
)
