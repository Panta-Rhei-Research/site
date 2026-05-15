---
{
  "projection_kind": "taulib_declaration",
  "title": "taureal_const_bridge",
  "permalink": "/corpus/taulib/docs/book-i-boundary-quaternions/taureal-const-bridge/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::taureal_const_bridge",
  "declaration_slug": "taureal-const-bridge",
  "kind": "theorem",
  "name": "taureal_const_bridge",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/corpus/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 133,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L133-L135",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Quaternions",
        "url": "/corpus/taulib/docs/book-i-boundary-quaternions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L133-L135",
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

- Module: [TauLib.BookI.Boundary.Quaternions](/corpus/taulib/docs/book-i-boundary-quaternions/)
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L133-L135)
- Source range: L133-L135
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: TauReal component equivalence on constant sequences reduces
    to TauRat equivalence, which reduces to TauInt via the bridge. -/
```

## Source Excerpt

```lean
private theorem taureal_const_bridge (a b : TauRat)
    (h : ∀ n : Nat, TauRat.equiv a b) : TauReal.equiv ⟨fun _ => a⟩ ⟨fun _ => b⟩ :=
  TauReal.equiv_of_pointwise (fun n => h n)
```
