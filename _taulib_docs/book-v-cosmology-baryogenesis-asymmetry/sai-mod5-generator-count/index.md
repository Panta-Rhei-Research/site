---
{
  "projection_kind": "taulib_declaration",
  "title": "sai_mod5_generator_count",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/sai-mod5-generator-count/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::sai_mod5_generator_count",
  "declaration_slug": "sai-mod5-generator-count",
  "kind": "def",
  "name": "sai_mod5_generator_count",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 206,
  "source_line_end": 206,
  "registry_ids": [
    "V.D245"
  ],
  "related_registry_items": [
    {
      "id": "V.D245",
      "title": "SA-i mod-5 Formal Proof: Geometric Series Mechanism",
      "url": "/registry/object/V.D245/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L206-L206",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L206-L206",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L206-L206)
- Source range: L206-L206
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D245` — SA-i mod-5 Formal Proof: Geometric Series Mechanism

## Immediate Comment / Docstring

```lean
/-- [V.D245] SA-i mod-5 Formal Proof.
    Geometric series S₅ = Σ_{k=0}^{4} ι_τ^{3k} = (1−ι_τ¹⁵)/(1−ι_τ³).
    Each generator contributes ι_τ^{dim(τ³)} = ι_τ³. -/
```

## Source Excerpt

```lean
def sai_mod5_generator_count : Nat := 5
```
