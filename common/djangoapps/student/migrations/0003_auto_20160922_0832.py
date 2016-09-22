# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20151208_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='educational_centre_code',
            field=models.CharField(default=b'00000000', max_length=8, validators=[django.core.validators.RegexValidator(b'^\\d{0,8}$')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='educational_centre_name',
            field=models.CharField(default='Empty', max_length=256),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='educational_role',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='specialty',
            field=models.CharField(default='None', max_length=256, choices=[(b'', 'Select a choice'), (b'acordeon', 'Acordeon'), (b'acrobacia', 'Acrobacia'), (b'actividades', 'Actividades (C.E.I.S)'), (b'administracion_empresa', 'Administracion de Empresas'), (b'adorno_figura', 'Adorno y Figura'), (b'aleman', 'Aleman'), (b'alfareria', 'Alfareria'), (b'alfombras', 'Alfombras'), (b'analisis_forma_color', 'An\xe1lisis de forma y color.'), (b'analisis_quimico_ceramica', 'An\xe1lisis qu\xedmicos de cer\xe1mica.')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='teaching_profession',
            field=models.CharField(default='None', max_length=256, choices=[(b'', 'Select a choice'), (b'lecturer_arts_design', 'Lecturers of Visual arts and Design'), (b'lecturer_secondary_education', 'Lecturers of Secondary Education'), (b'lecturer_languages_schools', 'Lecturers of Official Language Schools'), (b'lecturer_music_arts', 'Lecturers of Music and Performing arts'), (b'education_inspector', 'Education Inspectors'), (b'teacher', 'Teachers'), (b'teacher_workshop_arts_design', 'Teachers of Visual arts and Design Workshop'), (b'teacher_arts_degisn', 'Teachers of Visual arts and Design'), (b'teacher_secondary_education', 'Teachers of Secondary Education'), (b'teacher_languages_schools', 'Teachers of Official Language Schools'), (b'teacher_music_arts', 'Teachers of Music and Performing arts'), (b'teacher_religion', 'Teachers of Religion'), (b'teacher_professional_training', 'Teachers of Technical Professional Training'), (b'others', 'Others')]),
        ),
    ]
