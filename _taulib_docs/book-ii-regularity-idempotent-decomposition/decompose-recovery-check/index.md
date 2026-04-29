---
{
  "projection_kind": "taulib_declaration",
  "title": "decompose_recovery_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::decompose_recovery_check",
  "declaration_slug": "decompose-recovery-check",
  "kind": "def",
  "name": "decompose_recovery_check",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 126,
  "source_line_end": 146,
  "registry_ids": [
    "II.L07"
  ],
  "related_registry_items": [
    {
      "id": "II.L07",
      "title": "Idempotent Decomposition Lemma",
      "url": "/registry/object/II.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L126-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L126-L146",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L126-L146)
- Source range: L126-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L07` — Idempotent Decomposition Lemma

## Immediate Comment / Docstring

```lean
/-- [II.L07] Computational check: e₊ · bp + e₋ · bp = bp
    for all tau-admissible points in [2, bound]. -/
```

## Source Excerpt

```lean
def decompose_recovery_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      let (fp, fm) := idempotent_decompose bp
      -- Recovery: fp + fm = bp
      let recovery := SectorPair.add fp fm == bp
      -- Orthogonality: fp * fm = 0
      let ortho := SectorPair.mul fp fm == ⟨0, 0⟩
      -- Structure: fp has zero C, fm has zero B
      let struct := fp.c_sector == 0 && fm.b_sector == 0
      -- Preservation: fp.B = bp.B and fm.C = bp.C
      let pres := fp.b_sector == bp.b_sector && fm.c_sector == bp.c_sector
      recovery && ortho && struct && pres &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```
