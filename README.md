# Creativity Map — Toronto & beyond

Version 0.1.0. A static, public-facing cultural atlas prototype for Magnus's Social Activity project.

## Open the preview
Open `index.html` in a modern browser. Application code, catalogue and Leaflet are embedded in that file. An internet connection is required for the OpenStreetMap background and external source pages. The story catalogue and network do not call an AI service, require accounts or use a database. No analytics are installed.

## Included
- Ten sourced works, seven documented places, three media.
- Five approximate location markers. Two places are deliberately unpinned.
- Map, Stories and Connections views; search, medium, region and period filters.
- Story details with supporting sources and explicit location/date limitations.
- One-, two-, three- and up-to-six-degree graph exploration and a shortest documented path finder.
- Catalogue download, plus CSV for import into a future Google Sheet. There is no live Sheets integration yet.

## Publish with GitHub Pages
1. Create a public repository named `creativity-map` in the intended GitHub account. Initialize it with a README so a default branch exists.
2. Commit `index.html` and `.nojekyll` at the root of `main`. The other source files may also be committed.
3. In the repository's Settings > Pages, select “Deploy from a branch”, branch `main`, folder `/ (root)`, and save.
4. Wait for GitHub to report the deployed URL. Open it without signing in and check map loading, story links, filters and the Connections view on desktop and mobile.

Repository: https://github.com/mmwplus50fit-creator/creativity-map

The owner created the public repository and the prototype source is prepared for main. Pages must be enabled in repository settings. This README does not claim a verified live deployment.

## Edit and rebuild
`catalogue.json` is the data consumed by the build. Edit it and `index.template.html`, then run `python3 build.py`. This embeds the vendored Leaflet distribution and data in `index.html`. The initial `make_data.py` can regenerate the original seed catalogue and CSV, but running it overwrites catalogue edits; retain it as seed provenance, not the normal editor. Keep the CSV export synchronized after data edits.

## Research and mapping rules
Source links, publisher descriptions and evidence notes are in `catalogue.json`. Sources checked 15 October 2026. Recording, painting, writing and live recording are labelled separately; they do not establish the birthplace of every underlying idea. Positions are approximate orientation coordinates, not verified entrances. Studio/house-level certainty is not inferred from a city-level statement. All locations require further coordinate verification before route guidance is introduced.

The source plaque for Anne’s House of Dreams uses 1916; this is explicitly marked provisional and not represented as a publication date. For The Diviners the year 1972 is the display midpoint of the supported 1971–73 period, not a precise creation date. Dates in the filter are display years; see each story's full date label.

## Hosting and dependencies
A static GitHub Pages deployment needs no Neon, Vercel, paid API or secret. GitHub Pages and background-map usage remain subject to the providers' limits. Leaflet 1.9.4 is vendored under its BSD-2-Clause licence (`vendor/LICENSE-Leaflet`). Its bundled CSS mentions default marker image assets; those styles are unused because this app uses custom HTML markers.

The base map uses https://tile.openstreetmap.org/{z}/{x}/{y}.png. Attribution remains visible. Follow https://operations.osmfoundation.org/policies/tiles/: no bulk download, offline prefetch or cache bypass. A provider review is required if usage grows; do not assume unlimited service. Map requests reveal ordinary connection metadata to the tile provider. External sources open only when selected by the visitor.

Original decorative patterns are interface graphics, not artwork/album-cover reproductions. No licence to the owner's original code or editorial material is assigned by this package; the vendored Leaflet licence applies separately.

## Verification
JavaScript syntax and automated DOM interaction checks passed: filters, searches, empty results, reset, story dialog, sources, view switching, documented shortest path and disconnected-node feedback. Referential integrity of all ten records passed. Visual browser QA and production access checks have not been performed because the required browser-preview capability was not available. Complete those checks after hosting before treating this as a finished public release.
