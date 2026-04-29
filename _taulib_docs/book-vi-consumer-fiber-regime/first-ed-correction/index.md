---
{
  "projection_kind": "taulib_declaration",
  "title": "FirstEdCorrection",
  "permalink": "/verify/taulib/docs/book-vi-consumer-fiber-regime/first-ed-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.FiberRegime`.",
  "declaration_id": "TauLib.BookVI.Consumer.FiberRegime::FirstEdCorrection",
  "declaration_slug": "first-ed-correction",
  "kind": "structure",
  "name": "FirstEdCorrection",
  "module_name": "TauLib.BookVI.Consumer.FiberRegime",
  "module_url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/",
  "source_line_start": 70,
  "source_line_end": 77,
  "registry_ids": [
    "VI.R19"
  ],
  "related_registry_items": [
    {
      "id": "VI.R19",
      "title": "1st Ed Correction: Mixer (α,π) to (γ,η)",
      "url": "/registry/object/VI.R19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L70-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.FiberRegime",
        "url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L70-L77",
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

- Module: [TauLib.BookVI.Consumer.FiberRegime](/verify/taulib/docs/book-vi-consumer-fiber-regime/)
- Source path: [`TauLib/BookVI/Consumer/FiberRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L70-L77)
- Source range: L70-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R19` — 1st Ed Correction: Mixer (α,π) to (γ,η)

## Immediate Comment / Docstring

```lean
/-- [VI.R19] 1st Edition Correction: mixer placement.
    1st Ed paired (α, π) for consumer; 2nd Ed corrects to (π', π'').
    The mixed sector requires both fiber generators, not base generators. -/
```

## Source Excerpt

```lean
structure FirstEdCorrection where
  /-- Old (incorrect) pairing. -/
  old_pairing : String := "alpha_pi"
  /-- New (correct) pairing. -/
  new_pairing : String := "pi_prime_pi_double_prime"
  /-- Correction rationale: fiber generators required. -/
  rationale : String := "mixed_sector_requires_fiber_pair"
  deriving Repr
```
