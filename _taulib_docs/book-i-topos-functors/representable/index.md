---
{
  "projection_kind": "taulib_declaration",
  "title": "Presheaf.representable",
  "permalink": "/verify/taulib/docs/book-i-topos-functors/representable/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.Functors`.",
  "declaration_id": "TauLib.BookI.Topos.Functors::Presheaf.representable",
  "declaration_slug": "representable",
  "kind": "def",
  "name": "Presheaf.representable",
  "module_name": "TauLib.BookI.Topos.Functors",
  "module_url": "/verify/taulib/docs/book-i-topos-functors/",
  "source_line_start": 161,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L161-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.Functors",
        "url": "/verify/taulib/docs/book-i-topos-functors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L161-L162",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Topos.Functors](/verify/taulib/docs/book-i-topos-functors/)
- Source path: [`TauLib/BookI/Topos/Functors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/Functors.lean#L161-L162)
- Source range: L161-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A presheaf is representable if it equals y(X) for some X. -/
```

## Source Excerpt

```lean
def Presheaf.representable (P : Presheaf) : Prop :=
  ∃ x : TauIdx, P = yoneda x
```
