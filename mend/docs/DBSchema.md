// Mend - Database Schema
// Copy this to https://dbdiagram.io to visualize

Table user_profiles {
  id uuid [pk, note: 'References Supabase auth.users']
  faith_preference varchar(50) [default: 'christian']
  preferred_content_types text[] [note: 'Array: verse, song, movie, etc']
  music_genres text[]
  movie_genres text[]
  available_time_daily int [default: 15, note: 'Minutes per day']
  morning_notification_time time [default: '07:00:00']
  midday_notification_time time [default: '12:00:00']
  evening_notification_time time [default: '19:00:00']
  notifications_enabled boolean [default: true]
  onboarding_completed boolean [default: false]
  total_mood_entries int [default: 0]
  total_content_interactions int [default: 0]
  created_at timestamp [default: `now()`]
  updated_at timestamp [default: `now()`]
  
  indexes {
    id
  }
}

Table mood_entries {
  id uuid [pk]
  user_id uuid [ref: > user_profiles.id, note: 'ON DELETE CASCADE']
  mood varchar(50) [not null, note: 'sad, anxious, tired, etc']
  intensity int [not null, note: '1-10 scale']
  context text [note: 'Optional user note']
  location varchar(100) [note: 'work, home, etc']
  timestamp timestamp [default: `now()`]
  
  indexes {
    (user_id, timestamp) [name: 'idx_user_timestamp']
  }
}

Table content {
  id uuid [pk]
  type varchar(20) [not null, note: 'verse, quote, song, movie, book, activity, podcast']
  title varchar(500) [not null]
  description text
  content_data jsonb [note: 'Flexible schema per content type']
  primary_moods text[] [not null, note: 'Primary mood matches']
  secondary_moods text[] [note: 'Secondary mood matches']
  tags text[]
  duration_minutes int
  external_id varchar(255) [note: 'Spotify ID, TMDB ID, etc']
  thumbnail_url text
  source_url text
  admin_rating decimal(3,2) [default: 0]
  user_rating_avg decimal(3,2) [default: 0]
  interaction_count int [default: 0]
  created_at timestamp [default: `now()`]
  updated_at timestamp [default: `now()`]
  
  indexes {
    (type, primary_moods) [name: 'idx_type_moods']
    primary_moods [name: 'idx_mood_lookup']
  }
}

Table user_interactions {
  id uuid [pk]
  user_id uuid [ref: > user_profiles.id, note: 'ON DELETE CASCADE']
  content_id uuid [ref: > content.id, note: 'ON DELETE CASCADE']
  mood_at_interaction varchar(50)
  interaction_type varchar(20) [note: 'viewed, liked, completed, saved, skipped']
  helpfulness_rating int [note: '1-5 scale, optional']
  timestamp timestamp [default: `now()`]
  
  indexes {
    (user_id, content_id) [name: 'idx_user_content']
    (user_id, mood_at_interaction) [name: 'idx_user_mood']
  }
}

Table elevation_plans {
  id uuid [pk]
  user_id uuid [ref: > user_profiles.id, note: 'ON DELETE CASCADE']
  start_date date [not null]
  duration_days int [not null]
  current_mood varchar(50) [not null]
  target_mood varchar(50) [not null]
  status varchar(20) [default: 'active', note: 'active, completed, paused, abandoned']
  created_at timestamp [default: `now()`]
  completed_at timestamp
  
  indexes {
    (user_id, status) [name: 'idx_user_status']
  }
}

Table plan_days {
  id uuid [pk]
  plan_id uuid [ref: > elevation_plans.id, note: 'ON DELETE CASCADE']
  day_number int [not null]
  date date [not null]
  completed boolean [default: false]
  mood_check_in varchar(50)
  
  indexes {
    (plan_id, day_number) [unique, name: 'unique_plan_day']
  }
}

Table plan_activities {
  id uuid [pk]
  plan_day_id uuid [ref: > plan_days.id, note: 'ON DELETE CASCADE']
  content_id uuid [ref: > content.id, note: 'ON DELETE CASCADE']
  time_slot varchar(20) [note: 'morning, midday, evening, anytime']
  scheduled_time time
  completed boolean [default: false]
  completed_at timestamp
  helpfulness_rating int [note: '1-5 scale']
}

Table mood_insights {
  id uuid [pk]
  user_id uuid [ref: > user_profiles.id, note: 'ON DELETE CASCADE']
  insight_type varchar(50) [note: 'content_effectiveness, time_pattern, etc']
  insight_text text
  confidence decimal(3,2)
  data_points int [note: 'Number of data points analyzed']
  created_at timestamp [default: `now()`]
}

Table user_streaks {
  user_id uuid [pk, ref: - user_profiles.id, note: 'One-to-one, ON DELETE CASCADE']
  current_streak int [default: 0]
  longest_streak int [default: 0]
  last_check_in date
}

Table saved_content {
  id uuid [pk]
  user_id uuid [ref: > user_profiles.id, note: 'ON DELETE CASCADE']
  content_id uuid [ref: > content.id, note: 'ON DELETE CASCADE']
  saved_at timestamp [default: `now()`]
  
  indexes {
    (user_id, content_id) [unique, name: 'unique_user_content']
  }
}

// Relationships Summary:
// - user_profiles (1) → (many) mood_entries
// - user_profiles (1) → (many) user_interactions
// - user_profiles (1) → (many) elevation_plans
// - user_profiles (1) → (1) user_streaks
// - content (1) → (many) user_interactions
// - elevation_plans (1) → (many) plan_days
// - plan_days (1) → (many) plan_activities
// - content (1) → (many) plan_activities