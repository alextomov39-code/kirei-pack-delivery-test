import concurrent.futures,hashlib,json,sys,urllib.request
from pathlib import Path
b=sys.argv[1]; keys={'1':['774','776','777','default'],'2':['767','768','769','770'],'3':['771','772','773']}[b]
p=Path('public');p.mkdir()
m=json.loads(Path('manifest.json').read_text())
def stage(key):
 r=m[key];name=r['url'].split('/')[-1];dst=p/name
 urllib.request.urlretrieve(r['url'],dst)
 with dst.open('rb') as f:assert hashlib.file_digest(f,'sha1').hexdigest()==r['sha1']
with concurrent.futures.ThreadPoolExecutor(4) as pool:list(pool.map(stage,keys))
(p/('batch-'+b+'.txt')).write_text(b)
(p/'index.html').write_text('<title>Kirei pack delivery test</title>Temporary pack delivery benchmark.')
