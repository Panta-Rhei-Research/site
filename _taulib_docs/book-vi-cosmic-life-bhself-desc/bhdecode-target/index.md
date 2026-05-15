---
{
  "projection_kind": "taulib_declaration",
  "title": "BHDecodeTarget",
  "permalink": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/bhdecode-target/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.BHSelfDesc`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHSelfDesc::BHDecodeTarget",
  "declaration_slug": "bhdecode-target",
  "kind": "structure",
  "name": "BHDecodeTarget",
  "module_name": "TauLib.BookVI.CosmicLife.BHSelfDesc",
  "module_url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/",
  "source_line_start": 38,
  "source_line_end": 45,
  "registry_ids": [
    "VI.D58"
  ],
  "related_registry_items": [
    {
      "id": "VI.D58",
      "title": "BH DecodeTarget",
      "url": "/registry/object/VI.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L38-L45",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHSelfDesc",
        "url": "/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L38-L45",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVI.CosmicLife.BHSelfDesc](/corpus/taulib/docs/book-vi-cosmic-life-bhself-desc/)
- Source path: [`TauLib/BookVI/CosmicLife/BHSelfDesc.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHSelfDesc.lean#L38-L45)
- Source range: L38-L45
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VI.D58` — BH DecodeTarget

## Immediate Comment / Docstring

```lean
/-- [VI.D58] BH DecodeTarget: argmin of lex defect = Kerr-Newman.
    The unique minimizer (Israel-Carter-Robinson uniqueness theorem). -/
```

## Source Excerpt

```lean
structure BHDecodeTarget where
  /-- Selects argmin of lexicographic defect. -/
  selects_argmin : Bool := true
  /-- Target is the Kerr-Newman solution. -/
  kerr_newman : Bool := true
  /-- Charge parameters determining the target. -/
  charge_count : Nat := 3  -- (M, J, Q)
  deriving Repr
```
