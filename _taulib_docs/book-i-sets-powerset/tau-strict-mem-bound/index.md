---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem_bound",
  "permalink": "/corpus/taulib/docs/book-i-sets-powerset/tau-strict-mem-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem_bound",
  "declaration_slug": "tau-strict-mem-bound",
  "kind": "theorem",
  "name": "tau_strict_mem_bound",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/corpus/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 68,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L68-L70",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L68-L70",
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
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L68-L70)
- Source range: L68-L70
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If a is a strict member of b, and b > 0, then a is strictly smaller. -/
```

## Source Excerpt

```lean
theorem tau_strict_mem_bound {a b : TauIdx} (h : tau_strict_mem a b) (hb : b > 0) :
    a < b :=
  tau_strict_mem_lt h (fun heq => by subst heq; exact Nat.lt_irrefl 0 hb)
```
