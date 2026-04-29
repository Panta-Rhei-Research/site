---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_roundtrip_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/crt-roundtrip-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::crt_roundtrip_check",
  "declaration_slug": "crt-roundtrip-check",
  "kind": "def",
  "name": "crt_roundtrip_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 205,
  "source_line_end": 222,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L205-L222",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L205-L222",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L205-L222)
- Source range: L205-L222
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT reconstruction round-trip check: for each x in [0, M_k),
    reconstruct from Laurent coefficients and verify recovery.

    Given x, compute (x%p_1, ..., x%p_k), then reconstruct y from these
    residues, and verify y = x. -/
```

## Source Excerpt

```lean
def crt_roundtrip_check (db : TauIdx) : Bool :=
  go_k 1 (db + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let mk := primorial k
      go_x 0 mk k (fuel - 1) && go_k (k + 1) (fuel - 1)
  termination_by fuel
  go_x (x mk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= mk then true
    else
      let coeffs := laurent_expansion x k
      let reconstructed := crt_reconstruct coeffs k
      (reconstructed == x) && go_x (x + 1) mk k (fuel - 1)
  termination_by fuel
```
