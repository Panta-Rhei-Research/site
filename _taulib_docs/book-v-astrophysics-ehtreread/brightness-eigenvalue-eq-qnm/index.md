---
{
  "projection_kind": "taulib_declaration",
  "title": "brightness_eigenvalue_eq_qnm",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/brightness-eigenvalue-eq-qnm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::brightness_eigenvalue_eq_qnm",
  "declaration_slug": "brightness-eigenvalue-eq-qnm",
  "kind": "theorem",
  "name": "brightness_eigenvalue_eq_qnm",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 437,
  "source_line_end": 439,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L437-L439",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L437-L439",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L437-L439)
- Source range: L437-L439
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [Sprint 22A] The brightness harmonic eigenvalue formula (V.D279) is identical to
    the QNM eigenvalue structure (V.D242). Both are eigenvalues of the Laplacian on
    the flat torus T² = (R·S¹)×(r·S¹) with r/R = ι_τ.

    This is the Peter-Weyl theorem for U(1)×U(1): the characters ψ_{nm} = exp(i(nφ+mθ))
    form a complete orthonormal basis for L²(T²), with eigenvalues λ_{nm} = n² + m²ι_τ⁻².

    The link is structural: both V.D279 and V.D242 use the same eigenvalue formula,
    and the fundamental frequency ratio f_{0,1}/f_{1,0} = ι_τ⁻¹ ≈ 2.930 is identical
    to V.T185 (τ-effective QNM frequency ratio discriminator). -/
```

## Source Excerpt

```lean
theorem brightness_eigenvalue_eq_qnm :
    harmonic_frequency_ratio_x1000 = birotational_synchrotron_ratio_x1000 := by
  rfl
```
