---
{
  "projection_kind": "taulib_declaration",
  "title": "tauquat_add_assoc",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/tauquat-add-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::tauquat_add_assoc",
  "declaration_slug": "tauquat-add-assoc",
  "kind": "theorem",
  "name": "tauquat_add_assoc",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 255,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L255-L259",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Quaternions",
        "url": "/verify/taulib/docs/book-i-boundary-quaternions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L255-L259",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.Quaternions](/verify/taulib/docs/book-i-boundary-quaternions/)
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L255-L259)
- Source range: L255-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Quaternion addition is associative (up to equiv). -/
```

## Source Excerpt

```lean
theorem tauquat_add_assoc (a b c : TauQuaternion) :
    TauQuaternion.equiv ((TauQuaternion.add a b).add c)
                        (TauQuaternion.add a (TauQuaternion.add b c)) :=
  ⟨taureal_add_assoc a.w b.w c.w, taureal_add_assoc a.x b.x c.x,
   taureal_add_assoc a.y b.y c.y, taureal_add_assoc a.z b.z c.z⟩
```
