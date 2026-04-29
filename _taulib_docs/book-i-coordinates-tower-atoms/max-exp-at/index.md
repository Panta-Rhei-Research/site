---
{
  "projection_kind": "taulib_declaration",
  "title": "max_exp_at",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/max-exp-at/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::max_exp_at",
  "declaration_slug": "max-exp-at",
  "kind": "def",
  "name": "max_exp_at",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 188,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L188-L197",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L188-L197",
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
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L188-L197)
- Source range: L188-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Max exponent: largest b such that base^(b+1) divides n. Returns 0-indexed. -/
```

## Source Excerpt

```lean
def max_exp_at (base n : TauIdx) : TauIdx :=
  if base ≤ 1 then 0
  else go base n 0 n
where
  go (base n b fuel : TauIdx) : TauIdx :=
    if fuel = 0 then b
    else if n % (base ^ (b + 1)) ≠ 0 then b
    else go base n (b + 1) (fuel - 1)
  termination_by fuel
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
