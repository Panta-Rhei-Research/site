---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_reconstruct",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/crt-reconstruct/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::crt_reconstruct",
  "declaration_slug": "crt-reconstruct",
  "kind": "def",
  "name": "crt_reconstruct",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 183,
  "source_line_end": 198,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L183-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L183-L198",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L183-L198)
- Source range: L183-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT reconstruction: given residues (r_1, ..., r_k), find x in [0, M_k)
    such that x mod p_i = r_i for all i.

    Implemented by brute-force search over [0, M_k). This is computable
    for small k since M_k grows relatively slowly (M_4 = 210). -/
```

## Source Excerpt

```lean
def crt_reconstruct (residues : List TauIdx) (k : TauIdx) : TauIdx :=
  let mk := primorial k
  go 0 mk residues k
where
  go (x fuel : Nat) (residues : List TauIdx) (k : Nat) : TauIdx :=
    if fuel = 0 then 0  -- not found
    else if x >= primorial k then 0  -- not found
    else if matches_all x residues 1 k then x
    else go (x + 1) (fuel - 1) residues k
  termination_by fuel
  matches_all (x : Nat) (residues : List TauIdx) (i k : Nat) : Bool :=
    match residues with
    | [] => true
    | r :: rs =>
      if i > k then true
      else (x % nth_prime i == r) && matches_all x rs (i + 1) k
```
