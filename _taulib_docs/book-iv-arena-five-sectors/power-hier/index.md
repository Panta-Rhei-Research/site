---
{
  "projection_kind": "taulib_declaration",
  "title": "power_hier",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/power-hier/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::power_hier",
  "declaration_slug": "power-hier",
  "kind": "theorem",
  "name": "power_hier",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 113,
  "source_line_end": 120,
  "registry_ids": [
    "IV.P156"
  ],
  "related_registry_items": [
    {
      "id": "IV.P156",
      "title": "Power Hierarchy",
      "url": "/registry/object/IV.P156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L113-L120",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L113-L120",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L113-L120)
- Source range: L113-L120
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P156` — Power Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.P156] Power hierarchy: κ(B;2) = κ(A;1)² and κ(A,C) = κ(A;1)·κ(C;3).
    Wraps CouplingFormulas power relations and multiplicative closure. -/
```

## Source Excerpt

```lean
theorem power_hier :
    -- κ(B;2) = κ(A;1)²
    kappa_BB.numer * (kappa_AA.denom * kappa_AA.denom) =
    (kappa_AA.numer * kappa_AA.numer) * kappa_BB.denom ∧
    -- κ(A,C) = κ(A;1)·κ(C;3) (multiplicative closure)
    kappa_AC.numer * (kappa_AA.denom * kappa_CC.denom) =
    (kappa_AA.numer * kappa_CC.numer) * kappa_AC.denom :=
  ⟨em_is_weak_squared, weak_strong_is_multiplicative⟩
```
