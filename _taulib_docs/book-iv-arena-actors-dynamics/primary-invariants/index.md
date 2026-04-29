---
{
  "projection_kind": "taulib_declaration",
  "title": "primary_invariants",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/primary-invariants/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::primary_invariants",
  "declaration_slug": "primary-invariants",
  "kind": "def",
  "name": "primary_invariants",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 102,
  "source_line_end": 103,
  "registry_ids": [
    "IV.D270"
  ],
  "related_registry_items": [
    {
      "id": "IV.D270",
      "title": "Five primary invariants",
      "url": "/registry/object/IV.D270/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L102-L103",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L102-L103",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L102-L103)
- Source range: L102-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D270` — Five primary invariants

## Immediate Comment / Docstring

```lean
/-- [IV.D270] The 5 primary invariants: {Entropy, Time, Energy, Mass, Gravity}.
    These are the complete set of E₁-level observables, one per sector.
    Wraps PrimaryInvariant from QuantityFramework. -/
```

## Source Excerpt

```lean
def primary_invariants : List PrimaryInvariant :=
  [.Entropy, .Time, .Energy, .Mass, .Gravity]
```
