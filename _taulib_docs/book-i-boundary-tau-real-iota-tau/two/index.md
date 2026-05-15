---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.two",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/two/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealIotaTau`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealIotaTau::TauReal.two",
  "declaration_slug": "two",
  "kind": "def",
  "name": "TauReal.two",
  "module_name": "TauLib.BookI.Boundary.TauRealIotaTau",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/",
  "source_line_start": 77,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L77-L78",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealIotaTau",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L77-L78",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.TauRealIotaTau](/corpus/taulib/docs/book-i-boundary-tau-real-iota-tau/)
- Source path: [`TauLib/BookI/Boundary/TauRealIotaTau.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L77-L78)
- Source range: L77-L78
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The TauReal constant 2. -/
```

## Source Excerpt

```lean
def TauReal.two : TauReal :=
  TauReal.fromTauRat ⟨⟨2, 0⟩, 1, Nat.one_pos⟩
```
