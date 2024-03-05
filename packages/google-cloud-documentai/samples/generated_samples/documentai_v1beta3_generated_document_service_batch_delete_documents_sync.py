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
# Snippet for BatchDeleteDocuments
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_v1beta3_generated_DocumentService_BatchDeleteDocuments_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import documentai_v1beta3


def sample_batch_delete_documents():
    # Create a client
    client = documentai_v1beta3.DocumentServiceClient()

    # Initialize request argument(s)
    dataset_documents = documentai_v1beta3.BatchDatasetDocuments()
    dataset_documents.individual_document_ids.document_ids.gcs_managed_doc_id.gcs_uri = "gcs_uri_value"

    request = documentai_v1beta3.BatchDeleteDocumentsRequest(
        dataset="dataset_value",
        dataset_documents=dataset_documents,
    )

    # Make the request
    operation = client.batch_delete_documents(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END documentai_v1beta3_generated_DocumentService_BatchDeleteDocuments_sync]
