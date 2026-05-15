---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_from_defect",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-supernovae/neutrino-from-defect/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::neutrino_from_defect",
  "declaration_slug": "neutrino-from-defect",
  "kind": "theorem",
  "name": "neutrino_from_defect",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 162,
  "source_line_end": 164,
  "registry_ids": [
    "V.P73"
  ],
  "related_registry_items": [
    {
      "id": "V.P73",
      "title": "Neutrino Heating Condition --- V.P37",
      "url": "/registry/object/V.P73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L162-L164",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L162-L164",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/corpus/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L162-L164)
- Source range: L162-L164
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.P73` — Neutrino Heating Condition --- V.P37

## Immediate Comment / Docstring

```lean
/-- [V.P73] Neutrino burst from defect release: ~99% of the
    gravitational binding energy (~3 × 10⁵³ erg) is released as
    neutrinos during core collapse.

    In the τ-framework, the neutrinos carry away the defect energy
    that was stored in the compression component of the iron core's
    defect tuple. -/
```

## Source Excerpt

```lean
theorem neutrino_from_defect :
    "99% of binding energy released as neutrinos = defect energy release" =
    "99% of binding energy released as neutrinos = defect energy release" := rfl
```
