from sqlalchemy import *

metadata = MetaData()

def create_database(data=None):
    # Creates or opens a file called mydb with a SQLite3 DB
    engine = create_engine('sqlite:///data/pelotondb.sqlite')
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
        Column('end_time', DateTime()),
        Column('fitbit_id', String(255)),
        Column('fitness_discipline', String(255)),
        Column('has_leaderboard_metrics', Boolean()),
        Column('has_pedaling_metrics', Boolean()),
        Column('id', String(255), primary_key=True),
        Column('is_total_work_personal_record', Boolean()),
        Column('metrics_type', String(255)),
        Column('name', String(255)),
        Column('peloton_id', String(255)),
        Column('platform', String(255)),
        Column('start_time', DateTime()),
        Column('status', String(255)),
        Column('strava_id', String(255)),
        Column('timezone', String(255)),
        Column('title', String(255)),
        Column('total_work', Float()),
        Column('user_id', String(255), ForeignKey("user.id"), nullable=False),
        Column('workout_type', String(255)),
)
    connection = engine.connect()
    metadata.create_all(engine)

def insert_user(data):
    engine = create_engine('sqlite:///data/pelotondb.sqlite')
    table_names = inspect(engine).get_table_names()
    user_id = data['id']
    #first we check if the table exists
    if 'user' not in table_names:
        create_database()
    else:
        #we check if a user with the id already exists
        connection = engine.connect()
        metadata = MetaData()
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
    engine = create_engine('sqlite:///data/pelotondb.sqlite')
    table_names = inspect(engine).get_table_names()
    if 'user' not in table_names:
        return(False)
    else:
        connection = engine.connect()
        metadata = MetaData()
        user = Table('user', metadata, autoload=True, autoload_with=engine)
        stmt = select([user]).where(user.columns.is_me == True)
        result = connection.execute(stmt).fetchall()
        if len(result)>0:
            user_id = result[0].id
            return(user_id)
        else:
            return False

def count_workouts(user_id):
    pass
