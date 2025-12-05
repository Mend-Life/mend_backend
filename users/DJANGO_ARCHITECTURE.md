# Django Architecture Overview

## Django MVT Pattern (Model-View-Template)

```
┌─────────────────────────────────────────────────────────────┐
│                    REQUEST FLOW                              │
└─────────────────────────────────────────────────────────────┘

1. CLIENT (Mobile App/Web)
   │
   │ HTTP Request (GET/POST/PUT/DELETE)
   │
   ▼
2. URLS (urls.py)
   │  - Routes requests to appropriate views
   │  - Example: /api/users/ → UserListView
   │
   ▼
3. VIEWS (views.py)
   │  - Business logic
   │  - Handles request/response
   │  - Calls models to get/save data
   │
   ▼
4. SERIALIZERS (serializers.py) - For REST APIs
   │  - Converts model data ↔ JSON
   │  - Validates incoming data
   │
   ▼
5. MODELS (models.py)
   │  - Database structure
   │  - Data access layer
   │
   ▼
6. DATABASE (SQLite/PostgreSQL)
   │
   ▼
7. RESPONSE (JSON/HTML)
   │
   ▼
   CLIENT receives response
```

## For REST APIs (Django REST Framework):

```
Model → Serializer → ViewSet/APIView → URL Router → Client
```

### Components:

1. **MODEL** (`models.py`)
   - Defines database structure
   - Fields, relationships, methods
   - Example: `User` model with email, name, etc.

2. **SERIALIZER** (`serializers.py`)
   - Converts Python objects ↔ JSON
   - Validates data
   - Handles create/update logic
   - Example: `UserSerializer` converts User model to JSON

3. **VIEW** (`views.py`)
   - Handles HTTP requests (GET, POST, PUT, DELETE)
   - Uses serializers to process data
   - Returns JSON responses
   - Example: `UserViewSet` handles all user operations

4. **URL** (`urls.py`)
   - Maps URLs to views
   - Example: `/api/users/` → `UserViewSet`

## Example Flow for User API:

```
POST /api/users/
   │
   ├─→ urls.py routes to UserViewSet.create()
   │
   ├─→ ViewSet receives JSON: {"email": "user@example.com", "password": "123"}
   │
   ├─→ UserSerializer validates data
   │
   ├─→ serializer.save() creates User model instance
   │
   ├─→ Model.save() writes to database
   │
   └─→ Response: {"id": 1, "email": "user@example.com", "name": "Happy_A3B2"}
```

## File Structure:

```
users/
├── models.py          # Database structure (User model)
├── serializers.py     # Data conversion (UserSerializer)
├── views.py           # Request handlers (UserViewSet)
├── urls.py            # URL routing
└── admin.py           # Admin interface
```

