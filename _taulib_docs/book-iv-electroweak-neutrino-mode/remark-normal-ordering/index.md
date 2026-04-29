---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_normal_ordering",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/remark-normal-ordering/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::remark_normal_ordering",
  "declaration_slug": "remark-normal-ordering",
  "kind": "def",
  "name": "remark_normal_ordering",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 423,
  "source_line_end": 426,
  "registry_ids": [
    "IV.R395"
  ],
  "related_registry_items": [
    {
      "id": "IV.R395",
      "title": "Normal Ordering from sigma-Structure",
      "url": "/registry/object/IV.R395/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L423-L426",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L423-L426",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L423-L426)
- Source range: L423-L426
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R395` — Normal Ordering from sigma-Structure

## Immediate Comment / Docstring

```lean
/-- [IV.R395] Normal ordering is predicted structurally from σ-equivariance.
    Since ι_τ < 1: larger exponent → smaller value.
    r = 2.8 < p = 3.7  =>  c = ι_τ^2.8 ≈ 0.049 > ι_τ^3.7 ≈ 0.019 = a
    =>  crossing self-coupling c > lobe self-coupling a
    =>  σ-odd eigenvalue λ₂ = a lies between two σ-even eigenvalues
    =>  normal ordering m₁ < m₂ < m₃. -/
```

## Source Excerpt

```lean
def remark_normal_ordering : String :=
  "r < p => c = iota^r > iota^p = a (since iota < 1, larger exp = smaller val). " ++
  "sigma-odd eigenvalue = a is sandwiched: lambda_1 < a < lambda_3. " ++
  "Forces normal ordering m1 < m2 < m3. Inverted ordering requires r > p (disfavored)."
```
