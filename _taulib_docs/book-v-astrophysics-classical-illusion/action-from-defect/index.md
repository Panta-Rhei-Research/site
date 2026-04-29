---
{
  "projection_kind": "taulib_declaration",
  "title": "action_from_defect",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/action-from-defect/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::action_from_defect",
  "declaration_slug": "action-from-defect",
  "kind": "theorem",
  "name": "action_from_defect",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 175,
  "source_line_end": 177,
  "registry_ids": [
    "V.P57"
  ],
  "related_registry_items": [
    {
      "id": "V.P57",
      "title": "Bertrand as Readout Constraint --- V.P21",
      "url": "/registry/object/V.P57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L175-L177",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L175-L177",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/verify/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L175-L177)
- Source range: L175-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P57` — Bertrand as Readout Constraint --- V.P21

## Immediate Comment / Docstring

```lean
/-- [V.P57] Action principle from defect minimization: the least-action
    principle of classical mechanics is a readout of the τ-framework's
    defect minimization principle.

    In the classical limit, the defect functional reduces to the
    action integral S[q] = ∫ L(q, dq/dt) dt. -/
```

## Source Excerpt

```lean
theorem action_from_defect :
    "Least action = classical limit of defect minimization" =
    "Least action = classical limit of defect minimization" := rfl
```
