from datetime import datetime
import pytz


def filter_data(input_data, input_filter):
    output = {}
    timezone = False
    if 'timezone' in input_data:
        timezone = input_data['timezone'] 
    for item, value in input_data.items():
        if item in input_filter['items']:
            output[item] = value
        elif item in input_filter['dates']:
            if timezone:
                output[item] = datetime.fromtimestamp(value,pytz.timezone(timezone))
            else:
                output[item] = datetime.utcfromtimestamp(value)
    return (output)


user_filter = {
    "items": [
        "birthday",
        "block_explicit",
        "can_charge",
        "created_country",
        "customized_max_heart_rate",
        "cycling_ftp",
        "cycling_ftp_source",
        "cycling_ftp_workout_id",
        "cycling_workout_ftp",
        "default_max_heart_rate",
        "email",
        "estimated_cycling_ftp",
        "facebook_access_token",
        "facebook_id",
        "first_name",
        "gender",
        "hardware_settings",
        "has_active_device_subscription",
        "has_active_digital_subscription",
        "has_signed_waiver",
        "height",
        "id",
        "image_url",
        "instructor_id",
        "is_complete_profile",
        "is_demo",
        "is_external_beta_tester",
        "is_fitbit_authenticated",
        "is_internal_beta_tester",
        "is_profile_private",
        "is_provisional",
        "is_strava_authenticated",
        "last_name",
        "last_workout_at",
        "location",
        "middle_initial",
        "name",
        "obfuscated_email",
        "phone_number",
        "referrals_made",
        "total_followers",
        "total_following",
        "total_non_pedaling_metric_workouts",
        "total_pedaling_metric_workouts",
        "total_pending_followers",
        "total_workouts",
        "username",
        "v1_referrals_made",
        "weight",
    ],
    "dates": ["created_at"]
}

workout_filter = {
    "items": [
        "device_type",
        "fitbit_id",
        "fitness_discipline",
        "has_leaderboard_metrics",
        "has_pedaling_metrics",
        "id",
        "is_total_work_personal_record",
        "metrics_type",
        "name",
        "peloton_id",
        "total_leaderboard_users",
        "leaderboard_rank",
        "device_type_display_name",
        "platform",
        "status",
        "strava_id",
        "timezone",
        "title",
        "total_work",
        "user_id",
        "workout_type",
    ],
    "dates": [
        "created",
        "end_time",
        "created_at",
        "device_time_created_at",
        "start_time",
    ],
}
ride_filter = {
    "items": [
        "content_format",
        "content_provider",
        "description",
        "difficulty_estimate",
        "difficulty_level",
        "difficulty_rating_avg",
        "difficulty_rating_count",
        "duration",
        "fitness_discipline",
        "fitness_discipline_display_name",
        "has_closed_captions",
        "has_free_mode",
        "has_pedaling_metrics",
        "home_peloton_id",
        "id",
        "workout_id",
        "image_url",
        "instructor_id",
        "is_archived",
        "is_closed_caption_shown",
        "is_explicit",
        "is_live_in_studio_only",
        "language",
        "length",
        "live_stream_id",
        "live_stream_url",
        "location",
        "origin_locale",
        "overall_estimate",
        "overall_rating_avg",
        "overall_rating_count",
        "pedaling_duration",
        "pedaling_end_offset",
        "pedaling_start_offset",
        "rating",
        "ride_type_id",
        "sample_vod_stream_url",
        "series_id",
        "sold_out",
        "studio_peloton_id",
        "title",
        "total_in_progress_workouts",
        "total_ratings",
        "total_workouts",
        "vod_stream_id",
        "vod_stream_url",
    ],
    "dates": [
        "scheduled_start_time",
        "original_air_time",
    ],
}
following_filter = {
    "items": [
        "authed_user_follows",
        "category",
        "id",
        "image_url",
        "is_profile_private",
        "location",
        "total_followers",
        "total_following",
        "total_workouts",
        "username",
    ],
    "dates": []
}
