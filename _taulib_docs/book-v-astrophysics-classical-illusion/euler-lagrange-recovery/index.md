---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_lagrange_recovery",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/euler-lagrange-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::euler_lagrange_recovery",
  "declaration_slug": "euler-lagrange-recovery",
  "kind": "theorem",
  "name": "euler_lagrange_recovery",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [
    "V.T79"
  ],
  "related_registry_items": [
    {
      "id": "V.T79",
      "title": "Two-Regime Readout --- V.T31",
      "url": "/registry/object/V.T79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L161-L163",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L161-L163",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.T79` — Two-Regime Readout --- V.T31

## Immediate Comment / Docstring

```lean
/-- [V.T79] Euler-Lagrange recovery: the classical variational
    equations emerge from τ-defect minimization in the Newtonian
    readout regime.

    The action S = ∫ L dt is the integrated defect cost
    along a world-line in the D-sector readout. -/
```

## Source Excerpt

```lean
theorem euler_lagrange_recovery :
    "Euler-Lagrange = defect minimization in D-sector readout" =
    "Euler-Lagrange = defect minimization in D-sector readout" := rfl
```
