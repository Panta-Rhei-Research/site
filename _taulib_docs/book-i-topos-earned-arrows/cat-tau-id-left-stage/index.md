---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_tau_id_left_stage",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-left-stage/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::cat_tau_id_left_stage",
  "declaration_slug": "cat-tau-id-left-stage",
  "kind": "theorem",
  "name": "cat_tau_id_left_stage",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 90,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L90-L92",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedArrows",
        "url": "/verify/taulib/docs/book-i-topos-earned-arrows/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L90-L92",
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

- Module: [TauLib.BookI.Topos.EarnedArrows](/verify/taulib/docs/book-i-topos-earned-arrows/)
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L90-L92)
- Source range: L90-L92
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T22a] Left identity: id ∘ f gives the same stagewise output as
    applying id to the output of f. -/
```

## Source Excerpt

```lean
theorem cat_tau_id_left_stage (f : StageFun) (n k : TauIdx) :
    (StageFun.comp id_stage f).b_fun n k = reduce (f.b_fun n k) k := by
  simp [StageFun.comp, id_stage]
```
