from datetime import datetime

def filter_data(input_data,input_filter):
    output = {}
    for item,value in input_data.items():
        if item in input_filter['items']:
            output[item] = value
        elif item in input_filter['dates']:
            output[item] =  datetime.utcfromtimestamp(value)
    return(output)


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
        "end_time",
        "fitbit_id",
        "fitness_discipline",
        "has_leaderboard_metrics",
        "has_pedaling_metrics",
        "id",
        "is_total_work_personal_record",
        "metrics_type",
        "name",
        "peloton_id",
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
        "created_at",
        "device_time_created_at",
        "start_time",
    ],
}
