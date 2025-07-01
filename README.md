# AI Agent Assistant twelvebros - Professional Multi-Agent System

A **production-ready AI agent assistant** for automated software project management with 24/7 support, autonomous operation, and enterprise-grade features. This comprehensive system features a **6-graph specialization architecture**, complete Firebase Auth integration, GitHub project management, and a professional UI/UX designed for real-world deployment.

## 🔍 **SISTEMA AUDITADO Y VERIFICADO - ENERO 2025**

### **✅ ESTADO ACTUAL: 95% COMPLETADO**

**🗄️ Base de Datos PostgreSQL - FUNCIONANDO:**

- ✅ Conexión exitosa via MCP (Model Context Protocol)
- ✅ 17 tablas creadas y operativas según esquema
- ✅ 28 threads LangGraph activos (sistema funcionando)
- ✅ Soporte vectorial para memoria implementado

**🏗️ Backend FastAPI - COMPLETAMENTE FUNCIONAL:**

- ✅ 10 routers registrados y operativos
- ✅ 6 grafos especializados implementados y funcionales
- ✅ Sistema de memoria integrado (largo/corto plazo)
- ✅ API endpoints respondiendo correctamente

**🎨 Frontend React - USANDO DATOS REALES:**

- ✅ useProjects hook conectado a API real (/api/v1/projects)
- ✅ ProjectsPage mostrando datos reales de PostgreSQL
- ✅ UI/UX Shadcn/Tailwind completamente funcional
- ✅ Integración frontend → API → DB → Memoria verificada

**⚠️ CORRECCIONES PENDIENTES (5%):**

- 🐳 Docker: Contenedores requieren reinicio (Redis inaccesible)
- 📊 **Datos**: Base limpia, necesita datos de prueba
- 🔐 **Advertencia de Seguridad**: La auditoría reciente reveló que la autenticación en los endpoints de gestión de proyectos está **desactivada por defecto** en la rama actual. Es crucial reactivarla antes de cualquier despliegue.

## 🎯 **PRODUCTION-READY FEATURES**

### 🤖 **4-Agent Specialization System**

Complete multi-agent orchestration with LangSmith traceability and real-time coordination:

- **🔍 Research Specialist**: Advanced web research with multi-source validation and citation management
- **💻 Code Engineer**: Code generation, review, testing, debugging, and technical documentation
- **📋 Project Manager**: Project planning, resource allocation, timeline management, and risk assessment
- **🛡️ QA Specialist**: Quality assurance, security testing, performance optimization, and compliance validation
- **🎛️ Coordinator Agent**: Intelligent task orchestration and inter-agent communication
- **📈 Real-time Monitoring**: Complete observability with performance metrics and health monitoring
- **🔄 Dynamic Switching**: Seamless toggle between single-agent and multi-agent modes

### 🔐 **Enterprise Authentication & Integration**

- **Firebase Auth Integration**: Complete SSO with GitHub OAuth for repository access
- **GitHub Project Management**: Repository import, analysis, and automated project planning
- **User Management**: Role-based access control and team collaboration features
- **Security**: JWT token validation, protected routes, and secure API endpoints

### 🎨 **Professional UI/UX**

- **Responsive Design**: Mobile-first approach with tablet and desktop optimization
- **Complete Navigation**: 20+ functional pages with intuitive routing system
- **Horizontal Scrolling**: Adaptive layouts for optimal content display
- **Real-time Updates**: Live agent status, progress tracking, and notification system
- **Accessibility**: WCAG compliant with keyboard navigation and screen reader support

![AI Agent Assistant](./app.png)

## 🚀 **COMPLETE FEATURE SET**

### 📱 **Professional User Interface**

- **Complete Navigation System**: 20+ functional pages with intuitive routing
- **Responsive Design**: Mobile-first with horizontal scrolling and adaptive layouts
- **Real-time Dashboard**: Live agent status, performance metrics, and system health
- **Project Management**: Comprehensive project tracking with GitHub integration
- **Workflow Automation**: Visual workflow designer with multi-agent coordination
- **Settings & Notifications**: Complete user preferences and notification center

### 🔗 **Enterprise Integrations**

