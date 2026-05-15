---
{
  "projection_kind": "taulib_declaration",
  "title": "fe_involution",
  "permalink": "/corpus/taulib/docs/book-iii-doors-split-complex-zeta/fe-involution/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::fe_involution",
  "declaration_slug": "fe-involution",
  "kind": "def",
  "name": "fe_involution",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/corpus/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 71,
  "source_line_end": 72,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L71-L72",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L71-L72",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/corpus/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L71-L72)
- Source range: L71-L72
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `III.D27` — Functional Equation Involution J

## Immediate Comment / Docstring

```lean
/-- [III.D27] Functional equation involution: exchanges B-lobe and C-lobe
    components of a boundary normal form. J(b, c, x) = (c, b, x). -/
```

## Source Excerpt

```lean
def fe_involution (nf : BoundaryNF) : BoundaryNF :=
  ⟨nf.c_part, nf.b_part, nf.x_part, nf.depth⟩
```
