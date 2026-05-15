---
{
  "projection_kind": "taulib_declaration",
  "title": "reduction_compat_check",
  "permalink": "/corpus/taulib/docs/book-i-polarity-mod-arith/reduction-compat-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::reduction_compat_check",
  "declaration_slug": "reduction-compat-check",
  "kind": "def",
  "name": "reduction_compat_check",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/corpus/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 70,
  "source_line_end": 72,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L70-L72",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ModArith",
        "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L70-L72",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Polarity.ModArith](/corpus/taulib/docs/book-i-polarity-mod-arith/)
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L70-L72)
- Source range: L70-L72
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Reduction compatibility check: x % M_ℓ % M_k = x % M_k when k ≤ ℓ. -/
```

## Source Excerpt

```lean
def reduction_compat_check (x k l : TauIdx) : Bool :=
  if k ≤ l then reduce (reduce x l) k == reduce x k
  else true
```
