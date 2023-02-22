from django.contrib import admin

from .models import User, Building, Question, Answer, HasAnswered, Leaderboard, Achievement, UserAchievement, Fountain

# Register your models here.
admin.site.register(User)
admin.site.register(Building)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(HasAnswered)
admin.site.register(Leaderboard)
admin.site.register(Achievement)
admin.site.register(UserAchievement)
admin.site.register(Fountain)
