---
{
  "projection_kind": "taulib_declaration",
  "title": "BHEvolutionMode",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/bhevolution-mode/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::BHEvolutionMode",
  "declaration_slug": "bhevolution-mode",
  "kind": "inductive",
  "name": "BHEvolutionMode",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 166,
  "source_line_end": 177,
  "registry_ids": [
    "V.D09"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L166-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L166-L177",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L166-L177)
- Source range: L166-L177
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D09] The three admissible BH evolution modes.

    All three are monotone in the mass index M_n(x):
    1. Ringdown preserves M
    2. Transport preserves M
    3. Fusion strictly increases M

    No other τ-admissible evolution exists for mature BH states. -/
```

## Source Excerpt

```lean
inductive BHEvolutionMode where
  /-- Internal ringdown normalization.
      Mass preserved; internal degrees of freedom settle. -/
  | Ringdown
  /-- Boundary-induced holomorphic transport.
      Mass preserved; BH moves or deforms within carrier bounds. -/
  | Transport
  /-- Merger/fusion of two BH states.
      Mass strictly increases: M(result) > max(M₁, M₂).
      Gen_ω(g₁, g₂) := Norm_ω(Fuse_ω(g₁, g₂)). -/
  | Fusion
  deriving Repr, DecidableEq, BEq, Inhabited
```
