from django.contrib import admin

from .models import College, Program, Organization, Student, OrgMember

# admin for college model
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)


# admin for program model
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")
    search_fields = ("prog_name", "college__college_name")
    list_filter = ("college",)


# admin for organization model
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")
    search_fields = ("name", "description")
    list_filter = ("college",)


# student admin with extra list display and search
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id", "lastname", "firstname", "middlename", "program",
    )
    search_fields = ("lastname", "firstname",)


# orgmember admin showing related student program
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = (
        "student", "get_member_program", "organization", "date_joined",
    )
    search_fields = ("student__lastname", "student__firstname",)

    def get_member_program(self, obj):
        # return the program of the student belonging to this membership
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None
    get_member_program.short_description = "Program"

