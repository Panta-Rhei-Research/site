---
{
  "projection_kind": "taulib_declaration",
  "title": "cp_phase_origin",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/cp-phase-origin/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::cp_phase_origin",
  "declaration_slug": "cp-phase-origin",
  "kind": "theorem",
  "name": "cp_phase_origin",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 251,
  "source_line_end": 255,
  "registry_ids": [
    "IV.P67"
  ],
  "related_registry_items": [
    {
      "id": "IV.P67",
      "title": "CP Violation from Sigma-Polarity",
      "url": "/registry/object/IV.P67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L251-L255",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L251-L255",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L251-L255)
- Source range: L251-L255
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P67` — CP Violation from Sigma-Polarity

## Immediate Comment / Docstring

```lean
/-- [IV.P67] The CP-violating phase in the PMNS matrix arises from
    the sigma-polarity involution on L. The involution sigma acts
    on boundary characters, and its action on the A-sector produces
    a residual complex phase when combined with charge conjugation.
    This is the categorical origin of leptonic CP violation.

    Structural: the number of independent CP phases equals the
    number of generations minus 2 (for Dirac neutrinos):
    N_CP = (N-1)(N-2)/2 = (3-1)(3-2)/2 = 1. -/
```

## Source Excerpt

```lean
theorem cp_phase_origin :
    -- Formula: (N-1)(N-2)/2 for N=3 gives 1
    (3 - 1) * (3 - 2) / 2 = 1 ∧
    pmns_matrix.num_cp_phases = 1 := by
  exact ⟨by omega, rfl⟩
```
