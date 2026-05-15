---
{
  "projection_kind": "taulib_declaration",
  "title": "BaseTau1.valid",
  "permalink": "/corpus/taulib/docs/book-ii-interior-tau3-fibration/valid/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::BaseTau1.valid",
  "declaration_slug": "valid",
  "kind": "def",
  "name": "BaseTau1.valid",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/corpus/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 50,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L50-L51",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/corpus/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L50-L51",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/corpus/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L50-L51)
- Source range: L50-L51
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Validity check for base point. -/
```

## Source Excerpt

```lean
def BaseTau1.valid (b : BaseTau1) : Bool :=
  constraint_C1 b.a && constraint_C3 b.d b.a
```
