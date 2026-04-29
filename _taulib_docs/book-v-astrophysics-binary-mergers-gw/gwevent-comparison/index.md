---
{
  "projection_kind": "taulib_declaration",
  "title": "GWEventComparison",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwevent-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::GWEventComparison",
  "declaration_slug": "gwevent-comparison",
  "kind": "structure",
  "name": "GWEventComparison",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 294,
  "source_line_end": 301,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L294-L301",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L294-L301",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L294-L301)
- Source range: L294-L301
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- GW event comparison entry — V.D281 -/
```

## Source Excerpt

```lean
structure GWEventComparison where
  event_name : String
  m1_x10 : Nat           -- m₁ in 0.1 M☉
  m2_x10 : Nat           -- m₂ in 0.1 M☉
  chirp_mass_x10 : Nat   -- M_chirp in 0.1 M☉
  final_mass_x10 : Nat   -- M_final in 0.1 M☉ (0 for BNS)
  is_bbh : Bool          -- true for BBH, false for BNS
  deriving Repr
```
