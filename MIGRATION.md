# Migration record

Destination: [asheshg/skills](https://github.com/asheshg/skills).

| Skill | Historical source | Published commit checked |
|---|---|---|
| First Draft | [asheshg/first-draft](https://github.com/asheshg/first-draft) | cef19e81b56e5fecf728eb63a8c4e3e7c8ec44fd |
| Website Competitor Analysis | [asheshg/website-competitor-analysis](https://github.com/asheshg/website-competitor-analysis) | 0e7d39cfd6f668ba1983610bd0c20081689c4812 |

Imported the current local source and documentation as a new snapshot. Historical Git commits remain in the source repositories; they were not rewritten or imported as submodules. Existing repositories were not deleted, archived, or redirected.

Excluded nested `.git` directories, LFS object-store duplicates, Python bytecode, smoke artifacts, and empty working asset folders. Six actual presentation assets remain and use Git LFS. Local scanner environments and raw reports are not published.

Installation uses the individual `skills/<skill-name>` folder from this shared repository. The website skill includes framework and validator changes newer than its old published version. First Draft's helper scripts matched the historical published version before migration; this migration does not claim to repair their known rendering or destructive-write limitations.

Static syntax, JSON, internal links, and ZIP integrity were checked. Target scripts, renderers, and live audits were not executed. Both security reviews remain CAUTION, with First Draft's automated installation gate unresolved. See the per-skill review files for exact scanner scores, coverage, and triage.
