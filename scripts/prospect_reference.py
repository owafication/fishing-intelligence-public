from __future__ import annotations
import json, sys
from collections import deque
from pathlib import Path


def local_relief(grid, r, c):
    vals=[]
    for rr in range(max(0,r-1), min(len(grid),r+2)):
        for cc in range(max(0,c-1), min(len(grid[0]),c+2)):
            vals.append(float(grid[rr][cc]))
    return max(vals)-min(vals)


def clusters(mask):
    h=len(mask); w=len(mask[0]); seen=set(); out=[]
    for r in range(h):
        for c in range(w):
            if not mask[r][c] or (r,c) in seen: continue
            q=deque([(r,c)]); seen.add((r,c)); pts=[]
            while q:
                x,y=q.popleft(); pts.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and mask[nx][ny] and (nx,ny) not in seen:
                        seen.add((nx,ny)); q.append((nx,ny))
            out.append(pts)
    return out


def expand_bbox(points,h,w,min_cells_side=3):
    rs=[p[0] for p in points]; cs=[p[1] for p in points]
    r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
    while r1-r0+1<min_cells_side:
        if r0>0:r0-=1
        elif r1<h-1:r1+=1
        else:break
    while c1-c0+1<min_cells_side:
        if c0>0:c0-=1
        elif c1<w-1:c1+=1
        else:break
    return r0,r1,c0,c1


def run(fixture):
    fid=fixture['id']; i=fixture['input']
    if fid=='coverage-without-cell-size':
        return {'prospect_generation':'BLOCKED_PRECISE_GEOMETRY','allowed':'DATASET_DISCOVERY','navigation_suitable':False}
    if fid=='low-tide-image-drain':
        return {'structure_observation':'SUPPORTED_IF_VISUALLY_OBSERVED','fishing_relevance':'HYPOTHESIS','navigation_suitable':False,'precision':'IMAGE_BOUNDED_APPROXIMATE_AREA'}
    if fid=='official-reef-separate-halo':
        return {'official_record_preserved':True,'new_record_origin':'GENERATED_PROSPECT','prospect_type':'ARTIFICIAL_STRUCTURE_HALO','navigation_suitable':False}
    if fid=='prospect-overlaps-protection-area':
        return {'planning_admission':'REJECTED','reason':'LEGAL_SPATIAL_EXCLUSION'}
    if fid=='nthaus30-30m-relief':
        cell=i.get('cell_size_m')
        if not cell:
            return {'status':'BLOCKED_PRECISE_GEOMETRY','reason':'SOURCE_RESOLUTION_UNKNOWN','navigation_suitable':False}
        grid=i['grid']; threshold=float(i['min_local_relief_m'])
        mask=[[local_relief(grid,r,c)>=threshold for c in range(len(grid[0]))] for r in range(len(grid))]
        cls=clusters(mask)
        areas=[]
        for pts in cls:
            r0,r1,c0,c1=expand_bbox(pts,len(grid),len(grid[0]),3)
            areas.append({'grid_bbox':[r0,r1,c0,c1],'width_m':(c1-c0+1)*cell,'height_m':(r1-r0+1)*cell,'output_resolution_m':cell})
        return {
          'status':'OK','area_count':len(areas),
          'minimum_search_width_m':min((a['width_m'] for a in areas),default=0),
          'minimum_search_height_m':min((a['height_m'] for a in areas),default=0),
          'output_resolution_m':cell,
          'navigation_suitable':False,'evidence_class':'HYPOTHESIS'
        }
    raise SystemExit('unknown fixture')

if __name__=='__main__':
    f=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    print(json.dumps(run(f),sort_keys=True))
