# This file is part of HappySchool.
#
# HappySchool is the legal property of its developers, whose names
# can be found in the AUTHORS file distributed with this source
# distribution.
#
# HappySchool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HappySchool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with HappySchool.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.contrib.auth.models import User, Group

from core.models import StudentModel, TeachingModel, ClasseModel, GivenCourseModel


class StudentAbsenceTeacherSettingsModel(models.Model):
    CLASS = "CL"
    GIVEN_COURSE = "GC"
    CLASS_AND_GIVEN_COURSE = "CLGC"
    SELECT_STUDENT = [
        (CLASS, "Par classe"),
        (GIVEN_COURSE, "Par cours"),
        (CLASS_AND_GIVEN_COURSE, "Par classe et par cours"),
    ]
    teachings = models.ManyToManyField(TeachingModel, default=None)
    can_see_list = models.ManyToManyField(
        Group, default=None, blank=True, related_name="can_see_list"
    )
    can_see_adding = models.ManyToManyField(
        Group, default=None, blank=True, related_name="can_see_adding"
    )
    select_student_by = models.CharField(choices=SELECT_STUDENT, max_length=4, default=CLASS)


class LessonModel(models.Model):
    lesson = models.CharField(max_length=200)
    classe = models.ForeignKey(ClasseModel, on_delete=models.CASCADE, null=True)


class PeriodModel(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    name = models.CharField(max_length=200)
    day_of_week = models.CharField(max_length=10, default="1-5")

    @property
    def display(self):
        return "%s (%s-%s)" % (self.name, str(self.start)[:5], str(self.end)[:5])


class StudentAbsenceTeacherModel(models.Model):
    PRESENCE = "presence"
    LATENESS = "lateness"
    ABSENCE = "absence"
    EXCLUDED = "excluded"
    INTERNSHIP = "internship"
    STATUS_CHOICES = [
        (PRESENCE, "Présence"),
        (LATENESS, "Retard"),
        (ABSENCE, "Absence"),
        (EXCLUDED, "Exclus"),
        (INTERNSHIP, "Stage"),
    ]

    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    date_absence = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PRESENCE)
    given_course = models.ForeignKey(
        GivenCourseModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    period = models.ForeignKey(PeriodModel, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_creation = models.DateTimeField(
        "Date et heure de création de l'absence", auto_now_add=True
    )
    datetime_update = models.DateTimeField(
        "Date et heure de mise à jour de l'absence", auto_now=True
    )

    def __str__(self):
        return f"{self.date_absence} ({self.period.name}): {self.student} ({self.status})"
