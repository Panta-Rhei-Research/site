---
{
  "projection_kind": "taulib_declaration",
  "title": "laurent_range_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/laurent-range-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::laurent_range_check",
  "declaration_slug": "laurent-range-check",
  "kind": "def",
  "name": "laurent_range_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 79,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L79-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L79-L92",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L79-L92)
- Source range: L79-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Laurent expansion is well-defined: each coefficient is in the correct range.
    For 1 <= i <= k: 0 <= laurent_coeff(x, k, i) < p_i. -/
```

## Source Excerpt

```lean
def laurent_range_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 1 (fuel - 1)
    else if i > k then go x (k + 1) 1 (fuel - 1)
    else
      let coeff := laurent_coeff x k i
      let pi := nth_prime i
      let ok := coeff < pi
      ok && go x k (i + 1) (fuel - 1)
  termination_by fuel
```
