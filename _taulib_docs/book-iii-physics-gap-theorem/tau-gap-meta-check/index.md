---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_gap_meta_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/tau-gap-meta-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::tau_gap_meta_check",
  "declaration_slug": "tau-gap-meta-check",
  "kind": "def",
  "name": "tau_gap_meta_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 60,
  "source_line_end": 72,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L60-L72",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L60-L72",
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
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L60-L72)
- Source range: L60-L72
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T26` — τ-Gap Meta-Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T26] τ-gap meta-theorem check: at every level k ≥ 3 where
    the strong sector condition holds, the gap is positive. -/
```

## Source Excerpt

```lean
def tau_gap_meta_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- If the sector is strong, the gap must be positive
      let strong := strong_sector_at_level k
      let gap_pos := tau_gap_at_level k > 0
      let ok := if strong then gap_pos else true
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
