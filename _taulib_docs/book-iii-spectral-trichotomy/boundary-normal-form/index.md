---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_normal_form",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/boundary-normal-form/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::boundary_normal_form",
  "declaration_slug": "boundary-normal-form",
  "kind": "def",
  "name": "boundary_normal_form",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 132,
  "source_line_end": 138,
  "registry_ids": [
    "III.D24"
  ],
  "related_registry_items": [
    {
      "id": "III.D24",
      "title": "Boundary Normal Form",
      "url": "/registry/object/III.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L132-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L132-L138",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L132-L138)
- Source range: L132-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D24` — Boundary Normal Form

## Immediate Comment / Docstring

```lean
/-- [III.D24] Compute boundary normal form from a value at depth k. -/
```

## Source Excerpt

```lean
def boundary_normal_form (x k : TauIdx) : BoundaryNF :=
  let residues := crt_decompose (reduce x k) k
  let (b_res, c_res, x_res) := trichotomy_decompose residues k
  let b_val := crt_reconstruct b_res k
  let c_val := crt_reconstruct c_res k
  let x_val := crt_reconstruct x_res k
  ⟨b_val, c_val, x_val, k⟩
```
