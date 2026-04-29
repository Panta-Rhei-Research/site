---
{
  "projection_kind": "taulib_declaration",
  "title": "TauQuaternion.mul",
  "permalink": "/verify/taulib/docs/book-i-boundary-quaternions/mul/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Quaternions`.",
  "declaration_id": "TauLib.BookI.Boundary.Quaternions::TauQuaternion.mul",
  "declaration_slug": "mul",
  "kind": "def",
  "name": "TauQuaternion.mul",
  "module_name": "TauLib.BookI.Boundary.Quaternions",
  "module_url": "/verify/taulib/docs/book-i-boundary-quaternions/",
  "source_line_start": 113,
  "source_line_end": 117,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L113-L117",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L113-L117",
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

- Module: [TauLib.BookI.Boundary.Quaternions](/verify/taulib/docs/book-i-boundary-quaternions/)
- Source path: [`TauLib/BookI/Boundary/Quaternions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Quaternions.lean#L113-L117)
- Source range: L113-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Hamilton product:
    (a1 + b1i + c1j + d1k)(a2 + b2i + c2j + d2k) =
      (a1a2 - b1b2 - c1c2 - d1d2)
    + (a1b2 + b1a2 + c1d2 - d1c2)i
    + (a1c2 - b1d2 + c1a2 + d1b2)j
    + (a1d2 + b1c2 - c1b2 + d1a2)k -/
```

## Source Excerpt

```lean
def TauQuaternion.mul (a b : TauQuaternion) : TauQuaternion :=
  ⟨((a.w.mul b.w).sub (a.x.mul b.x)).sub ((a.y.mul b.y).add (a.z.mul b.z)),
   ((a.w.mul b.x).add (a.x.mul b.w)).add ((a.y.mul b.z).sub (a.z.mul b.y)),
   ((a.w.mul b.y).sub (a.x.mul b.z)).add ((a.y.mul b.w).add (a.z.mul b.x)),
   ((a.w.mul b.z).add (a.x.mul b.y)).sub ((a.y.mul b.x).sub (a.z.mul b.w))⟩
```
