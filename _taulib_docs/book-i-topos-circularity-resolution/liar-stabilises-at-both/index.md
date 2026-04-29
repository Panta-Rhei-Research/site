---
{
  "projection_kind": "taulib_declaration",
  "title": "liar_stabilises_at_Both",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-stabilises-at-both/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::liar_stabilises_at_Both",
  "declaration_slug": "liar-stabilises-at-both",
  "kind": "theorem",
  "name": "liar_stabilises_at_Both",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 251,
  "source_line_end": 253,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L251-L253",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L251-L253",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L251-L253)
- Source range: L251-L253
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The Liar lands at Both** (paper Theorem
    `liar-equals-both`).  The ω-germ stabilised truth value of the
    Liar `L = ¬L` is `Both = e_+ + e_- = 1`, the multiplicative unit
    of the boundary algebra `D` — Hegelian "unity of opposites" as
    an algebraic identity. -/
```

## Source Excerpt

```lean
theorem liar_stabilises_at_Both :
    StabilisedValue liarTemplate F B :=
  StabilisedValue.of_period2 liar_period2
```
