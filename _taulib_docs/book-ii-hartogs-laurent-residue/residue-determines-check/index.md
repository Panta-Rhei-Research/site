---
{
  "projection_kind": "taulib_declaration",
  "title": "residue_determines_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/residue-determines-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::residue_determines_check",
  "declaration_slug": "residue-determines-check",
  "kind": "def",
  "name": "residue_determines_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 158,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L158-L172",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L158-L172",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L158-L172)
- Source range: L158-L172
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Residues determine the point: if tau_residue(x, i) = tau_residue(y, i)
    for all 1 <= i <= k, then reduce(x, k) = reduce(y, k).
    This is the CRT uniqueness theorem. -/
```

## Source Excerpt

```lean
def residue_determines_check (bound db : TauIdx) : Bool :=
  go 2 2 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      -- Check: if all residues agree, then reductions agree
      let agree := all_residues_agree x y k
      let reductions_agree := reduce x k == reduce y k
      let ok := !agree || reductions_agree
      ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
