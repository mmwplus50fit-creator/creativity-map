# Creativity Map — Toronto & beyond

Version 0.3.0. A static, public-facing cultural atlas prototype for Magnus's Social Activity project.

## Open the preview
Open `index.html` in a modern browser. Application code, catalogue and Leaflet are embedded in that file. An internet connection is required for the OpenStreetMap background and external source pages. The story catalogue and network do not call an AI service, require accounts or use a database. No analytics are installed.

## Included
- Seventeen sourced works, twelve documented places, three media.
- Seven approximate location markers. Five places are deliberately unpinned.
- Map, Stories and Connections views; search, medium, region and period filters.
- Story details with supporting sources and explicit location/date limitations.
- Connection-depth slider up to the full connected component; shortest documented paths have no arbitrary six-step cap.
- Catalogue download, plus CSV for import into a future Google Sheet. There is no live Sheets integration yet.

## Publish with GitHub Pages
1. Create a public repository named `creativity-map` in the intended GitHub account. Initialize it with a README so a default branch exists.
2. Commit `index.html` and `.nojekyll` at the root of `main`. The other source files may also be committed.
3. In the repository's Settings > Pages, select “Deploy from a branch”, branch `main`, folder `/ (root)`, and save.
4. Wait for GitHub to report the deployed URL. Open it without signing in and check map loading, story links, filters and the Connections view on desktop and mobile.

Repository: https://github.com/mmwplus50fit-creator/creativity-map

Live site: https://creativity-map.bucketlistbooks.ca/

GitHub Pages serves main at the repository root. Public access to version 0.1.0 was verified on 15 October 2026.

## Edit and rebuild
`catalogue.json` is the data consumed by the build. Edit it and `index.template.html`, then run `python3 build.py`. This embeds the vendored Leaflet distribution and data in `index.html`. The initial `make_data.py` can regenerate the original seed catalogue and CSV, but running it overwrites catalogue edits; retain it as seed provenance, not the normal editor. The build also regenerates the CSV export.

## Research and mapping rules
Source links, publisher descriptions and evidence notes are in `catalogue.json`. Sources checked 15 October 2026. Recording, painting, writing and live recording are labelled separately; they do not establish the birthplace of every underlying idea. Positions are approximate orientation coordinates, not verified entrances. Studio/house-level certainty is not inferred from a city-level statement. All locations require further coordinate verification before route guidance is introduced.

The source plaque for Anne’s House of Dreams uses 1916; this is explicitly marked provisional and not represented as a publication date. For The Diviners the year 1972 is the display midpoint of the supported 1971–73 period, not a precise creation date. Dates in the filter are display years; see each story's full date label.

## Hosting and dependencies
A static GitHub Pages deployment needs no Neon, Vercel, paid API or secret. GitHub Pages and background-map usage remain subject to the providers' limits. Leaflet 1.9.4 is vendored under its BSD-2-Clause licence (`vendor/LICENSE-Leaflet`). Its bundled CSS mentions default marker image assets; those styles are unused because this app uses custom HTML markers.

The base map uses https://tile.openstreetmap.org/{z}/{x}/{y}.png. Attribution remains visible. Follow https://operations.osmfoundation.org/policies/tiles/: no bulk download, offline prefetch or cache bypass. A provider review is required if usage grows; do not assume unlimited service. Map requests reveal ordinary connection metadata to the tile provider. External sources open only when selected by the visitor.

Original decorative patterns are interface graphics, not artwork/album-cover reproductions. No licence to the owner's original code or editorial material is assigned by this package; the vendored Leaflet licence applies separately.

## Verification
JavaScript syntax and automated DOM interaction checks passed: filters, searches, empty results, reset, story dialog, sources, view switching, documented shortest path and disconnected-node feedback. Referential integrity of all seventeen records passed. Visual browser QA and production access checks have not been performed because the required browser-preview capability was not available. Complete those checks after hosting before treating this as a finished public release.

## Canadian expansion (0.2.0)
Adds MacDonald and Lismer (Group of Seven), The Tragically Hip, Gord Downie, Alanis Morissette and Maestro Fresh Wes. Adds sourced group membership edges and 1990s/2000-onward filters. Alanis relies on a clearly labelled secondary source; the full RPM scan was inaccessible. The Bathouse pin represents Bath community, not the studio. MacDonald House uses an approximate heritage-marker location. Five sites remain unpinned.

## Connections and honours (0.3.0, 23 October 2026)
- Constellation-inspired dark connection field, small translucent nodes, hover/focus labels, optional all-label display and a selected-node halo. Pulse ends after three cycles and respects reduced-motion preferences.
- Explore selector exposes every node in the filtered collection. Slider expands the selected connected component immediately, with counts and an Expand all button. Disconnected components remain accessible through the selector.
- From follows node selection. Destination starts blank; endpoint changes clear old path results. Reset connections restores the selected work and clears endpoints. No path state is stored across sessions.
- Four graph-only artist profiles: Norval Morrisseau, Kenojuak Ashevak, Alex Colville and Alex Janvier. Seven sourced honours edges, including existing Lismer and Downie, connect through Order of Canada and 2008 visual/media arts awards. Original 1967 Medal of Service designation is retained; later promotions are not asserted.
- Shared awards are not evidence of acquaintance or collaboration. New profiles do not establish creation locations, add map pins, or inflate the 17-work count. Region and era filters exclude graph-only artists until suitable place/work evidence is added.
- Sources checked 23 October 2026; official Governor General and Canada Council records linked per edge. Wikipedia artist list used only for discovery. Private BLB Constellation could not be inspected; this is an interpretation, not a reproduction.
- Automated DOM checks cover slider expansion, selected-node/path reset, honours evidence, paths longer than six edges, empty/filter/reset behaviour, graph-only artist search and referential integrity. Visual desktop/iPhone review remains outstanding.
