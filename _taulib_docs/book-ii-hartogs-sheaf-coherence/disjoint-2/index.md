---
{
  "projection_kind": "taulib_declaration",
  "title": "disjoint_2",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/disjoint-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::disjoint_2",
  "declaration_slug": "disjoint-2",
  "kind": "theorem",
  "name": "disjoint_2",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 462,
  "source_line_end": 463,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L462-L463",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L462-L463",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/corpus/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L462-L463)
- Source range: L462-L463
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem disjoint_2 :
    batch_disjoint_check 2 = true := by native_decide
```
