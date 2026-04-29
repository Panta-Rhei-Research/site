---
{
  "projection_kind": "taulib_declaration",
  "title": "CSectorDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/csector-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::CSectorDef",
  "declaration_slug": "csector-def",
  "kind": "structure",
  "name": "CSectorDef",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 59,
  "source_line_end": 72,
  "registry_ids": [
    "IV.D144"
  ],
  "related_registry_items": [
    {
      "id": "IV.D144",
      "title": "The C-sector",
      "url": "/registry/object/IV.D144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L59-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L59-L72",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L59-L72)
- Source range: L59-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D144` — The C-sector

## Immediate Comment / Docstring

```lean
/-- [IV.D144] The C-sector: E1 instantiation of the eta-generator.
    Primorial depth d=3, chi_minus-dominant polarity, fiber T^2 carrier,
    self-coupling kappa(C;3) = iota_tau^3/(1-iota_tau).
    The (1-iota_tau) denominator is the structural signature of confinement. -/
```

## Source Excerpt

```lean
structure CSectorDef where
  /-- Generator: eta. -/
  gen : Generator := .eta
  /-- Abstract sector label. -/
  sector : Sector := .C
  /-- Primorial activation depth. -/
  depth : Nat := 3
  /-- Chi-minus dominant polarity. -/
  polarity : PolaritySign := .ChiMinus
  /-- Coupling numerator (iota^3 * 10^6, common denom with (10^6 - iota)). -/
  coupling_numer : Nat := iota_cu_numer * iotaD
  /-- Coupling denominator (iota_cu_denom * (10^6 - iota)). -/
  coupling_denom : Nat := iota_cu_denom * (iotaD - iota)
  deriving Repr
```
