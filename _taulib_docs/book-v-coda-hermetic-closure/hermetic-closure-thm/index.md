---
{
  "projection_kind": "taulib_declaration",
  "title": "HermeticClosureThm",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/hermetic-closure-thm/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::HermeticClosureThm",
  "declaration_slug": "hermetic-closure-thm",
  "kind": "structure",
  "name": "HermeticClosureThm",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 163,
  "source_line_end": 174,
  "registry_ids": [
    "V.T161"
  ],
  "related_registry_items": [
    {
      "id": "V.T161",
      "title": "The Hermetic Closure",
      "url": "/registry/object/V.T161/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L163-L174",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L163-L174",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L163-L174)
- Source range: L163-L174
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T161` — The Hermetic Closure

## Immediate Comment / Docstring

```lean
/-- [V.T161] The Hermetic Closure: the 5-sector structure from ι_τ
    produces necessary conditions for observers.

    From 5 sectors → periodic table, nuclei, chemistry, planets, mass.
    This is NOT an anthropic argument: the conditions follow from the
    sector structure, which is fixed by the axioms. -/
```

## Source Excerpt

```lean
structure HermeticClosureThm where
  /-- Number of sectors. -/
  n_sectors : Nat
  /-- Five sectors. -/
  sectors_eq : n_sectors = 5
  /-- Produces observer conditions. -/
  observer_conditions : Bool := true
  /-- Not anthropic (structural). -/
  not_anthropic : Bool := true
  /-- Observer requirements (periodic table, nuclei, chemistry, planets, mass). -/
  observer_requirements : Nat := 5
  deriving Repr
```
