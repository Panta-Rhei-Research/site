---
{
  "projection_kind": "taulib_declaration",
  "title": "opposite_denom_contrast",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/opposite-denom-contrast/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::opposite_denom_contrast",
  "declaration_slug": "opposite-denom-contrast",
  "kind": "theorem",
  "name": "opposite_denom_contrast",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 407,
  "source_line_end": 412,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L407-L412",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L407-L412",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L407-L412)
- Source range: L407-L412
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The omega-sector coupling has the same numerator but different denominator.
    kappa(omega) = iota^3/(1+iota) vs kappa(C) = iota^3/(1-iota).
    The (1-iota) vs (1+iota) produces confinement vs stabilization. -/
```

## Source Excerpt

```lean
theorem opposite_denom_contrast :
    strong_sector.coupling_numer = higgs_sector.coupling_numer ∧
    strong_sector.coupling_denom ≠ higgs_sector.coupling_denom := by
  constructor
  · simp [strong_sector, higgs_sector]
  · simp [strong_sector, higgs_sector, iota_cu_denom, iotaD, iota, iota_tau_denom, iota_tau_numer]
```
