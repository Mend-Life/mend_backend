# Mend - Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** January 2025  
**Status:** Active Development  
**Product:** Mend - AI-Powered Mood & Wellness Companion

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Vision](#product-vision)
3. [Market Analysis](#market-analysis)
4. [User Personas](#user-personas)
5. [User Journeys](#user-journeys)
6. [Feature Specifications](#feature-specifications)
7. [Technical Architecture](#technical-architecture)
8. [API Specifications](#api-specifications)
9. [Database Schema](#database-schema)
10. [Non-Functional Requirements](#non-functional-requirements)
11. [Success Metrics](#success-metrics)
12. [Monetization Strategy](#monetization-strategy)
13. [Go-To-Market Strategy](#go-to-market-strategy)
14. [Development Roadmap](#development-roadmap)
15. [Risk Assessment](#risk-assessment)

---

## 1. Executive Summary

### Product Name
**Mend** - "Repair, heal, improve your emotional well-being"

### Product Vision
Mend is a personalized wellness companion that meets users in their emotional state and provides curated, multi-modal recommendations to elevate their mood and mental well-being. By combining mood tracking, AI-driven recommendations, and structured elevation plans, we help users navigate difficult emotional moments with personalized content from music, movies, Bible verses, quotes, books, and activities.

### Problem Statement
People experiencing negative emotional states (sadness, anxiety, weariness, loneliness) often don't know what specific actions or content will help them feel better. Existing solutions are either:
- Too generic (generic meditation apps)
- Single-modality (only music, only devotionals, only therapy)
- Not personalized to individual preferences
- Lack actionable, time-bound plans

### Solution
Mend provides real-time, personalized recommendations across multiple content types based on user's current mood, preferences, and historical data. It goes beyond recommendations by creating structured 1, 7, or 30-day elevation plans to guide users through their wellness journey.

### Target Market
- **Primary:** Young adults (18-35) experiencing stress, anxiety, loneliness
- **Secondary:** Faith-based individuals seeking spiritual + mental wellness
- **Tertiary:** Anyone seeking personalized mental health support

### Key Differentiators
1. **Multi-modal recommendations**: Music, movies, verses, quotes, books, activities - all in one place
2. **Mood-first approach**: Starts with how you feel, not what you want to do
3. **Structured plans**: Not just recommendations, but guided elevation journeys
4. **Personalized learning**: Learns what works for each individual user
5. **Faith-integrated wellness**: Combines spiritual and practical wellness

### Value Proposition
**"From any mood to elevated, in minutes - personalized for you."**

---

## 2. Product Vision

### Mission Statement
To provide accessible, personalized emotional wellness support that combines the best of mental health science, spiritual wisdom, and modern technology.

### Vision (3 Years)
Become the leading mood-first wellness platform, helping 1M+ people improve their emotional well-being through personalized, multi-modal content and AI-driven insights.

### Core Values
- **Empathy First**: We meet users where they are emotionally
- **Personalization**: No two journeys are the same
- **Holistic Wellness**: Mind, body, and spirit
- **Evidence-Based**: Grounded in psychology and proven practices
- **Accessible**: Mental wellness for everyone, not just those who can afford therapy

---

## 3. Market Analysis

### Market Size

**Total Addressable Market (TAM):**
- US mental health app market: $4.2B (2024)
- Christian app market: $500M+
- Overlap (faith-based mental wellness): ~$200M

**Serviceable Addressable Market (SAM):**
- English-speaking Christians (18-45) with smartphones: ~80M
- 10% willing to use mental health app: 8M potential users

**Serviceable Obtainable Market (SOM):**
- Year 1 goal: 10,000 users (0.125% of SAM)
- Year 3 goal: 200,000 users (2.5% of SAM)

### Target Demographics

**Primary Audience:**
- Age: 18-35
- Gender: 60% female, 40% male
- Faith: Christian (Protestant, Catholic, non-denominational)
- Income: $30k-$80k
- Location: US, Canada, UK, Australia
- Psychographics: Values faith, open about mental health, tech-savvy

**Secondary Audience:**
- Age: 36-50
- Similar profile but less tech-savvy
- More likely to seek faith-integrated solutions

### Competitive Landscape

| Competitor | Strengths | Weaknesses | Our Advantage |
|------------|-----------|------------|---------------|
| **Calm** | Beautiful UI, guided meditations, large user base | No mood-first approach, generic content, expensive ($70/year) | Personalized multi-modal, faith-integrated, mood-driven |
| **Headspace** | Great branding, structured courses, meditation focus | Expensive ($70/year), not faith-based, single-modality | More affordable, Christian focus, multi-modal content |
| **YouVersion Bible** | Huge user base (500M+), reading plans, community | No mood tracking, only Bible content, not wellness-focused | Multi-modal content, mood-driven, structured elevation plans |
| **Abide** | Faith-focused, audio meditations, Bible-based | Audio only, no mood tracking, limited content types | Text+audio+video, mood matching, comprehensive wellness |
| **Sanvello** | Mood tracking, CBT tools, evidence-based | Clinical feel, not uplifting, no faith integration | Positive focus, elevation plans, faith-integrated |

**Key Differentiator:** We're the ONLY app that combines mood tracking + multi-modal recommendations (verse/song/movie/book/activity) + structured elevation plans + faith integration.

### User Pain Points

1. **"I don't know what will help when I'm sad"**  
   → **Solution:** Personalized recommendations based on current mood

2. **"Devotional apps are too rigid"**  
   → **Solution:** Flexible, mood-driven content delivery

3. **"Mental health apps aren't aligned with my faith"**  
   → **Solution:** Faith-integrated wellness approach

4. **"I need structure but also flexibility"**  
   → **Solution:** Elevation plans with customization options

5. **"I want quick help, not hour-long therapy"**  
   → **Solution:** Micro-content (2-10 min activities)

---

## 4. User Personas

### Persona 1: "Stressed Sarah"
**Demographics:**
- Age: 26
- Occupation: Marketing professional
- Location: Austin, TX
- Income: $55k/year

**Profile:**
- High stress from work deadlines
- Feels anxious and overwhelmed frequently
- Active on social media
- Tries to maintain faith but struggles with consistency
- Limited time (15-20 min/day for self-care)

**Goals:**
- Quick relief during work breaks
- Long-term stress management strategies
- Reconnect with faith
- Improve sleep quality

**Behavior:**
- Opens app 2-3x daily during breaks
- Prefers short activities (5-10 min)
- Likes calming music and breathing exercises
- Responds well to uplifting quotes

**Pain Points:**
- Doesn't have time for long meditations
- Generic advice doesn't resonate
- Feels guilty for not praying/reading Bible more
- Doesn't know what will actually help

**How Mend Helps:**
- Quick mood check-in during lunch break
- 5-minute breathing exercises
- Uplifting worship songs
- Short Bible verses with modern context
- 7-day stress management plan

---

### Persona 2: "Lonely Lucas"
**Demographics:**
- Age: 22
- Occupation: Recent college grad, software developer
- Location: Seattle, WA
- Income: $70k/year

**Profile:**
- New to city, limited social connections
- Experiences loneliness and occasional depression
- Strong faith background
- Tech-savvy, early adopter
- Willing to commit to longer-term solutions

**Goals:**
- Feel more connected
- Find purpose and direction
- Build healthy routines
- Grow spiritually

**Behavior:**
- Evening usage (after work)
- Willing to commit to 7-30 day plans
- Enjoys podcasts and movies
- Active in online communities

**Pain Points:**
- Isolated in new city
- Feels disconnected from church community
- Doesn't know how to build social connections
- Struggles with motivation

**How Mend Helps:**
- Mood tracking reveals patterns
- 30-day "connection" elevation plan
- Community-focused activities (suggest local groups)
- Podcasts about purpose and belonging
- Movies that inspire hope

---

### Persona 3: "Weary Wanda"
**Demographics:**
- Age: 34
- Occupation: Mother of two, part-time teacher
- Location: Nashville, TN
- Income: $45k/year

**Profile:**
- Exhausted from parenting and work
- Feels spiritually dry
- Values faith but struggles to prioritize it
- Limited time (only when kids asleep)
- Seeks rest and renewal

**Goals:**
- Restore energy levels
- Reconnect with God
- Find moments of peace
- Be present with family

**Behavior:**
- Early morning (5-6 AM) or late night (10-11 PM) usage
- Prefers devotionals and worship music
- Needs gentle, grace-filled content
- Values structure but needs flexibility

**Pain Points:**
- No time for self-care
- Feels guilty about exhaustion
- Church attendance is hit-or-miss
- Needs quick spiritual nourishment

**How Mend Helps:**
- 5-minute morning devotionals
- Calming worship music for bedtime
- Grace-focused Bible verses
- 1-day "renewal" plans for tough days
- Activities that can include kids

---

## 5. User Journeys

### Journey 1: First-Time User Onboarding

```
1. Download App from App Store/Play Store
   ↓
2. Welcome Screen
   - "Meet Mend: Your personal wellness companion"
   - "From any mood to elevated"
   - [Get Started] button
   ↓
3. Sign Up
   - Email + Password
   - Or: Continue with Google/Apple
   ↓
4. Onboarding Question 1: "What brings you here today?"
   - Feeling anxious or stressed
   - Feeling sad or down
   - Feeling lonely
   - Feeling tired or burnt out
   - Just want to improve my mental wellness
   - Other
   ↓
5. Onboarding Question 2: "What helps you feel better?"
   - [ ] Bible verses & devotionals
   - [ ] Music & worship songs
   - [ ] Movies & shows
   - [ ] Quotes & affirmations
   - [ ] Meditation & breathing exercises
   - [ ] Journaling & reflection
   - [ ] Books & podcasts
   ↓
6. Onboarding Question 3: "Do you have faith preferences?"
   - Christian (Protestant)
   - Christian (Catholic)
   - Christian (non-denominational)
   - Spiritual but not religious
   - No preference
   ↓
7. Onboarding Question 4: "How much time can you dedicate daily?"
   - 5 minutes
   - 15 minutes
   - 30+ minutes
   - It varies
   ↓
8. First Mood Check-In
   - "How are you feeling right now?"
   - Mood selector (emoji grid)
   - Intensity slider (1-10)
   - [Continue] button
   ↓
9. Instant Recommendations
   - "Here's what might help you today..."
   - 5 personalized content cards
   - [Explore] or [Create a Plan]
   ↓
10. Home Screen (Main App)
```

**Duration:** 3-5 minutes  
**Drop-off Prevention:**
- Keep questions minimal (4 total)
- Show progress bar
- Allow skip for optional questions
- Provide immediate value (recommendations)

---

### Journey 2: Daily Active User - Mood Check-In

```
1. User Opens App
   ↓
2. Quick Mood Check-In Prompt (Optional, dismissible)
   - "How are you feeling today?"
   - Mood selector (quick view: 6 common moods)
   - [Skip for now] option
   ↓
3. User Selects Mood: "Anxious"
   ↓
4. Intensity Slider
   - "How anxious? (1-10)"
   - Optional: "What's happening?" (text input)
   ↓
5. [Submit] → Loading animation (1 second)
   ↓
6. Home Feed Updates
   - "Based on how you're feeling..."
   - 5 fresh recommendations
   - Today's plan activity (if active plan exists)
   - Mood insights widget
   ↓
7. User Browses Recommendations
   ↓
8. User Selects "5-Minute Breathing Exercise"
   ↓
9. Content Detail Screen
   - Instructions
   - [Start Exercise] button
   - Duration: 5 minutes
   ↓
10. Guided Exercise (Timer + Instructions)
   ↓
11. Completion Screen
   - "Great job! 🎉"
   - "Did this help?" (👍 👎)
   - [Continue] button
   ↓
12. Optional: Post-Activity Mood Check
   - "How are you feeling now?"
   - Quick mood selector
   ↓
13. Return to Home Feed
```

**Duration:** 5-10 minutes  
**Engagement Hooks:**
- Streaks ("7 days in a row!")
- Progress badges
- Mood improvement visualization
- Personalized insights

---

### Journey 3: Creating & Following an Elevation Plan

```
1. User Opens App (Feeling: "Sad")
   ↓
2. Home Screen Shows:
   - Recent mood: Sad (7/10)
   - Recommendation feed
   - [Create Elevation Plan] CTA
   ↓
3. User Taps "Create Elevation Plan"
   ↓
4. Plan Creation Flow
   
   Step 1: Current Mood
   - "How are you feeling now?"
   - Mood: Sad ✓
   - Intensity: 7/10
   
   Step 2: Target Mood
   - "How do you want to feel?"
   - Options: Peaceful, Hopeful, Joyful, Energized, Content
   - Selection: Peaceful ✓
   
   Step 3: Duration
   - "How long can you commit?"
   - [ ] 1 Day - Quick reset
   - [✓] 7 Days - Build momentum
   - [ ] 30 Days - Transform your life
   
   Step 4: Preview
   - "Your Personalized Plan: Sad → Peaceful (7 days)"
   - Day 1: Acknowledge & Accept (3 activities)
   - Day 2: Begin Healing (3 activities)
   - ...
   - [Start My Plan] button
   ↓
5. Plan Active - Day 1
   - Home screen shows: "Day 1 of 7: Acknowledge & Accept"
   - Morning Activity: Psalm 34:18 (5 min)
   - Midday Activity: "Goodness of God" song (6 min)
   - Evening Activity: Journaling prompt (10 min)
   ↓
6. User Completes Morning Activity
   - Read verse
   - Reflect on meaning
   - [Mark Complete] ✓
   - "Did this help?" → Rate 1-5 stars
   ↓
7. Progress Updates
   - "1/3 activities complete today"
   - Visual progress bar
   - Streak counter updates
   ↓
8. Day 1 Complete
   - "Amazing! Day 1 complete 🎉"
   - Mood check-in: "How are you feeling now?"
   - Mood: Still sad but less intense (5/10)
   ↓
9. Day 2 Notification (Next Morning)
   - Push notification: "Good morning! Ready for Day 2?"
   - Opens to Day 2 activities
   ↓
10. Days 3-7: Continue Pattern
   ↓
11. Plan Complete (Day 7)
   - Celebration screen
   - Before/After mood comparison:
     - Started: Sad (7/10)
     - Now: Peaceful (8/10)
   - Insights: "What worked best for you"
     - Worship songs: 5/5 stars
     - Breathing exercises: 4/5 stars
     - Journaling: 3/5 stars
   - Options:
     - [Create New Plan]
     - [Continue Exploring]
     - [Share Progress]
```

**Duration:** 7 days, 10-15 min/day  
**Completion Drivers:**
- Daily push notifications
- Visual progress tracking
- Before/after mood comparison
- Personalized insights
- Celebration moments

---

### Journey 4: Discovering & Saving Content

```
1. User on Home Feed
   ↓
2. Recommendation Appears: "The Pursuit of Happyness" (Movie)
   - Thumbnail + Title
   - "Uplifting · Drama · 2h"
   - "For when you're feeling: Discouraged"
   ↓
3. User Taps Card
   ↓
4. Content Detail Screen
   - Movie poster
   - Description
   - "Why we recommend this: Based on your mood and preferences"
   - Tags: uplifting, perseverance, hope
   - User ratings: 4.8/5 (from other Mend users)
   - [Watch Trailer] (YouTube)
   - [Save for Later] (bookmark icon)
   - [Not Interested] (X icon)
   ↓
5. User Taps [Save for Later]
   - Animation: Bookmark fills in
   - Toast: "Saved to your library"
   ↓
6. Later: User Opens Profile → Saved Content
   - Sees all saved items
   - Organized by type (Verses, Songs, Movies, etc.)
   - Can remove from saved
   ↓
7. User Watches Movie (External: Netflix/Prime)
   ↓
8. Returns to App Next Day
   - Prompt: "Did 'The Pursuit of Happyness' help?"
   - Rate 1-5 stars
   - Helps improve future recommendations
```

---

## 6. Feature Specifications

### 6.1 Mood Tracking

**Priority:** P0 (Must Have)  
**Phase:** MVP (Phase 1)

#### Description
Core feature allowing users to log their emotional state with mood selection and intensity rating.

#### User Stories
- As a user, I want to quickly select my current mood so I get relevant recommendations
- As a user, I want to track my mood over time so I can see patterns
- As a user, I want to add context to my mood so recommendations are more accurate
- As a user, I want to see how my mood changes throughout the day

#### Functional Requirements

**Mood Options (10 Primary Moods):**
1. 😢 Sad
2. 😰 Anxious
3. 😴 Tired
4. 😔 Lonely
5. 😠 Angry
6. 😞 Weary
7. 😣 Stressed
8. 😊 Hopeful
9. 😌 Peaceful
10. ⚡ Energized

**Mood Check-In Flow:**
1. Mood selector (grid of emoji + labels)
2. Intensity slider (1-10 scale with visual feedback)
3. Optional context field (50 characters max, e.g., "work deadline")
4. Optional location tag (work, home, commute, etc.)
5. Submit button

**Mood History:**
- List view: Chronological mood entries
- Calendar view: Mood heatmap
- Graph view: Intensity over time
- Filter by date range (last 7 days, 30 days, all time)
- Export as PDF/CSV

**Quick Check-In:**
- 1-tap mood selection (skip intensity for speed)
- Accessible from any screen via floating action button
- Can skip check-in without penalty

#### Technical Specifications

**Database Model:**
```python
class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_entries')
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    intensity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    context = models.TextField(blank=True, null=True, max_length=200)
    location = models.CharField(max_length=100, blank=True, choices=LOCATION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', '-timestamp']),
            models.Index(fields=['mood']),
        ]
    
    def __str__(self):
        return f"{self.user.email} - {self.mood} ({self.intensity}/10) at {self.timestamp}"
```

**API Endpoints:**

POST `/api/moods/`
```json
Request:
{
  "mood": "anxious",
  "intensity": 7,
  "context": "work presentation today",
  "location": "work"
}

Response (201 Created):
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "mood": "anxious",
  "intensity": 7,
  "context": "work presentation today",
  "location": "work",
  "timestamp": "2025-01-15T09:30:00Z",
  "recommendations": [...]  // Immediate recommendations included
}
```

GET `/api/moods/`
```json
Query Parameters:
- start_date: ISO date (optional)
- end_date: ISO date (optional)
- mood: Filter by specific mood (optional)
- limit: Int, default 50
- offset: Int, default 0

Response (200 OK):
{
  "count": 145,
  "next": "/api/moods/?offset=50",
  "previous": null,
  "results": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "mood": "anxious",
      "intensity": 7,
      "context": "work presentation",
      "timestamp": "2025-01-15T09:30:00Z"
    },
    ...
  ],
  "summary": {
    "most_common_mood": "tired",
    "average_intensity": 6.2,
    "total_entries": 145,
    "current_streak": 12
  }
}
```

GET `/api/moods/insights/`
```json
Response (200 OK):
{
  "insights": [
    {
      "type": "time_pattern",
      "text": "You tend to feel most anxious on Monday mornings",
      "confidence": 0.87,
      "data_points": 23,
      "icon": "calendar"
    },
    {
      "type": "content_effectiveness",
      "text": "Worship songs improve your mood by 40% on average",
      "confidence": 0.92,
      "data_points": 34,
      "icon": "music"
    },
    {
      "type": "duration_pattern",
      "text": "Your mood typically improves after 15 minutes of activity",
      "confidence": 0.78,
      "data_points": 18,
      "icon": "clock"
    }
  ],
  "mood_distribution": {
    "anxious": 32,
    "tired": 28,
    "sad": 15,
    "peaceful": 25
  },
  "improvement_rate": 0.68  // 68% of check-ins show improvement after activity
}
```

#### UI/UX Requirements

**Mood Selector:**
- Grid layout: 3x4 (mobile) or 5x2 (tablet)
- Large touch targets (min 60x60 dp)
- Emoji + text label
- Haptic feedback on selection
- Color-coded by mood category:
  - Red tones: Angry, Stressed
  - Blue tones: Sad, Anxious, Lonely
  - Gray tones: Tired, Weary
  - Green/Yellow tones: Peaceful, Hopeful, Energized

**Intensity Slider:**
- Visual representation: 1 (light) → 10 (intense)
- Color gradient matching mood
- Numeric display
- Haptic feedback at intervals (2, 4, 6, 8, 10)

**Context Input:**
- Optional, clearly marked
- Placeholder text: "What's happening? (optional)"
- Character counter: 50/50
- Quick suggestions: "Work", "Family", "Health", "Finances"

**Mood History:**
- Tab navigation: List / Calendar / Graph
- Pull-to-refresh
- Empty state: Encouraging message + illustration
- Share functionality (screenshot with branding)

#### Success Metrics
- 70%+ daily active users complete mood check-in
- Average 2+ mood entries per day for engaged users
- < 30 seconds average time to complete check-in
- 10%+ users add context to mood entries
- 60%+ users return to view mood history weekly

#### Acceptance Criteria
- [ ] User can select from 10 mood options
- [ ] Intensity slider works smoothly (1-10)
- [ ] Optional context field saves correctly
- [ ] Mood entry saves to database
- [ ] Mood history displays chronologically
- [ ] Calendar view shows mood heatmap
- [ ] Graph view shows intensity trends
- [ ] Streaks update automatically
- [ ] Can access mood check-in from any screen
- [ ] Recommendations appear immediately after check-in

---

### 6.2 Content Recommendation Engine

**Priority:** P0 (Must Have)  
**Phase:** MVP (Phase 1)

#### Description
AI-powered system that matches user's current mood to relevant content across multiple types (verses, songs, movies, books, quotes, activities).

#### User Stories
- As a user, I want to see content that matches my current emotional state
- As a user, I want recommendations to learn my preferences over time
- As a user, I want variety in recommendations (not same content repeatedly)
- As a user, I want to discover new content types I might not have considered
- As a user, I want recommendations I can act on immediately

#### Functional Requirements

**Content Types Supported:**
1. **Bible Verses**
   - Text with reference
   - Translation options (NIV, ESV, NLT)
   - Reflection prompt
   - 2-5 minute read time

2. **Songs**
   - Spotify integration
   - Artist, album, duration
   - Play preview or full song
   - Lyrics snippet (optional)

3. **Quotes**
   - Inspirational quotes
   - Author attribution
   - Visual card (shareable)
   - 1 minute read time

4. **Movies**
   - TMDB integration
   - Poster, description, rating
   - Where to watch (Netflix, Prime, etc.)
   - Trailer link (YouTube)

5. **Books**
   - Google Books integration
   - Cover, description, author
   - Purchase/borrow links
   - Estimated read time

6. **Activities**
   - Guided exercises
   - Meditation, breathing, journaling
   - Step-by-step instructions
   - 5-30 minute duration

7. **Podcasts** (Phase 2)
   - Episode recommendations
   - Topic-matched
   - Audio player integration

**Recommendation Algorithm (v1 - MVP):**

```python
def generate_recommendations(user, current_mood, count=5):
    """
    Simple rule-based recommendation engine for MVP
    """
    # 1. Filter content by mood match
    content_pool = Content.objects.filter(
        Q(primary_moods__contains=[current_mood]) |
        Q(secondary_moods__contains=[current_mood])
    )
    
    # 2. Apply user preferences
    preferred_types = user.profile.preferred_content_types
    if preferred_types:
        content_pool = content_pool.filter(type__in=preferred_types)
    
    # 3. Exclude recently viewed (last 7 days)
    recent_interactions = UserInteraction.objects.filter(
        user=user,
        timestamp__gte=timezone.now() - timedelta(days=7)
    ).values_list('content_id', flat=True)
    content_pool = content_pool.exclude(id__in=recent_interactions)
    
    # 4. Score each item
    scored_content = []
    for content in content_pool:
        score = 0
        
        # Primary mood match (10 points)
        if current_mood in content.primary_moods:
            score += 10
        # Secondary mood match (5 points)
        elif current_mood in content.secondary_moods:
            score += 5
        
        # User has liked this type before (5 points)
        if user_has_liked_type(user, content.type):
            score += 5
        
        # High overall rating (0-5 points)
        score += content.user_rating_avg
        
        # Time-appropriate (2 points)
        if is_time_appropriate(content, current_time()):
            score += 2
        
        # Duration matches user availability (2 points)
        if content.duration_minutes <= user.profile.available_time_daily:
            score += 2
        
        scored_content.append((content, score))
    
    # 5. Sort by score
    scored_content.sort(key=lambda x: x[1], reverse=True)
    
    # 6. Diversify content types (don't return all verses)
    diverse_recommendations = diversify_by_type(scored_content, count)
    
    return diverse_recommendations

def diversify_by_type(scored_content, count):
    """
    Ensure mix of content types in recommendations
    """
    recommendations = []
    types_used = set()
    
    for content, score in scored_content:
        # Allow max 2 of same type in top 5
        if types_used.count(content.type) < 2:
            recommendations.append(content)
            types_used.add(content.type)
        
        if len(recommendations) >= count:
            break
    
    return recommendations
```

**Recommendation Refresh:**
- Manual refresh: Pull-to-refresh gesture
- Auto-refresh: After mood check-in
- Smart refresh: If user skips 3+ recommendations
- Timed refresh: Every 4 hours (max)

**Interaction Tracking:**
- Viewed: User opens content detail
- Liked: User gives thumbs up
- Completed: User marks activity as complete
- Saved: User bookmarks content
- Skipped: User swipes away or taps "Not interested"
- Helpful rating: 1-5 stars after interaction

#### Technical Specifications

**Database Models:**

```python
class Content(models.Model):
    CONTENT_TYPES = [
        ('verse', 'Bible Verse'),
        ('quote', 'Quote'),
        ('song', 'Song'),
        ('movie', 'Movie'),
        ('book', 'Book'),
        ('activity', 'Activity'),
        ('podcast', 'Podcast'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    title = models.CharField(max_length=500)
    description = models.TextField()
    content_data = models.JSONField()  # Flexible schema per type
    
    # Mood matching
    primary_moods = ArrayField(models.CharField(max_length=50))
    secondary_moods = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    tags = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    
    # Metadata
    duration_minutes = models.IntegerField(null=True, blank=True)
    external_id = models.CharField(max_length=255, blank=True)  # Spotify ID, TMDB ID, etc.
    thumbnail_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    
    # Quality signals
    admin_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    user_rating_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    interaction_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['type', 'primary_moods']),
            models.Index(fields=['user_rating_avg']),
        ]

class UserInteraction(models.Model):
    INTERACTION_TYPES = [
        ('viewed', 'Viewed'),
        ('liked', 'Liked'),
        ('completed', 'Completed'),
        ('saved', 'Saved'),
        ('skipped', 'Skipped'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    mood_at_interaction = models.CharField(max_length=50)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    helpfulness_rating = models.IntegerField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'content']),
            models.Index(fields=['user', 'mood_at_interaction']),
            models.Index(fields=['-timestamp']),
        ]
```

**API Endpoints:**

GET `/api/recommendations/`
```json
Query Parameters:
- mood: string (optional, uses latest mood if not provided)
- count: int, default 5
- exclude_types: comma-separated list (optional)
- refresh: boolean, default false (force new recommendations)

Response (200 OK):
{
  "recommendations": [
    {
      "id": "content-uuid",
      "type": "verse",
      "title": "Philippians 4:6-7",
      "description": "Do not be anxious about anything...",
      "content": {
        "text": "Do not be anxious about anything, but in every situation...",
        "reference": "Philippians 4:6-7",
        "translation": "NIV"
      },
      "thumbnail": "https://cdn.mend.com/verses/phil-4-6.jpg",
      "duration_minutes": 2,
      "confidence": 0.94,
      "reasoning": "This verse has helped you before when feeling anxious",
      "tags": ["peace", "prayer", "anxiety"]
    },
    {
      "id": "content-uuid-2",
      "type": "song",
      "title": "Way Maker - Sinach",
      "description": "Uplifting worship song",
      "content": {
        "artist": "Sinach",
        "album": "Way Maker",
        "spotify_uri": "spotify:track:abc123",
        "preview_url": "https://p.scdn.co/preview.mp3",
        "duration_ms": 324000
      },
      "thumbnail": "https://i.scdn.co/image/album-art.jpg",
      "duration_minutes": 5,
      "confidence": 0.89,
      "tags": ["worship", "uplifting", "faith"]
    },
    {
      "id": "content-uuid-3",
      "type": "activity",
      "title": "5-Minute Box Breathing",
      "description": "Calm your nervous system with this simple technique",
      "content": {
        "instructions": [
          "Find a comfortable seated position",
          "Breathe in for 4 counts",
          "Hold for 4 counts",
          "Breathe out for 4 counts",
          "Hold for 4 counts",
          "Repeat for 5 minutes"
        ],
        "difficulty": "beginner",
        "audio_guide_url": "https://cdn.mend.com/audio/box-breathing.mp3"
      },
      "duration_minutes": 5,
      "confidence": 0.85,
      "tags": ["breathing", "meditation", "quick"]
    }
  ],
  "based_on": {
    "mood": "anxious",
    "intensity": 7,
    "timestamp": "2025-01-15T14:30:00Z",
    "user_preferences": {
      "preferred_types": ["verse", "song", "activity"],
      "faith_preference": "christian"
    }
  },
  "refresh_available_in": 3600  // seconds until can refresh
}
```

POST `/api/recommendations/{id}/interact/`
```json
Request:
{
  "interaction_type": "completed",  // viewed, liked, completed, saved, skipped
  "helpfulness_rating": 4,  // 1-5, optional
  "notes": "Really helped me calm down"  // optional
}

Response (200 OK):
{
  "message": "Interaction recorded",
  "updated_recommendations": true,  // Will affect future recommendations
  "streak_updated": false
}
```

#### UI/UX Requirements

**Recommendation Feed:**
- Vertical scrolling list of cards
- Card components vary by content type
- Large, tappable cards (min 280dp height)
- Image/thumbnail prominent
- Quick actions: Save, Skip, Share
- Loading skeleton while fetching
- Pull-to-refresh gesture
- Empty state: "Getting personalized recommendations..."

**Content Cards by Type:**

**Verse Card:**
- Verse text (truncated if long)
- Reference (Psalm 23:4)
- Translation badge (NIV)
- Estimated read time
- Save icon (bookmark)
- Share icon

**Song Card:**
- Album art
- Song title + artist
- Duration
- Play button (Spotify integration)
- Save icon
- Mood tags

**Activity Card:**
- Illustration/icon
- Activity title
- Duration + difficulty
- "Start" button
- Brief description
- Save icon

**Movie Card:**
- Movie poster
- Title + year
- Rating (stars)
- Duration
- "Watch Trailer" button
- Save for later

**Interaction Feedback:**
- Haptic feedback on all interactions
- Save animation (bookmark fills)
- Skip animation (card swipes away)
- Like animation (heart appears)
- Toast messages ("Saved to your library")

#### Success Metrics
- 60%+ recommendation engagement rate (user interacts with content)
- 70%+ "helpful" ratings (4-5 stars)
- Users return within 24 hours after helpful recommendation
- < 1 second recommendation generation time
- 40%+ users save at least 1 piece of content weekly
- 20%+ users explore multiple content types

#### Acceptance Criteria
- [ ] Returns 5 relevant recommendations for any mood
- [ ] Mixes content types (no more than 2 of same type)
- [ ] Excludes recently viewed content (7 days)
- [ ] Respects user content type preferences
- [ ] Matches mood intensity (calming for high intensity)
- [ ] Response time < 500ms
- [ ] Can refresh recommendations manually
- [ ] Tracks all user interactions
- [ ] Updates recommendations based on interaction history
- [ ] Gracefully handles no matching content (fallback to popular)

---

### 6.3 Elevation Plans

**Priority:** P1 (Should Have)  
**Phase:** Phase 2 (Post-MVP)

#### Description
Structured, multi-day programs that guide users from their current emotional state to a desired target state through daily activities and content.

#### User Stories
- As a user, I want a structured plan so I don't have to decide what to do each day
- As a user, I want to choose plan duration based on my commitment level
- As a user, I want daily reminders to stay on track
- As a user, I want to see my progress visually
- As a user, I want to understand how the plan is helping me
- As a user, I want flexibility to skip or reschedule activities

#### Functional Requirements

**Plan Durations:**
- 1-day: Quick emotional reset
- 7-day: Build momentum and habits
- 30-day: Transformative journey

**Plan Creation Flow:**
1. Assess current mood (or use latest mood entry)
2. Select target mood from list
3. Choose duration (1/7/30 days)
4. Review generated plan preview
5. Customize (optional): Swap activities, set reminder times
6. Confirm and activate plan

**Daily Structure:**
Each day includes 3 scheduled activities:
- **Morning (7-9 AM):** Verse/quote + reflection (5-10 min)
- **Midday (12-2 PM):** Song, exercise, or short activity (5-15 min)
- **Evening (7-9 PM):** Longer content (movie, book, meditation) (15-60 min)

Plus optional "anytime" activities (bonus challenges)

**Plan Themes (Arc Over Duration):**
- **Days 1-2:** Acknowledge & Accept
  - Validate current feelings
  - Create space for healing
  
- **Days 3-5:** Engage & Grow (7-day) or Days 3-20 (30-day)
  - Active participation
  - Building new patterns
  - Exploring different modalities
  
- **Days 6-7 (7-day) or 21-30 (30-day):** Celebrate & Sustain
  - Recognize progress
  - Establish maintenance practices
  - Plan for continued wellness

**Mood Progression:**
Plans calculate gradual mood improvement:
```
Example: Sad (7/10) → Peaceful (8/10) over 7 days
Day 1: Sad (7) - Acknowledge sadness
Day 2: Sad (6) - Begin processing
Day 3: Melancholic (5) - Opening to change
Day 4: Neutral (5) - Finding stability
Day 5: Calm (6) - Growing peace
Day 6: Peaceful (7) - Deepening serenity
Day 7: Peaceful (8) - Sustained peace
```

**Activity Completion:**
- Mark activity as complete (checkmark)
- Optional: Rate helpfulness (1-5 stars)
- Optional: Add reflection note
- Streak tracking (consecutive days)