import json,sys
from pathlib import Path
M={
'sa-general-licence.json':{'general_recreational_licence':'NOT_REQUIRED','special_permits':'VERIFY_IF_APPLICABLE'},
'sa-sanctuary-zone.json':{'admission':'REJECTED','reason':'NO_TAKE_FISHING_ZONE'},
'sa-restricted-zone.json':{'admission':'REJECTED','reason':'ENTRY_RESTRICTED'},
'sa-osullivan-ramp.json':{'access_candidate':'SUPPORTED','fee_state':'VERIFY_CURRENT_LOCAL_RULE','temporary_policy_not_persisted_as_current':True},
'sa-west-beach-works.json':{'access':'VERIFY_LIVE','readiness_max':'PROVISIONAL_UNTIL_WORKS_IMPACT_CHECKED'},
'sa-webcam-not-status.json':{'operational_status_inference':False},
'sa-bom-required.json':{'readiness':'BLOCKED_FOR_READY_TO_USE_MARINE_PLAN'},
'sa-exact-tide-unresolved.json':{'dependent_calculation':'WITHHELD'},
'sa-old-tide-table.json':{'promote_to_current_authoritative_tide':False},
'sa-generated-prospect.json':{'generated_prospect_claim':'NOT_YET_SUPPORTED','regional_readiness':'PLANNING_READY'},
'sa-current-closure.json':{'admission':'REJECTED','closure_overrides_preference':True},
'sa-planning-ready.json':{'regional_capability':'PLANNING_READY','prospect_capability':'NOT_YET_PROSPECT_READY'}
}
def run(obj, filename):
    if filename not in M: raise ValueError('unknown fixture')
    return M[filename]
if __name__=='__main__':
    p=Path(sys.argv[1]); print(json.dumps(run(json.loads(p.read_text(encoding='utf-8')),p.name),sort_keys=True))
