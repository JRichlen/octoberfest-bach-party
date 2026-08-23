import json
d=json.load(open('bootstrap.json'))
media={m['id']:(m['files'][0]['width'],m['files'][0]['height'],m['files'][0]['url'])
       for m in d['page']['E'] if m.get('files')}

def own_media(o,depth=0):
    """media ids referenced anywhere under o, but NOT descending into child elements 'c'"""
    acc=set()
    def rec(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if k=='c': continue
                if isinstance(v,str) and v in media: acc.add(v)
                else: rec(v)
        elif isinstance(x,list):
            for v in x: rec(v)
    rec(o); return acc

def own_text(o):
    """text runs directly on this element (its 'a' payload), not children"""
    acc=[]
    def rec(x):
        if isinstance(x,dict):
            if x.get('A?')=='A' and isinstance(x.get('A'),str): acc.append(x['A']); return
            # compact form: {"C":{"A":["text\n"], "B":[len], "C":[styles]}}
            c=x.get('C')
            if isinstance(c,dict) and isinstance(c.get('A'),list) and c['A'] and all(isinstance(z,str) for z in c['A']):
                acc.extend(c['A']); return
            for k,v in x.items():
                if k=='c': continue
                rec(v)
        elif isinstance(x,list):
            for v in x: rec(v)
    rec(o.get('a'))
    return [s for s in acc if isinstance(s,str)]

def style_of(o):
    """pull font-size / color / font-family from the element's style payload"""
    found={}
    def rec(x):
        if isinstance(x,dict):
            for key in ('font-size','color','font-family','text-transform','font-weight'):
                if key in x and isinstance(x[key],dict) and 'B' in x[key]:
                    found.setdefault(key,x[key]['B'])
            # compact style form
            if 'G' in x and isinstance(x.get('G'),str) and x['G'].endswith('px'):
                found.setdefault('font-size',x['G'].replace('px',''))
            if 'M' in x and isinstance(x.get('M'),str) and x['M'].startswith('#'):
                found.setdefault('color',x['M'])
            for k,v in x.items():
                if k!='c': rec(v)
        elif isinstance(x,list):
            for v in x: rec(v)
    rec(o.get('a'))
    return found

atoms=[]
def walk(el,ox,oy,sx,sy,sec,path):
    y=(el.get('A') or 0); x=(el.get('B') or 0)
    h=(el.get('C') or 0); w=(el.get('D') or 0)
    ax=ox+x*sx; ay=oy+y*sy; aw=w*sx; ah=h*sy
    tx=[s.strip() for s in own_text(el) if s and s.strip()]
    mid=sorted(own_media(el))
    if tx or mid:
        atoms.append(dict(sec=sec,path=path,ty=el.get('A?'),x=round(ax,1),y=round(ay,1),
                          w=round(aw,1),h=round(ah,1),txt=tx,media=mid,style=style_of(el)))
    kids=el.get('c') or []
    if kids:
        a=el.get('a'); b=el.get('b')
        ksx=(w/b*sx) if isinstance(b,(int,float)) and b else sx
        ksy=(h/a*sy) if isinstance(a,(int,float)) and a else sy
        for i,k in enumerate(kids):
            if isinstance(k,dict): walk(k,ax,ay,ksx,ksy,sec,path+[i])

t=d['page']['A']['A'][0]['t']
for si,s in enumerate(t):
    for ei,el in enumerate(s.get('E',[])):
        walk(el,0,0,1,1,si,[ei])
json.dump(atoms,open('atoms.json','w'),indent=1)
print("atoms:",len(atoms))