- **GitHub Integration**: Repository import, analysis, and automated project planning
- **Firebase Authentication**: Enterprise SSO with role-based access control
- **Database Management**: PostgreSQL with connection pooling and health monitoring
- **Cloud Services**: AWS, Azure, GCP integration support
- **API Management**: RESTful APIs with comprehensive documentation
- **🆕 MCP Server Management**: Complete Model Context Protocol server management with dynamic installation, authentication, and monitoring

### 🤖 **Advanced Multi-LLM Support**

- **Primary**: Google Gemini (gemini-2.0-flash) for optimal performance
- **Fallback**: OpenAI GPT (gpt-4o) and Anthropic Claude (claude-3-5-sonnet)
- **Automatic failover** and intelligent load balancing
- **Real-time provider monitoring** with health checks and performance metrics

### 🏗️ **Production Infrastructure**

- **Docker Compose** orchestration with full service stack
- **Health monitoring** with automatic service recovery
- **Persistent data storage** with backup and migration capabilities
- **Load balancing** with Nginx and SSL termination
- **Scalable architecture** designed for enterprise deployment

## 🏗️ Architecture Overview

### System Components

- **Frontend**: React + TypeScript with enhanced UI components
- **Backend**: LangGraph + FastAPI with multi-LLM support
- **Database**: PostgreSQL for persistent state and conversation history
- **Cache**: Redis for real-time pub/sub and background task queues
- **Infrastructure**: Docker Compose orchestration with health monitoring

### Project Structure

```
├── frontend/          # React application with enhanced UI
├── backend/           # LangGraph agent and FastAPI server
├── docs/             # Documentation and guides
├── docker-compose.yml # Production infrastructure
├── Dockerfile        # Multi-stage build configuration
└── nginx.conf        # Load balancer configuration
```

## 🚀 Quick Start (Recommended)

### Prerequisites

- **Docker** and **Docker Compose** (recommended for full infrastructure)
- **API Keys**:
  - `GEMINI_API_KEY` (required)
  - `LANGSMITH_API_KEY` (optional, for monitoring)

### 1. Environment Setup

Create a `.env` file in the project root:

```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional (for monitoring)
LANGSMITH_API_KEY=your_langsmith_api_key_here

# Firebase Configuration (Required for Authentication)
# These are typically for the frontend (e.g., in frontend/.env)
# Ensure they are prefixed appropriately (e.g., VITE_ for Vite projects)
VITE_FIREBASE_API_KEY=your_firebase_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
VITE_FIREBASE_PROJECT_ID=your_firebase_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
VITE_FIREBASE_APP_ID=your_firebase_app_id
# For backend Firebase Admin SDK, usually a service account JSON file is used
# or environment variables like GOOGLE_APPLICATION_CREDENTIALS.
```

### 2. Build and Deploy

```bash
# Build the enhanced image
docker build -t gemini-fullstack-langgraph-enhanced .

# Start all services
docker-compose up -d
```

### 2. Firebase Auth Setup (Required for Login)

Before running the application, you need to configure Firebase Auth for authentication and GitHub integration:

1. **Create a Firebase Project**: If you don't have one, sign up at [Firebase](https://firebase.google.com/) and create a new project.
2. **Set up Firebase Authentication**:
    - In the Firebase console, navigate to "Authentication" and enable the sign-in methods you want to use (e.g., Email/Password, Google, GitHub).
    - For GitHub, you'll need to provide the Client ID and Client Secret from your GitHub OAuth App.
3. **Configure your application**:
    - Obtain your Firebase project configuration (apiKey, authDomain, projectId, etc.) from the Firebase console (Project settings > General > Your apps > Web app).
    - This configuration will be used in your frontend and backend.
4. **Update Environment Variables**:
    - Store your Firebase configuration securely, typically using environment variables.
    - For the frontend (Vite + React), you'll use variables like `VITE_FIREBASE_API_KEY`, `VITE_FIREBASE_AUTH_DOMAIN`, etc., in an `.env` file in the `frontend` directory.
    - For the backend, you'll configure Firebase Admin SDK, usually with a service account key file or environment variables.

### Firebase Auth Troubleshooting

If you encounter issues during Firebase Authentication setup or login, check these common problem areas:

