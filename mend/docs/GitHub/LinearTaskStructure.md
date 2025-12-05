# Mend - Phase 1 MVP Task Breakdown

## Setup Instructions

### For GitHub Projects:
1. Go to your GitHub repo
2. Click "Projects" tab
3. Create new project "Mend MVP"
4. Copy tasks below as issues

### For Linear:
1. Create project "Mend"
2. Create cycle "Phase 1: MVP"
3. Copy tasks below

---

## 🎯 Phase 1: MVP (Weeks 1-12)

**Goal:** Launch functional app with core mood tracking and recommendations

---

## Week 1-2: Project Setup & Infrastructure

### ✅ Task 1.1: Initialize Backend Project
**Priority:** High | **Estimate:** 4 hours

**Description:**
Set up Django project with basic configuration

**Checklist:**
- [ ] Create Django project: `django-admin startproject mend_backend`
- [ ] Create core apps: `users`, `moods`, `content`, `recommendations`
- [ ] Configure settings for dev/prod environments
- [ ] Set up environment variables (.env file)
- [ ] Create requirements.txt with dependencies
- [ ] Initialize Git repository
- [ ] Create .gitignore file

**Dependencies:**
```
Django==5.0
djangorestframework==3.14
psycopg2-binary==2.9
python-decouple==3.8
django-cors-headers==4.3
```

**Acceptance Criteria:**
- Django server runs on localhost:8000
- All apps are registered in INSTALLED_APPS
- Environment variables load correctly

---

### ✅ Task 1.2: Database Setup (Supabase)
**Priority:** High | **Estimate:** 3 hours

**Description:**
Connect Django to Supabase PostgreSQL database

**Checklist:**
- [ ] Create Supabase project
- [ ] Get database credentials (host, port, password)
- [ ] Configure Django DATABASES settings
- [ ] Test database connection
- [ ] Enable Row Level Security (RLS) in Supabase
- [ ] Create database backup schedule

**Django Settings:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('SUPABASE_PASSWORD'),
        'HOST': os.getenv('SUPABASE_HOST'),
        'PORT': '5432',
    }
}
```

**Acceptance Criteria:**
- Django can connect to Supabase
- Can run migrations successfully
- Database appears in Supabase dashboard

---

### ✅ Task 1.3: Authentication Setup (Supabase Auth)
**Priority:** High | **Estimate:** 6 hours

**Description:**
Integrate Supabase authentication with Django

**Checklist:**
- [ ] Install supabase-py library
- [ ] Create custom user model extending AbstractUser
- [ ] Configure JWT authentication in DRF
- [ ] Create auth endpoints (signup, login, logout)
- [ ] Implement JWT token refresh
- [ ] Test auth flow with Postman

**Endpoints to Create:**
- POST /api/auth/signup/
- POST /api/auth/login/
- POST /api/auth/logout/
- POST /api/auth/refresh/

**Acceptance Criteria:**
- User can sign up and receive JWT token
- Token-based authentication works
- Protected endpoints require valid token

---

## Week 3-4: Core Models & APIs

### ✅ Task 2.1: Create User Profile Model
**Priority:** High | **Estimate:** 4 hours

**Description:**
Create UserProfile model with preferences

**Checklist:**
- [ ] Create UserProfile model (see PRD Section 6.4)
- [ ] Add fields: faith_preference, preferred_content_types, etc.
- [ ] Create migration
- [ ] Run migration
- [ ] Create serializer
- [ ] Create API endpoints (GET, PATCH)
- [ ] Test with Postman

**Model Fields:**
```python
class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    faith_preference = CharField(max_length=50, default='christian')
    preferred_content_types = ArrayField(CharField(max_length=50))
    music_genres = ArrayField(CharField(max_length=50))
    # ... see PRD for complete fields
