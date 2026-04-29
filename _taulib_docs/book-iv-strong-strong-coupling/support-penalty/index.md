---
{
  "projection_kind": "taulib_declaration",
  "title": "SupportPenalty",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/support-penalty/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::SupportPenalty",
  "declaration_slug": "support-penalty",
  "kind": "structure",
  "name": "SupportPenalty",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 166,
  "source_line_end": 175,
  "registry_ids": [
    "IV.D183"
  ],
  "related_registry_items": [
    {
      "id": "IV.D183",
      "title": "π-support penalty",
      "url": "/registry/object/IV.D183/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L166-L175",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L166-L175",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L166-L175)
- Source range: L166-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D183` — π-support penalty

## Immediate Comment / Docstring

```lean
/-- [IV.D183] Pi-support penalty Pen_pi[n](x):
    measures how far an endomorphism deviates from pure pi-typed
    action at stages beyond n. Penalizes non-pi-typed contributions. -/
```

## Source Excerpt

```lean
structure SupportPenalty where
  /-- Stage n. -/
  stage : Nat
  /-- Penalty range: stages n+1 to 2n. -/
  penalty_range : String := "stages n+1 to 2n"
  /-- Measures deviation from pi-typed action. -/
  measures_deviation : Bool := true
  /-- Non-negative valued. -/
  nonneg : Bool := true
  deriving Repr
```
