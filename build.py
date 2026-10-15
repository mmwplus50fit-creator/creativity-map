from pathlib import Path
p=Path(__file__).parent
html=p.joinpath('index.template.html').read_text()
for marker,file in [('/* CATALOGUE */','catalogue.json'),('/* LEAFLET_CSS */','vendor/leaflet.css'),('/* LEAFLET_JS */','vendor/leaflet.js')]:
 html=html.replace(marker,p.joinpath(file).read_text().replace('</script','<\\/script'))
p.joinpath('index.html').write_text(html)
print('Built index.html:',len(html),'characters')

# Keep the editorial CSV synchronized with the canonical catalogue.
import csv, json
catalogue=json.loads(p.joinpath('catalogue.json').read_text())
places={place['id']:place for place in catalogue['places']}
with p.joinpath('catalogue.csv').open('w',newline='') as f:
 writer=csv.writer(f)
 writer.writerow(['id','work','creator','medium','creation_stage','date_label','place','location_precision','source_url','checked','notes'])
 for work in catalogue['works']:
  place=places[work['place']]
  writer.writerow([work['id'],work['title'],work['creator'],work['medium'],work['stage'],work['date'],place['name'],place['precision'],catalogue['sources'][work['source']]['url'],work['checked'],work['aside']])
