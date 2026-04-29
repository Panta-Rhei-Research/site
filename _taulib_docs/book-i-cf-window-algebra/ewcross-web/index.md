---
{
  "projection_kind": "taulib_declaration",
  "title": "EWCrossWeb",
  "permalink": "/verify/taulib/docs/book-i-cf-window-algebra/ewcross-web/",
  "summary_short": "`structure` declaration in `TauLib.BookI.CF.WindowAlgebra`.",
  "declaration_id": "TauLib.BookI.CF.WindowAlgebra::EWCrossWeb",
  "declaration_slug": "ewcross-web",
  "kind": "structure",
  "name": "EWCrossWeb",
  "module_name": "TauLib.BookI.CF.WindowAlgebra",
  "module_url": "/verify/taulib/docs/book-i-cf-window-algebra/",
  "source_line_start": 152,
  "source_line_end": 156,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L152-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.CF.WindowAlgebra",
        "url": "/verify/taulib/docs/book-i-cf-window-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L152-L156",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.CF.WindowAlgebra](/verify/taulib/docs/book-i-cf-window-algebra/)
- Source path: [`TauLib/BookI/CF/WindowAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/CF/WindowAlgebra.lean#L152-L156)
- Source range: L152-L156
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The electroweak cross-web: all three EW observables (g_A, sin²θ_W, M_W/m_n)
    are determined by two adjacent W₃ windows at positions 3 and 4.
    - g_A NLO: 8/W₃(3) = 8/17
    - sin²θ_W NLO: W₃(4)/(W₃(3)−2·W₃(4)) = 5/7
    - M_W/m_n: W₃(3)/W₃(4) = 17/5
    This structure packages 3 from the 17 that is expressible as a sum of
    sums from two overlapping W₃ windows. -/
```

## Source Excerpt

```lean
structure EWCrossWeb where
  w3_3 : Nat  -- W₃(3) = 17
  w3_4 : Nat  -- W₃(4) = 5
  hw3 : w3_3 = windowSum cf_head 3 3
  hw4 : w3_4 = windowSum cf_head 3 4
```
