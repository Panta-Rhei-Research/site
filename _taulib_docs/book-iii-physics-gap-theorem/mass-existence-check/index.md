---
{
  "projection_kind": "taulib_declaration",
  "title": "mass_existence_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/mass-existence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::mass_existence_check",
  "declaration_slug": "mass-existence-check",
  "kind": "def",
  "name": "mass_existence_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 119,
  "source_line_end": 131,
  "registry_ids": [
    "III.P17"
  ],
  "related_registry_items": [
    {
      "id": "III.P17",
      "title": "Gap Stabilization",
      "url": "/registry/object/III.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L119-L131",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L119-L131",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L119-L131)
- Source range: L119-L131
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P17` — Gap Stabilization

## Immediate Comment / Docstring

```lean
/-- [III.P17] Mass existence: the gap constant is strictly positive
    at all levels ≥ 3 where B and C are non-trivial. This is the
    mass gap existence theorem in τ. -/
```

## Source Excerpt

```lean
def mass_existence_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let gc := gap_constant k
      let (b_ct, c_ct, _) := label_counts k
      -- Mass exists iff gap is positive
      let has_mass := if b_ct > 0 && c_ct > 0 then gc > 0 else true
      has_mass && go (k + 1) (fuel - 1)
  termination_by fuel
```
