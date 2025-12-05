# User API Guide

## Architecture Summary

```
Model (models.py) 
    ↓
Serializer (serializers.py) - Converts to/from JSON
    ↓
ViewSet (views.py) - Handles HTTP requests
    ↓
URL Router (urls.py) - Maps URLs to views
    ↓
Client receives JSON response
```

## API Endpoints

All endpoints are prefixed with `/api/`

### 1. List All Users
```
GET /api/users/
```
**Response:**
```json
[
  {
    "id": 1,
    "email": "user@example.com",
    "name": "Happy_A3B2",
    "age": null,
    "gender": null,
    "location": null,
    "created_at": "2025-01-15T10:30:00Z",
    "updated_at": "2025-01-15T10:30:00Z"
  }
]
```

### 2. Get Specific User
```
GET /api/users/{id}/
```

### 3. Create User (Signup)
```
POST /api/users/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "mypassword",
  "name": "John Doe"  // Optional - will auto-generate if not provided
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",  // Or "Happy_A3B2" if not provided
  "age": null,
  "gender": null,
  "location": null,
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

### 4. Update User (Full)
```
PUT /api/users/{id}/
Content-Type: application/json

{
  "email": "newemail@example.com",
  "name": "Jane Doe",
  "age": 25,
  "gender": "Female",
  "location": "New York"
}
```

### 5. Update User (Partial)
```
PATCH /api/users/{id}/
Content-Type: application/json

{
  "name": "Updated Name"
}
```

### 6. Delete User
```
DELETE /api/users/{id}/
```

### 7. Custom Endpoint: Get Current User
```
GET /api/users/me/
```

### 8. Custom Endpoint: Update Profile
```
PATCH /api/users/{id}/update_profile/
Content-Type: application/json

{
  "name": "New Name",
  "age": 30
}
```

## Testing with curl

```bash
# Create a user
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "test123"}'

# List all users
curl http://localhost:8000/api/users/

# Get specific user
curl http://localhost:8000/api/users/1/

# Update user
curl -X PATCH http://localhost:8000/api/users/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'

# Delete user
curl -X DELETE http://localhost:8000/api/users/1/
```

## Testing with Django Shell

```python
python manage.py shell

from users.models import User
from users.serializers import UserSerializer

# Create user
user = User.objects.create(email="test@example.com", password="test123")
# Name will be auto-generated: "Happy_A3B2" or similar

# Serialize to JSON
serializer = UserSerializer(user)
print(serializer.data)
```

## Notes

1. **Random Name Generation**: If `name` is not provided during user creation, it will be auto-generated (e.g., "Happy_A3B2", "Peaceful_X9K1")

2. **Password Handling**: Currently passwords are stored as plain text. In production, you should:
   - Use `user.set_password(password)` instead of `user.password = password`
   - Use Django's authentication system
   - Consider using JWT tokens

3. **Permissions**: Currently set to `AllowAny` for testing. Change to `IsAuthenticated` in production.

4. **random_name field**: You have both `random_name` and `name` fields. The `name` field auto-generates, so `random_name` might be redundant. Consider removing it.

