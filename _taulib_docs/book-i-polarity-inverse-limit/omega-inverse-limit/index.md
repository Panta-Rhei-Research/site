---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaInverseLimit",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/omega-inverse-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::OmegaInverseLimit",
  "declaration_slug": "omega-inverse-limit",
  "kind": "structure",
  "name": "OmegaInverseLimit",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 85,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L85-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.InverseLimit",
        "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L85-L91",
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L85-L91)
- Source range: L85-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Inverse-limit ω-tower**: an infinite coherent tower of
    residues, one per depth `k ≥ 1`, with the reduction map
    `(mod M_l) ↦ (mod M_k)` respected for every `k ≤ l`.

    This is the τ-native infinite-depth boundary object that
    Hinges 5–6 use as the target of pre-Yoneda collapse and
    ω-germ stabilisation. -/
```

## Source Excerpt

```lean
structure OmegaInverseLimit where
  /-- The k-th component: a residue mod the k-th primorial. -/
  coeff : TauIdx → TauIdx
  /-- Compatibility: the (l)-th component reduces to the (k)-th
      under (mod primorial k), for every `1 ≤ k ≤ l`. -/
  compat : ∀ k l : TauIdx, 1 ≤ k → k ≤ l →
    coeff l % primorial k = coeff k
```