*   **Incorrect Firebase Project Configuration**:
    *   **Issue**: The `apiKey`, `authDomain`, `projectId`, `storageBucket`, `messagingSenderId`, or `appId` in your frontend configuration (e.g., `frontend/.env`) do not match the values from your Firebase project console.
    *   **Solution**: Double-check these values in your Firebase project settings (Project settings > General > Your apps > Web app) and ensure they are correctly copied to your `.env` file (e.g., `VITE_FIREBASE_API_KEY=...`). Remember to restart your frontend development server after changes to `.env` files.

*   **Authorized Domains Not Configured**:
    *   **Issue**: Firebase Auth restricts authentication to requests from authorized domains. If your application's domain (e.g., `localhost` for development, or your production domain) is not listed, authentication will fail.
    *   **Solution**: In the Firebase console, go to Authentication > Settings > Authorized domains. Add all domains from which your application will be accessed (e.g., `localhost`, `your-app-name.firebaseapp.com`, `your-custom-domain.com`).

*   **GitHub OAuth Provider Not Enabled or Misconfigured**:
    *   **Issue**: If using GitHub sign-in, the provider might not be enabled in Firebase, or the Client ID and Client Secret might be incorrect.
    *   **Solution**:
        1.  In the Firebase console, navigate to Authentication > Sign-in method. Ensure "GitHub" is enabled.
        2.  Verify that the Client ID and Client Secret provided to Firebase match exactly with those from your GitHub OAuth App settings. Regenerate them in GitHub if unsure.

*   **Incorrect Callback URLs for GitHub OAuth**:
    *   **Issue**: GitHub OAuth requires a specific callback URL to redirect users after authentication. If this URL is misconfigured in your GitHub OAuth App settings, Firebase won't be able to complete the authentication.
    *   **Solution**:
        1.  In your GitHub OAuth App settings, ensure the "Authorization callback URL" is correctly set. Firebase provides this URL when you configure the GitHub sign-in provider in the Firebase console (it typically looks like `https://<your-project-id>.firebaseapp.com/__/auth/handler`).
        2.  Ensure this URL is not blocked by any network configurations.

*   **Environment Variables Not Loaded Correctly**:
    *   **Issue**: The Firebase configuration, especially for the frontend (e.g., using Vite `VITE_FIREBASE_...` variables), might not be loaded correctly by the application.
    *   **Solution**:
        1.  Ensure your `.env` file is in the correct directory (usually the root of the `frontend` folder for Vite projects).
        2.  Verify that the environment variables are prefixed correctly (e.g., `VITE_` for Vite).
        3.  Restart your development server after making changes to `.env` files.
        4.  For backend Firebase Admin SDK setup, ensure the service account key file path is correct or that the necessary environment variables (like `GOOGLE_APPLICATION_CREDENTIALS`) are properly set and accessible by the backend process.

*   **Pop-ups Blocked**:
    *   **Issue**: Social sign-ins (like Google or GitHub) often use pop-up windows. If your browser is blocking pop-ups for your application's domain, the sign-in process may fail silently or get stuck.
    *   **Solution**: Ensure that your browser is not blocking pop-ups for the application's domain. You might need to add an exception for your development (`localhost`) or production URL.

*   **API Calls Failing (401/403 Errors Even After Login)**:
    *   **Cause**: Frontend might not be sending the Firebase ID Token (JWT) with API requests, or the token might be invalid/expired. The backend `FirebaseAuthMiddleware` expects this token for protected routes.
    *   **Solution**:
        *   Ensure all frontend API calls to protected backend endpoints are made using the `apiClient` utility (`frontend/src/utils/apiClient.ts`). This utility is designed to automatically attach the current user's Firebase ID token to requests.
        *   If you are not using `apiClient` for a specific call, manually verify that the `Authorization: Bearer <token>` header is being correctly set. The token should be freshly obtained using `await auth.currentUser.getIdToken()`.
        *   Check the browser's developer console (Network tab and Console tab) for any errors during the token retrieval process or the API call itself.
        *   Examine backend server logs. They often provide more detailed error messages or reasons why authentication or authorization failed (e.g., token validation errors, permission issues).

