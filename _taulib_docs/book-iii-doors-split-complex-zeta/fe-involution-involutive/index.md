---
{
  "projection_kind": "taulib_declaration",
  "title": "fe_involution_involutive",
  "permalink": "/corpus/taulib/docs/book-iii-doors-split-complex-zeta/fe-involution-involutive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::fe_involution_involutive",
  "declaration_slug": "fe-involution-involutive",
  "kind": "theorem",
  "name": "fe_involution_involutive",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/corpus/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 188,
  "source_line_end": 190,
  "registry_ids": [
    "III.D27"
  ],
  "related_registry_items": [
    {
      "id": "III.D27",
      "title": "Functional Equation Involution J",
      "url": "/registry/object/III.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L188-L190",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/corpus/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L188-L190",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/corpus/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L188-L190)
- Source range: L188-L190
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D27` — Functional Equation Involution J

## Immediate Comment / Docstring

```lean
/-- [III.D27] Structural: involution is own inverse. -/
```

## Source Excerpt

```lean
theorem fe_involution_involutive (nf : BoundaryNF) :
    fe_involution (fe_involution nf) = nf := by
  cases nf; rfl
```
