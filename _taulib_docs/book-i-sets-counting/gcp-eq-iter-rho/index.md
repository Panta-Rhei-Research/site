---
{
  "projection_kind": "taulib_declaration",
  "title": "gcp_eq_iter_rho",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/gcp-eq-iter-rho/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::gcp_eq_iter_rho",
  "declaration_slug": "gcp-eq-iter-rho",
  "kind": "theorem",
  "name": "gcp_eq_iter_rho",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 71,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L71-L73",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Counting",
        "url": "/verify/taulib/docs/book-i-sets-counting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L71-L73",
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

- Module: [TauLib.BookI.Sets.Counting](/verify/taulib/docs/book-i-sets-counting/)
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L71-L73)
- Source range: L71-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The generative counting map agrees with iter_rho from the generator. -/
```

## Source Excerpt

```lean
theorem gcp_eq_iter_rho (g : Generator) (hg : g ≠ omega) (n : Nat) :
    (generative_counting_principle g hg).phi n = iter_rho n (TauObj.ofGen g) := by
  simp [generative_counting_principle, TauObj.ofGen, iter_rho_depth g hg 0 n]
```
