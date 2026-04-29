---
{
  "projection_kind": "taulib_declaration",
  "title": "fe_involution_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/fe-involution-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::fe_involution_check",
  "declaration_slug": "fe-involution-check",
  "kind": "def",
  "name": "fe_involution_check",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 75,
  "source_line_end": 89,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L75-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L75-L89",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/verify/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L75-L89)
- Source range: L75-L89
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D27` — Functional Equation Involution J

## Immediate Comment / Docstring

```lean
/-- [III.D27] Involution check: J² = identity for all BNFs in range. -/
```

## Source Excerpt

```lean
def fe_involution_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let nf := boundary_normal_form x k
      let j2 := fe_involution (fe_involution nf)
      let ok := j2.b_part == nf.b_part &&
                j2.c_part == nf.c_part &&
                j2.x_part == nf.x_part
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
