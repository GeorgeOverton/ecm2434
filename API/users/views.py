import math
from database.models import User, UserAchievement, Achievement
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from achievements.views import getAllUserAchievements

##Creates a function for frontend to make a POST request to backend
@csrf_exempt
def index(request):
    print("here the request")
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        name = str(body_data.get('name'))
        username = str(body_data.get('username'))
        password = str(body_data.get('password'))
        print(name)
        print(username)
        u = User(username = username, name = name, password = password,
            xp = 0, points = 0, has_been_verified = False)
        u.save()

##Function that will verify the account
def verifyAccount(current_username):
    current_username.has_been_verified = True
    current_username.save()

##Adds xp when a bottle is filled
def bottleFilled(current_username):
    current_username.xp = current_username.xp + 10
    current_username.save()

##Updates the name of a user 
def setName(current_username, new_name):
    updating_user = User.objects.get(username = current_username)
    updating_user.name = new_name
    updating_user.save()

##Gets data needed to display data for the profile page by returning a json
def getUserProfileData(request, current_username):
    name = User.objects.get(username = current_username).name
    level = int(User.objects.get(username = current_username).level)
    xpLeft = int(User.objects.get(username = current_username).xpLeft)
    points = User.objects.get(username = current_username).points
    achievement = getAllUserAchievements(current_username)
    return JsonResponse({"name":name, "level":level, "XP":xpLeft, "streak":0, "points": points, "achievements": achievement})

    


