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
from google.cloud.dialogflow_v2 import gapic_version as package_version

__version__ = package_version.__version__


from .services.agents import AgentsAsyncClient, AgentsClient
from .services.answer_records import AnswerRecordsAsyncClient, AnswerRecordsClient
from .services.contexts import ContextsAsyncClient, ContextsClient
from .services.conversation_datasets import (
    ConversationDatasetsAsyncClient,
    ConversationDatasetsClient,
)
from .services.conversation_models import (
    ConversationModelsAsyncClient,
    ConversationModelsClient,
)
from .services.conversation_profiles import (
    ConversationProfilesAsyncClient,
    ConversationProfilesClient,
)
from .services.conversations import ConversationsAsyncClient, ConversationsClient
from .services.documents import DocumentsAsyncClient, DocumentsClient
from .services.entity_types import EntityTypesAsyncClient, EntityTypesClient
from .services.environments import EnvironmentsAsyncClient, EnvironmentsClient
from .services.fulfillments import FulfillmentsAsyncClient, FulfillmentsClient
from .services.intents import IntentsAsyncClient, IntentsClient
from .services.knowledge_bases import KnowledgeBasesAsyncClient, KnowledgeBasesClient
from .services.participants import ParticipantsAsyncClient, ParticipantsClient
from .services.session_entity_types import (
    SessionEntityTypesAsyncClient,
    SessionEntityTypesClient,
)
from .services.sessions import SessionsAsyncClient, SessionsClient
from .services.versions import VersionsAsyncClient, VersionsClient
from .types.agent import (
    Agent,
    DeleteAgentRequest,
    ExportAgentRequest,
    ExportAgentResponse,
    GetAgentRequest,
    GetValidationResultRequest,
    ImportAgentRequest,
    RestoreAgentRequest,
    SearchAgentsRequest,
    SearchAgentsResponse,
    SetAgentRequest,
    TrainAgentRequest,
)
from .types.answer_record import (
    AgentAssistantFeedback,
    AgentAssistantRecord,
    AnswerFeedback,
    AnswerRecord,
    ListAnswerRecordsRequest,
    ListAnswerRecordsResponse,
    UpdateAnswerRecordRequest,
)
from .types.audio_config import (
    AudioEncoding,
    InputAudioConfig,
    OutputAudioConfig,
    OutputAudioEncoding,
    SpeechContext,
    SpeechModelVariant,
    SpeechToTextConfig,
    SpeechWordInfo,
    SsmlVoiceGender,
    SynthesizeSpeechConfig,
    TelephonyDtmf,
    TelephonyDtmfEvents,
    VoiceSelectionParams,
)
from .types.context import (
    Context,
    CreateContextRequest,
    DeleteAllContextsRequest,
    DeleteContextRequest,
    GetContextRequest,
    ListContextsRequest,
    ListContextsResponse,
    UpdateContextRequest,
)
from .types.conversation import (
    CompleteConversationRequest,
    Conversation,
    ConversationPhoneNumber,
    CreateConversationRequest,
    GenerateStatelessSummaryRequest,
    GenerateStatelessSummaryResponse,
    GetConversationRequest,
    ListConversationsRequest,
    ListConversationsResponse,
    ListMessagesRequest,
    ListMessagesResponse,
    SearchKnowledgeAnswer,
    SearchKnowledgeRequest,
    SearchKnowledgeResponse,
    SuggestConversationSummaryRequest,
    SuggestConversationSummaryResponse,
)
from .types.conversation_dataset import (
    ConversationDataset,
    ConversationInfo,
    CreateConversationDatasetOperationMetadata,
    CreateConversationDatasetRequest,
    DeleteConversationDatasetOperationMetadata,
    DeleteConversationDatasetRequest,
    GetConversationDatasetRequest,
    ImportConversationDataOperationMetadata,
    ImportConversationDataOperationResponse,
    ImportConversationDataRequest,
    InputConfig,
    ListConversationDatasetsRequest,
    ListConversationDatasetsResponse,
)
from .types.conversation_event import ConversationEvent
from .types.conversation_model import (
    ArticleSuggestionModelMetadata,
    ConversationModel,
    ConversationModelEvaluation,
    CreateConversationModelEvaluationOperationMetadata,
    CreateConversationModelEvaluationRequest,
    CreateConversationModelOperationMetadata,
    CreateConversationModelRequest,
    DeleteConversationModelOperationMetadata,
    DeleteConversationModelRequest,
    DeployConversationModelOperationMetadata,
    DeployConversationModelRequest,
    EvaluationConfig,
    GetConversationModelEvaluationRequest,
    GetConversationModelRequest,
    InputDataset,
    ListConversationModelEvaluationsRequest,
    ListConversationModelEvaluationsResponse,
    ListConversationModelsRequest,
    ListConversationModelsResponse,
    SmartReplyMetrics,
    SmartReplyModelMetadata,
    UndeployConversationModelOperationMetadata,
    UndeployConversationModelRequest,
)
from .types.conversation_profile import (
    AutomatedAgentConfig,
    ClearSuggestionFeatureConfigOperationMetadata,
    ClearSuggestionFeatureConfigRequest,
    ConversationProfile,
    CreateConversationProfileRequest,
    DeleteConversationProfileRequest,
    GetConversationProfileRequest,
    HumanAgentAssistantConfig,
    HumanAgentHandoffConfig,
    ListConversationProfilesRequest,
    ListConversationProfilesResponse,
    LoggingConfig,
    NotificationConfig,
    SetSuggestionFeatureConfigOperationMetadata,
    SetSuggestionFeatureConfigRequest,
    SuggestionFeature,
    UpdateConversationProfileRequest,
)
from .types.document import (
    CreateDocumentRequest,
    DeleteDocumentRequest,
    Document,
    ExportDocumentRequest,
    ExportOperationMetadata,
    GetDocumentRequest,
    ImportDocumentsRequest,
    ImportDocumentsResponse,
    ImportDocumentTemplate,
    KnowledgeOperationMetadata,
    ListDocumentsRequest,
    ListDocumentsResponse,
    ReloadDocumentRequest,
    UpdateDocumentRequest,
)
from .types.entity_type import (
    BatchCreateEntitiesRequest,
    BatchDeleteEntitiesRequest,
    BatchDeleteEntityTypesRequest,
    BatchUpdateEntitiesRequest,
    BatchUpdateEntityTypesRequest,
    BatchUpdateEntityTypesResponse,
    CreateEntityTypeRequest,
    DeleteEntityTypeRequest,
    EntityType,
    EntityTypeBatch,
    GetEntityTypeRequest,
    ListEntityTypesRequest,
    ListEntityTypesResponse,
    UpdateEntityTypeRequest,
)
from .types.environment import (
    CreateEnvironmentRequest,
    DeleteEnvironmentRequest,
    Environment,
    EnvironmentHistory,
    GetEnvironmentHistoryRequest,
    GetEnvironmentRequest,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    TextToSpeechSettings,
    UpdateEnvironmentRequest,
)
from .types.fulfillment import (
    Fulfillment,
    GetFulfillmentRequest,
    UpdateFulfillmentRequest,
)
from .types.gcs import GcsDestination, GcsSources
from .types.human_agent_assistant_event import HumanAgentAssistantEvent
from .types.intent import (
    BatchDeleteIntentsRequest,
    BatchUpdateIntentsRequest,
    BatchUpdateIntentsResponse,
    CreateIntentRequest,
    DeleteIntentRequest,
    GetIntentRequest,
    Intent,
    IntentBatch,
    IntentView,
    ListIntentsRequest,
    ListIntentsResponse,
    UpdateIntentRequest,
)
from .types.knowledge_base import (
    CreateKnowledgeBaseRequest,
    DeleteKnowledgeBaseRequest,
    GetKnowledgeBaseRequest,
    KnowledgeBase,
    ListKnowledgeBasesRequest,
    ListKnowledgeBasesResponse,
    UpdateKnowledgeBaseRequest,
)
from .types.participant import (
    AnalyzeContentRequest,
    AnalyzeContentResponse,
    AnnotatedMessagePart,
    ArticleAnswer,
    AssistQueryParameters,
    AutomatedAgentReply,
    CreateParticipantRequest,
    DialogflowAssistAnswer,
    DtmfParameters,
    FaqAnswer,
    GetParticipantRequest,
    InputTextConfig,
    IntentSuggestion,
    ListParticipantsRequest,
    ListParticipantsResponse,
    Message,
    MessageAnnotation,
    OutputAudio,
    Participant,
    SmartReplyAnswer,
    StreamingAnalyzeContentRequest,
    StreamingAnalyzeContentResponse,
    SuggestArticlesRequest,
    SuggestArticlesResponse,
    SuggestFaqAnswersRequest,
    SuggestFaqAnswersResponse,
    SuggestionInput,
    SuggestionResult,
    SuggestSmartRepliesRequest,
    SuggestSmartRepliesResponse,
    UpdateParticipantRequest,
)
from .types.session import (
    CloudConversationDebuggingInfo,
    DetectIntentRequest,
    DetectIntentResponse,
    EventInput,
    QueryInput,
    QueryParameters,
    QueryResult,
    Sentiment,
    SentimentAnalysisRequestConfig,
    SentimentAnalysisResult,
    StreamingDetectIntentRequest,
    StreamingDetectIntentResponse,
    StreamingRecognitionResult,
    TextInput,
)
from .types.session_entity_type import (
    CreateSessionEntityTypeRequest,
    DeleteSessionEntityTypeRequest,
    GetSessionEntityTypeRequest,
    ListSessionEntityTypesRequest,
    ListSessionEntityTypesResponse,
    SessionEntityType,
    UpdateSessionEntityTypeRequest,
)
from .types.validation_result import ValidationError, ValidationResult
from .types.version import (
    CreateVersionRequest,
    DeleteVersionRequest,
    GetVersionRequest,
    ListVersionsRequest,
    ListVersionsResponse,
    UpdateVersionRequest,
    Version,
)
from .types.webhook import OriginalDetectIntentRequest, WebhookRequest, WebhookResponse

