---
{
  "projection_kind": "taulib_declaration",
  "title": "injectivity_check_go",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact/injectivity-check-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Hyperfact`.",
  "declaration_id": "TauLib.BookI.Coordinates.Hyperfact::injectivity_check_go",
  "declaration_slug": "injectivity-check-go",
  "kind": "def",
  "name": "injectivity_check_go",
  "module_name": "TauLib.BookI.Coordinates.Hyperfact",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact/",
  "source_line_start": 94,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L94-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Hyperfact",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L94-L100",
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

- Module: [TauLib.BookI.Coordinates.Hyperfact](/verify/taulib/docs/book-i-coordinates-hyperfact/)
- Source path: [`TauLib/BookI/Coordinates/Hyperfact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L94-L100)
- Source range: L94-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check Φ is injective on [2..n]: no two distinct X values share coordinates. -/
```

## Source Excerpt

```lean
def injectivity_check_go (i n : Nat) (fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if i > n then true
  else
    let ok := hyperfact_check i && encoding_check i
    ok && injectivity_check_go (i + 1) n (fuel - 1)
termination_by fuel
```
