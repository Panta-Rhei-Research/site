---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_extension_b",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-thinness/crt-extension-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.Thinness`.",
  "declaration_id": "TauLib.BookI.Holomorphy.Thinness::crt_extension_b",
  "declaration_slug": "crt-extension-b",
  "kind": "theorem",
  "name": "crt_extension_b",
  "module_name": "TauLib.BookI.Holomorphy.Thinness",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-thinness/",
  "source_line_start": 87,
  "source_line_end": 90,
  "registry_ids": [
    "I.L08"
  ],
  "related_registry_items": [
    {
      "id": "I.L08",
      "title": "CRT Extension",
      "url": "/registry/object/I.L08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L87-L90",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.Thinness",
        "url": "/verify/taulib/docs/book-i-holomorphy-thinness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L87-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Holomorphy.Thinness](/verify/taulib/docs/book-i-holomorphy-thinness/)
- Source path: [`TauLib/BookI/Holomorphy/Thinness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L87-L90)
- Source range: L87-L90
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L08` — CRT Extension

## Immediate Comment / Docstring

```lean
/-- [I.L08] CRT Extension: tower coherence constrains function output
    via the reduce map. The output at stage k is always reduced mod
    primorial k — this is the vertical consistency that enables extension.

    For the B-sector: reduce(f.b_fun(n, l), k) = f.b_fun(n, k) for k ≤ l. -/
```

## Source Excerpt

```lean
theorem crt_extension_b (f : StageFun) (hcoh : TowerCoherent f)
    (n k l : TauIdx) (hkl : k ≤ l) :
    reduce (f.b_fun n l) k = f.b_fun n k :=
  hcoh.1 n k l hkl
```
