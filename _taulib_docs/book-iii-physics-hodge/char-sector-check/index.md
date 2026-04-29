---
{
  "projection_kind": "taulib_declaration",
  "title": "char_sector_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/char-sector-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::char_sector_check",
  "declaration_slug": "char-sector-check",
  "kind": "def",
  "name": "char_sector_check",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 138,
  "source_line_end": 156,
  "registry_ids": [
    "III.P18"
  ],
  "related_registry_items": [
    {
      "id": "III.P18",
      "title": "Hodge Requires E₁",
      "url": "/registry/object/III.P18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L138-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L138-L156",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L138-L156)
- Source range: L138-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P18` — Hodge Requires E₁

## Immediate Comment / Docstring

```lean
/-- [III.P18] Character-sector correspondence: each non-zero element at
    level k has at least one non-zero component (lives in some sector). -/
```

## Source Excerpt

```lean
def char_sector_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go (k + 1) (fuel - 1)
      else
        check_nonzero 1 pk k && go (k + 1) (fuel - 1)
  termination_by fuel
  check_nonzero (x pk k : Nat) : Bool :=
    if x >= pk then true
    else
      let nf := boundary_normal_form x k
      -- Non-zero element has at least one non-zero component
      let has_sector := nf.b_part > 0 || nf.c_part > 0 || nf.x_part > 0
      has_sector && check_nonzero (x + 1) pk k
```
