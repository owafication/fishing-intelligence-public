from pathlib import Path
import json, sys, hashlib, re
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R))
errors=[]; checks=0; fixture_pass=0

def req(cond,msg):
    global checks
    checks+=1
    if not cond: errors.append(msg)

def load(rel): return json.loads((R/rel).read_text(encoding='utf-8'))

p=load('plugin.json'); c=load('.codex-plugin/plugin.json'); op=load('plugin-operating-manifest.json'); bi=load('build-info.json')
req(p.get('version')=='0.15.2','root version')
req(c.get('version')=='0.15.2','compat version')
req(op.get('version')=='0.15.2' and op.get('plugin_version')=='0.15.2','manifest version')
req(op.get('runtime_mode')=='PORTABLE_ONLY','portable-only runtime')
req(op.get('dedicated_service_required') is False,'no dedicated service')
req(op.get('persistent_storage_required') is False,'no persistent store requirement')
req(op.get('license')=='Apache-2.0','Apache-2.0 manifest marker')
req((R/'LICENSE').exists() and 'Apache License' in (R/'LICENSE').read_text(errors='ignore'),'Apache license text')
req((R/'NOTICE').exists(),'NOTICE present')
req(p['extensions']['com.openai']['interface']['displayName']=='Fishing Intelligence','public display name')

# JSON integrity
json_files=list(R.rglob('*.json'))
for f in json_files:
    try: json.loads(f.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'json parse {f.relative_to(R)}: {e}')
    checks+=1

# Public cleanup and leakage guardrails.
forbidden_paths=[
 'docs/AUDIT_REPORT.md','docs/QUALITY_AUDIT.md','docs/CONVERSATIONAL_REGRESSION.md','docs/PUBLIC_RELEASE_CHECKLIST.md',
 'docs/REQUIREMENTS_TRACEABILITY.md','docs/STORAGE_AND_CONTINUITY.md','docs/DATA_MODEL.md','references/EXECUTION_PROFILES.md',
 'shared/connected-drive-store.md','shared/continuity-storage.md','shared/nt-source-policy.md'
]
for rel in forbidden_paths: req(not (R/rel).exists(),f'forbidden public artifact remains: {rel}')

forbidden_text=[
 'ContinuationHead','provider-neutral','HOSTED_SERVICE','DEV FINAL','private development build',
 'source-available but not open-source','commercial production requires','PRIVATE_EVALUATION_REFERENCE_ONLY',
 'REQUIRED_SINGLE_RERUN','ACCEPTED CANDIDATE','Plugin Foundry','CanonicalOps','Project Auditor'
]
scan_ext={'.md','.json','.py','.txt'}
for f in R.rglob('*'):
    if f.is_file() and f.suffix.lower() in scan_ext and f.name not in {'CHECKSUMS.sha256','validate.py'}:
        txt=f.read_text(encoding='utf-8',errors='ignore')
        for term in forbidden_text:
            req(term not in txt,f'forbidden public text {term!r} in {f.relative_to(R)}')

# External source registries are links, not rights/commercial metadata or live weather/tide snapshots.
rights_keys={'commercial_use','derivative_use','cache_policy','offline_redistribution','attribution_required','use_conditions','terms_url','reuse_status','reuse_note','licence','license'}
for f in (R/'regional-packs').rglob('*.json'):
    obj=json.loads(f.read_text())
    def walk(v):
        if isinstance(v,dict):
            for k in v:
                req(k not in rights_keys,f'rights metadata {k} in {f.relative_to(R)}')
            if 'source_id' in v:
                req(v.get('use_mode')=='LINK_REFERENCE',f'non-link source mode in {f.relative_to(R)}')
            for vv in v.values(): walk(vv)
        elif isinstance(v,list):
            for vv in v: walk(vv)
    walk(obj)

# Relative markdown references that target local files must resolve.
linkpat=re.compile(r'`([^`]+\.(?:md|json))`')
for f in list((R/'skills').rglob('*.md'))+list((R/'shared').rglob('*.md'))+list((R/'docs').rglob('*.md')):
    txt=f.read_text(encoding='utf-8')
    for target in linkpat.findall(txt):
        if '://' in target or target.startswith('/'):
            continue
        t=(f.parent/target).resolve()
        # Only enforce paths that are clearly local references.
        if target.startswith('.'):
            req(t.exists(),f'broken local ref {target} from {f.relative_to(R)}')

# Deterministic retained fixture groups.
from scripts import planning_reference, prospect_reference, australia_pack_reference, sa_planning_reference, global_region_reference, authority_applicability_reference

def exact_group(dirname,runner,needs_filename=False):
    global fixture_pass
    for f in sorted((R/'fixtures'/dirname).glob('*.json')):
        obj=json.loads(f.read_text(encoding='utf-8'))
        try: obs=runner(obj,f.name) if needs_filename else runner(obj)
        except Exception as e: errors.append(f'{dirname} execution failed {f.name}: {e}'); continue
        ok=obs==obj.get('expected')
        req(ok,f'{dirname} mismatch {f.name}: {obs!r} != {obj.get("expected")!r}')
        if ok: fixture_pass+=1

exact_group('ph03',planning_reference.run)
exact_group('ph04',prospect_reference.run)
exact_group('ph09',australia_pack_reference.run,True)
exact_group('ph09b',sa_planning_reference.run,True)
exact_group('ph12',global_region_reference.run)
exact_group('ph13',authority_applicability_reference.run)

# Checksum manifest when present.
cs=R/'CHECKSUMS.sha256'
if cs.exists():
    listed={}
    for line in cs.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        digest, rel=line.split('  ',1)
        listed[rel]=digest
    actual=[]
    for f in R.rglob('*'):
        if f.is_file() and f.name!='CHECKSUMS.sha256' and '__pycache__' not in f.parts and f.suffix not in {'.pyc','.pyo'}:
            rel=f.relative_to(R).as_posix(); actual.append(rel)
            got=hashlib.sha256(f.read_bytes()).hexdigest()
            req(listed.get(rel)==got,f'checksum mismatch/missing: {rel}')
    req(set(listed)==set(actual),'checksum path set mismatch')

# Package residue.
for f in R.rglob('*'):
    if not f.is_file():
        continue
    rel=str(f.relative_to(R)).replace('\\','/')
    req('__pycache__' not in rel and not rel.endswith(('.pyc','.pyo')),'cache/bytecode residue')

if errors:
    print('FISHING INTELLIGENCE PUBLIC OPEN-SOURCE VALIDATION: FAIL')
    print(f'checks={checks} fixture_pass={fixture_pass} json_files={len(json_files)} errors={len(errors)}')
    for e in errors: print('- '+e)
    sys.exit(1)
print('FISHING INTELLIGENCE PUBLIC OPEN-SOURCE VALIDATION: PASS')
print(f'checks={checks} fixture_pass={fixture_pass} json_files={len(json_files)}')
print('runtime=PORTABLE_ONLY license=Apache-2.0 externalSourceMaterialEmbedded=0')
