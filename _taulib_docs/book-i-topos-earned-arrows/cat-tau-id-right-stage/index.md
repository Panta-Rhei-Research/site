---
{
  "projection_kind": "taulib_declaration",
  "title": "cat_tau_id_right_stage",
  "permalink": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau-id-right-stage/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::cat_tau_id_right_stage",
  "declaration_slug": "cat-tau-id-right-stage",
  "kind": "theorem",
  "name": "cat_tau_id_right_stage",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/corpus/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 95,
  "source_line_end": 97,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L95-L97",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedArrows",
        "url": "/corpus/taulib/docs/book-i-topos-earned-arrows/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L95-L97",
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

- Module: [TauLib.BookI.Topos.EarnedArrows](/corpus/taulib/docs/book-i-topos-earned-arrows/)
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L95-L97)
- Source range: L95-L97
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T22b] Right identity: f ∘ id gives the same stagewise output. -/
```

## Source Excerpt

```lean
theorem cat_tau_id_right_stage (f : StageFun) (n k : TauIdx) :
    (StageFun.comp f id_stage).b_fun n k = f.b_fun (reduce n k) k := by
  simp [StageFun.comp, id_stage]
```