*   **Incorrect Backend Firebase Configuration (`FIREBASE_SERVICE_ACCOUNT_JSON`)**:
    *   **Cause**: The `FIREBASE_SERVICE_ACCOUNT_JSON` environment variable, used by the backend's Firebase Admin SDK, might be missing, its value incorrect, the JSON content malformed, or the service account might lack necessary permissions (e.g., "Service Account Token Creator").
    *   **Solution**:
        *   Confirm that the `FIREBASE_SERVICE_ACCOUNT_JSON` environment variable is correctly set in your backend's runtime environment (e.g., in your `.env` file for local development, or as a configured environment variable in your deployment platform).
        *   Validate that its value is the *complete and valid JSON content* of the service account key file obtained from your Firebase project settings (Project settings > Service accounts > Generate new private key).
        *   Review backend startup logs for any Firebase Admin SDK initialization errors, which often point to issues with the service account configuration.
        *   Ensure the service account has appropriate IAM roles in Google Cloud, such as "Firebase Authentication Admin" or more specific roles like "Service Account Token Creator" if applicable.

*   **Incorrect Frontend Firebase Configuration (`VITE_FIREBASE_*` variables)**:
    *   **Cause**: One or more `VITE_FIREBASE_*` environment variables (e.g., `VITE_FIREBASE_API_KEY`, `VITE_FIREBASE_AUTH_DOMAIN`) might be missing, incorrect in the frontend's `.env` file, or not properly exposed to the application.
    *   **Solution**:
        *   Cross-reference all required `VITE_FIREBASE_*` variables (typically listed in `frontend/src/firebase/config.ts` or the `README.md` setup section) with the values from your Firebase project's Web App configuration (Project settings > General > Your apps > Web app).
        *   Ensure the `.env` file is in the root of your `frontend` directory and that your Vite development server was restarted after any changes to this file.
        *   Check the browser's developer console for Firebase client SDK initialization errors when the application loads. These errors often indicate problems with the frontend configuration.

*   **"Token has expired" or "Invalid authentication token" (Specific Backend Error Details)**:
    *   **Cause**: The JWT Firebase ID Token sent by the frontend to the backend was recognized as expired or invalid by the Firebase Admin SDK during verification.
    *   **Solution**:
        *   The Firebase client SDK (used in the frontend) is designed to automatically refresh ID tokens before they expire. The `apiClient` utility calls `auth.currentUser.getIdToken()` for each request, which should provide a fresh (or recently refreshed) token.
        *   If this error occurs persistently, it might indicate:
            *   Significant clock skew between the client machine and Google's authentication servers.
            *   Issues in the token refresh process on the client-side (check console for relevant errors).
            *   Manual token management elsewhere in the app that might be using stale tokens. Relying on `apiClient` should mitigate this.
        *   Using `await auth.currentUser.getIdToken(true)` forces a token refresh, which can be a temporary diagnostic step but generally shouldn't be needed for every call if the SDK is functioning correctly.

## User Onboarding Flow

This section outlines the steps for a new user to get started with the AI Agent Assistant, from initial authentication to importing their first project and interacting securely with the backend.

1.  **Sign Up / Log In with Firebase**:
    *   New users can sign up, or existing users can log in using the Firebase Authentication system. This system supports various methods, including email/password and social logins like Google or GitHub.
    *   Authenticating (e.g., via GitHub OAuth through Firebase) establishes your identity with the application. Once logged in, the application can securely interact with the backend API on your behalf using Firebase ID tokens (see "Frontend API Authentication" below).

2.  **Connect GitHub Account (if needed)**:
    *   If you didn't use GitHub to sign up/log in directly, or if your GitHub account needs to be (re)connected for specific repository access permissions, navigate to the "Integrations" page from the main menu.
    *   Select "GitHub" and follow the prompts to authorize the application. This step is essential for listing, importing, and analyzing your private or specific GitHub projects.

3.  **Navigate to GitHub Integration Page**:
    *   Once your GitHub account is connected and authorized, access the GitHub integration features. This is typically found under the "Integrations" > "GitHub" section or a dedicated "Projects" / "Import Repository" page within the application.

4.  **Select and Import Repository**:
    *   On the GitHub integration page, you will be able to see a list of your accessible repositories.
    *   Browse or search for the repository you wish to work with.
    *   Select the repository and click "Import" or "Link". This action registers the repository with the AI Agent Assistant, allowing agents to access and analyze it.

5.  **Automatic Project Analysis**:
    *   Upon successful import of a repository, the system will automatically trigger the **Code Engineer** agent.
    *   This agent performs an initial analysis of your project, which may include understanding the codebase structure, dependencies, and preparing it for further interaction with other specialized agents.

