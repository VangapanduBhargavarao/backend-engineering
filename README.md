# Backend Engineering — 100 Days

A hands-on journey to become a strong backend developer by learning backend engineering principles from first principles and implementing them using Python.

This repository focuses on understanding **how backend systems work internally**, not just learning a framework.

The goal is to learn the underlying concepts first, implement them from scratch where practical, test them, document them, and finally apply them using **FastAPI** to build production-style backend systems.

---

## 🎯 Goal

My primary goal is to become a strong backend developer with a solid understanding of:

- HTTP and networking fundamentals
- REST API design
- Authentication and authorization
- Backend architecture
- Databases and SQL
- Transactions
- Caching
- Redis
- Background jobs
- Search systems
- Error handling
- Fault tolerance
- Security
- Logging
- Observability
- Concurrency and asynchronous programming
- Testing
- API documentation
- Webhooks
- Docker and deployment concepts
- FastAPI
- Production backend architecture

The focus is not simply on completing a course.

The goal is to be able to **design, implement, debug, explain, test, and improve backend systems.**

---

# 🧠 Learning Philosophy

The learning process for every topic follows:

```text
Learn
  ↓
Understand WHY
  ↓
Understand HOW
  ↓
Implement
  ↓
Test
  ↓
Document
  ↓
Commit
  ↓
Reflect
```

I am intentionally avoiding a framework-first approach.

Instead of immediately learning:

```text
FastAPI → decorators → endpoints → CRUD
```

I first want to understand:

```text
HTTP
 ↓
Request / Response
 ↓
Routing
 ↓
Serialization
 ↓
Validation
 ↓
Authentication
 ↓
Authorization
 ↓
Business Logic
 ↓
Database
 ↓
Caching
 ↓
Background Jobs
 ↓
Concurrency
 ↓
Observability
```

Then I will use FastAPI as a tool to implement these concepts in a real backend application.

---

# 🛠️ Technology Stack

## Programming

- Python
- SQL
- Bash / PowerShell

## Backend

- HTTP
- REST
- FastAPI
- Pydantic
- SQLAlchemy

## Databases

- SQLite
- MySQL

## Caching

- Redis

## Search

- Elasticsearch / OpenSearch

## Testing

- Pytest

## DevOps

- Git
- GitHub
- Docker
- Docker Compose
- Linux

## Concepts

- Authentication
- Authorization
- Transactions
- Caching
- Queues
- Concurrency
- Async programming
- Fault tolerance
- Security
- Observability
- Scalability

---

# 📚 Learning Resource

The primary theoretical resource for this journey is:

**Backend from First Principles**

The playlist is being used as the conceptual foundation for this repository.

The implementation in this repository is independently written in Python to reinforce the concepts.

---

# 🗺️ 100-Day Roadmap

## Phase 1 — Backend Fundamentals

### Days 1–7

- Client-server architecture
- HTTP
- HTTP requests
- HTTP responses
- HTTP methods
- HTTP headers
- Cookies
- Basic request/response lifecycle

### Implementation

Build a small HTTP-related system using Python without FastAPI.

---

# Phase 2 — Routing & Data Handling

## Days 8–14

- Routing
- Path parameters
- Query parameters
- Serialization
- Deserialization
- JSON
- Validation
- Nested data

### Implementation

Build a small API framework-like system using Python.

---

# Phase 3 — Authentication & Authorization

## Days 15–21

- Password hashing
- Registration
- Login
- Sessions
- Cookies
- Authentication
- Authorization
- Roles
- JWT

### Implementation

Build an authentication and authorization service.

Example roles:

```text
ADMIN
MANAGER
USER
```

---

# Phase 4 — Backend Architecture & REST

## Days 22–28

- Controllers
- Services
- Repositories
- Separation of concerns
- Dependency management
- REST principles
- Resource-oriented API design
- Pagination
- Filtering
- Sorting
- API errors

### Architecture

```text
Request
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
Database
```

### Implementation

Build a layered REST-style backend without relying heavily on a framework.

---

# Phase 5 — Databases

## Days 29–40

- SQL
- Tables
- Primary keys
- Foreign keys
- Relationships
- CRUD
- Joins
- Indexes
- Query optimization
- Transactions
- ACID
- Isolation concepts
- Connection pooling
- SQLite
- MySQL

### Implementation

Build a banking-style backend demonstrating:

```text
Users
Accounts
Transactions
Transfers
Database Transactions
```

The focus will be on correctness and consistency rather than just CRUD operations.

---

# Phase 6 — Caching & Background Processing

## Days 41–50

- Caching
- Cache hit
- Cache miss
- TTL
- Cache invalidation
- Eviction
- Redis
- Background jobs
- Queues
- Workers
- Search systems
- Elasticsearch / OpenSearch

### Architecture

```text
             ┌─────────────┐
             │   Client    │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │     API     │
             └──────┬──────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Redis               Database
          │
          │
          ▼
       Cached Data
```

