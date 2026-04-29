---
{
  "projection_kind": "taulib_declaration",
  "title": "planck_sigma_fixed",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/planck-sigma-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::planck_sigma_fixed",
  "declaration_slug": "planck-sigma-fixed",
  "kind": "theorem",
  "name": "planck_sigma_fixed",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 238,
  "source_line_end": 239,
  "registry_ids": [
    "IV.T03"
  ],
  "related_registry_items": [
    {
      "id": "IV.T03",
      "title": "Sector Lifts σ-Equivariant",
      "url": "/registry/object/IV.T03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L238-L239",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/verify/taulib/docs/book-iv-physics-planck-character/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L238-L239",
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/verify/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L238-L239)
- Source range: L238-L239
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T03` — Sector Lifts σ-Equivariant

## Immediate Comment / Docstring

```lean
/-- [IV.T03] ℏ_τ is σ-fixed by definition (structural property). -/
```

## Source Excerpt

```lean
theorem planck_sigma_fixed (h : PlanckCharacter) (hσ : h.sigma_fixed = true) :
    h.sigma_fixed = true := hσ
```
