---
{
  "projection_kind": "taulib_declaration",
  "title": "WindowRGPeriod",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/window-rgperiod/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::WindowRGPeriod",
  "declaration_slug": "window-rgperiod",
  "kind": "structure",
  "name": "WindowRGPeriod",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 604,
  "source_line_end": 613,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L604-L613",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L604-L613",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L604-L613)
- Source range: L604-L613
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.P191 upgrade] W₃(4)^k governs k-th perturbative order.

    The holonomy spectral renormalization group has fundamental
    period W₃(4) = 5 at each perturbative order:
    - NLO: one lemniscate traversal → W₃(4)
    - NNLO: double traversal → W₃(4)²
    - k-th order: k traversals → W₃(4)^k

    W₃(4) = a₃ + a₄ = 3 + 1 + 1 = 5 (CF partial quotients
    in the [3,4] window). This is the "CF-RG correspondence". -/
```

## Source Excerpt

```lean
structure WindowRGPeriod where
  /-- Window modulus W₃(4). -/
  w34 : Nat := 5
  /-- NLO exponent. -/
  nlo_power : Nat := 1
  /-- NNLO power = W₃(4)². -/
  nnlo_value : Nat := 25
  /-- Period structure: NNLO = W₃(4)². -/
  nnlo_is_square : nnlo_value = w34 * w34
  deriving Repr
```