---

# Phase 7 — Reliability & Fault Tolerance

## Days 51–60

- Error handling
- Custom exceptions
- Timeouts
- Retries
- Exponential backoff
- Circuit breakers
- External service failures
- Fault tolerance
- Configuration management
- Environment variables
- Secrets

### Implementation

Build a resilient external API client capable of handling:

```text
Timeout
Connection Error
Temporary Failure
Repeated Failure
Slow Response
```

---

# Phase 8 — Logging, Observability & Security

## Days 61–70

### Logging

- Python logging
- Log levels
- Structured logging
- Request IDs

### Observability

- Metrics
- Latency
- Error rates
- Request tracking
- Basic monitoring concepts

### Security

- Input validation
- Password security
- SQL injection
- XSS
- CSRF
- CORS
- Rate limiting
- Security headers
- Secrets management

### Implementation

Build a secure backend core with logging and basic observability.

---

# Phase 9 — Concurrency & Async Programming

## Days 71–80

- Processes
- Threads
- CPU-bound work
- I/O-bound work
- Concurrency
- Parallelism
- Async programming
- `asyncio`
- Event loops
- Concurrent API requests

### Comparison

```text
Sequential
    ↓
Threading
    ↓
Multiprocessing
    ↓
Asyncio
```

The goal is to understand **when and why** each approach should be used.

---

# Phase 10 — FastAPI

## Days 81–90

After understanding the underlying backend principles, FastAPI will be introduced as the main Python web framework.

Topics:

- FastAPI basics
- Routing
- Path parameters
- Query parameters
- Request bodies
- Response models
- Pydantic
- Validation
- Dependency injection
- Authentication
- Authorization
- JWT
- SQLAlchemy
- MySQL
- Redis
- Background tasks
- Error handling
- Testing
- OpenAPI documentation

---

# Phase 11 — Production-Style Backend

## Days 91–100

The final phase combines the concepts learned throughout the journey.

### Main Project

**Production-Style Task Management API**

The project will include:

- User registration
- Login
- JWT authentication
- Role-based authorization
- Task management
- Pagination
- Filtering
- Sorting
- MySQL
- SQLAlchemy
- Redis caching
- Background processing
- Error handling
- Logging
- Request tracking
- Rate limiting
- Testing
- OpenAPI documentation
- Docker

---

# 🏗️ Target Architecture

The final backend will aim toward an architecture similar to:

```text
                         Client
                           │
                           ▼
                     ┌───────────┐
                     │  FastAPI  │
                     └─────┬─────┘
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
              Authentication   Validation
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                       Services
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                 Redis          MySQL
                    │
                    │
                    ▼
              Background Jobs
                    │
                    ▼
                  Worker
```

This architecture will evolve throughout the 100 days rather than being implemented all at once.

---

# 📁 Repository Structure

```text
backend-engineering-100-days/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── 01_backend_fundamentals/
├── 02_http/
├── 03_routing/
├── 04_serialization/
├── 05_authentication/
├── 06_authorization/
├── 07_backend_architecture/
├── 08_rest_api/
├── 09_database/
├── 10_transactions/
├── 11_caching/
├── 12_redis/
├── 13_background_jobs/
├── 14_elasticsearch/
├── 15_error_handling/
├── 16_fault_tolerance/
├── 17_configuration/
├── 18_logging/
├── 19_observability/
├── 20_graceful_shutdown/
├── 21_security/
├── 22_concurrency/
├── 23_object_storage/
├── 24_realtime/
├── 25_testing/
├── 26_openapi/
├── 27_webhooks/
├── 28_devops/
│
└── projects/
    ├── project_01_task_management/
    ├── project_02_ecommerce_api/
    └── project_03_production_backend/
```

---

# 🧪 Implementation Rules

Every topic should contain implementation whenever practical.

For example:

```text
02_http/
│
├── README.md
├── http_request.py
├── http_response.py
└── tests/
```

The implementation should answer:

### What?

What is the concept?

### Why?

Why does this concept exist?

### How?

How does it work?

### When?

When should it be used?

### Trade-offs

What are its advantages and disadvantages?

### Implementation

How can it be implemented in Python?

### Testing

What happens with valid and invalid inputs?

---

# 🧑‍💻 Coding Philosophy

The implementations should prioritize:

- Readability
- Correctness
- Simplicity
- Testability
- Separation of concerns
- Meaningful naming
- Error handling
- Edge cases
- Documentation

The goal is not to write the shortest code.

The goal is to write code that another developer can understand and maintain.

---

# 🧪 Testing Philosophy

Testing will be introduced gradually.

For important implementations, tests will cover:

```text
Normal case
Edge case
Invalid input
Failure case
Boundary case
```

For example:

```text
Authentication

✓ valid login
✓ invalid password
✓ unknown user
✓ missing credentials
✓ expired token
✓ unauthorized role
```

---

# 📊 Progress Tracker

