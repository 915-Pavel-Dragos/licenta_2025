from django.db import models

difficulty_CHOICES = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard')
    ]

class Problem(models.Model):
    text = models.CharField(max_length=200, help_text='Text that describes the goal of the problem.')
    answer = models.CharField(max_length=200, help_text='The correct answer of the problem.')
    score = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=difficulty_CHOICES, help_text='How hard is the problem')

class Game(models.Model):
    score = models.IntegerField()
    goal_text = models.CharField(max_length=500, help_text='The goal that one has to meet to "win" the game')
    title = models.CharField(max_length=150, help_text='The title of the game')
    difficulty = models.CharField(max_length=10, choices=difficulty_CHOICES, help_text='Indicator of how hard is the game')

class Subject(models.Model):
    text = models.CharField(max_length=500, help_text='THe text of the subject')
    problems_to_solve = models.ForeignKey(Problem, on_delete=models.CASCADE)

class Year(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the user')
    email = models.EmailField(max_length=150, help_text='Email of the user')
    password = models.CharField(max_length=100, help_text='The password for the user')
    photo = models.ImageField()
    problems_solved = models.ForeignKey(Problem, on_delete=models.CASCADE)
    total_score = models.IntegerField()
    games_played = models.ForeignKey(Game, on_delete=models.CASCADE)
    level = models.IntegerField()
