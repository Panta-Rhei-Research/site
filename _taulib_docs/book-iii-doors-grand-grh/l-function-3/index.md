---
{
  "projection_kind": "taulib_declaration",
  "title": "l_function_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/l-function-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::l_function_3",
  "declaration_slug": "l-function-3",
  "kind": "theorem",
  "name": "l_function_3",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 245,
  "source_line_end": 247,
  "registry_ids": [
    "III.D32"
  ],
  "related_registry_items": [
    {
      "id": "III.D32",
      "title": "L-Function as Spectral Determinant",
      "url": "/registry/object/III.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L245-L247",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L245-L247",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L245-L247)
- Source range: L245-L247
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D32` — L-Function as Spectral Determinant

## Immediate Comment / Docstring

```lean
/-- [III.D32] Structural: L-function at depth 3 = Prim(3). -/
```

## Source Excerpt

```lean
theorem l_function_3 :
    split_zeta_b 3 * split_zeta_c 3 * split_zeta_x 3 = primorial 3 := by
  native_decide
```
