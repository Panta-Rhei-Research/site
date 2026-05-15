---
{
  "projection_kind": "taulib_declaration",
  "title": "t2_qnm_eigenvalue_structure",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-qnm-eigenvalue-structure/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::t2_qnm_eigenvalue_structure",
  "declaration_slug": "t2-qnm-eigenvalue-structure",
  "kind": "def",
  "name": "t2_qnm_eigenvalue_structure",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 273,
  "source_line_end": 275,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L273-L275",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L273-L275",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L273-L275)
- Source range: L273-L275
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `V.D242` — T² QNM Eigenvalue Structure: ω_{n,m} = √(n²+m²ι_τ⁻²)/(2πr_s)

## Immediate Comment / Docstring

```lean
/-- [V.D242] T² QNM Eigenvalue Structure.
    ω_{n,m} = √(n²+m²·ι_τ⁻²)/(2π·r_s). First 3 overtones:
    (1,0): 1.000, (0,1): ι_τ⁻¹=2.930, (1,1): √(1+ι_τ⁻²)=3.096. -/
```

## Source Excerpt

```lean
def t2_qnm_eigenvalue_structure : String :=
  "T² QNM: ω_{n,m} = √(n²+m²·ι_τ⁻²)/(2πr_s). " ++
  "Overtones: (1,0)→1.000, (0,1)→2.930, (1,1)→3.096."
```
