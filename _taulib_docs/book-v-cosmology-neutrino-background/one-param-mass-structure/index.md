---
{
  "projection_kind": "taulib_declaration",
  "title": "OneParamMassStructure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/one-param-mass-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::OneParamMassStructure",
  "declaration_slug": "one-param-mass-structure",
  "kind": "structure",
  "name": "OneParamMassStructure",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 125,
  "source_line_end": 135,
  "registry_ids": [
    "V.P187"
  ],
  "related_registry_items": [
    {
      "id": "V.P187",
      "title": "One-Parameter Neutrino Mass Structure",
      "url": "/registry/object/V.P187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L125-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L125-L135",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L125-L135)
- Source range: L125-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P187` — One-Parameter Neutrino Mass Structure

## Immediate Comment / Docstring

```lean
/-- [V.P187] One-parameter neutrino mass structure.
    NNLO exponents: q = q₀, p = q₀ − 203/175, r = q₀ − 1421/700.
    Single free parameter q₀ determines all three masses. -/
```

## Source Excerpt

```lean
structure OneParamMassStructure where
  /-- Spacing Δpq = 203/175 (rational). -/
  delta_pq_num : Nat := 203
  delta_pq_den : Nat := 175
  /-- Spacing Δpr = 609/700 (rational). -/
  delta_pr_num : Nat := 609
  delta_pr_den : Nat := 700
  /-- Total spacing Δqr = 1421/700. -/
  delta_qr_num : Nat := 1421
  delta_qr_den : Nat := 700
  deriving Repr
```
