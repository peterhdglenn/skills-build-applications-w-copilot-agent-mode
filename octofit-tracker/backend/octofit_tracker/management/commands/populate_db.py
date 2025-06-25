from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Copilot agent mode: Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Copilot agent mode: Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Copilot agent mode: Add test data for users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Copilot agent mode: Add test data for teams
        team1 = Team.objects.create(name='Team Alpha', member_emails=[user1.email, user2.email])
        team2 = Team.objects.create(name='Team Beta', member_emails=[user3.email])

        # Copilot agent mode: Add test data for activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='strength', duration=60, date=timezone.now())

        # Copilot agent mode: Add test data for leaderboard
        Leaderboard.objects.create(team=team1, points=150)
        Leaderboard.objects.create(team=team2, points=100)

        # Copilot agent mode: Add test data for workouts
        Workout.objects.create(user=user1, workout_type='cardio', details='5km run', date=timezone.now())
        Workout.objects.create(user=user2, workout_type='cardio', details='3km walk', date=timezone.now())
        Workout.objects.create(user=user3, workout_type='strength', details='weight lifting', date=timezone.now())

        # Copilot agent mode: Test data population complete
        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
