---
{
  "projection_kind": "taulib_declaration",
  "title": "second_law_inv",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/second-law-inv/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::second_law_inv",
  "declaration_slug": "second-law-inv",
  "kind": "theorem",
  "name": "second_law_inv",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 114,
  "source_line_end": 121,
  "registry_ids": [
    "IV.P157"
  ],
  "related_registry_items": [
    {
      "id": "IV.P157",
      "title": "Second-law inversion",
      "url": "/registry/object/IV.P157/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L114-L121",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L114-L121",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L114-L121)
- Source range: L114-L121
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P157` — Second-law inversion

## Immediate Comment / Docstring

```lean
/-- [IV.P157] Second-law inversion: time-reversal swaps entropy
    increase/decrease. The arrow of time and the arrow of entropy
    are the same structural arrow from the refinement tower. -/
```

## Source Excerpt

```lean
theorem second_law_inv :
    -- Time and Entropy are distinct invariants
    PrimaryInvariant.Time ≠ PrimaryInvariant.Entropy ∧
    -- Time is carried by the base (temporal sector)
    PrimaryInvariant.carrier .Time = .Base ∧
    -- Entropy spans the crossing (all sectors)
    PrimaryInvariant.carrier .Entropy = .Crossing := by
  exact ⟨by decide, rfl, rfl⟩
```
