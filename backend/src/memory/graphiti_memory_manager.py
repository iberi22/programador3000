"""
Graphiti Memory Manager for AI Agents

This module provides memory storage and retrieval using the graphiti-core library.
"""

import os
import logging
from typing import Optional, Dict, Any, List

from graphiti_core import Graphiti
from graphiti_core.llms import LLMProvider

logger = logging.getLogger(__name__)

class GraphitiMemoryManager:
    """
    Manages memory using the Graphiti-Core library, connecting directly to Neo4j.
    """

    def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_pass: str, llm_config: dict):
        self.graphiti_client = Graphiti(
            neo4j_uri=neo4j_uri,
            neo4j_user=neo4j_user,
            neo4j_password=neo4j_pass,
            llm_provider=LLMProvider.GOOGLE,
            llm_config=llm_config
        )
        logger.info("GraphitiMemoryManager initialized successfully.")

    async def initialize(self):
        """Placeholder for initialization logic. Currently not needed for Graphiti-Core."""
        pass

    async def close(self):
        """Placeholder for closing logic. Currently not needed for Graphiti-Core."""
        logger.info("GraphitiMemoryManager closed.")

    async def get_or_create_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Sessions are managed implicitly by Graphiti. This method confirms readiness."""
        return {"session_id": session_id, "status": "active"}

    async def add_memory(self, session_id: str, role: str, content: str) -> bool:
        """Add a memory to the knowledge graph for a given session."""
        try:
            # `arun` processes the input and stores the interaction in the graph.
            await self.graphiti_client.arun(human_input=content, session_id=session_id)
            logger.debug(f"Added memory to session {session_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to add memory to session {session_id}: {e}")
            return False

    async def search_memory(self, session_id: str, query: str, limit: int = 5) -> Optional[List[Dict[str, Any]]]:
        """Search for memories in the knowledge graph."""
        try:
            # `aquery` is used to ask questions against the graph.
            response = await self.graphiti_client.aquery(query, session_id=session_id)
            # Adapt the response to the expected format
            return [{"content": response}] if response else []
        except Exception as e:
            logger.error(f"Failed to search memory in session {session_id}: {e}")
            return None

# Global instance
_graphiti_memory_manager: Optional[GraphitiMemoryManager] = None

async def get_graphiti_memory_manager() -> Optional[GraphitiMemoryManager]:
    """Get the global Graphiti memory manager instance."""
    global _graphiti_memory_manager
    if _graphiti_memory_manager is None:
        neo4j_uri = os.getenv('NEO4J_URI')
        neo4j_user = os.getenv('NEO4J_USER')
        neo4j_pass = os.getenv('NEO4J_PASSWORD')
        google_api_key = os.getenv('GEMINI_API_KEY')

        if not all([neo4j_uri, neo4j_user, neo4j_pass, google_api_key]):
            logger.warning(
                "Graphiti not configured. Ensure NEO4J_URI, NEO4J_USER, "
                "NEO4J_PASSWORD, and GEMINI_API_KEY are set."
            )
            return None

        try:
            llm_config = {
                "api_key": google_api_key,
                "model_name": "gemini-1.5-flash-latest"
            }
            _graphiti_memory_manager = GraphitiMemoryManager(
                neo4j_uri=neo4j_uri,
                neo4j_user=neo4j_user,
                neo4j_pass=neo4j_pass,
                llm_config=llm_config
            )
            await _graphiti_memory_manager.initialize()
        except Exception as e:
            logger.error(f"Failed to initialize GraphitiMemoryManager: {e}")
            _graphiti_memory_manager = None
            return None
            
    return _graphiti_memory_manager

async def close_graphiti_memory_manager():
    """Close the global Graphiti memory manager instance."""
    global _graphiti_memory_manager
    if _graphiti_memory_manager:
        await _graphiti_memory_manager.close()
        _graphiti_memory_manager = None
