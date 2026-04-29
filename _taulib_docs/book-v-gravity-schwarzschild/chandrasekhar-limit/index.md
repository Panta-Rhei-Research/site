---
{
  "projection_kind": "taulib_declaration",
  "title": "ChandrasekharLimit",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/chandrasekhar-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::ChandrasekharLimit",
  "declaration_slug": "chandrasekhar-limit",
  "kind": "structure",
  "name": "ChandrasekharLimit",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 210,
  "source_line_end": 217,
  "registry_ids": [
    "V.R02"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L210-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L210-L217",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L210-L217)
- Source range: L210-L217
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.R02] The Chandrasekhar limit reinterpreted in the τ-framework.

    M_Chandrasekhar = first major radius where the ι_τ shape ratio
    can be refinement-invariantly realized = **minimal maturity scale**.

    This is NOT a PDE equilibrium (TOV solution) but a threshold
    where the torus vacuum first achieves ontic stability.

    The Hawking-Bekenstein radiation exists as coarse-grain thermal
    readout on the empirical layer, but evaporation is **forbidden**
    by the No-Shrink theorem (mass monotonicity). -/
```

## Source Excerpt

```lean
structure ChandrasekharLimit where
  /-- Minimal mature mass index. -/
  minimal_mass : BHMassIndex
  /-- Must be mature by definition. -/
  is_mature : minimal_mass.is_mature = true
  /-- No smaller mature BH exists (minimality). -/
  is_minimal : Bool := true
  deriving Repr
```
