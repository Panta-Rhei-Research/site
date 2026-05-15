---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_constant_check",
  "permalink": "/corpus/taulib/docs/book-iii-physics-gap-theorem/gap-constant-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::gap_constant_check",
  "declaration_slug": "gap-constant-check",
  "kind": "def",
  "name": "gap_constant_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/corpus/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 98,
  "source_line_end": 110,
  "registry_ids": [
    "III.D45"
  ],
  "related_registry_items": [
    {
      "id": "III.D45",
      "title": "Gap Constant Γ*",
      "url": "/registry/object/III.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L98-L110",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/corpus/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L98-L110",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/corpus/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L98-L110)
- Source range: L98-L110
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D45` — Gap Constant Γ*

## Immediate Comment / Docstring

```lean
/-- [III.D45] Gap constant check: the constant is well-defined and
    positive for all strong sector levels. -/
```

## Source Excerpt

```lean
def gap_constant_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let gc := gap_constant k
      let (b_ct, c_ct, _) := label_counts k
      -- Positive when both sectors present
      let ok := if b_ct > 0 && c_ct > 0 then gc > 0 else true
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
