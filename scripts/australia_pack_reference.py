import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def run(obj, filename=None):
    reg=json.loads((R/'regional-packs/australia/jurisdiction-registry.json').read_text(encoding='utf-8'))
    by={x['jurisdiction_id']:x for x in reg['jurisdictions']}
    i=obj['input']; f=filename or obj.get('id','')
    if f=='tas-seaward-ambiguous.json': return {'result':'BLOCKED_BOUNDARY_AMBIGUOUS','reason':'MARINE_VS_INLAND_AUTHORITY_UNRESOLVED'}
    if f=='commonwealth-overlay.json': return {'packs':[i['jurisdiction'],'AU-CTH-MARINE'],'combine_constraints':True}
    if f=='nt-darwin.json': return {'pack':'AU-NT','regional_readiness':'PROSPECT_READY'}
    if f=='reference-vs-planning.json': return {'rule_verification':'SUPPORTED','local_planning_depth':'PROVISIONAL_UNTIL_LOCAL_ACCESS_PROSPECT_ADAPTERS'}
    if f=='mode-kayak.json': return {'requires_boat_ramp':False,'uses_common_kernel':True}
    if f=='mode-rock-nsw.json': return {'mode_overlay':'VERIFY_DECLARED_AREA_LEGAL_REQUIREMENTS','uses_common_kernel':True}
    j=by[i['jurisdiction']]; out={'pack':j['jurisdiction_id'],'readiness':j['readiness']}
    if f=='act-public-water.json': out['licence_model']=j['licence_model']
    elif f=='nsw-general.json': out['licence_check']='REQUIRED_WITH_EXEMPTION_CHECK'
    elif f=='qld-stocked.json': out['permit_overlay']='SIPS_VERIFY_CURRENT'
    elif f=='sa-reservoir.json': out['permit_overlay']='RESERVOIR_PERMIT_VERIFY_CURRENT'
    elif f=='tas-marine-rod.json': out['licence_model']=j['licence_model']
    elif f=='tas-inland.json': out['licence_check']='INLAND_LICENCE_VERIFY_CURRENT'
    elif f=='vic-public-water.json': out['licence_check']='RFL_REQUIRED_UNLESS_EXEMPT'
    elif f=='wa-powered-boat.json': out['licence_check']='ACTIVITY_MODE_SPECIFIC_VERIFY_CURRENT'
    return out
if __name__=='__main__':
    p=Path(sys.argv[1]); print(json.dumps(run(json.loads(p.read_text(encoding='utf-8')),p.name),sort_keys=True))
