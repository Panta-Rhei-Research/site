---
{
  "projection_kind": "taulib_declaration",
  "title": "all_regime_independent",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/all-regime-independent/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::all_regime_independent",
  "declaration_slug": "all-regime-independent",
  "kind": "theorem",
  "name": "all_regime_independent",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 211,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L211-L214",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L211-L214",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L211-L214)
- Source range: L211-L214
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All no-running entries are regime-independent. -/
```

## Source Excerpt

```lean
theorem all_regime_independent :
    (all_no_running.map NoRunningPrinciple.regime_independent).all (· == true) = true := by
  simp [all_no_running, no_running_em, no_running_weak, no_running_strong,
        no_running_gravity, no_running_higgs]
```
