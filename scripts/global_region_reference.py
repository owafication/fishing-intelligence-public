from __future__ import annotations

CRITICAL={'FISHERIES_RULES','LICENSING_PERMITS','AREA_CLOSURES_PROTECTED','ACCESS'}
BOAT={'BOATING_SAFETY','NAVIGATION_NOTICES'}
VALID={'VERIFIED_CURRENT','VERIFIED_AS_OF','STALE','CONFLICTING','UNAVAILABLE','NOT_REQUIRED'}

def run(x:dict)->dict:
    mode=x.get('mode','shore')
    required=set(CRITICAL)
    if mode in {'powered_boat','boat','kayak_route'}: required |= BOAT
    if x.get('weather_material',True): required.add('WEATHER_WARNINGS')
    if x.get('water_level_material'): required.add('TIDE_WATER_LEVEL')
    if x.get('species_identity_material'): required.add('SPECIES_TAXONOMY')
    if x.get('biosecurity_health_material'): required.add('BIOSECURITY_HEALTH_ADVISORY')
    domains=x.get('domains') or {}
    missing=[]; conflicting=[]; stale=[]
    for d in sorted(required):
        st=(domains.get(d) or {}).get('verification','UNAVAILABLE')
        if st not in VALID: missing.append(d); continue
        if st=='CONFLICTING': conflicting.append(d)
        elif st=='UNAVAILABLE': missing.append(d)
        elif st=='STALE': stale.append(d)
    legal_blockers=[d for d in conflicting+missing if d in {'FISHERIES_RULES','LICENSING_PERMITS','AREA_CLOSURES_PROTECTED','ACCESS','BOATING_SAFETY','NAVIGATION_NOTICES','SPECIES_TAXONOMY'}]
    if legal_blockers:
        readiness='INSUFFICIENT'
    elif missing or conflicting or stale:
        readiness='REFERENCE_READY'
    else:
        readiness='PLANNING_READY'
        if x.get('prospect_sources_adequate') is True: readiness='PROSPECT_READY'
    return {
        'pack_class':'GENERATED_PROVISIONAL',
        'required_domains':sorted(required),
        'missing':sorted(missing),
        'conflicting':sorted(conflicting),
        'stale':sorted(stale),
        'readiness':readiness,
        'self_promotes':False,
        'reuse_requires_freshness_recheck':True,
    }
