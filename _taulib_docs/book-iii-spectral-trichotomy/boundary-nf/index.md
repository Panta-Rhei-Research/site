---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryNF",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/boundary-nf/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::BoundaryNF",
  "declaration_slug": "boundary-nf",
  "kind": "structure",
  "name": "BoundaryNF",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 124,
  "source_line_end": 129,
  "registry_ids": [
    "III.D24"
  ],
  "related_registry_items": [
    {
      "id": "III.D24",
      "title": "Boundary Normal Form",
      "url": "/registry/object/III.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L124-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L124-L129",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L124-L129)
- Source range: L124-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D24` — Boundary Normal Form

## Immediate Comment / Docstring

```lean
/-- [III.D24] Boundary normal form: decompose x into (a, b) where
    a is B-supported and b is C-supported. The X-component goes to
    whichever has a larger contribution (tie → B). -/
```

## Source Excerpt

```lean
structure BoundaryNF where
  b_part : TauIdx    -- B-supported value
  c_part : TauIdx    -- C-supported value
  x_part : TauIdx    -- X-supported value (crossing prime contribution)
  depth : TauIdx     -- depth of decomposition
  deriving Repr, DecidableEq, BEq
```
