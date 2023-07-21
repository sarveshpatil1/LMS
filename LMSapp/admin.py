from django.contrib import admin
from .models import *

class what_you_learn_TubulurinLine(admin.TabularInline):
    model=what_to_learn

class Video_TubulurinLine(admin.TabularInline):
    model=Video

class requirements_TublurinLine(admin.TabularInline):
    model = requirements
class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TubulurinLine,requirements_TublurinLine,Video_TubulurinLine)

# Register your models here.
admin.site.register(Categories)
admin.site.register(Course,course_admin)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(what_to_learn)
admin.site.register(requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(UserCourse)