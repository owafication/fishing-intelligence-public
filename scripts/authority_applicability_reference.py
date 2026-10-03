from __future__ import annotations

LEGAL_SAFETY={'FISHERIES_RULES','LICENSING_PERMITS','AREA_CLOSURES_PROTECTED','ACCESS','BOATING_SAFETY','NAVIGATION_NOTICES','SPECIES_TAXONOMY'}
VALID_APPLICABILITY={'REQUIRED','CONDITIONAL','NOT_APPLICABLE','UNRESOLVED'}
VALID_SPATIAL={'INTERSECTS','DOES_NOT_INTERSECT','UNRESOLVED','NOT_SPATIAL'}

def run(x:dict)->dict:
    out=[]
    for item in x.get('observations',[]):
        domain=item['domain']
        app=item.get('applicability','UNRESOLVED')
        spatial=item.get('spatial_relation','NOT_SPATIAL')
        verification=item.get('verification','UNAVAILABLE')
        material=bool(item.get('material',True))
        trigger_state=item.get('condition_triggered',None)
        app_basis=bool(item.get('applicability_basis_verified',True))
        spatial_basis=bool(item.get('spatial_basis_verified',True))
        if app not in VALID_APPLICABILITY: app='UNRESOLVED'
        if spatial not in VALID_SPATIAL: spatial='UNRESOLVED'
        if app=='NOT_APPLICABLE' and not app_basis: app='UNRESOLVED'
        if spatial=='DOES_NOT_INTERSECT' and not spatial_basis: spatial='UNRESOLVED'
        if spatial=='DOES_NOT_INTERSECT':
            effect='NONE'; constrains=False
        elif app=='NOT_APPLICABLE':
            effect='NONE'; constrains=False
        elif app=='CONDITIONAL' and trigger_state is False:
            effect='NONE'; constrains=False
        elif app=='CONDITIONAL' and trigger_state is None:
            effect='BLOCK' if material and domain in LEGAL_SAFETY else 'DOWNGRADE'; constrains=True
        elif app=='UNRESOLVED' or spatial=='UNRESOLVED':
            effect='BLOCK' if material and domain in LEGAL_SAFETY else 'DOWNGRADE'
            constrains=True
        elif verification in {'CONFLICTING','UNAVAILABLE'}:
            effect='BLOCK' if material and domain in LEGAL_SAFETY else 'DOWNGRADE'
            constrains=True
        elif verification=='STALE':
            effect='DOWNGRADE'; constrains=True
        else:
            effect='NONE'; constrains=True
        out.append({'id':item.get('id'), 'constrains_plan':constrains, 'readiness_effect':effect})
    return {'results':out}
