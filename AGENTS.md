# AI Agent Assistant - Agent Overview

This document provides an overview of the specialized AI agents within the AI Agent Assistant system, their roles, and their integration into the overall architecture.

## 🤖 Agent Specialization System

The system features a 6-graph specialization architecture, enabling comprehensive project management and intelligent task execution through a multi-agent orchestration approach.

### Core Agents

- **📖 Jules (Documentation & Best Practices Agent)**
  - **Role**: Understands the project's architecture, tools, and conventions by reading documentation. It ensures that all development work aligns with the established guidelines.
  - **Integration**: Consumes `AGENTS.md`, `PLANNING.md`, `TASK.md`, `README.md`, and `gemini.md` to gain context.
  - **Workflow**: Before executing a task, Jules reviews the relevant documentation to formulate a plan that is consistent with the project's standards.

- **🔍 Research Specialist**
  - **Role**: Advanced web research, multi-source validation, and citation management.
  - **Integration**: Utilizes the Google Search API and integrates with the system's memory for long-term knowledge retention.
  - **Workflow**: Generates initial search queries, performs web research, and refines searches iteratively.

- **💻 Code Engineer**
  - **Role**: Code generation, review, testing, debugging, and technical documentation.
  - **Integration**: Can be triggered automatically upon repository import from GitHub to improve newly created projects.
  - **Workflow**: Analyzes codebase, identifies areas for improvement, and implements code changes.

- **📋 Project Manager**
  - **Role**: Project planning, resource allocation, timeline management, and risk assessment.
  - **Integration**: Manages project-related tasks, milestones, and overall project status.
  - **Workflow**: Oversees the project lifecycle, coordinates agent activities, and provides real-time updates.

- **🛡️ QA Specialist**
  - **Role**: Quality assurance, security testing, performance optimization, and compliance validation.
  - **Integration**: Ensures the quality and reliability of the system's outputs and code.
  - **Workflow**: Conducts various tests, identifies vulnerabilities, and suggests optimizations.

- **🎛️ Coordinator Agent**
  - **Role**: Intelligent task orchestration and inter-agent communication.
  - **Integration**: Facilitates seamless collaboration between different specialized agents.
  - **Workflow**: Selects appropriate agents for specific tasks, decomposes complex tasks, and distributes them among agents.

- **📈 Real-time Monitoring Agent**
  - **Role**: Provides complete observability with performance metrics and health monitoring of all agents and system components.
  - **Integration**: Collects and displays real-time data on agent status, execution, and system health.
  - **Workflow**: Continuously monitors the system, generates reports, and alerts on anomalies.

## 📚 Project Context & Rules

This section provides links to essential project documentation that all agents and contributors must follow.

- **[Project Planning (PLANNING.md)](./PLANNING.md)**: High-level architecture, project goals, and strategic planning.
- **[Task Management (TASK.md)](./TASK.md)**: Detailed list of current, pending, and completed tasks.
- **[Project Overview (README.md)](./README.md)**: General information, setup instructions, and feature overview.
- **[Coding & Style Guide (gemini.md)](./gemini.md)**: **CRITICAL READ**. Contains the rules, conventions, and best practices for writing code in this project. All code contributions must adhere to this guide.

## Agent Workflow and Orchestration

The agents operate within a LangGraph-based orchestration layer, allowing for dynamic task routing, state persistence, and agent lifecycle management. The system supports both single-agent and multi-agent modes, with seamless dynamic switching.

### Key Orchestration Principles

- **LangGraph Orchestration Layer**: Central workflow management, state persistence and recovery, and agent lifecycle management.
- **Multi-LLM Manager**: Supports multiple LLM providers (Google Gemini, OpenAI GPT, Anthropic Claude) with fallback mechanisms and cost optimization.
- **Agent Router & Dispatcher**: Intelligent agent selection, task decomposition and distribution, and load balancing.
- **Tool Ecosystem**: Comprehensive set of tools for web research, code execution, file operations, and project management, including a production-ready MCP (Model Context Protocol) Server Management System.

## Integration and Features

- **Firebase Auth Integration**: Complete SSO with GitHub OAuth for secure authentication and repository access.
- **GitHub Project Management**: Enables repository import, analysis, and automated project planning by the Code Engineer agent.
- **Real-time Updates**: Live agent status, progress tracking, and notification system through a professional UI/UX.
- **Memory System**: Utilizes PostgreSQL for long-term memory (vector support) and Redis for short-term memory and real-time pub/sub.

This multi-agent system is designed for robust, autonomous operation, providing a powerful platform for AI-driven software project management.
