---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryonState",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/baryon-state/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::BaryonState",
  "declaration_slug": "baryon-state",
  "kind": "structure",
  "name": "BaryonState",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 337,
  "source_line_end": 348,
  "registry_ids": [
    "IV.D191"
  ],
  "related_registry_items": [
    {
      "id": "IV.D191",
      "title": "Baryon state",
      "url": "/registry/object/IV.D191/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L337-L348",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L337-L348",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L337-L348)
- Source range: L337-L348
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D191` — Baryon state

## Immediate Comment / Docstring

```lean
/-- [IV.D191] A baryon: composite |q_r q_g q_b> with three quarks,
    pairwise distinct colors {0,1,2}, total color 0 mod 3. -/
```

## Source Excerpt

```lean
structure BaryonState where
  /-- Three quark flavors. -/
  flavor_1 : String
  flavor_2 : String
  flavor_3 : String
  /-- Three color classes (must be {0,1,2}). -/
  color_1 : Nat := 0
  color_2 : Nat := 1
  color_3 : Nat := 2
  /-- Total color mod 3 = 0. -/
  is_singlet : Bool := true
  deriving Repr
```
