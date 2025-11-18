"""
Django management command to populate the octofit_db database with superhero test data.
"""
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        self.stdout.write(self.style.SUCCESS('Connected to MongoDB'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email field
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))

        # Insert Teams
        self.stdout.write('Inserting teams...')
        teams_data = [
            {
                '_id': 'team_marvel',
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': datetime.now(),
                'members_count': 0
            },
            {
                '_id': 'team_dc',
                'name': 'Team DC',
                'description': 'Justice League United',
                'created_at': datetime.now(),
                'members_count': 0
            }
        ]
        db.teams.insert_many(teams_data)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(teams_data)} teams'))

        # Insert Users (Superheroes)
        self.stdout.write('Inserting users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'alias': 'Iron Man', 'email': 'tony.stark@avengers.com', 'power': 'Genius, Powered Armor'},
            {'name': 'Steve Rogers', 'alias': 'Captain America', 'email': 'steve.rogers@avengers.com', 'power': 'Super Soldier Serum'},
            {'name': 'Thor Odinson', 'alias': 'Thor', 'email': 'thor@asgard.com', 'power': 'God of Thunder'},
            {'name': 'Natasha Romanoff', 'alias': 'Black Widow', 'email': 'natasha@avengers.com', 'power': 'Master Spy'},
            {'name': 'Bruce Banner', 'alias': 'Hulk', 'email': 'bruce.banner@avengers.com', 'power': 'Super Strength'},
            {'name': 'Peter Parker', 'alias': 'Spider-Man', 'email': 'peter.parker@dailybugle.com', 'power': 'Spider Powers'},
        ]

        dc_heroes = [
            {'name': 'Clark Kent', 'alias': 'Superman', 'email': 'clark.kent@dailyplanet.com', 'power': 'Super Strength, Flight'},
            {'name': 'Bruce Wayne', 'alias': 'Batman', 'email': 'bruce.wayne@wayneent.com', 'power': 'Detective, Martial Arts'},
            {'name': 'Diana Prince', 'alias': 'Wonder Woman', 'email': 'diana@themyscira.com', 'power': 'Amazon Warrior'},
            {'name': 'Barry Allen', 'alias': 'The Flash', 'email': 'barry.allen@starlabs.com', 'power': 'Super Speed'},
            {'name': 'Arthur Curry', 'alias': 'Aquaman', 'email': 'arthur@atlantis.com', 'power': 'Underwater, Super Strength'},
            {'name': 'Hal Jordan', 'alias': 'Green Lantern', 'email': 'hal.jordan@oa.com', 'power': 'Power Ring'},
        ]

        users_data = []
        user_id = 1

        for hero in marvel_heroes:
            users_data.append({
                '_id': f'user_{user_id}',
                'name': hero['name'],
                'alias': hero['alias'],
                'email': hero['email'],
                'power': hero['power'],
                'team': 'team_marvel',
                'joined_at': datetime.now() - timedelta(days=random.randint(1, 365)),
                'total_workouts': 0,
                'total_calories_burned': 0
            })
            user_id += 1

        for hero in dc_heroes:
            users_data.append({
                '_id': f'user_{user_id}',
                'name': hero['name'],
                'alias': hero['alias'],
                'email': hero['email'],
                'power': hero['power'],
                'team': 'team_dc',
                'joined_at': datetime.now() - timedelta(days=random.randint(1, 365)),
                'total_workouts': 0,
                'total_calories_burned': 0
            })
            user_id += 1

        db.users.insert_many(users_data)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(users_data)} users'))

        # Update team member counts
        db.teams.update_one({'_id': 'team_marvel'}, {'$set': {'members_count': len(marvel_heroes)}})
        db.teams.update_one({'_id': 'team_dc'}, {'$set': {'members_count': len(dc_heroes)}})

        # Insert Activities and Workouts
        self.stdout.write('Inserting activities and workouts...')
        activity_types = [
            'Flying', 'Running', 'Swimming', 'Fighting', 'Training',
            'Weightlifting', 'Cardio', 'Meditation', 'Combat Practice'
        ]

        activities_data = []
        workouts_data = []
        activity_id = 1
        workout_id = 1

        for user in users_data:
            num_activities = random.randint(5, 15)
            total_calories = 0
            
            for _ in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(15, 120)
                calories = duration * random.randint(5, 15)
                total_calories += calories
                
                activity_date = datetime.now() - timedelta(days=random.randint(0, 90))
                
                activity = {
                    '_id': f'activity_{activity_id}',
                    'user_id': user['_id'],
                    'user_name': user['name'],
                    'user_alias': user['alias'],
                    'team': user['team'],
                    'activity_type': activity_type,
                    'duration_minutes': duration,
                    'calories_burned': calories,
                    'date': activity_date,
                    'notes': f'{user["alias"]} performed {activity_type.lower()}'
                }
                activities_data.append(activity)
                
                # Create corresponding workout
                workout = {
                    '_id': f'workout_{workout_id}',
                    'user_id': user['_id'],
                    'activity_id': f'activity_{activity_id}',
                    'exercise': activity_type,
                    'duration': duration,
                    'calories': calories,
                    'intensity': random.choice(['Low', 'Medium', 'High', 'Extreme']),
                    'date': activity_date
                }
                workouts_data.append(workout)
                
                activity_id += 1
                workout_id += 1
            
            # Update user's total workouts and calories
            db.users.update_one(
                {'_id': user['_id']},
                {'$set': {
                    'total_workouts': num_activities,
                    'total_calories_burned': total_calories
                }}
            )

        db.activities.insert_many(activities_data)
        db.workouts.insert_many(workouts_data)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(activities_data)} activities'))
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(workouts_data)} workouts'))

        # Generate Leaderboard
        self.stdout.write('Generating leaderboard...')
        
        # Individual leaderboard
        users_with_stats = list(db.users.find().sort('total_calories_burned', -1))
        individual_leaderboard = []
        
        for rank, user in enumerate(users_with_stats, 1):
            individual_leaderboard.append({
                '_id': f'leader_individual_{rank}',
                'type': 'individual',
                'rank': rank,
                'user_id': user['_id'],
                'name': user['name'],
                'alias': user['alias'],
                'team': user['team'],
                'total_workouts': user['total_workouts'],
                'total_calories_burned': user['total_calories_burned'],
                'updated_at': datetime.now()
            })
        
        # Team leaderboard
        marvel_total = sum(u['total_calories_burned'] for u in users_with_stats if u['team'] == 'team_marvel')
        dc_total = sum(u['total_calories_burned'] for u in users_with_stats if u['team'] == 'team_dc')
        
        team_leaderboard = [
            {
                '_id': 'leader_team_1',
                'type': 'team',
                'rank': 1 if marvel_total > dc_total else 2,
                'team_id': 'team_marvel',
                'team_name': 'Team Marvel',
                'total_calories_burned': marvel_total,
                'total_workouts': sum(u['total_workouts'] for u in users_with_stats if u['team'] == 'team_marvel'),
                'updated_at': datetime.now()
            },
            {
                '_id': 'leader_team_2',
                'type': 'team',
                'rank': 1 if dc_total > marvel_total else 2,
                'team_id': 'team_dc',
                'team_name': 'Team DC',
                'total_calories_burned': dc_total,
                'total_workouts': sum(u['total_workouts'] for u in users_with_stats if u['team'] == 'team_dc'),
                'updated_at': datetime.now()
            }
        ]
        
        # Sort team leaderboard by rank
        team_leaderboard.sort(key=lambda x: x['rank'])
        
        db.leaderboard.insert_many(individual_leaderboard + team_leaderboard)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(individual_leaderboard) + len(team_leaderboard)} leaderboard entries'))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('Database Population Complete!'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(f'Teams: {db.teams.count_documents({})}')
        self.stdout.write(f'Users: {db.users.count_documents({})}')
        self.stdout.write(f'Activities: {db.activities.count_documents({})}')
        self.stdout.write(f'Workouts: {db.workouts.count_documents({})}')
        self.stdout.write(f'Leaderboard Entries: {db.leaderboard.count_documents({})}')
        self.stdout.write(self.style.SUCCESS('='*60))

        client.close()
