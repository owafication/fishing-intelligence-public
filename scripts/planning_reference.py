import json,sys
from pathlib import Path

def run(o):
    i=o["input"]; unknown=set(i.get("unknowns",[]))
    return {
      "no_exact_departure_time_from_origin": i.get("origin_precision")!="EXACT",
      "no_range_inference_from_engine": "usable_fuel" in unknown or "fuel_economy" in unknown,
      "target_behavior": "COMPARE_FAMILIES" if i.get("target_intent")=="UNSPECIFIED" else "USE_SPECIFIED_TARGET",
      "pelagic_offshore": "WITHHOLD_IF_RANGE_OR_CRITICAL_CAPABILITY_REQUIRED" if {"usable_fuel","fuel_economy"}&unknown else "EVALUATE",
      "tide_access": "PROVISIONAL_OR_BLOCKED_IF_AUTHORITATIVE_EXACT_TIDE_UNRESOLVED",
      "plan_readiness": "NOT_READY_TO_USE_UNLESS_ALL_CRITICAL_DEPENDENCIES_VERIFY",
      "prohibit_safe_safer_labels": True,
      "option_families":["ESTUARY_CREEK","REEF_DEMERSAL","PELAGIC_OFFSHORE"]
    }
if __name__=='__main__':
    print(json.dumps(run(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),sort_keys=True))
