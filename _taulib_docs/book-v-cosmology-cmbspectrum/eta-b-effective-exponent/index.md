---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_b_effective_exponent",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-cmbspectrum/eta-b-effective-exponent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::eta_b_effective_exponent",
  "declaration_slug": "eta-b-effective-exponent",
  "kind": "theorem",
  "name": "eta_b_effective_exponent",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 861,
  "source_line_end": 865,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L861-L865",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/corpus/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L861-L865",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/corpus/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L861-L865)
- Source range: L861-L865
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The effective η_B exponent 19 = W₅(3). -/
```

## Source Excerpt

```lean
theorem eta_b_effective_exponent :
    eta_b_resolution.effective_exponent = 19 ∧
    eta_b_resolution.prefactor_numer = 121 ∧
    eta_b_resolution.prefactor_denom = 270 :=
  ⟨rfl, rfl, rfl⟩
```
