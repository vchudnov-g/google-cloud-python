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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateQuotaPreference
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-quotas


# [START cloudquotas_v1_generated_CloudQuotas_UpdateQuotaPreference_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import cloudquotas_v1


async def sample_update_quota_preference():
    # Create a client
    client = cloudquotas_v1.CloudQuotasAsyncClient()

    # Initialize request argument(s)
    quota_preference = cloudquotas_v1.QuotaPreference()
    quota_preference.quota_config.preferred_value = 1595
    quota_preference.service = "service_value"
    quota_preference.quota_id = "quota_id_value"
    quota_preference.contact_email = "contact_email_value"

    request = cloudquotas_v1.UpdateQuotaPreferenceRequest(
        quota_preference=quota_preference,
    )

    # Make the request
    response = await client.update_quota_preference(request=request)

    # Handle the response
    print(response)

# [END cloudquotas_v1_generated_CloudQuotas_UpdateQuotaPreference_async]
