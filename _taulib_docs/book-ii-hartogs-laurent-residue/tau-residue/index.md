---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_residue",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/tau-residue/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::tau_residue",
  "declaration_slug": "tau-residue",
  "kind": "def",
  "name": "tau_residue",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 123,
  "source_line_end": 125,
  "registry_ids": [
    "II.D43"
  ],
  "related_registry_items": [
    {
      "id": "II.D43",
      "title": "Residue",
      "url": "/registry/object/II.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L123-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L123-L125",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L123-L125)
- Source range: L123-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D43` — Residue

## Immediate Comment / Docstring

```lean
/-- [II.D43] The residue of x at prime index i:
    tau_residue(x, i) = x mod p_i.

    This is the stage-independent version: the residue at a prime
    does not depend on which stage k we compute at (as long as k >= i),
    because p_i divides M_k for k >= i. -/
```

## Source Excerpt

```lean
def tau_residue (x i : TauIdx) : TauIdx :=
  if i == 0 then 0
  else x % nth_prime i
```