```

**Endpoints:**
- GET /api/profile/
- PATCH /api/profile/

**Acceptance Criteria:**
- UserProfile created automatically on user signup
- Can update preferences via API
- Data persists in database

---

### ✅ Task 2.2: Mood Tracking Models & API
**Priority:** High | **Estimate:** 6 hours

**Description:**
Implement mood entry system

**Checklist:**
- [ ] Create MoodEntry model
- [ ] Create UserStreak model
- [ ] Run migrations
- [ ] Create MoodEntry serializer
- [ ] Implement POST /api/moods/ (create entry)
- [ ] Implement GET /api/moods/ (list entries)
- [ ] Implement GET /api/moods/insights/
- [ ] Add streak tracking logic
- [ ] Test all endpoints

**Endpoints:**
- POST /api/moods/
- GET /api/moods/
- GET /api/moods/insights/
- GET /api/moods/stats/

**Acceptance Criteria:**
- Can create mood entry with mood + intensity
- Can retrieve mood history
- Streak updates automatically
- Mood stats calculate correctly

---

### ✅ Task 2.3: Content Library Models
**Priority:** High | **Estimate:** 4 hours

**Description:**
Create content storage system

**Checklist:**
- [ ] Create Content model (see PRD)
- [ ] Create UserInteraction model
- [ ] Create SavedContent model
- [ ] Run migrations
- [ ] Create admin interface for content management
- [ ] Add sample content (10-20 items for testing)

**Acceptance Criteria:**
- Content model stores all content types
- Admin can add/edit content via Django admin
- Foreign key relationships work correctly

---

### ✅ Task 2.4: Content CRUD API
**Priority:** High | **Estimate:** 5 hours

**Description:**
Build APIs to browse and interact with content

**Checklist:**
- [ ] Create Content serializer
- [ ] Implement GET /api/content/ (list with filters)
- [ ] Implement GET /api/content/{id}/ (detail)
- [ ] Implement POST /api/content/{id}/save/
- [ ] Implement DELETE /api/content/{id}/save/
- [ ] Implement POST /api/content/{id}/interact/
- [ ] Add pagination
- [ ] Test with various content types

**Endpoints:**
- GET /api/content/?type=verse&mood=sad
- GET /api/content/{id}/
- POST /api/content/{id}/save/
- POST /api/content/{id}/interact/

**Acceptance Criteria:**
- Can browse content by type and mood
- Can save/unsave content
- Interactions are recorded
- Pagination works (20 items per page)

---

## Week 5-6: Recommendation System (Basic)

### ✅ Task 3.1: Basic Recommendation Logic (Django)
**Priority:** High | **Estimate:** 8 hours

**Description:**
Implement simple mood-to-content matching

**Checklist:**
- [ ] Create recommendation service class
- [ ] Implement mood matching algorithm (v1: simple filtering)
- [ ] Add user preference filtering
- [ ] Implement content diversification (mix types)
- [ ] Add "recently viewed" filtering
- [ ] Create GET /api/recommendations/ endpoint
- [ ] Cache recommendations in Redis (30 min)
- [ ] Test with different moods

**Algorithm v1 (Simple):**
```python
def get_recommendations(user, mood, count=5):
    # 1. Filter content by primary/secondary moods
    # 2. Filter by user preferences
    # 3. Exclude recently seen
    # 4. Diversify content types
    # 5. Return top 5
```

**Acceptance Criteria:**
- Returns 5 relevant recommendations for any mood
- Mixes content types (not all verses)
- Doesn't show same content repeatedly
- Response time < 500ms

---

### ✅ Task 3.2: Integration with Mood Check-in
**Priority:** Medium | **Estimate:** 3 hours

**Description:**
Return recommendations immediately after mood entry

**Checklist:**
- [ ] Modify POST /api/moods/ to include recommendations
- [ ] Test integrated flow
- [ ] Add error handling if recommendations fail
- [ ] Document API response format

**Response Format:**
```json
{
  "mood_entry": {...},
  "recommendations": [...]
}
```

**Acceptance Criteria:**
- Mood check-in returns recommendations in same request
- Graceful fallback if recommendations fail

---

## Week 7-8: External API Integrations

### ✅ Task 4.1: Spotify API Integration
**Priority:** Medium | **Estimate:** 6 hours

**Description:**
Integrate Spotify for song playback

**Checklist:**
- [ ] Register Spotify app, get API credentials
- [ ] Install spotipy library
- [ ] Create Spotify service class
- [ ] Implement search functionality
- [ ] Store Spotify track IDs in content
- [ ] Test playback in Postman
- [ ] Handle rate limits

**Acceptance Criteria:**
- Can search Spotify for songs
- Can retrieve track details
- Can generate Spotify URIs for playback

---

### ✅ Task 4.2: Bible API Integration
**Priority:** Medium | **Estimate:** 4 hours

**Description:**
Fetch Bible verses dynamically

**Checklist:**
- [ ] Choose Bible API (api.bible or alternatives)
- [ ] Get API key
- [ ] Create Bible service class
- [ ] Implement verse fetching by reference
- [ ] Handle multiple translations
- [ ] Cache responses
- [ ] Add 100 verses to content library

**Acceptance Criteria:**
- Can fetch any Bible verse by reference
- Supports NIV translation (minimum)
- Verses cached to reduce API calls

---

### ✅ Task 4.3: TMDB API Integration (Movies)
**Priority:** Low | **Estimate:** 4 hours

**Description:**
Integrate movie database

**Checklist:**
- [ ] Register TMDB account, get API key
- [ ] Create TMDB service class
- [ ] Implement movie search
- [ ] Fetch movie details (poster, description)
- [ ] Add 50 movies to content library with mood tags

**Acceptance Criteria:**
- Can fetch movie details
- Posters display correctly
- Movies tagged with appropriate moods

---

## Week 9-10: Flutter App (Basic)

### ✅ Task 5.1: Flutter Project Setup
**Priority:** High | **Estimate:** 4 hours

**Description:**
Initialize Flutter project and dependencies

**Checklist:**
- [ ] Create Flutter project: `flutter create mend_app`
- [ ] Add dependencies (dio, provider, hive)
- [ ] Set up project structure (lib/screens, lib/services, lib/models)
- [ ] Configure API base URL
- [ ] Set up environment variables
- [ ] Test Flutter app runs on emulator

**Dependencies:**
```yaml
dependencies:
  flutter:
    sdk: flutter
  dio: ^5.4.0
  provider: ^6.1.1
  hive: ^2.2.3
  hive_flutter: ^1.1.0
  shared_preferences: ^2.2.2