## Backend Fundamentals

- [ ] Client-server architecture
- [ ] HTTP
- [ ] HTTP requests
- [ ] HTTP responses
- [ ] HTTP methods
- [ ] Headers
- [ ] Cookies
- [ ] Routing
- [ ] Serialization
- [ ] Validation

## Authentication

- [ ] Password hashing
- [ ] Registration
- [ ] Login
- [ ] Sessions
- [ ] JWT
- [ ] Authorization
- [ ] RBAC

## Architecture

- [ ] Controller
- [ ] Service
- [ ] Repository
- [ ] Dependency separation
- [ ] REST
- [ ] Pagination
- [ ] Filtering
- [ ] Sorting

## Databases

- [ ] SQL
- [ ] CRUD
- [ ] Relationships
- [ ] Joins
- [ ] Indexes
- [ ] Transactions
- [ ] ACID
- [ ] Connection pooling
- [ ] MySQL

## Performance

- [ ] Caching
- [ ] Redis
- [ ] Background jobs
- [ ] Queues
- [ ] Workers
- [ ] Search

## Reliability

- [ ] Error handling
- [ ] Timeouts
- [ ] Retries
- [ ] Backoff
- [ ] Circuit breaker
- [ ] Fault tolerance
- [ ] Configuration
- [ ] Secrets

## Observability

- [ ] Logging
- [ ] Structured logging
- [ ] Request IDs
- [ ] Metrics
- [ ] Latency tracking

## Security

- [ ] Input validation
- [ ] SQL injection
- [ ] XSS
- [ ] CSRF
- [ ] CORS
- [ ] Rate limiting
- [ ] Security headers

## Concurrency

- [ ] Processes
- [ ] Threads
- [ ] CPU-bound vs I/O-bound
- [ ] Async programming
- [ ] asyncio
- [ ] Event loop
- [ ] Concurrent requests

## FastAPI

- [ ] Routing
- [ ] Request models
- [ ] Response models
- [ ] Pydantic
- [ ] Dependencies
- [ ] Authentication
- [ ] SQLAlchemy
- [ ] MySQL
- [ ] Redis
- [ ] Background tasks
- [ ] Testing
- [ ] OpenAPI

## DevOps

- [ ] Docker
- [ ] Docker Compose
- [ ] Environment configuration
- [ ] Linux
- [ ] Deployment concepts

## Projects

- [ ] Mini HTTP server
- [ ] Mini API framework
- [ ] Authentication service
- [ ] Layered REST API
- [ ] Banking backend
- [ ] Resilient API client
- [ ] Secure API core
- [ ] Concurrent API client
- [ ] Production-style FastAPI project

---

# 📈 Daily Workflow

Each day follows this workflow:

```text
1. Watch the relevant backend concept
          ↓
2. Take minimal notes
          ↓
3. Understand the WHY
          ↓
4. Design a small implementation
          ↓
5. Write Python code
          ↓
6. Test the implementation
          ↓
7. Handle edge cases
          ↓
8. Document what I learned
          ↓
9. Commit to Git
          ↓
10. Push to GitHub
```

---

# 📝 Git Commit Convention

Commits follow a simple convention:

```text
day 01: implement client server communication
day 02: model HTTP request
day 03: implement HTTP response
day 04: implement HTTP methods
day 05: implement HTTP headers
```

For larger changes:

```text
day 40: build banking backend core
day 50: add Redis caching
day 60: implement resilient API client
day 80: implement async API client
day 100: complete production backend
```

---

# 🚀 Why This Repository Exists

The purpose of this repository is not to prove that I completed a playlist.

It is a record of my progression from:

```text
Learning concepts
      ↓
Understanding concepts
      ↓
Implementing concepts
      ↓
Testing concepts
      ↓
Building systems
      ↓
Understanding trade-offs
      ↓
Building production-style backends
```

The ultimate goal is to become someone who can look at a backend problem and reason about:

```text
Architecture
   +
Performance
   +
Security
   +
Reliability
   +
Data
   +
Concurrency
   +
Maintainability
```

rather than simply knowing how to create an API endpoint.

---

# 🔮 Next Step After 100 Days

After completing the backend foundation, the next phase will focus on becoming an **AI Engineer** while continuing to use backend engineering as the foundation.

The planned direction is:

```text
Strong Backend
      ↓
FastAPI
      ↓
AI APIs
      ↓
LLMs
      ↓
Embeddings
      ↓
Vector Databases
      ↓
RAG
      ↓
Tool Calling
      ↓
AI Agents
      ↓
Production AI Systems
```

The objective is to combine backend engineering with AI engineering rather than treating AI systems as isolated model-calling scripts.

---

# 📅 Start Date

**September 2026**

## Target

**100 days of consistent backend engineering practice.**

---

# ⭐ Principle

> Learn the concept.
> Understand why it exists.
> Build it.
> Break it.
> Test it.
> Fix it.
> Document it.
> Ship it.
