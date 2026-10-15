from pathlib import Path
p=Path(__file__).parent
html=p.joinpath('index.template.html').read_text()
for marker,file in [('/* CATALOGUE */','catalogue.json'),('/* LEAFLET_CSS */','vendor/leaflet.css'),('/* LEAFLET_JS */','vendor/leaflet.js')]:
 html=html.replace(marker,p.joinpath(file).read_text().replace('</script','<\\/script'))
p.joinpath('index.html').write_text(html)
print('Built index.html:',len(html),'characters')
