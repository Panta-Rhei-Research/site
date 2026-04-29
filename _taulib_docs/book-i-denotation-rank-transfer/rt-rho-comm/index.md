---
{
  "projection_kind": "taulib_declaration",
  "title": "RT_rho_comm",
  "permalink": "/verify/taulib/docs/book-i-denotation-rank-transfer/rt-rho-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.RankTransfer`.",
  "declaration_id": "TauLib.BookI.Denotation.RankTransfer::RT_rho_comm",
  "declaration_slug": "rt-rho-comm",
  "kind": "theorem",
  "name": "RT_rho_comm",
  "module_name": "TauLib.BookI.Denotation.RankTransfer",
  "module_url": "/verify/taulib/docs/book-i-denotation-rank-transfer/",
  "source_line_start": 61,
  "source_line_end": 64,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L61-L64",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.RankTransfer",
        "url": "/verify/taulib/docs/book-i-denotation-rank-transfer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L61-L64",
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

- Module: [TauLib.BookI.Denotation.RankTransfer](/verify/taulib/docs/book-i-denotation-rank-transfer/)
- Source path: [`TauLib/BookI/Denotation/RankTransfer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L61-L64)
- Source range: L61-L64
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- RT commutes with ρ: RT_g(n+1) = ρ(RT_g(n)) for g ≠ ω. -/
```

## Source Excerpt

```lean
theorem RT_rho_comm (g : Generator) (hg : g ≠ omega) (n : TauIdx) :
    RT g (n + 1) = rho (RT g n) := by
  simp [RT]
  exact (K4_no_jump g hg n).symm
```
