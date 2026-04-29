---
{
  "projection_kind": "taulib_declaration",
  "title": "BellInequality",
  "permalink": "/verify/taulib/docs/book-v-orthodox-measurement-unification/bell-inequality/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "declaration_id": "TauLib.BookV.Orthodox.MeasurementUnification::BellInequality",
  "declaration_slug": "bell-inequality",
  "kind": "structure",
  "name": "BellInequality",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/",
  "source_line_start": 164,
  "source_line_end": 177,
  "registry_ids": [
    "V.T135"
  ],
  "related_registry_items": [
    {
      "id": "V.T135",
      "title": "Bell inequality in tau",
      "url": "/registry/object/V.T135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L164-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.MeasurementUnification",
        "url": "/verify/taulib/docs/book-v-orthodox-measurement-unification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L164-L177",
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

- Module: [TauLib.BookV.Orthodox.MeasurementUnification](/verify/taulib/docs/book-v-orthodox-measurement-unification/)
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean#L164-L177)
- Source range: L164-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T135` — Bell inequality in tau

## Immediate Comment / Docstring

```lean
/-- [V.T135] Bell inequality in tau: the CHSH bound is 2*sqrt(2),
    exactly matching the quantum prediction (Tsirelson bound).

    Boundary characters are non-local: they live on the connected
    space L = S^1 v S^1. The crossing point of L enables correlations
    that exceed the CHSH classical bound |S| <= 2.

    There are no hidden variables because boundary characters are
    not factorable over space-like separation. The "hidden variable"
    is the boundary character itself, which is shared across the
    lemniscate -- but sharing a boundary character is not the same
    as a classical hidden variable (it respects Tsirelson). -/
```

## Source Excerpt

```lean
structure BellInequality where
  /-- Classical CHSH bound (|S| <= 2). -/
  classical_bound : Nat := 2
  /-- Quantum Tsirelson bound numerator (2*sqrt(2) ~ 2828/1000). -/
  tsirelson_numer : Nat := 2828
  /-- Tsirelson bound denominator. -/
  tsirelson_denom : Nat := 1000
  /-- Denominator positive. -/
  tsirelson_denom_pos : tsirelson_denom > 0 := by omega
  /-- tau reproduces Tsirelson (not classical). -/
  reproduces_tsirelson : Bool := true
  /-- No hidden variables. -/
  no_hidden_variables : Bool := true
  deriving Repr
```
