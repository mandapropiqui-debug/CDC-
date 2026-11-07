"""Gera ../index.html (arquivo unico, com fotos e fontes embutidas) a partir de tpl.html + a/."""
import re,base64,os
here=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(here,'tpl.html'),encoding='utf-8').read()
def uri(m):
    f=m.group(1);b=open(os.path.join(here,'a',f),'rb').read()
    mime={'jpg':'image/jpeg','png':'image/png','woff2':'font/woff2'}[f.split('.')[-1]]
    return 'data:%s;base64,%s'%(mime,base64.b64encode(b).decode())
out=os.path.join(here,'..','index.html')
open(out,'w',encoding='utf-8').write(re.sub(r'\{\{([\w.\-]+)\}\}',uri,t))
print('ok ->',os.path.abspath(out))
