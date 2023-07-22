from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'AUTHOR COURSE DASHBOARD'


class what_you_learn_TubulurinLine(admin.TabularInline):
    model = what_to_learn


class Video_TubulurinLine(admin.TabularInline):
    model = Video


class requirements_TublurinLine(admin.TabularInline):
    model = requirements


class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TubulurinLine, requirements_TublurinLine, Video_TubulurinLine)


class AuthorsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Get the default queryset for the model
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        # Filter the queryset to show only entries added by the current user
        print(request.user)
        return queryset.filter(user_name__startswith=request.user)


# Register your models here.
admin.site.register(Categories)
admin.site.register(Course, course_admin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Level)
admin.site.register(what_to_learn)
admin.site.register(requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(UserCourse)

