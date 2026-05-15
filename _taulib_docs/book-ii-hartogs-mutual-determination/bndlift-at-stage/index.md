---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_at_stage",
  "permalink": "/corpus/taulib/docs/book-ii-hartogs-mutual-determination/bndlift-at-stage/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::bndlift_at_stage",
  "declaration_slug": "bndlift-at-stage",
  "kind": "theorem",
  "name": "bndlift_at_stage",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/corpus/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 291,
  "source_line_end": 293,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L291-L293",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/corpus/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L291-L293",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/corpus/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L291-L293)
- Source range: L291-L293
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- BndLift at the same stage: reduce(bndlift(x, k), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem bndlift_at_stage (x k : TauIdx) :
    reduce (bndlift x k) k = reduce x k := by
  exact bndlift_coherent x (Nat.le_refl k)
```
