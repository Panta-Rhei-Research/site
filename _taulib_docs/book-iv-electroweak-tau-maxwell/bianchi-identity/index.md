---
{
  "projection_kind": "taulib_declaration",
  "title": "BianchiIdentity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/bianchi-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::BianchiIdentity",
  "declaration_slug": "bianchi-identity",
  "kind": "structure",
  "name": "BianchiIdentity",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 219,
  "source_line_end": 227,
  "registry_ids": [
    "IV.T42"
  ],
  "related_registry_items": [
    {
      "id": "IV.T42",
      "title": "Homogeneous Maxwell Equations",
      "url": "/registry/object/IV.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L219-L227",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L219-L227",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L219-L227)
- Source range: L219-L227
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T42` — Homogeneous Maxwell Equations

## Immediate Comment / Docstring

```lean
/-- [IV.T42] Bianchi identity dF = 0: automatic from F = dA and d² = 0.
    In component form: ∂_{[μ} F_{νρ]} = 0.
    Physical content: div B = 0 (no magnetic monopoles) + Faraday's law. -/
```

## Source Excerpt

```lean
structure BianchiIdentity where
  /-- dF = 0 holds. -/
  df_zero : Bool := true
  /-- Follows from d² = 0. -/
  from_d_squared : Bool := true
  /-- Maxwell equation count from Bianchi: 2 (div B = 0, Faraday). -/
  maxwell_count : Nat
  count_eq : maxwell_count = 2
  deriving Repr
```
