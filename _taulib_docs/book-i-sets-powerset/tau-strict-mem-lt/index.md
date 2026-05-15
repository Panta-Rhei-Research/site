---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem_lt",
  "permalink": "/corpus/taulib/docs/book-i-sets-powerset/tau-strict-mem-lt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem_lt",
  "declaration_slug": "tau-strict-mem-lt",
  "kind": "theorem",
  "name": "tau_strict_mem_lt",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/corpus/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 58,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L58-L61",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Powerset",
        "url": "/corpus/taulib/docs/book-i-sets-powerset/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L58-L61",
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

- Module: [TauLib.BookI.Sets.Powerset](/corpus/taulib/docs/book-i-sets-powerset/)
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L58-L61)
- Source range: L58-L61
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Strict membership with nonzero target implies strict inequality.
    If a | b, a ≠ b, and b ≠ 0, then a < b. -/
```

## Source Excerpt

```lean
theorem tau_strict_mem_lt {a b : TauIdx} (h : tau_strict_mem a b) (hb : b ≠ 0) :
    a < b := by
  have hle : a ≤ b := tau_mem_le h.1 hb
  exact Nat.lt_of_le_of_ne hle h.2
```
