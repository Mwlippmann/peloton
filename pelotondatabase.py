from sqlalchemy import *

metadata = MetaData()
engine = create_engine('sqlite:///data/pelotondb.sqlite')

def create_database(data=None):
    # Creates or opens a file called mydb with a SQLite3 DB
    user = Table(
        'user',
        metadata,
        Column('birthday', Integer()),
        Column('block_explicit', Boolean()),
        Column('can_charge', Boolean()),
        Column('created_at', DateTime()),
        Column('created_country', String(255)),
        Column('customized_max_heart_rate', Integer()),
        Column('cycling_ftp', Integer()),
        Column('cycling_ftp_source', String(255)),
        Column('cycling_ftp_workout_id', String(255)),
        Column('cycling_workout_ftp', Integer()),
        Column('default_max_heart_rate', Integer()),
        Column('email', String(255)),
        Column('estimated_cycling_ftp', Integer()),
        Column('facebook_access_token', String(255)),
        Column('facebook_id', String(255)),
        Column('first_name', String(255)),
        Column('gender', String(255)),
        Column('hardware_settings', String(255)),
        Column('has_active_device_subscription', Boolean()),
        Column('has_active_digital_subscription', Boolean()),
        Column('has_signed_waiver', Boolean()),
        Column('height', Float()),
        Column('id', String(255), primary_key=True),
        Column('image_url', String(255)),
        Column('instructor_id', String(255)),
        Column('is_complete_profile', Boolean()),
        Column('is_demo', Boolean()),
        Column('is_me', Boolean()),
        Column('is_external_beta_tester', Boolean()),
        Column('is_fitbit_authenticated', Boolean()),
        Column('is_internal_beta_tester', Boolean()),
        Column('is_profile_private', Boolean()),
        Column('is_provisional', Boolean()),
        Column('is_strava_authenticated', Boolean()),
        Column('last_name', String(255)),
        Column('last_workout_at', Integer()),
        Column('location', String(255)),
        Column('middle_initial', String(255)),
        Column('name', String(255)),
        Column('obfuscated_email', String(255)),
        Column('phone_number', Integer()),
        Column('referrals_made', Integer()),
        Column('total_followers', Integer()),
        Column('total_following', Integer()),
        Column('total_non_pedaling_metric_workouts', Integer()),
        Column('total_pedaling_metric_workouts', Integer()),
        Column('total_pending_followers', Integer()),
        Column('total_workouts', Integer()),
        Column('username', String(255)),
        Column('v1_referrals_made', Integer()),
        Column('weight', Float()),
    )
    workout = Table('workout', metadata,
        Column('created', DateTime()),
        Column('created_at', DateTime()),
        Column('device_time_created_at', DateTime()),
        Column('device_type', String(255)),
        Column('device_type_display_name', String(255)),
        Column('end_time', DateTime()),
        Column('fitbit_id', String(255)),
        Column('fitness_discipline', String(255)),
        Column('has_leaderboard_metrics', Boolean()),
        Column('has_pedaling_metrics', Boolean()),
        Column('id', String(255), primary_key=True),
        Column('is_total_work_personal_record', Boolean()),
        Column('leaderboard_rank', Integer()),
        Column('metrics_type', String(255)),
        Column('name', String(255)),
        Column('peloton_id', String(255)),
        Column('platform', String(255)),
        Column('start_time', DateTime()),
        Column('status', String(255)),
        Column('strava_id', String(255)),
        Column('timezone', String(255)),
        Column('title', String(255)),
        Column('total_leaderboard_users', Integer()),
        Column('total_work', Float()),
        Column('user_id', String(255), ForeignKey("user.id"), nullable=False),
        Column('workout_type', String(255)),
    )
    ride = Table('ride', metadata,
        Column('content_format', String(255)),
        Column('content_provider', String(255)),
        Column('description', String(255)),
        Column('difficulty_estimate', String(255)),
        Column('difficulty_level', String(255)),
        Column('difficulty_rating_avg', Float()),
        Column('difficulty_rating_count', Integer()),
        Column('duration', Integer()),
        Column('fitness_discipline', String(255)),
        Column('fitness_discipline_display_name', String(255)),
        Column('has_closed_captions', Boolean()),
        Column('has_free_mode', Boolean()),
        Column('has_pedaling_metrics', Boolean()),
        Column('home_peloton_id', String(255)),
        Column('id', String(255), primary_key=True),
        Column('workout_id', String(255), ForeignKey("workout.id"), nullable=False),
        Column('image_url', String(255)),
        Column('instructor_id', String(255)),
        Column('is_archived', Boolean()),
        Column('is_closed_caption_shown', Boolean()),
        Column('is_explicit', Boolean()),
        Column('is_live_in_studio_only', Boolean()),
        Column('language', String(255)),
        Column('length', Integer()),
        Column('live_stream_id', String(255)),
        Column('live_stream_url', String(255)),
        Column('location', String(255)),
        Column('origin_locale', String(255)),
        Column('original_air_time', DateTime()),
        Column('overall_estimate', Float()),
        Column('overall_rating_avg', Float()),
        Column('overall_rating_count', Integer()),
        Column('pedaling_duration', Integer()),
        Column('pedaling_end_offset', Integer()),
        Column('pedaling_start_offset', Integer()),
        Column('rating', Integer()),
        Column('ride_type_id', String(255)),
        Column('sample_vod_stream_url', String(255)),
        Column('scheduled_start_time', DateTime()),
        Column('series_id', String(255)),
        Column('sold_out', Boolean()),
        Column('studio_peloton_id', String(255)),
        Column('title', String(255)),
        Column('total_in_progress_workouts', Integer()),
        Column('total_ratings', Integer()),
        Column('total_workouts', Integer()),
        Column('vod_stream_id', String(255)),
        Column('vod_stream_url', String(255)),
    )
    connection = engine.connect()
    metadata.create_all(engine)