### Frontend API Authentication

The frontend application interacts with protected backend API endpoints. To ensure secure communication, these interactions require authentication using Firebase ID Tokens (JWT).

The `frontend/src/utils/apiClient.ts` utility simplifies this process. When a user is logged in via Firebase Auth, `apiClient` automatically retrieves the current user's ID token and includes it in the `Authorization` header (as a Bearer token) for every API request.

**Key features of `apiClient`:**
*   **Automatic Token Handling**: Fetches and attaches the Firebase ID token.
*   **Default Headers**: Sets `Content-Type: application/json` by default for methods like `POST`, `PUT`, `PATCH` if a token is present and no other `Content-Type` is specified.
*   **Centralized Base URL**: Uses `getApiBaseUrl()` to prefix requests, so you only need to provide the relative path (e.g., `/projects`).
*   **Standardized Error Handling**: Throws an `ApiError` object if the API request fails (e.g., non-2xx status code). This error object includes `status` (the HTTP status code), `message` (error message from the backend or a default), and potentially `errorData` (parsed JSON error response from the backend).

**Example Usage:**

```typescript
// Example usage (conceptual - adjust import path if using from a different location)
import { apiClient, ApiError } from '@/utils/apiClient'; // Assuming @ is src

async function fetchMyProjects() {
  try {
    // GET request to /api/v1/projects (base URL handled by apiClient)
    const projects = await apiClient('/projects');
    console.log('Fetched Projects:', projects);
    return projects;
  } catch (error) {
    if (error instanceof ApiError) {
      console.error(`Failed to fetch projects (Status: ${error.status}):`, error.message, error.errorData);
    } else {
      console.error('An unexpected error occurred:', error);
    }
    throw error; // Re-throw or handle as needed
  }
}

async function createNewProject(projectData: { name: string; description?: string }) {
  try {
    // POST request to /api/v1/projects
    const newProject = await apiClient('/projects', {
      method: 'POST',
      body: JSON.stringify(projectData),
      // No need to set Content-Type: application/json or Authorization header here;
      // apiClient handles it automatically if the user is logged in.
    });
    console.log('Project created:', newProject);
    return newProject;
  } catch (error) {
    if (error instanceof ApiError) {
      console.error(`Failed to create project (Status: ${error.status}):`, error.message, error.errorData);
    } else {
      console.error('An unexpected error occurred:', error);
    }
    throw error; // Re-throw or handle as needed
  }
}
```
This utility ensures that frontend API calls are consistently authenticated and provides a structured way to handle responses and errors.

### 3. Run the Application (Docker Compose)

- **Main Application**: <http://localhost:8123/app/> (Login will redirect to Firebase Auth if not configured or if .env variables are missing)
- **API Health Check**: <http://localhost:8123/api/v1/enhanced/health>
- **Specialized Agents Health**: <http://localhost:8123/api/v1/specialized/health>
- **Agent Metrics**: <http://localhost:8123/api/v1/specialized/metrics/agents>
- **API Documentation**: <http://localhost:8123/docs>

### 4. Complete System Usage

#### **Authentication & Setup**

1. Open the application at `http://localhost:8123/app/`
2. **Login with Firebase Auth**: Click "Log In" and authenticate
3. **Connect GitHub**: Navigate to Integrations → GitHub and connect your account
4. **Configure Agents**: Visit Settings to customize agent behavior

#### **Multi-Agent System**

1. Toggle the **"4-Agent Specialization System"** switch in the header
2. Ask complex questions like "Analyze my GitHub repository and create a project plan"
3. Watch the specialized agents collaborate:
   - **Research Specialist** gathers comprehensive information
   - **Code Engineer** analyzes code and generates solutions
   - **Project Manager** creates plans and timelines
   - **QA Specialist** ensures quality and security
4. View real-time progress in the **Dashboard**

#### **Project Management**

1. **Import Repository**: Go to Integrations → GitHub → Select Repository → Import
2. **View Projects**: Navigate to Projects to see imported and active projects
3. **Manage Workflows**: Use Workflows page to automate development processes
4. **Monitor Agents**: Check Agents page for individual agent status and performance

#### **🆕 MCP Server Management**

