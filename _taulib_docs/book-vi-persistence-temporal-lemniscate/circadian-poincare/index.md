---
{
  "projection_kind": "taulib_declaration",
  "title": "CircadianPoincare",
  "permalink": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/circadian-poincare/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::CircadianPoincare",
  "declaration_slug": "circadian-poincare",
  "kind": "structure",
  "name": "CircadianPoincare",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/verify/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 69,
  "source_line_end": 82,
  "registry_ids": [
    "VI.T17"
  ],
  "related_registry_items": [
    {
      "id": "VI.T17",
      "title": "Circadian Rhythm as Poincaré Orbit",
      "url": "/registry/object/VI.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L69-L82",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L69-L82",
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
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L69-L82)
- Source range: L69-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T17` — Circadian Rhythm as Poincaré Orbit

## Immediate Comment / Docstring

```lean
/-- [VI.T17] Circadian Rhythm as Poincaré Orbit Theorem.
    The persistence Life loop projected onto τ¹ is a Poincaré limit cycle
    tracing L_T = S¹_act ∨ S¹_rest with period T ≈ 24h.
    Authority: Book III, Part II (Poincaré force ensures periodic orbits). -/
```

## Source Excerpt

```lean
structure CircadianPoincare where
  /-- Period in hours. -/
  period_hours : Nat
  /-- Period ≈ 24 hours. -/
  period_eq : period_hours = 24
  /-- Is a Poincaré limit cycle. -/
  is_limit_cycle : Bool := true
  /-- Traces temporal lemniscate. -/
  traces_L_T : Bool := true
  /-- Winding number w_α = 1 per cycle. -/
  winding_alpha : Nat := 1
  /-- Three characteristics: entrainable, temperature-compensated, free-running. -/
  characteristics : Nat := 3
  deriving Repr
```
