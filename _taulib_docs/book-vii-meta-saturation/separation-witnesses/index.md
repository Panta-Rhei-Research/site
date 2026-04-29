---
{
  "projection_kind": "taulib_declaration",
  "title": "separation_witnesses",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/separation-witnesses/",
  "summary_short": "`def` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::separation_witnesses",
  "declaration_slug": "separation-witnesses",
  "kind": "def",
  "name": "separation_witnesses",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 87,
  "source_line_end": 90,
  "registry_ids": [
    "VII.L04"
  ],
  "related_registry_items": [
    {
      "id": "VII.L04",
      "title": "Strictness Between Layers",
      "url": "/registry/object/VII.L04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L87-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L87-L90",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L87-L90)
- Source range: L87-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `VII.L04` — Strictness Between Layers

## Immediate Comment / Docstring

```lean
/-- [VII.L04] Strictness: E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃.
    Separation witnesses:
    - E₀→E₁: sector admissibility (coupling constants under RG flow)
    - E₁→E₂: internal code evaluation (decode map in phenotype)
    - E₂→E₃: self-model consistency (MetaDecode operator) -/
```

## Source Excerpt

```lean
def separation_witnesses : List SeparationWitness :=
  [ ⟨.e0, .e1, "sector_admissibility", true⟩
  , ⟨.e1, .e2, "internal_code_evaluation", true⟩
  , ⟨.e2, .e3, "self_model_consistency", true⟩ ]
```
