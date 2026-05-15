---
{
  "projection_kind": "taulib_declaration",
  "title": "RT_surjective",
  "permalink": "/corpus/taulib/docs/book-i-denotation-rank-transfer/rt-surjective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.RankTransfer`.",
  "declaration_id": "TauLib.BookI.Denotation.RankTransfer::RT_surjective",
  "declaration_slug": "rt-surjective",
  "kind": "theorem",
  "name": "RT_surjective",
  "module_name": "TauLib.BookI.Denotation.RankTransfer",
  "module_url": "/corpus/taulib/docs/book-i-denotation-rank-transfer/",
  "source_line_start": 43,
  "source_line_end": 46,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L43-L46",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.RankTransfer",
        "url": "/corpus/taulib/docs/book-i-denotation-rank-transfer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L43-L46",
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

- Module: [TauLib.BookI.Denotation.RankTransfer](/corpus/taulib/docs/book-i-denotation-rank-transfer/)
- Source path: [`TauLib/BookI/Denotation/RankTransfer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/RankTransfer.lean#L43-L46)
- Source range: L43-L46
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- RT hits every orbit ray element. -/
```

## Source Excerpt

```lean
theorem RT_surjective (g : Generator) (_hg : g ≠ omega) (x : TauObj)
    (hx : OrbitRay g x) : ∃ n, RT g n = x := by
  obtain ⟨hseed, _⟩ := hx
  exact ⟨x.depth, by cases x; simp [RT] at hseed ⊢; exact hseed.symm⟩
```