__all__ = (
    "AgentsAsyncClient",
    "AnswerRecordsAsyncClient",
    "ContextsAsyncClient",
    "ConversationDatasetsAsyncClient",
    "ConversationModelsAsyncClient",
    "ConversationProfilesAsyncClient",
    "ConversationsAsyncClient",
    "DocumentsAsyncClient",
    "EntityTypesAsyncClient",
    "EnvironmentsAsyncClient",
    "FulfillmentsAsyncClient",
    "IntentsAsyncClient",
    "KnowledgeBasesAsyncClient",
    "ParticipantsAsyncClient",
    "SessionEntityTypesAsyncClient",
    "SessionsAsyncClient",
    "VersionsAsyncClient",
    "Agent",
    "AgentAssistantFeedback",
    "AgentAssistantRecord",
    "AgentsClient",
    "AnalyzeContentRequest",
    "AnalyzeContentResponse",
    "AnnotatedMessagePart",
    "AnswerFeedback",
    "AnswerRecord",
    "AnswerRecordsClient",
    "ArticleAnswer",
    "ArticleSuggestionModelMetadata",
    "AssistQueryParameters",
    "AudioEncoding",
    "AutomatedAgentConfig",
    "AutomatedAgentReply",
    "BatchCreateEntitiesRequest",
    "BatchDeleteEntitiesRequest",
    "BatchDeleteEntityTypesRequest",
    "BatchDeleteIntentsRequest",
    "BatchUpdateEntitiesRequest",
    "BatchUpdateEntityTypesRequest",
    "BatchUpdateEntityTypesResponse",
    "BatchUpdateIntentsRequest",
    "BatchUpdateIntentsResponse",
    "ClearSuggestionFeatureConfigOperationMetadata",
    "ClearSuggestionFeatureConfigRequest",
    "CloudConversationDebuggingInfo",
    "CompleteConversationRequest",
    "Context",
    "ContextsClient",
    "Conversation",
    "ConversationDataset",
    "ConversationDatasetsClient",
    "ConversationEvent",
    "ConversationInfo",
    "ConversationModel",
    "ConversationModelEvaluation",
    "ConversationModelsClient",
    "ConversationPhoneNumber",
    "ConversationProfile",
    "ConversationProfilesClient",
    "ConversationsClient",
    "CreateContextRequest",
    "CreateConversationDatasetOperationMetadata",
    "CreateConversationDatasetRequest",
    "CreateConversationModelEvaluationOperationMetadata",
    "CreateConversationModelEvaluationRequest",
    "CreateConversationModelOperationMetadata",
    "CreateConversationModelRequest",
    "CreateConversationProfileRequest",
    "CreateConversationRequest",
    "CreateDocumentRequest",
    "CreateEntityTypeRequest",
    "CreateEnvironmentRequest",
    "CreateIntentRequest",
    "CreateKnowledgeBaseRequest",
    "CreateParticipantRequest",
    "CreateSessionEntityTypeRequest",
    "CreateVersionRequest",
    "DeleteAgentRequest",
    "DeleteAllContextsRequest",
    "DeleteContextRequest",
    "DeleteConversationDatasetOperationMetadata",
    "DeleteConversationDatasetRequest",
    "DeleteConversationModelOperationMetadata",
    "DeleteConversationModelRequest",
    "DeleteConversationProfileRequest",
    "DeleteDocumentRequest",
    "DeleteEntityTypeRequest",
    "DeleteEnvironmentRequest",
    "DeleteIntentRequest",
    "DeleteKnowledgeBaseRequest",
    "DeleteSessionEntityTypeRequest",
    "DeleteVersionRequest",
    "DeployConversationModelOperationMetadata",
    "DeployConversationModelRequest",
    "DetectIntentRequest",
    "DetectIntentResponse",
    "DialogflowAssistAnswer",
    "Document",
    "DocumentsClient",
    "DtmfParameters",
    "EntityType",
    "EntityTypeBatch",
    "EntityTypesClient",
    "Environment",
    "EnvironmentHistory",
    "EnvironmentsClient",
    "EvaluationConfig",
    "EventInput",
    "ExportAgentRequest",
    "ExportAgentResponse",
    "ExportDocumentRequest",
    "ExportOperationMetadata",
    "FaqAnswer",
    "Fulfillment",
    "FulfillmentsClient",
    "GcsDestination",
    "GcsSources",
    "GenerateStatelessSummaryRequest",
    "GenerateStatelessSummaryResponse",
    "GetAgentRequest",
    "GetContextRequest",
    "GetConversationDatasetRequest",
    "GetConversationModelEvaluationRequest",
    "GetConversationModelRequest",
    "GetConversationProfileRequest",
    "GetConversationRequest",
    "GetDocumentRequest",
    "GetEntityTypeRequest",
    "GetEnvironmentHistoryRequest",
    "GetEnvironmentRequest",
    "GetFulfillmentRequest",
    "GetIntentRequest",
    "GetKnowledgeBaseRequest",
    "GetParticipantRequest",
    "GetSessionEntityTypeRequest",
    "GetValidationResultRequest",
    "GetVersionRequest",
    "HumanAgentAssistantConfig",
    "HumanAgentAssistantEvent",
    "HumanAgentHandoffConfig",
    "ImportAgentRequest",
    "ImportConversationDataOperationMetadata",
    "ImportConversationDataOperationResponse",
    "ImportConversationDataRequest",
    "ImportDocumentTemplate",
    "ImportDocumentsRequest",
    "ImportDocumentsResponse",
    "InputAudioConfig",
    "InputConfig",
    "InputDataset",
    "InputTextConfig",
    "Intent",
    "IntentBatch",
    "IntentSuggestion",
    "IntentView",
    "IntentsClient",
    "KnowledgeBase",
    "KnowledgeBasesClient",
    "KnowledgeOperationMetadata",
    "ListAnswerRecordsRequest",
    "ListAnswerRecordsResponse",
    "ListContextsRequest",
    "ListContextsResponse",
    "ListConversationDatasetsRequest",
    "ListConversationDatasetsResponse",
    "ListConversationModelEvaluationsRequest",
    "ListConversationModelEvaluationsResponse",
    "ListConversationModelsRequest",
    "ListConversationModelsResponse",
    "ListConversationProfilesRequest",
    "ListConversationProfilesResponse",
    "ListConversationsRequest",
    "ListConversationsResponse",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListEntityTypesRequest",
    "ListEntityTypesResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListIntentsRequest",
    "ListIntentsResponse",
    "ListKnowledgeBasesRequest",
    "ListKnowledgeBasesResponse",
    "ListMessagesRequest",
    "ListMessagesResponse",
    "ListParticipantsRequest",
    "ListParticipantsResponse",
    "ListSessionEntityTypesRequest",
    "ListSessionEntityTypesResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "LoggingConfig",
    "Message",
    "MessageAnnotation",
    "NotificationConfig",
    "OriginalDetectIntentRequest",
    "OutputAudio",
    "OutputAudioConfig",
    "OutputAudioEncoding",
    "Participant",
    "ParticipantsClient",
    "QueryInput",
    "QueryParameters",
    "QueryResult",
    "ReloadDocumentRequest",
    "RestoreAgentRequest",
    "SearchAgentsRequest",
    "SearchAgentsResponse",
    "SearchKnowledgeAnswer",
    "SearchKnowledgeRequest",
    "SearchKnowledgeResponse",
    "Sentiment",
    "SentimentAnalysisRequestConfig",
    "SentimentAnalysisResult",
    "SessionEntityType",
    "SessionEntityTypesClient",
    "SessionsClient",
    "SetAgentRequest",
    "SetSuggestionFeatureConfigOperationMetadata",
    "SetSuggestionFeatureConfigRequest",
    "SmartReplyAnswer",
    "SmartReplyMetrics",
    "SmartReplyModelMetadata",
    "SpeechContext",
    "SpeechModelVariant",
    "SpeechToTextConfig",
    "SpeechWordInfo",
    "SsmlVoiceGender",
    "StreamingAnalyzeContentRequest",
    "StreamingAnalyzeContentResponse",
    "StreamingDetectIntentRequest",
    "StreamingDetectIntentResponse",
    "StreamingRecognitionResult",
    "SuggestArticlesRequest",
    "SuggestArticlesResponse",
    "SuggestConversationSummaryRequest",
    "SuggestConversationSummaryResponse",
    "SuggestFaqAnswersRequest",
    "SuggestFaqAnswersResponse",
    "SuggestSmartRepliesRequest",
    "SuggestSmartRepliesResponse",
    "SuggestionFeature",
    "SuggestionInput",
    "SuggestionResult",
    "SynthesizeSpeechConfig",
    "TelephonyDtmf",
    "TelephonyDtmfEvents",
    "TextInput",
    "TextToSpeechSettings",
    "TrainAgentRequest",
    "UndeployConversationModelOperationMetadata",
    "UndeployConversationModelRequest",
    "UpdateAnswerRecordRequest",
    "UpdateContextRequest",
    "UpdateConversationProfileRequest",
    "UpdateDocumentRequest",
    "UpdateEntityTypeRequest",
    "UpdateEnvironmentRequest",
    "UpdateFulfillmentRequest",
    "UpdateIntentRequest",
    "UpdateKnowledgeBaseRequest",
    "UpdateParticipantRequest",
    "UpdateSessionEntityTypeRequest",
    "UpdateVersionRequest",
    "ValidationError",
    "ValidationResult",
    "Version",
    "VersionsClient",
    "VoiceSelectionParams",
    "WebhookRequest",
    "WebhookResponse",
)
