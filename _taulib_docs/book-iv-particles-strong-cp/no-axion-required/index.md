---
{
  "projection_kind": "taulib_declaration",
  "title": "no_axion_required",
  "permalink": "/verify/taulib/docs/book-iv-particles-strong-cp/no-axion-required/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.StrongCP`.",
  "declaration_id": "TauLib.BookIV.Particles.StrongCP::no_axion_required",
  "declaration_slug": "no-axion-required",
  "kind": "def",
  "name": "no_axion_required",
  "module_name": "TauLib.BookIV.Particles.StrongCP",
  "module_url": "/verify/taulib/docs/book-iv-particles-strong-cp/",
  "source_line_start": 102,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L102-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.StrongCP",
        "url": "/verify/taulib/docs/book-iv-particles-strong-cp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L102-L105",
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

- Module: [TauLib.BookIV.Particles.StrongCP](/verify/taulib/docs/book-iv-particles-strong-cp/)
- Source path: [`TauLib/BookIV/Particles/StrongCP.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L102-L105)
- Source range: L102-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Peccei-Quinn mechanism resolves strong CP by introducing U(1)_PQ → axion.
    SA-i achieves the same result without any new field:

    Structural correspondence:
    - PQ U(1)       ↔  ℤ/3ℤ winding symmetry of C-sector (discrete, not continuous)
    - Axion field   ↔  η-winding number (integer, not a dynamical field)
    - PQ scale f_PQ ↔  κ(C;3)·m_n ≈ 57 MeV (structurally fixed, not a free parameter)

    τ-prediction: no axion exists; ADMX, CASPEr, and related experiments
    should find null results.
    Scope: tau-effective. -/
```

## Source Excerpt

```lean
def no_axion_required : String :=
  "SA-i is the τ-native Peccei-Quinn mechanism: θ_QCD = 0 without any new field. " ++
  "PQ U(1) ↔ ℤ/3ℤ; axion ↔ η-winding number; f_PQ ↔ κ(C;3)·m_n. " ++
  "Prediction: no axion; ADMX/CASPEr should find null result."
```
