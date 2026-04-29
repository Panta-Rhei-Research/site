---
{
  "projection_kind": "taulib_declaration",
  "title": "to_tau3",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/to-tau3/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::to_tau3",
  "declaration_slug": "to-tau3",
  "kind": "def",
  "name": "to_tau3",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 78,
  "source_line_end": 79,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L78-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L78-L79",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/verify/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L78-L79)
- Source range: L78-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Convert TauAdmissiblePoint to Tau3 (fibered product form). -/
```

## Source Excerpt

```lean
def to_tau3 (p : TauAdmissiblePoint) : Tau3 :=
  ⟨⟨p.d, p.a⟩, ⟨p.b, p.c⟩⟩
```
