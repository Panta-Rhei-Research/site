---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_complement_recap",
  "permalink": "/verify/taulib/docs/book-v-prologue-hermetic-principle/temporal-complement-recap/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.HermeticPrinciple`.",
  "declaration_id": "TauLib.BookV.Prologue.HermeticPrinciple::temporal_complement_recap",
  "declaration_slug": "temporal-complement-recap",
  "kind": "theorem",
  "name": "temporal_complement_recap",
  "module_name": "TauLib.BookV.Prologue.HermeticPrinciple",
  "module_url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/",
  "source_line_start": 125,
  "source_line_end": 127,
  "registry_ids": [
    "V.R05"
  ],
  "related_registry_items": [
    {
      "id": "V.R05",
      "title": "The Temporal Complement as test case",
      "url": "/registry/object/V.R05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L125-L127",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.HermeticPrinciple",
        "url": "/verify/taulib/docs/book-v-prologue-hermetic-principle/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L125-L127",
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

- Module: [TauLib.BookV.Prologue.HermeticPrinciple](/verify/taulib/docs/book-v-prologue-hermetic-principle/)
- Source path: [`TauLib/BookV/Prologue/HermeticPrinciple.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/HermeticPrinciple.lean#L125-L127)
- Source range: L125-L127
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R05` — The Temporal Complement as test case

## Immediate Comment / Docstring

```lean
/-- [V.R05] Temporal complement recap: κ(A;1) + κ(D;1) = 1 from Book IV.

    This identity means the base sectors (Gravity + Weak) fully account
    for the temporal coupling budget. The temporal pair is hermetically
    closed: no coupling leaks between temporal and spatial sectors.

    Wraps Tau.BookIV.Arena.temporal_complement. -/
```

## Source Excerpt

```lean
theorem temporal_complement_recap :
    kappa_AA.numer + kappa_DD.numer = kappa_AA.denom :=
  Tau.BookIV.Arena.temporal_complement
```
