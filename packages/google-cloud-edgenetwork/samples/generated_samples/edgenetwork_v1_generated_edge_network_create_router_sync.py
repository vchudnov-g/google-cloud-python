# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
# Snippet for CreateRouter
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-edgenetwork


# [START edgenetwork_v1_generated_EdgeNetwork_CreateRouter_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import edgenetwork_v1


def sample_create_router():
    # Create a client
    client = edgenetwork_v1.EdgeNetworkClient()

    # Initialize request argument(s)
    router = edgenetwork_v1.Router()
    router.name = "name_value"
    router.network = "network_value"

    request = edgenetwork_v1.CreateRouterRequest(
        parent="parent_value",
        router_id="router_id_value",
        router=router,
    )

    # Make the request
    operation = client.create_router(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END edgenetwork_v1_generated_EdgeNetwork_CreateRouter_sync]
