---
{
  "projection_kind": "taulib_declaration",
  "title": "HomochiralityParityShadow",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/homochirality-parity-shadow/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::HomochiralityParityShadow",
  "declaration_slug": "homochirality-parity-shadow",
  "kind": "structure",
  "name": "HomochiralityParityShadow",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 136,
  "source_line_end": 143,
  "registry_ids": [
    "VI.P10"
  ],
  "related_registry_items": [
    {
      "id": "VI.P10",
      "title": "L-Amino Acid Preference as Parity Shadow",
      "url": "/registry/object/VI.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L136-L143",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L136-L143",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L136-L143)
- Source range: L136-L143
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P10` — L-Amino Acid Preference as Parity Shadow

## Immediate Comment / Docstring

```lean
/-- [VI.P10] L-amino acid preference as Parity Shadow (conjectural).
    The weak sector's chirality (IV.T146 σ=C_τ Majorana, IV.T160 θ_QCD=0)
    seeds the biological enantiomeric excess via the Parity Bridge. -/
```

## Source Excerpt

```lean
structure HomochiralityParityShadow where
  /-- IV.T146: σ = C_τ, all neutrinos Majorana from self-adjointness. -/
  iv_t146_majorana : Bool := true
  /-- IV.T160: θ_QCD = 0, strong CP solved from SA-i mod-3. -/
  iv_t160_strong_cp : Bool := true
  /-- Temporal stability protects chirality. -/
  temporal_protection : Bool := true
  deriving Repr
```
