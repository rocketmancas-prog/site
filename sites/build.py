"""Build three independent static sites from the existing layout and authored copy."""
import json,re,html,zipfile
from pathlib import Path
root=Path(__file__).resolve().parent.parent
sites=json.loads((root/'sites/content.json').read_text())
source=(root/'app.js').read_text()
runtime=source[source.index('const labels='):]
for domain,site in sites.items():
    out=root/'sites'/domain
    out.mkdir(exist_ok=True)
    data={lang:site[lang] for lang in ('en','hi')}
    for lang,sections in data.items():
        for section,(title,text) in sections.items():
            assert len(text)>=600,(domain,lang,section,len(text))
            sections[section]=[title,[text]]
    script=source[:source.index('const content=')]+'const content='+json.dumps(data,ensure_ascii=False)+';\n'
    script+='const siteMeta='+json.dumps({'en':{'title':site['enTitle'],'description':site['enDescription']},'hi':{'title':site['hiTitle'],'description':site['hiDescription']}},ensure_ascii=False)+';\n'
    script+=runtime
    script=re.sub(r"document.title=lang==='hi'\?.*?;document.querySelector\('meta\[name=\"description\"\]'\).content=lang==='hi'\?.*?;try",'document.title=siteMeta[lang].title;document.querySelector(\'meta[name="description"]\').content=siteMeta[lang].description;try',script)
    assert 'document.title=siteMeta' in script
    (out/'app.js').write_text(script)
    page=(root/'index.html').read_text()
    page=re.sub(r'<title>.*?</title>','<title>'+html.escape(site['enTitle'])+'</title>',page)
    page=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+html.escape(site['enDescription'],quote=True)+'">',page)
    seo=f'<link rel="canonical" href="https://{domain}/"><meta property="og:type" content="website"><meta property="og:site_name" content="{site["name"]}"><meta property="og:title" content="{html.escape(site["enTitle"],quote=True)}"><meta property="og:description" content="{html.escape(site["enDescription"],quote=True)}"><meta property="og:url" content="https://{domain}/"><meta property="og:locale" content="en_IN">'
    page=page.replace('</head>',seo+'</head>')
    for section,(title,paragraphs) in data['en'].items():
        page=re.sub(r'(<h[12] data-title="'+section+r'">).*?(</h[12]>)',lambda m:m[1]+title+m[2],page)
        page=re.sub(r'(<div[^>]* data-copy="'+section+r'">).*?(</div>)',lambda m:m[1]+''.join('<p>'+html.escape(p)+'</p>' for p in paragraphs)+m[2],page)
    url='https://brm.best/?partner_id=p42863p153032p8389&subid=12&code=bingame'
    page=re.sub(r'<a class="([^"]*\boutbound\b[^"]*)"',lambda m:'<a href="'+html.escape(url,quote=True)+'" rel="sponsored nofollow" class="'+m[1]+'"',page)
    page=page.replace('Quotex India guide',site['name']+' · India')
    page=page.replace('A clearer way to explore the markets',{'quotexreview.in':'An informed look at the details','quotexguide.in':'A practical path through the essentials','quotexhub.in':'Your account and learning resources'}[domain])
    page=page.replace('<span class="brand-dot">.</span>','<span class="brand-dot">.</span><span class="site-label">'+site['name'].split()[-1]+'</span>')
    page=page.replace('Illustration','Illustration · '+site['name'].split()[-1])
    page=page.replace('id="language"','id="language" aria-label="Choose language / भाषा चुनें"')
    (out/'index.html').write_text(page)
    css=(root/'style.css').read_text().replace('--green:#36e5a0','--green:'+site['accent'])
    css+='\n.site-label{font:600 9px Arial,sans-serif;text-transform:uppercase;letter-spacing:1.5px;margin-left:10px;color:var(--green);border-left:1px solid var(--line);padding-left:10px}\n'
    (out/'style.css').write_text(css)
    (out/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: https://{domain}/sitemap.xml\n')
    (out/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://{domain}/</loc></url></urlset>\n')
    with zipfile.ZipFile(root/'sites'/f'{domain}.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(out.iterdir()): archive.write(p,p.name)
    print(domain,':',[(lang,min(len(v[1][0]) for v in data[lang].values())) for lang in data])
