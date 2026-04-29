---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_mul_cancel",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/nat-mul-cancel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::nat_mul_cancel",
  "declaration_slug": "nat-mul-cancel",
  "kind": "theorem",
  "name": "nat_mul_cancel",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 146,
  "source_line_end": 155,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L146-L155",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Operations",
        "url": "/verify/taulib/docs/book-i-sets-operations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L146-L155",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L146-L155)
- Source range: L146-L155
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Nat multiplication left cancellation: a > 0 and a * b = a * c implies b = c. -/
```

## Source Excerpt

```lean
private theorem nat_mul_cancel {a b c : Nat} (ha : a > 0) (h : a * b = a * c) : b = c := by
  rcases Nat.lt_or_ge b c with hbc | hbc
  · have h1 := Nat.mul_le_mul_left a hbc
    have h2 : a * Nat.succ b = a * b + a := Nat.mul_succ a b
    omega
  · rcases Nat.lt_or_ge c b with hcb | hcb
    · have h1 := Nat.mul_le_mul_left a hcb
      have h2 : a * Nat.succ c = a * c + a := Nat.mul_succ a c
      omega
    · omega
```
