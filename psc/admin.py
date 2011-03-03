#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.contrib import admin
from .models import Zone, State, District, LGA, Ward, RegistrationCenter, VRChecklist, VRIncident, DCOChecklist, DCOIncident, Observer, EDAYChecklist, EDAYIncident
from .models import Partner

admin.site.register(Zone)
admin.site.register(State)
admin.site.register(District)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(RegistrationCenter)
admin.site.register(VRChecklist)
admin.site.register(VRIncident)
admin.site.register(DCOChecklist)
admin.site.register(DCOIncident)
admin.site.register(Observer)
admin.site.register(Partner)
admin.site.register(EDAYChecklist)
admin.site.register(EDAYIncident)