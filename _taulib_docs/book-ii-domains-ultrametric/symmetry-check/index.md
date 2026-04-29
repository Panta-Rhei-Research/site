---
{
  "projection_kind": "taulib_declaration",
  "title": "symmetry_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-ultrametric/symmetry-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Ultrametric`.",
  "declaration_id": "TauLib.BookII.Domains.Ultrametric::symmetry_check",
  "declaration_slug": "symmetry-check",
  "kind": "def",
  "name": "symmetry_check",
  "module_name": "TauLib.BookII.Domains.Ultrametric",
  "module_url": "/verify/taulib/docs/book-ii-domains-ultrametric/",
  "source_line_start": 60,
  "source_line_end": 69,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L60-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Ultrametric",
        "url": "/verify/taulib/docs/book-ii-domains-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L60-L69",
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

- Module: [TauLib.BookII.Domains.Ultrametric](/verify/taulib/docs/book-ii-domains-ultrametric/)
- Source path: [`TauLib/BookII/Domains/Ultrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L60-L69)
- Source range: L60-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Symmetry: δ(x,y) = δ(y,x). Flat double loop. -/
```

## Source Excerpt

```lean
def symmetry_check (bound : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else (disagree_depth x y 5 == disagree_depth y x 5) &&
         go x (y + 1) (fuel - 1)
  termination_by fuel
```
