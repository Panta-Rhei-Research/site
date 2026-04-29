---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_to_inverse_limit",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::nat_to_inverse_limit",
  "declaration_slug": "nat-to-inverse-limit",
  "kind": "def",
  "name": "nat_to_inverse_limit",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 99,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L99-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L99-L108",
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L99-L108)
- Source range: L99-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical embedding `n ↦ (n mod M_k)_{k ≥ 1}` of a natural
    number into the inverse-limit ω-tower. -/
```

## Source Excerpt

```lean
def nat_to_inverse_limit (n : TauIdx) : OmegaInverseLimit where
  coeff := fun k => reduce n k
  compat := by
    intro k l hk hkl
    -- coeff l = reduce n l = n % primorial l
    -- coeff k = reduce n k = n % primorial k
    -- Goal: (n % primorial l) % primorial k = n % primorial k
    show (reduce n l) % primorial k = reduce n k
    unfold reduce
    exact reduction_compat n hkl
```
