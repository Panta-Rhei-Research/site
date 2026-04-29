---
{
  "projection_kind": "taulib_declaration",
  "title": "count_nonzero_generators",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/count-nonzero-generators/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::count_nonzero_generators",
  "declaration_slug": "count-nonzero-generators",
  "kind": "def",
  "name": "count_nonzero_generators",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 186,
  "source_line_end": 196,
  "registry_ids": [
    "II.T31"
  ],
  "related_registry_items": [
    {
      "id": "II.T31",
      "title": "Finite Spectral Support",
      "url": "/registry/object/II.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L186-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L186-L196",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L186-L196)
- Source range: L186-L196
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T31` — Finite Spectral Support

## Immediate Comment / Docstring

```lean
/-- [II.T31] Count of nonzero cylinder generators at stage k for a given x.
    At stage k, each prime contributes exactly 1 active residue class. -/
```

## Source Excerpt

```lean
def count_nonzero_generators (k _x : TauIdx) : Nat :=
  go 1 (k + 1) 0
where
  go (pi_idx fuel acc : Nat) : Nat :=
    if fuel = 0 then acc
    else if pi_idx > k then acc
    else
      let p := nth_prime pi_idx
      let active := if p > 0 then 1 else 0
      go (pi_idx + 1) (fuel - 1) (acc + active)
  termination_by fuel
```