```

---

### ✅ Task 5.2: Authentication Screens
**Priority:** High | **Estimate:** 8 hours

**Description:**
Build login and signup screens

**Checklist:**
- [ ] Create LoginScreen
- [ ] Create SignupScreen
- [ ] Create AuthService (API calls)
- [ ] Implement form validation
- [ ] Store JWT token securely
- [ ] Handle auth state (Provider)
- [ ] Add error handling
- [ ] Test complete auth flow

**Screens:**
- Login (email, password)
- Signup (email, password, confirm password)

**Acceptance Criteria:**
- User can sign up successfully
- User can log in and stay logged in
- Token persists after app restart
- Error messages display correctly

---

### ✅ Task 5.3: Mood Check-in Screen
**Priority:** High | **Estimate:** 6 hours

**Description:**
Build mood selection interface

**Checklist:**
- [ ] Create MoodCheckInScreen
- [ ] Design mood selector (grid of emoji + labels)
- [ ] Add intensity slider (1-10)
- [ ] Add optional context text field
- [ ] Implement API call to POST /api/moods/
- [ ] Navigate to recommendations after submit
- [ ] Add animations

**Design:**
- Grid: 3x3 mood options with emoji
- Slider: Visual 1-10 scale
- Submit button

**Acceptance Criteria:**
- User can select mood intuitively
- Submitting saves mood and shows recommendations
- Smooth animations and transitions

---

### ✅ Task 5.4: Recommendation Feed Screen
**Priority:** High | **Estimate:** 8 hours

**Description:**
Display personalized recommendations

**Checklist:**
- [ ] Create RecommendationFeedScreen
- [ ] Build ContentCard widget (verse, song, quote, etc.)
- [ ] Implement API call to GET /api/recommendations/
- [ ] Add pull-to-refresh
- [ ] Implement "Save" functionality
- [ ] Implement "Not interested" functionality
- [ ] Add content type icons
- [ ] Handle different content types appropriately

**Content Cards:**
- Verse: Show text, reference, save button
- Song: Show title, artist, play button (Spotify link)
- Quote: Show quote, author
- Activity: Show title, duration, start button

**Acceptance Criteria:**
- Recommendations display correctly
- User can interact with content
- Refresh gets new recommendations
- Different content types render appropriately

---

### ✅ Task 5.5: Profile & Settings Screen
**Priority:** Medium | **Estimate:** 5 hours

**Description:**
User profile and preferences

**Checklist:**
- [ ] Create ProfileScreen
- [ ] Display user stats (streak, mood entries)
- [ ] Create PreferencesScreen
- [ ] Implement preference editing
- [ ] Add logout functionality
- [ ] Show mood history graph (basic)

**Acceptance Criteria:**
- User can view and edit preferences
- Stats display correctly
- Logout clears session

---

## Week 11-12: Testing, Polish & Launch Prep

### ✅ Task 6.1: Backend Testing
**Priority:** High | **Estimate:** 8 hours

**Description:**
Write tests for critical paths

**Checklist:**
- [ ] Write tests for auth endpoints
- [ ] Write tests for mood tracking
- [ ] Write tests for recommendations
- [ ] Write tests for content API
- [ ] Test error handling
- [ ] Load testing (100 concurrent users)
- [ ] Fix bugs found during testing

**Target Coverage:** 70%+ for core features

---

### ✅ Task 6.2: Flutter Testing
**Priority:** Medium | **Estimate:** 6 hours

**Description:**
Test Flutter app on devices

**Checklist:**
- [ ] Test on iOS simulator
- [ ] Test on Android emulator
- [ ] Test on real iOS device
- [ ] Test on real Android device
- [ ] Fix UI bugs
- [ ] Optimize performance
- [ ] Test offline behavior

---

### ✅ Task 6.3: Content Population
**Priority:** High | **Estimate:** 8 hours

**Description:**
Populate database with initial content

**Checklist:**
- [ ] Add 200 Bible verses (various moods)
- [ ] Add 100 quotes
- [ ] Add 50 songs (Spotify links)
- [ ] Add 30 movies
- [ ] Add 20 activities
- [ ] Tag all content with appropriate moods
- [ ] Verify all content displays correctly

**Content Distribution:**
- Verses: 40%
- Songs: 25%
- Quotes: 20%
- Activities: 10%
- Movies: 5%

---

### ✅ Task 6.4: Documentation
**Priority:** Medium | **Estimate:** 4 hours

**Description:**
Create essential documentation

**Checklist:**
- [ ] README.md with setup instructions
- [ ] API documentation (Postman collection)
- [ ] Deployment guide
- [ ] Environment variables documentation
- [ ] Content management guide (for admin)

---

### ✅ Task 6.5: Deployment Setup
**Priority:** High | **Estimate:** 8 hours

**Description:**
Deploy backend to production

**Checklist:**
- [ ] Set up Railway/Render account
- [ ] Configure production environment
- [ ] Set up PostgreSQL (Supabase production)
- [ ] Set up Redis
- [ ] Deploy Django backend
- [ ] Configure HTTPS/SSL
- [ ] Set up monitoring (Sentry)
- [ ] Test production API

**Deployment Checklist:**
- [ ] Environment variables configured
- [ ] Database migrations run
- [ ] Static files served correctly
- [ ] CORS configured for Flutter app
- [ ] API accessible via HTTPS

---

### ✅ Task 6.6: App Store Submission Prep
**Priority:** High | **Estimate:** 6 hours

**Description:**
Prepare for app store launch

**Checklist:**
- [ ] Create app icons (iOS & Android)
- [ ] Create splash screens
- [ ] Write app description
- [ ] Take screenshots (5 per platform)
- [ ] Set up App Store Connect account
- [ ] Set up Google Play Console account
- [ ] Build release APK/IPA
- [ ] Test release builds

**App Store Requirements:**
- App name: Mend
- Tagline: "From any mood to elevated"
- Description: 500 characters
- Screenshots: iPhone, iPad, Android

---

### ✅ Task 6.7: Beta Testing
**Priority:** High | **Estimate:** Ongoing

**Description:**
Get feedback from beta testers

**Checklist:**
- [ ] Recruit 10-20 beta testers
- [ ] Distribute via TestFlight (iOS) / internal testing (Android)
- [ ] Collect feedback
- [ ] Fix critical bugs
- [ ] Iterate on UX issues

**Beta Testing Timeline:** 2 weeks

---

## 🎯 Definition of Done for Phase 1

**Phase 1 is complete when:**
- [ ] Users can sign up and log in
- [ ] Users can check in with their mood
- [ ] Users receive 5 personalized recommendations
- [ ] Users can interact with content (view, save, skip)
- [ ] Users can view their mood history
- [ ] Users can edit preferences
- [ ] Backend is deployed and stable
- [ ] Flutter app runs on iOS and Android
- [ ] 500+ content items in database
- [ ] Beta testing complete with positive feedback
- [ ] Ready for App Store submission

---

## Estimated Timeline

| Week | Focus Area | Hours |
|------|-----------|-------|
| 1-2 | Infrastructure & Auth | 20 |
| 3-4 | Core Models & APIs | 24 |
| 5-6 | Recommendations | 16 |
| 7-8 | External APIs | 14 |
| 9-10 | Flutter App | 26 |
| 11-12 | Testing & Launch Prep | 32 |
| **Total** | | **132 hours** |

**Working 20 hours/week:** ~6-7 weeks  
**Working 40 hours/week:** ~3-4 weeks

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| API integrations fail | Have fallback content stored locally |
| Recommendation quality poor | Collect feedback early, iterate on algorithm |
| Database performance issues | Add indexes, implement caching |
| Deployment issues | Test deployment process early (Week 8) |
| Beta testers give negative feedback | Allow 2 weeks buffer for fixes |

---

## Success Metrics for MVP

- [ ] 20+ beta testers signed up
- [ ] 70%+ daily active usage among testers
- [ ] 4+ star average rating from testers
- [ ] < 5% crash rate
- [ ] Recommendations engagement rate > 50%
- [ ] Average session duration > 5 minutes