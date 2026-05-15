---
{
  "projection_kind": "taulib_declaration",
  "title": "birotation_ratio_eq_qnm_ratio",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/birotation-ratio-eq-qnm-ratio/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::birotation_ratio_eq_qnm_ratio",
  "declaration_slug": "birotation-ratio-eq-qnm-ratio",
  "kind": "theorem",
  "name": "birotation_ratio_eq_qnm_ratio",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 456,
  "source_line_end": 457,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L456-L457",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/corpus/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L456-L457",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/corpus/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L456-L457)
- Source range: L456-L457
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [Sprint 22B] The bi-rotational frequency ratio (V.D277/V.T218) is identical to
    the QNM frequency ratio (V.T185, τ-effective). Both equal ι_τ⁻¹ × 1000 = 2930.
    This structural identity confirms that bi-rotational synchrotron modes are
    boundary-character oscillations read through the B-sector (EM), not accretion dynamics. -/
```

## Source Excerpt

```lean
theorem birotation_ratio_eq_qnm_ratio :
    birotational_synchrotron_ratio_x1000 = harmonic_frequency_ratio_x1000 := by rfl
```
