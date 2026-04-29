---
{
  "projection_kind": "taulib_declaration",
  "title": "ChainComplex",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/chain-complex/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::ChainComplex",
  "declaration_slug": "chain-complex",
  "kind": "structure",
  "name": "ChainComplex",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 48,
  "source_line_end": 50,
  "registry_ids": [
    "II.D84"
  ],
  "related_registry_items": [
    {
      "id": "II.D84",
      "title": "Chain Complex",
      "url": "/registry/object/II.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L48-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L48-L50",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L48-L50)
- Source range: L48-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D84` — Chain Complex

## Immediate Comment / Docstring

```lean
/-- [II.D84] A chain complex on the primorial tower. The boundary map
    d_n reduces from stage n to stage n-1 (mod prime p_n). -/
```

## Source Excerpt

```lean
structure ChainComplex where
  max_degree : Nat
  boundary : Nat → Nat → Nat  -- boundary(n, x) = d_n(x)
```
