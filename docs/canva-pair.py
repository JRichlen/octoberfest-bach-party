import json
a=json.load(open('atoms.json'))
d=json.load(open('bootstrap.json'))
media={m['id']:(m['files'][0]['width'],m['files'][0]['height'],m['files'][0]['url'])
       for m in d['page']['E'] if m.get('files')}
cards=[];decor=[]
for si in (1,2,3,4):
    at=[z for z in a if z['sec']==si]
    imgs=[z for z in at if z['media'] and not z['txt']]
    txts=[z for z in at if z['txt'] and not z['media']]
    for im in imgs:
        below=[t for t in txts
               if abs(t['x']-im['x'])<30 and 0 <= t['y']-(im['y']+im['h']) < 70]
        below.sort(key=lambda t:t['y'])
        if not below:
            decor.append(dict(sec=si,media=im['media'][0],x=im['x'],y=im['y'],file=media[im['media'][0]][2]))
            continue
        name=below[0]['txt'][0].strip()
        role=None
        rest=[t for t in below[1:] if 0<t['y']-below[0]['y']<60]
        if rest: role=rest[0]['txt'][0].strip()
        mid=im['media'][0]
        cards.append(dict(sec=si,name=name,role=role,media=mid,x=im['x'],y=im['y'],
                          file=media[mid][2],px=list(media[mid][:2]),
                          name_fs=below[0]['style'].get('font-size')))
    print(f"sec{si}: {len([c for c in cards if c['sec']==si])} cards / {len(imgs)} imgs")
json.dump(cards,open('roster-truth.json','w'),indent=1)
json.dump(decor,open('decorative.json','w'),indent=1)
print(f"\nTOTAL {len(cards)}   no-role={[c['name'] for c in cards if not c['role']]}")
print(f"decorative (no caption): {[(x['sec'],x['media']) for x in decor]}\n")
LAD={1:'ladies',2:'ladies',3:'lads',4:'lads'}
for c in cards: print(f"  {LAD[c['sec']]:<7} {c['name']:<22} {str(c['role']):<22} {c['media']:<15} {c['px']}")
names=[c['name'] for c in cards]
print("\ndup names:",[n for n in set(names) if names.count(n)>1])
print("dup media:",[m for m in set(c['media'] for c in cards) if [c['media'] for c in cards].count(m)>1])
