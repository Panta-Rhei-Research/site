---
{
  "projection_kind": "taulib_declaration",
  "title": "nth_prime_pos",
  "permalink": "/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::nth_prime_pos",
  "declaration_slug": "nth-prime-pos",
  "kind": "theorem",
  "name": "nth_prime_pos",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/corpus/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 134,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L134-L138",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L134-L138",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L134-L138)
- Source range: L134-L138
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- nth_prime k ≥ 1 for k ≥ 1. -/
```

## Source Excerpt

```lean
theorem nth_prime_pos {k : TauIdx} (hk : k ≥ 1) : nth_prime k ≥ 1 := by
  simp only [nth_prime]
  have hk0 : k ≠ 0 := by simp only [TauIdx] at *; omega
  rw [if_neg hk0]
  exact nth_prime_go_ge k 0 1 (k * k * 10 + 10)
```
