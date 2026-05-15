---
{
  "projection_kind": "taulib_declaration",
  "title": "CatTau",
  "permalink": "/corpus/taulib/docs/book-i-topos-earned-arrows/cat-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::CatTau",
  "declaration_slug": "cat-tau",
  "kind": "structure",
  "name": "CatTau",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/corpus/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 71,
  "source_line_end": 73,
  "registry_ids": [
    "I.D51"
  ],
  "related_registry_items": [
    {
      "id": "I.D51",
      "title": "Cat_tau",
      "url": "/registry/object/I.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L71-L73",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L71-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L71-L73)
- Source range: L71-L73
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.D51` — Cat_tau

## Immediate Comment / Docstring

```lean
/-- [I.D51] The data of Cat_τ: objects, identity arrows, and composition.
    Cat_τ is the earned category — not imported but built from HolFun. -/
```

## Source Excerpt

```lean
structure CatTau where
  -- Identity arrow at each object
  id_ : TauIdx → TauArrow
```