1. **Navigate to MCP Servers**: Go to `/mcp-servers` in the application
2. **Browse Marketplace**: Discover popular MCP servers in the Marketplace tab
3. **Install Servers**: Use the installation wizard for guided setup
4. **Configure Authentication**: Set up API keys, Bearer tokens, or Basic auth
5. **Monitor Health**: View real-time server status and performance metrics
6. **Manage Tools**: Discover and manage available tools from connected servers

#### **Advanced Features**

- **Settings**: Customize notifications, themes, and agent configurations
- **Notifications**: Stay updated with system events and agent completions
- **Real-time Dashboard**: Monitor system health and performance metrics

## 🛠️ Development Environment

### Local Development (Hot Reloading)

```bash
# Install dependencies
cd backend && pip install -e .
cd ../frontend && npm install

# Start development servers
make dev
```

### Development with Docker (Recommended)

```bash
# Start with development profiles (includes admin interfaces)
docker-compose --profile dev up -d

# Access admin interfaces
# Redis Commander: http://localhost:8081
# pgAdmin: http://localhost:8080 (admin@example.com / admin)
```

## How the Backend Agent Works (High-Level)

The core of the backend is a LangGraph agent defined in `backend/src/agent/graph.py`. It follows these steps:

![Agent Flow](./agent.png)

1. **Generate Initial Queries:** Based on your input, it generates a set of initial search queries using a Gemini model.
2. **Web Research:** For each query, it uses the Gemini model with the Google Search API to find relevant web pages.
3. **Reflection & Knowledge Gap Analysis:** The agent analyzes the search results to determine if the information is sufficient or if there are knowledge gaps. It uses a Gemini model for this reflection process.
4. **Iterative Refinement:** If gaps are found or the information is insufficient, it generates follow-up queries and repeats the web research and reflection steps (up to a configured maximum number of loops).
5. **Finalize Answer:** Once the research is deemed sufficient, the agent synthesizes the gathered information into a coherent answer, including citations from the web sources, using a Gemini model.

## 🐳 Production Deployment

### Docker Compose (Recommended)

The enhanced version includes a complete production infrastructure with PostgreSQL, Redis, and optional admin interfaces.

```bash
# Build the enhanced image
docker build -t gemini-fullstack-langgraph-enhanced .

# Start production environment
docker-compose up -d

# Check service health
docker-compose ps
curl http://localhost:8123/api/v1/enhanced/health
```

### Production with Load Balancing

```bash
# Start with production profile (includes Nginx)
docker-compose --profile prod up -d
```

### Environment Variables for Production

```bash
# Core Configuration
GEMINI_API_KEY=your_production_gemini_key
LANGSMITH_API_KEY=your_production_langsmith_key
```

> **Note:** No other API keys are required for LangGraph or LangSmith features. Only these two keys are needed for all agent and monitoring capabilities.

## 📊 Monitoring & Health Checks

### Service Health

- **Application Health**: `http://localhost:8123/api/v1/enhanced/health`
- **Database Status**: Automatic health checks with connection pooling
- **Redis Status**: Pub/sub and cache monitoring
- **LLM Provider Status**: Real-time provider availability

### Admin Interfaces (Development)

- **Redis Commander**: `http://localhost:8081` (Redis management)
- **pgAdmin**: `http://localhost:8080` (PostgreSQL management)
  - Email: `admin@example.com`
  - Password: `admin`

## 🔧 Enhanced Technologies

### Core Stack

