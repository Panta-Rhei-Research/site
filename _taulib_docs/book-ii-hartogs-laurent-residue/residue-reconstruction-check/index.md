---
{
  "projection_kind": "taulib_declaration",
  "title": "residue_reconstruction_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/residue-reconstruction-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::residue_reconstruction_check",
  "declaration_slug": "residue-reconstruction-check",
  "kind": "def",
  "name": "residue_reconstruction_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 240,
  "source_line_end": 253,
  "registry_ids": [
    "II.T30"
  ],
  "related_registry_items": [
    {
      "id": "II.T30",
      "title": "Residue Theorem",
      "url": "/registry/object/II.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L240-L253",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.LaurentResidue",
        "url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L240-L253",
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

- Module: [TauLib.BookII.Hartogs.LaurentResidue](/verify/taulib/docs/book-ii-hartogs-laurent-residue/)
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L240-L253)
- Source range: L240-L253
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T30` — Residue Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T30] Residue theorem: the CRT residues at stage k completely
    determine the function value.

    For each x in [2, bound] and stage k in [1, db]:
    - Compute the Laurent expansion (all residues)
    - Reconstruct via CRT
    - Verify the reconstruction equals reduce(x, k)

    This is the tau-analog of the classical residue theorem:
    "the sum of all residues recovers the function value."
    In our setting: "the tuple of all prime residues recovers the
    stage-k projection via CRT." -/
```

## Source Excerpt

```lean
def residue_reconstruction_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let reduced := reduce x k
      let coeffs := laurent_expansion reduced k
      let reconstructed := crt_reconstruct coeffs k
      let ok := reconstructed == reduced
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