def insert_user(data):
    table_names = inspect(engine).get_table_names()
    user_id = data['id']
    #first we check if the table exists
    if 'user' not in table_names:
        create_database()
    else:
        #we check if a user with the id already exists
        connection = engine.connect()
        user = Table('user', metadata, autoload=True, autoload_with=engine)
        stmt = select([user]).where(user.columns.id == user_id)
        result = connection.execute(stmt).fetchall()
        if len(result)>0:
            print('User with id %s already exists in the database.' % user_id)
        else:
            stmt = insert(user).values(**data)
            result_proxy = connection.execute(stmt)
    return(user_id)

'''
This function returns the user id of the 'is_me' user.
If it does not exist, it returns False.
'''
def get_user_id():
    table_names = inspect(engine).get_table_names()
    if 'user' not in table_names:
        return(False)
    else:
        connection = engine.connect()
        user = Table('user', metadata, autoload=True, autoload_with=engine)
        stmt = select([user]).where(user.columns.is_me == True)
        result = connection.execute(stmt).fetchall()
        if len(result)>0:
            user_id = result[0].id
            return(user_id)
        else:
            return False

def insert_workouts(values_list):
    workout_count = len(values_list)
    user_id = values_list[0]['user_id']
    connection = engine.connect()
    workout = Table('workout', metadata, autoload=True, autoload_with=engine)
    stmt = select([workout]).where(workout.columns.user_id == user_id)
    result = connection.execute(stmt).fetchall()
    if len(result) == workout_count:
        print('All workouts are already in the database')
    else:
        stmt = insert(workout)
        result_proxy = connection.execute(stmt, values_list)


def get_workoutids(user_id):
    connection = engine.connect()
    workout = Table('workout', metadata, autoload=True, autoload_with=engine)
    workout_ids = []
    stmt = select([workout]).where(workout.columns.user_id == user_id)
    results = connection.execute(stmt).fetchall()
    for result in results:
        workout_ids.append(result.id)
    return(workout_ids)


def update_workout(values_list):
    workout_id = values_list['id']
    connection = engine.connect()
    workout = Table('workout', metadata, autoload=True, autoload_with=engine)
    update_stmt = update(workout).values(**values_list)
    update_stmt = update_stmt.where(workout.columns.id == workout_id)
    update_results = connection.execute(update_stmt)


def upsert_rides(values_list):
    connection = engine.connect()
    ride = Table('ride', metadata, autoload=True, autoload_with=engine)
    for ride_data in values_list:
        ride_id = ride_data['id']
        stmt = select([ride]).where(ride.columns.id == ride_id)
        result = connection.execute(stmt).fetchall()
        if len(result) == 1:
            stmt = update(ride).values(**ride_data)
            stmt = stmt.where(ride.columns.id == ride_id)
        elif len(result) == 0:
            stmt = insert(ride).values(**ride_data)
        results = connection.execute(stmt)


def get_ride_output(user_id):
    connection = engine.connect()
    workouts = Table('workout', metadata, autoload=True, autoload_with=engine)
    rides = Table('ride', metadata, autoload=True, autoload_with=engine)
    columns = [
        workouts.columns.start_time, workouts.columns.name,
        rides.columns.duration, workouts.columns.total_work,
        rides.columns.title, rides.columns.original_air_time
    ]
    stmt = select(columns)
    stmt = stmt.select_from(workouts.join(rides)).order_by(asc(workouts.columns.total_work)).order_by(asc(rides.columns.duration))
    results = connection.execute(stmt).fetchall()
    output = []
    for result in results:
        item_list = list(result)
        item_list[0] = result[0].strftime("%A, %d %b %Y")
        item_list[2] = '%s minutes' % str(round(result[2]/60))
        item_list[3] = '%s kj' % str(round(result[3]/1000))
        if len(item_list)==6 and item_list[5] is not None:
            item_list[5] = result[5].strftime("%A, %d %b %Y")
        output.append(item_list)
    return(output)

