---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_growth_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/gap-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::gap_growth_check",
  "declaration_slug": "gap-growth-check",
  "kind": "def",
  "name": "gap_growth_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 76,
  "source_line_end": 86,
  "registry_ids": [
    "III.T26"
  ],
  "related_registry_items": [
    {
      "id": "III.T26",
      "title": "τ-Gap Meta-Theorem",
      "url": "/registry/object/III.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L76-L86",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L76-L86",
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
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L76-L86)
- Source range: L76-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T26` — τ-Gap Meta-Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T26] Gap growth check: the gap is non-decreasing across levels
    (B and C products can only grow as more primes are included). -/
```

## Source Excerpt

```lean
def gap_growth_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let gap_k := tau_gap_at_level k
      let gap_k1 := tau_gap_at_level (k + 1)
      gap_k1 >= gap_k && go (k + 1) (fuel - 1)
  termination_by fuel
```
