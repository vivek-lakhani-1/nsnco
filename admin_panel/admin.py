from django.contrib import admin
from .model_client import client_table
from .model_project import project_table
from .model_artist_panel import artist_table
from .model_artist_panel import worklink
from .model_artist_feedback import artist_feedback
from .model_artist_project_demos import project_demos
from .model_artist_request import artist_request
from .model_project_fee import project_fee
from .model_project import project_table
from .other_tables import skill
from .other_tables import genre_table
from .other_tables import location
from .other_tables import language


admin.site.register(client_table)
admin.site.register(project_table)
admin.site.register(artist_table)
admin.site.register(worklink)
admin.site.register(artist_feedback)
admin.site.register(project_demos)
admin.site.register(artist_request)
admin.site.register(project_fee)
admin.site.register(skill)
admin.site.register(location)
admin.site.register(language)
admin.site.register(genre_table)