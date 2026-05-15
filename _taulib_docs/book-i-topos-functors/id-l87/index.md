---
{
  "projection_kind": "taulib_declaration",
  "title": "NatTrans.id",
  "permalink": "/corpus/taulib/docs/book-i-topos-functors/id-l87/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::NatTrans.id",
  "declaration_slug": "id-l87",
  "kind": "def",
  "name": "NatTrans.id",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/corpus/taulib/docs/book-i-topos-functors/",
  "source_line_start": 87,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L87-L88",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.Functors",
        "url": "/corpus/taulib/docs/book-i-topos-functors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L87-L88",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Topos.Functors](/corpus/taulib/docs/book-i-topos-functors/)
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L87-L88)
- Source range: L87-L88
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The identity natural transformation. -/
```

## Source Excerpt

```lean
def NatTrans.id (F : TauFunctor) : NatTrans F F :=
  ⟨fun x => F.obj_map x, fun _ => rfl⟩
```
