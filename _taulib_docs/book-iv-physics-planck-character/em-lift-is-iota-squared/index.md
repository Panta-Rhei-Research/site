---
{
  "projection_kind": "taulib_declaration",
  "title": "em_lift_is_iota_squared",
  "permalink": "/corpus/taulib/docs/book-iv-physics-planck-character/em-lift-is-iota-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::em_lift_is_iota_squared",
  "declaration_slug": "em-lift-is-iota-squared",
  "kind": "theorem",
  "name": "em_lift_is_iota_squared",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/corpus/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 265,
  "source_line_end": 268,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L265-L268",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/corpus/taulib/docs/book-iv-physics-planck-character/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L265-L268",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/corpus/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L265-L268)
- Source range: L265-L268
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The EM sector lift is ι_τ² (weak squared). -/
```

## Source Excerpt

```lean
theorem em_lift_is_iota_squared :
    lift_em.target_numer = iota_sq_numer ∧
    lift_em.target_denom = iota_sq_denom := by
  exact ⟨rfl, rfl⟩
```
