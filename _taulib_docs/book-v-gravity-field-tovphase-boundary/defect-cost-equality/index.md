---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_cost_equality",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/defect-cost-equality/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::defect_cost_equality",
  "declaration_slug": "defect-cost-equality",
  "kind": "theorem",
  "name": "defect_cost_equality",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 219,
  "source_line_end": 221,
  "registry_ids": [
    "V.T48"
  ],
  "related_registry_items": [
    {
      "id": "V.T48",
      "title": "Defect Cost Jump at Phase Boundary",
      "url": "/registry/object/V.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L219-L221",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L219-L221",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L219-L221)
- Source range: L219-L221
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.T48` — Defect Cost Jump at Phase Boundary

## Immediate Comment / Docstring

```lean
/-- [V.T48] Defect cost equality at the phase boundary:
    at M = M_n*, both topology branches have equal tension.

    Structural recording of the phase transition condition. -/
```

## Source Excerpt

```lean
theorem defect_cost_equality :
    "T_S2(M_n*) = T_T2(M_n*)" =
    "T_S2(M_n*) = T_T2(M_n*)" := rfl
```
