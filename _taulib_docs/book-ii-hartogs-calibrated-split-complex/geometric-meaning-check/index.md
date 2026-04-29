---
{
  "projection_kind": "taulib_declaration",
  "title": "geometric_meaning_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/geometric-meaning-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::geometric_meaning_check",
  "declaration_slug": "geometric-meaning-check",
  "kind": "def",
  "name": "geometric_meaning_check",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 166,
  "source_line_end": 187,
  "registry_ids": [
    "II.R10"
  ],
  "related_registry_items": [
    {
      "id": "II.R10",
      "title": "Geometric Meaning of Bipolar Idempotents",
      "url": "/registry/object/II.R10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L166-L187",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
        "url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L166-L187",
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

- Module: [TauLib.BookII.Hartogs.CalibratedSplitComplex](/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/)
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L166-L187)
- Source range: L166-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R10` — Geometric Meaning of Bipolar Idempotents

## Immediate Comment / Docstring

```lean
/-- [II.R10] Geometric meaning of the idempotents.

    e₊ projects onto the B-channel:
    - B carries the exponent (γ-orbit) data
    - Calibrated by π (circle winding number)
    - At stage k: B-residues form Z/p_k Z, with p_k arcs of angular width 2π/p_k

    e₋ projects onto the C-channel:
    - C carries the tetration height (η-orbit) data
    - Calibrated by e (factorial eigenvalue / growth base)
    - Growth rate of the tower: exponential with base related to e

    Evidence: for τ-admissible points, e₊-projection extracts B only,
    e₋-projection extracts C only. -/
```

## Source Excerpt

```lean
def geometric_meaning_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      -- e₊ · (B, C) = (B, 0): keeps B-channel, kills C-channel
      let proj_plus := SectorPair.mul e_plus_sector bp
      -- e₋ · (B, C) = (0, C): kills B-channel, keeps C-channel
      let proj_minus := SectorPair.mul e_minus_sector bp
      -- Verify projection structure
      (proj_plus.c_sector == 0) &&
      (proj_minus.b_sector == 0) &&
      (proj_plus.b_sector == bp.b_sector) &&
      (proj_minus.c_sector == bp.c_sector) &&
      -- Sum recovers full bipolar pair
      (SectorPair.add proj_plus proj_minus == bp) &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```
