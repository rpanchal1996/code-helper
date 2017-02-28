from django.contrib import admin
#from .models import Publisher
# Register your models here.
from .models import Helper
from .models import Coder
from .models import Classify
from .models import Skill
from .models import Cost
from .models import HelperProfile
from .models import HelperPicture
from .models import Message
admin.site.register(Helper)
admin.site.register(Coder)
admin.site.register(Classify)
admin.site.register(Skill)
admin.site.register(Cost)
admin.site.register(HelperProfile)
admin.site.register(HelperPicture)
admin.site.register(Message)