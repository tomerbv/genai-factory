# Copyright 2023 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum

from genai_factory.schemas.base import BaseWithVerMetadata

class DeploymentType(str, Enum):
    MODEL = "model"
    WORKFLOW = "workflow"
    KNOWLEDGE_BASE = "knowledge-base"
    AGENT = "agent"
    MCP_SERVER = "mcp-server"

class Deployment(BaseWithVerMetadata):
    _top_level_fields = ["is_remote", "type"]

    model_id: str
    workflow_id: str

    is_remote: bool
    type: DeploymentType
    type_kwargs: dict[str, str] = {}
    configuration: dict[str, str] = {}
    status: dict[str, str] = {}
    profile: dict[str, str] = {}