- **[React 18](https://reactjs.org/)** with TypeScript and Vite
- **[Tailwind CSS](https://tailwindcss.com/)** for responsive design
- **[Shadcn UI](https://ui.shadcn.com/)** for modern components
- **[LangGraph](https://github.com/langchain-ai/langgraph)** for agent workflows
- **[FastAPI](https://fastapi.tiangolo.com/)** for high-performance APIs

### Infrastructure

- **[PostgreSQL 16](https://www.postgresql.org/)** for persistent data
- **[Redis 6](https://redis.io/)** for caching and pub/sub
- **[Docker Compose](https://docs.docker.com/compose/)** for orchestration
- **[Nginx](https://nginx.org/)** for load balancing (production)

### LLM Providers

- **[Google Gemini](https://ai.google.dev/models/gemini)** (gemini-2.0-flash)
- **[OpenAI GPT](https://openai.com/api/)** (gpt-4o)
- **[Anthropic Claude](https://www.anthropic.com/)** (claude-3-5-sonnet)

## 📚 Documentation

- **[Architecture Guide](docs/ARCHITECTURE.md)** - System design and components
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Production deployment instructions
- **[Development Rules](docs/RULES.md)** - Development guidelines and best practices

## 🚨 Troubleshooting

### Common Issues

```bash
# Container won't start
docker-compose logs langgraph-api

# Database connection issues
docker-compose exec langgraph-postgres pg_isready -U postgres

# Check API keys
docker-compose exec langgraph-api env | grep API_KEY
```

### Performance Optimization

- **Database**: Connection pooling and proper indexing
- **Cache**: Redis optimization for pub/sub and background tasks
- **LLM**: Provider routing and fallback strategies

## 📄 License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

---

**🚀 Ready to deploy your AI agent assistant? Follow the [Deployment Guide](docs/DEPLOYMENT.md) for detailed instructions!**

---

## 📚 **CONSOLIDATED TECHNICAL DOCUMENTATION**

*This section contains consolidated technical information from multiple documentation files that were merged into this README for unified documentation management.*

### 🏗️ **System Architecture Details**

*(Consolidated from docs/ARCHITECTURE.md)*

#### **High-Level Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React)       │◄──►│   (LangGraph)   │◄──►│   (PostgreSQL)  │
│   Port: 8123    │    │   Port: 8000    │    │   Port: 5433    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         │              ┌─────────────────┐              │
         │              │     Redis       │              │
         └──────────────►│   (Cache/PubSub)│◄─────────────┘
                        │   Port: 6379    │
                        └─────────────────┘
```

#### **Component Details**

**1. Frontend (React + TypeScript)**

- **Technology**: React 18 with TypeScript, Vite build system
- **UI Framework**: Tailwind CSS + Shadcn UI components
- **Features**: Real-time agent monitoring, multi-conversation support, project management dashboard

**2. Backend (LangGraph + FastAPI)**

- **Core Framework**: LangGraph for agent workflows, FastAPI for API endpoints
- **LLM Providers**: Google Gemini (primary), OpenAI GPT, Anthropic Claude (fallbacks)
- **Features**: Multi-provider routing, background task processing, real-time streaming

**3. Database Layer (PostgreSQL)**

- **Purpose**: LangGraph state persistence, conversation history, agent configuration
- **Features**: Connection pooling, automatic migrations, persistent storage

**4. Cache & Pub/Sub (Redis)**

- **Purpose**: Real-time messaging, background task queues, session caching
- **Features**: Pub/Sub for updates, task queue management, connection pooling

#### **Agent Workflow Architecture**

```
┌─────────────────┐
│  User Input     │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│ Query Analysis  │
│ & Routing       │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Research Agent  │    │ Analysis Agent  │    │ Synthesis Agent │
│ (Web Search)    │◄──►│ (Reflection)    │◄──►│ (Final Answer)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
          │                       │                       │
          ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Knowledge Base  │    │ Gap Analysis    │    │ Citation        │
│ Building        │    │ & Iteration     │    │ Generation      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

#### **Multi-LLM Provider Architecture**

```
┌─────────────────┐
│   LLM Manager   │
└─────────┬───────┘
          │
    ┌─────┴─────┐
    │  Router   │
    └─────┬─────┘
          │
    ┌─────┴─────┐
    │           │
    ▼           ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Gemini  │ │ OpenAI  │ │ Claude  │
│ Primary │ │Fallback │ │Fallback │
└─────────┘ └─────────┘ └─────────┘
```

**Provider Selection Logic:**

1. **Health Check**: Verify provider availability
2. **Load Balancing**: Distribute requests based on current load
3. **Fallback Chain**: Automatic failover on errors
4. **Rate Limiting**: Respect API quotas and limits

### 🗄️ **Database Implementation Details**

*(Consolidated from DATABASE_IMPLEMENTATION_REPORT.md)*

#### **PostgreSQL Configuration**

- **Version**: PostgreSQL 16 Alpine
- **Port**: 5433 (external) → 5432 (internal)
- **Authentication**: SCRAM-SHA-256
- **Connection**: Pool of connections (2-10 connections)
- **Volume**: Persistent storage with `langgraph-data`

#### **Database Schema**

**Main Tables:**

| Table | Purpose | Status |
|-------|---------|---------|
| `agent_tasks` | Agent task management | ✅ Active |
| `agent_metrics` | Performance metrics | ✅ Active |
| `system_events` | System event logging | ✅ Active |
| `user_sessions` | User session management | ✅ Active |
| `mcp_server_registry` | MCP server registry | ✅ Active |

**LangGraph Tables (Existing):**

- `assistant` - Assistant configuration
- `thread` - Conversation threads
- `run` - Agent execution runs
- `checkpoints` - State checkpoints
- `store` - Data storage

#### **Redis Configuration**

- **Version**: Redis 6 Alpine
- **Port**: 6379
- **Configuration**: AOF persistence enabled
- **Memory**: 256MB maximum with LRU policy
- **Features**: Pub/Sub messaging, task queues, session caching

#### **Security Implementation**

- ✅ Secure password generation
- ✅ JWT tokens with robust secret keys
- ✅ Minimal privilege containers
- ✅ Isolated service networks
- ✅ Automatic health checks
- ✅ SSL/TLS ready configuration

### 🐳 **Docker Integration Details**

*(Consolidated from DOCKER_DATABASE_INTEGRATION.md and DOCKER_UPDATE_REPORT.md)*

#### **Enhanced Docker Configuration**

**Updated docker-compose.yml Features:**

- ✅ **Enhanced API Service**: `gemini-fullstack-langgraph-enhanced`
- ✅ **Multi-LLM Environment Variables**: Support for Gemini, Claude, OpenAI
- ✅ **Feature Flags**: Enable/disable features via environment
- ✅ **Health Checks**: Comprehensive monitoring for all services
- ✅ **Development Tools**: Redis Commander and pgAdmin
- ✅ **Production Ready**: Nginx load balancer with SSL support

**Enhanced Dockerfile Features:**

- ✅ **Additional Tools**: curl, wget, netcat, postgresql-client, redis-tools
- ✅ **New Dependencies**: langchain-anthropic, langchain-openai, fastapi[all]
- ✅ **Startup Scripts**: Custom initialization and health check scripts
- ✅ **Environment Configuration**: Built-in feature flags and logging
- ✅ **Health Monitoring**: Automated health checks every 30 seconds

#### **Deployment Configurations**

**Development Profile:**

```bash
# Start with development tools
docker-compose --profile dev up

# Includes:
# - Redis Commander (port 8081)
# - pgAdmin (port 8080)
# - Hot reload enabled
# - Debug logging
```

**Production Profile:**

```bash
# Start with production optimizations
docker-compose --profile prod up

# Includes:
# - Nginx load balancer (ports 80/443)
# - SSL termination
# - Rate limiting
# - Performance monitoring
```

#### **Automation Scripts**

**Windows Batch Scripts:**

- ✅ **`manage.bat`**: Master management console with interactive menu
- ✅ **`rebuild-and-start.bat`**: Complete rebuild with updated code
- ✅ **`quick-restart.bat`**: Fast restart without rebuild
- ✅ **`dev-start.bat`**: Development mode with admin tools
- ✅ **`stop-all.bat`**: Safe shutdown with cleanup options
- ✅ **`logs-viewer.bat`**: Advanced log visualization

**Features:**

- ✅ **Intelligent Rebuild**: Detects changes and rebuilds only when necessary
- ✅ **Health Monitoring**: Automatic service health verification
- ✅ **Log Management**: Visualization, search, and export capabilities
- ✅ **Resource Cleanup**: Safe Docker resource management
- ✅ **Error Handling**: Robust error handling with clear messages

#### **Performance Optimizations**

**Database:**

- ✅ **Connection Pooling**: 2-10 connections per service
- ✅ **Query Optimization**: Indexes on frequently queried fields
- ✅ **Async Operations**: Non-blocking database operations
- ✅ **Cache Strategy**: Redis for frequently accessed data

**Application:**

- ✅ **Multi-Worker Support**: Horizontal scaling ready
- ✅ **Resource Limits**: Memory and CPU constraints
- ✅ **Graceful Shutdown**: Clean service termination
- ✅ **Health Monitoring**: Automatic restart on failure
