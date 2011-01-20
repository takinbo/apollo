from django.db.models import Q
from django.db import models
from models import *
from numpy import *

def vr_QA(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(A__isnull=False).values_list('A', flat=True)
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0}
    for vr in vrs:
        options[vr] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('A')[0].help_text }

def vr_QB(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(B__gt=0).values_list('B', flat=True)
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('B')[0].help_text }

def vr_QC(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(C__isnull=False).values_list('C', flat=True)
    total = len(vrs)
    valid = []
    options = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        if vr in range(0, 10):
            key = vr
            if options.has_key(key):
                options[key] += 1
                valid.append(vr)
            else:
                options[5] += 1
                valid.append(vr)
        else:
            options[5] += 1

    return {'n': total, 'valid_n': len(valid), 'options': options, 'mean': mean(valid), 'label': VRChecklist._meta.get_field_by_name('C')[0].help_text }

def vr_QD(q=Q()):
    qs = Q(D1__isnull=False) | Q(D2__isnull=False) | Q(D3__isnull=False) | Q(D4__isnull=False)
    vrs = VRChecklist.objects.filter(q).filter(qs).values('D1','D2', 'D3', 'D4')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0}
    for vr in vrs:
        if vr['D1']:
            options[1] += 1
        if vr['D2']:
            options[2] += 1
        if vr['D3']:
            options[3] += 1
        if vr['D4']:
            options[4] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('D1')[0].help_text }

def vr_QE(q=Q()):
    qs = Q(E1__isnull=False) | Q(E2__isnull=False) | Q(E3__isnull=False) | Q(E4__isnull=False) | Q(E5__isnull=False)
    vrs = VRChecklist.objects.filter(q).filter(qs).values('E1','E2', 'E3', 'E4', 'E5')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        if vr['E1']:
            options[1] += 1
        if vr['E2']:
            options[2] += 1
        if vr['E3']:
            options[3] += 1
        if vr['E4']:
            options[4] += 1
        if vr['E5']:
            options[5] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('E1')[0].help_text }

def vr_QF(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(F__isnull=False).values_list('F', flat=True)
    total = len(vrs)
    valid = []
    for vr in vrs:
        if vr in range(0, 61):
                valid.append(vr)
    return {'n': total, 'valid_n': len(valid), 'mean': mean(valid), 'label': VRChecklist._meta.get_field_by_name('F')[0].help_text }

def vr_QG(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(G__gt=0).values('G')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['G']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('G')[0].help_text }

def vr_QH(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(H__isnull=False).values('H')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['H']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('H')[0].help_text }

def vr_QJ(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(J__isnull=False).values('J')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['J']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('J')[0].help_text }

def vr_QK(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(K__isnull=False).values('K')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['K']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('K')[0].help_text }

def vr_QM(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(M__isnull=False).values('M')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['M']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('M')[0].help_text }

def vr_QN(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(N__isnull=False).values('N')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['N']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('N')[0].help_text }

def vr_QP(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(P__isnull=False).values('P')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['P']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('P')[0].help_text }

def vr_QQ(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(Q__isnull=False).values('Q')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['Q']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('Q')[0].help_text }

def vr_QR(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(R__isnull=False).values('R')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['R']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('R')[0].help_text }

def vr_QS(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(S__isnull=False).values('S')
    n = len(vrs)
    options = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for vr in vrs:
        options[vr['S']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('S')[0].help_text }

def vr_QT(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(T__gt=0).values('T')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['T']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('T')[0].help_text }

def vr_QU(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(U__gt=0).values('U')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['U']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('U')[0].help_text }

def vr_QV(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(V__gt=0).values('V')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['V']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('V')[0].help_text }

def vr_QW(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(W__gt=0).values('W')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['W']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('W')[0].help_text }

def vr_QX(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(X__gt=0).values('X')
    n = len(vrs)
    options = {1: 0, 2: 0}
    for vr in vrs:
        options[vr['X']] += 1
    return {'n': n, 'options': options, 'label': VRChecklist._meta.get_field_by_name('X')[0].help_text }

def vr_QY(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(Y__isnull=False).values_list('Y', flat=True)
    total = len(vrs)
    valid = []
    for vr in vrs:
        if vr in range(0, 201):
            valid.append(vr)

    return {'n': total, 'valid_n': len(valid), 'mean': mean(valid), 'label': VRChecklist._meta.get_field_by_name('Y')[0].help_text }

def vr_QZ(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(Z__isnull=False).values_list('Z', flat=True)
    total = len(vrs)
    valid = []
    for vr in vrs:
        if vr in range(0, 2501):
            valid.append(vr)

    return {'n': total, 'valid_n': len(valid), 'mean': mean(valid), 'label': VRChecklist._meta.get_field_by_name('Z')[0].help_text }

def vr_QAA(q=Q()):
    vrs = VRChecklist.objects.filter(q).filter(AA__isnull=False).values_list('AA', flat=True)
    total = len(vrs)
    valid = []
    for vr in vrs:
        if vr in range(0, 2501):
            valid.append(vr)

    return {'n': total, 'valid_n': len(valid), 'mean': mean(valid), 'label': VRChecklist._meta.get_field_by_name('AA')[0].help_text }

def model_sieve(model, fields, exclude=False):
    if issubclass(model, models.Model):         
        def process_fields(fields, cond='AND'):
            query = Q()
            for field in fields:
                if type(field) == list:
                    query &= process_fields(field, 'OR')
                else:
                    if cond == 'AND':
                        if type(field) == tuple:
                            query &= eval('Q(%s=%s)' % field)
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.IntegerField) and \
                            type(model._meta.get_field_by_name(field)[0].default) == int:
                            query &= eval('~Q(%s=%d)' % (field, model._meta.get_field_by_name(field)[0].default))
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.IntegerField):
                            query &= eval('Q(%s__isnull=False)' % field)
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.BooleanField):
                            query &= eval('Q(%s=True)' % field)
                        else:
                            query &= eval('Q(%s__isnull=False)' % field)
                    else:
                        if type(field) == tuple:
                            query &= eval('Q(%s=%s)' % field)
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.IntegerField) and \
                            type(model._meta.get_field_by_name(field)[0].default) == int:
                            query |= eval('~Q(%s=%d)' % (field, model._meta.get_field_by_name(field)[0].default))
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.IntegerField):
                            query |= eval('Q(%s__isnull=False)' % field)
                        elif issubclass(model._meta.get_field_by_name(field)[0].__class__, models.fields.BooleanField):
                            query |= eval('Q(%s=True)' % field)
                        else:
                            query |= eval('Q(%s__isnull=False)' % field)
            return query
        
        if exclude:
            return model.objects.exclude(process_fields(fields))
        else:
            return model.objects.filter(process_fields(fields))

