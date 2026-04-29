---
{
  "projection_kind": "taulib_declaration",
  "title": "max_tet_div",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/max-tet-div/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::max_tet_div",
  "declaration_slug": "max-tet-div",
  "kind": "def",
  "name": "max_tet_div",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 200,
  "source_line_end": 209,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L200-L209",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.TowerAtoms",
        "url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L200-L209",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Coordinates.TowerAtoms](/verify/taulib/docs/book-i-coordinates-tower-atoms/)
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L200-L209)
- Source range: L200-L209
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Max c such that a↑↑(c-1) divides v. Starts at c=1; increments while a↑↑c | v. -/
```

## Source Excerpt

```lean
def max_tet_div (a v : TauIdx) : TauIdx :=
  if a ≤ 1 then 1
  else go a v 1 v
where
  go (a v c fuel : TauIdx) : TauIdx :=
    if fuel = 0 then c
    else if v % (tetration a c) ≠ 0 then c
    else go a v (c + 1) (fuel - 1)
  termination_by fuel
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
