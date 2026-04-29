---
{
  "projection_kind": "taulib_declaration",
  "title": "T2QNMEigenvalues",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnmeigenvalues/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::T2QNMEigenvalues",
  "declaration_slug": "t2-qnmeigenvalues",
  "kind": "structure",
  "name": "T2QNMEigenvalues",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 276,
  "source_line_end": 288,
  "registry_ids": [
    "V.D242"
  ],
  "related_registry_items": [
    {
      "id": "V.D242",
      "title": "T² QNM Eigenvalue Structure: ω_{n,m} = √(n²+m²ι_τ⁻²)/(2πr_s)",
      "url": "/registry/object/V.D242/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L276-L288",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L276-L288",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L276-L288)
- Source range: L276-L288
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D242` — T² QNM Eigenvalue Structure: ω_{n,m} = √(n²+m²ι_τ⁻²)/(2πr_s)

## Immediate Comment / Docstring

```lean
/-- [V.D242] Structure capturing the T² QNM eigenvalue structure.
    3 primitive modes from 2 S¹ cycles (outer winding n, inner winding m).
    Spectrum is anisotropic because r ≠ R (aspect ratio = ι_τ). -/
```

## Source Excerpt

```lean
structure T2QNMEigenvalues where
  /-- Number of primitive torus modes with lowest non-zero frequency. -/
  n_primitive_modes : Nat := 3
  /-- Outer S¹ winding quantum number for fundamental mode. -/
  outer_winding : Nat := 1
  /-- Inner S¹ winding quantum number for fundamental mode. -/
  inner_winding : Nat := 1
  /-- Number of independent frequencies from the 2 S¹ cycles (anisotropic: r ≠ R). -/
  n_independent_frequencies : Nat := 2
  deriving Repr

/-- Canonical T² QNM eigenvalue data. -/
instance : Inhabited T2QNMEigenvalues := ⟨{}⟩
```
